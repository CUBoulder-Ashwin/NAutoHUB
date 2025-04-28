import os
import yaml
import shutil
import sys
import time
import docker
import json
from flask import Flask, render_template, request, redirect, url_for, jsonify, stream_with_context, Response
from jinja2 import Environment, FileSystemLoader
import subprocess
from threading import Thread
from pathlib import Path
import requests
import asyncio


# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to 'templates' folder at NSOT level
templates_dir = os.path.join(current_dir, "..", "..", "templates")

# Go up two levels and into the 'python-files' directory
python_files_dir = os.path.join(current_dir, "..", "..", "python-files")

# Add 'python-files' to the system path
sys.path.append(os.path.abspath(python_files_dir))

# Import your custom modules from 'python-files'
from create_hosts import write_hosts_csv
from ping import ping_local, ping_remote
from goldenConfig import generate_configs
from show_commands import execute_show_command
from generate_yaml import create_yaml_from_form_data
from config_Gen import conf_gen  # Updated import for config generation
from update_topo import update_topology, get_hosts_from_csv
from dhcp_updates import configure_dhcp_relay, configure_dhcp_server
from update_hosts import update_hosts_csv
from git_jenkins import push_and_monitor_jenkins
from push_config import push_configuration
from read_IPAM import IPAMReader
from read_hosts import HostsReader
from clab_builder import build_clab_topology
from clab_push import get_docker_images
from machine_learning import ask_llama_for_command_full, ask_llama_to_summarize_stream, send_to_backend,  run_command_on_device


# File path for IPAM CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IPAM_DIR = os.path.join(BASE_DIR, "..", "..", "IPAM")
PILOT_DIR = os.path.join(BASE_DIR, "..", "..", "..", "pilot-config")
ipam_file_path = os.path.join(IPAM_DIR, "ipam_output.csv")

# Initialize
ipam_reader = IPAMReader(file_path=ipam_file_path, update_interval=10)
hosts_reader = HostsReader(BASE_DIR)

app = Flask(__name__)

# Set up Jinja2 environment to load templates from 'NSOT/templates' folder
env = Environment(loader=FileSystemLoader(templates_dir))


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route('/chat-query', methods=['POST'])
def chat_query():
    data = request.json
    user_input = data.get('message')

    def generate_sync():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def inner():
            # First fully collect classification
            first_response = await ask_llama_for_command_full("llama3.1", user_input)

            if first_response.startswith("{"):
                # JSON means CLI question
                parsed = json.loads(first_response)
                device = parsed["device"]
                command = parsed["command"]

                cli_output = send_to_backend(device, command)
                if not cli_output:
                    yield "⚠️ No CLI output received from device."
                    return

                # Now stream summarized answer
                async for token in ask_llama_to_summarize_stream("llama3.1", user_input, cli_output):
                    yield token
            else:
                # Smalltalk — just stream the text
                for char in first_response:
                    yield char

        async_gen = inner()

        while True:
            try:
                token = loop.run_until_complete(async_gen.__anext__())
                yield token
            except StopAsyncIteration:
                break

    return Response(stream_with_context(generate_sync()), content_type='text/event-stream')



@app.route('/run-command', methods=['POST'])
def run_command():
    data = request.json
    device = data.get('device')
    command = data.get('command')
    return run_command_on_device(device, command)


@app.route("/add-hosts", methods=["GET", "POST"])
def add_hosts():
    message = None
    if request.method == "POST":
        hostnames = request.form.getlist("hostname[]")
        usernames = request.form.getlist("username[]")
        passwords = request.form.getlist("password[]")
        management_ips = request.form.getlist("management_ip[]")
        save_mode = request.form.get("save_mode", "new")

        rows = []
        for i in range(len(hostnames)):
            if hostnames[i] and usernames[i] and passwords[i] and management_ips[i]:
                rows.append(
                    [hostnames[i], usernames[i], passwords[i], management_ips[i]]
                )

        if rows:
            path = write_hosts_csv(rows, append=(save_mode == "append"))
            mode_label = "Appended to" if save_mode == "append" else "Created"
            message = f"✅ {mode_label} hosts.csv with {len(rows)} new device(s)."
        else:
            message = "⚠️ No valid entries to save."

    return render_template("add_hosts.html", message=message)


@app.route("/build-topology", methods=["GET", "POST"])
def build_topology():
    if request.method == "POST" and "generate" in request.form:
        topo_name = request.form.get("topo_name", "custom_topo")
        devices = []
        links = []

        # ✅ Dynamically detect how many devices were posted
        i = 0
        while True:
            name = request.form.get(f"device_name_{i}")
            if not name:
                break
            kind = request.form.get(f"device_kind_{i}")
            image = request.form.get(f"device_image_{i}")
            config = request.form.get(f"device_config_{i}")
            exec_lines = request.form.getlist(f"device_exec_{i}[]")

            devices.append(
                {
                    "name": name,
                    "kind": kind,
                    "image": image,
                    "config": config,
                    "exec": exec_lines,
                }
            )
            i += 1

        # Parse links
        link_dev1_list = request.form.get("link_dev1_json")
        link_dev2_list = request.form.get("link_dev2_json")
        if link_dev1_list and link_dev2_list:
            dev1_list = json.loads(link_dev1_list)
            dev2_list = json.loads(link_dev2_list)
            links = list(zip(dev1_list, dev2_list))

        print("[INFO] Generating topology YAML...")
        output_path = build_clab_topology(topo_name, devices, links)
        print(f"[✔] YAML saved at: {output_path}")

        message = f"✅ topo.yml generated at: <code>{output_path}</code>"
        client = docker.from_env()
        images = [tag for img in client.images.list() for tag in img.tags if ":" in tag]
        return render_template(
            "build_topology.html", docker_images=images, message=message
        )

    # GET request fallback
    client = docker.from_env()
    images = [tag for img in client.images.list() for tag in img.tags if ":" in tag]
    return render_template("build_topology.html", docker_images=images)


@app.route("/deploy-topology", methods=["POST"], endpoint="deploy_topology_route")
def deploy_topology_route():
    yaml_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "pilot-config", "topo.yml"
        )
    )
    print("[INFO] Destroying old topology...")
    try:
        destroy_output = subprocess.check_output(
            f"containerlab destroy -t {yaml_path}",
            shell=True,
            stderr=subprocess.STDOUT,
            text=True,
        )
        print("[✔] Destroy output:")
        print(destroy_output)

        with open(yaml_path) as f:
            data = yaml.safe_load(f)
        lab_name = data.get("name", "unknown")

        lab_dir = Path(yaml_path).parent / f"clab-{lab_name}"
        if lab_dir.exists() and lab_dir.is_dir():
            shutil.rmtree(lab_dir)
            print(f"[✔] Deleted old lab folder: {lab_dir}")
        else:
            print(f"[ℹ] Lab folder {lab_dir} not found or already deleted.")

    except subprocess.CalledProcessError as e:
        print("[ERROR] Failed to destroy old topology:")
        print(e.output)

    print("[INFO] Deploying new topology...")
    try:
        deploy_output = subprocess.check_output(
            f"containerlab deploy -t {yaml_path}",
            shell=True,
            stderr=subprocess.STDOUT,
            text=True,
        )
        time.sleep(2)
        subprocess.run(["sudo", "systemctl", "restart", "ipam.service"], check=True)
        print("[✔] Deploy output:")
        print(deploy_output)
        message = "✅ Containerlab topology deployed successfully."
    except subprocess.CalledProcessError as e:
        print("[ERROR] Deployment failed:")
        print(e.output)
        message = f"❌ Failed to deploy topology:<br><pre>{e.output}</pre>"

    return render_template(
        "build_topology.html", docker_images=get_docker_images(), message=message
    )


@app.route("/delete-topology", methods=["POST"], endpoint="delete_topology_route")
def delete_topology_route():
    yaml_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "pilot-config", "topo.yml"
        )
    )
    print("[INFO] Deleting topology...")
    try:
        delete_output = subprocess.check_output(
            f"containerlab destroy -t {yaml_path}",
            shell=True,
            stderr=subprocess.STDOUT,
            text=True,
        )
        print("[✔] Destroy output:")
        print(delete_output)

        with open(yaml_path) as f:
            data = yaml.safe_load(f)
        lab_name = data.get("name", "unknown")

        lab_dir = Path(yaml_path).parent / f"clab-{lab_name}"
        if lab_dir.exists() and lab_dir.is_dir():
            shutil.rmtree(lab_dir)
            print(f"[✔] Deleted lab folder: {lab_dir}")
        else:
            print(f"[ℹ] Lab folder {lab_dir} not found or already deleted.")

        message = "✅ Topology deleted successfully."

    except subprocess.CalledProcessError as e:
        print("[ERROR] Delete failed:")
        print(e.output)
        message = f"❌ Failed to delete topology:<br><pre>{e.output}</pre>"

    return render_template(
        "build_topology.html", docker_images=get_docker_images(), message=message
    )




@app.route("/dashboard")
def dashboard():
    # Embed your Grafana dashboard in the dashboard template
    return render_template("dashboard.html")


def run_deployment_and_relay_config(
    deploy_command,
    relay_toggle,
    connected_device,
    connected_interface,
    connected_ip,
    helper_ip,
    mac_address,
    dhcp_server,
    new_subnet,
    range_lower,
    range_upper,
    default_gateway,
    ip_address,
):
    # Run deployment synchronously in the thread
    deploy_result = subprocess.run(deploy_command, shell=True)

    # Only proceed with DHCP configuration if the deployment was successful
    if deploy_result.returncode == 0 and relay_toggle:
        configure_dhcp_relay(
            connected_device, connected_interface, connected_ip, helper_ip
        )
        configure_dhcp_server(
            mac_address,
            dhcp_server,
            new_subnet,
            range_lower,
            range_upper,
            default_gateway,
            ip_address,
        )


@app.route("/add-device", methods=["GET", "POST"])
def add_device():
    message = None

    if request.method == "POST":
        device_name = request.form["device_name"]
        kind = request.form["kind"]
        image = request.form["image"]
        config = request.form.get("config", "")
        exec_lines = request.form.getlist("exec[]")
        mac_address = request.form.get("mac_address", "")
        ip_with_subnet = request.form.get("ip_address", "")
        ip_address = ip_with_subnet.split("/")[0]
        connection_count = int(request.form.get("connection_count", "0"))

        # Optional DHCP relay values
        relay_toggle = request.form.get("relay_toggle")
        connected_ip = request.form.get("connected_ip")
        helper_ip = request.form.get("helper_ip")
        dhcp_server = request.form.get("dhcp_server")
        new_subnet = request.form.get("new_subnet")
        range_lower = request.form.get("range_lower")
        range_upper = request.form.get("range_upper")
        default_gateway = request.form.get("default_gateway")

        connect_to = [
            request.form.get(f"connect_to_{i}")
            for i in range(connection_count)
            if request.form.get(f"connect_to_{i}")
        ]

        topo_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../pilot-config/topo.yml")
        )
        print("[INFO] Destroying old topology before update...")
        os.system(f"containerlab destroy -t {topo_path} || true")

        try:
            update_topology(
                topo_path=topo_path,
                device_name=device_name,
                kind=kind,
                image=image,
                config=config,
                exec_lines=exec_lines,
                mac=mac_address,
                connect_to_list=connect_to,
                mgmt_ip=ip_with_subnet,
            )

            if kind == "ceos":
                update_hosts_csv(device_name, ip_address)

            print("[INFO] Deploying new topology...")

            clab_path = os.path.join(PILOT_DIR, "clab-example")

            if os.path.exists(clab_path):
                shutil.rmtree(clab_path)
                print(f"✅ Removed: {clab_path}")
            else:
                print(f"⚠️ Path does not exist, skipping: {clab_path}")

            deploy_output = subprocess.check_output(
                f"containerlab deploy -t {topo_path}",
                shell=True,
                stderr=subprocess.STDOUT,
                text=True,
            )
            time.sleep(2)
            subprocess.run(["sudo", "systemctl", "restart", "ipam.service"], check=True)
            print("[✔] Deploy output:")
            print(deploy_output)

            # Optionally run DHCP relay config if enabled
            if relay_toggle:
                configure_dhcp_relay(
                    connected_device=connect_to[0] if connect_to else "",
                    connected_interface="eth1",
                    connected_ip=connected_ip,
                    helper_ip=helper_ip,
                )
                configure_dhcp_server(
                    mac_address,
                    dhcp_server,
                    new_subnet,
                    range_lower,
                    range_upper,
                    default_gateway,
                    ip_address,
                )

            message = "✅ Topology deployed successfully."

        except subprocess.CalledProcessError as e:
            print("[ERROR] Deployment failed:")
            print(e.output)
            message = f"❌ Deployment failed:<br><pre>{e.output}</pre>"

    docker_images = [
        tag for img in docker.from_env().images.list() for tag in img.tags if ":" in tag
    ]
    return render_template(
        "add_device.html",
        docker_images=docker_images,
        available_hosts=get_hosts_from_csv(),
        message=message,
    )


@app.route("/configure-device", methods=["GET", "POST"])
def configure_device():
    try:
        if request.method == "POST":
            device_id = request.form.get("device_id")
            device_vendor = request.form.get("device_vendor")

            # Interfaces
            interfaces = []
            for i_type, i_num, ip, mask, sp in zip(
                request.form.getlist("interface_type[]"),
                request.form.getlist("interface_number[]"),
                request.form.getlist("interface_ip[]"),
                request.form.getlist("interface_mask[]"),
                request.form.getlist("switchport[]"),
            ):
                interfaces.append(
                    {
                        "type": i_type,
                        "number": i_num,
                        "ip": ip if sp != "yes" else None,
                        "mask": mask if sp != "yes" else None,
                        "switchport": sp == "yes",
                    }
                )

            # Subinterfaces
            subinterfaces = []
            for parent, sid, vlan, ip, mask in zip(
                request.form.getlist("subinterface_parent[]"),
                request.form.getlist("subinterface_id[]"),
                request.form.getlist("subinterface_vlan[]"),
                request.form.getlist("subinterface_ip[]"),
                request.form.getlist("subinterface_mask[]"),
            ):
                subinterfaces.append(
                    {"parent": parent, "id": sid, "vlan": vlan, "ip": ip, "mask": mask}
                )

            # VLANs
            vlans = []
            for vlan_id, vlan_name in zip(
                request.form.getlist("vlan_id[]"),
                request.form.getlist("vlan_name[]"),
            ):
                vlans.append({"id": vlan_id, "name": vlan_name})

            # RIP
            rip = None
            rip_versions = request.form.getlist("rip_version[]")
            rip_networks = request.form.getlist("rip_network[]")
            rip_redistribute_selected = request.form.get("rip_redistribute")
            rip_bgp_as = request.form.getlist("rip_bgp_as[]")
            rip_bgp_metric = request.form.getlist("rip_bgp_metric[]")

            if rip_versions:
                rip = {
                    "version": rip_versions[0],
                    "networks": [{"ip": net} for net in rip_networks if net],
                }

                if rip_redistribute_selected:
                    redistribute = {}
                    if rip_bgp_as and rip_bgp_as[0]:
                        redistribute["as_number"] = rip_bgp_as[0]
                    if rip_bgp_metric and rip_bgp_metric[0]:
                        redistribute["metric"] = int(rip_bgp_metric[0])
                    if redistribute:
                        rip["redistribute"] = redistribute

            # OSPF
            ospf = None
            ospf_process_ids = request.form.getlist("ospf_process_id[]")
            ospf_networks = request.form.getlist("ospf_network[]")
            ospf_wildcards = request.form.getlist("ospf_wildcard[]")
            ospf_areas = request.form.getlist("ospf_area[]")
            ospf_redistribute_connected = request.form.getlist(
                "ospf_redistribute_connected[]"
            )
            ospf_redistribute_bgp = request.form.getlist("ospf_redistribute_bgp[]")

            if ospf_process_ids:
                ospf = {
                    "process_id": ospf_process_ids[0],
                    "networks": [
                        {
                            "ip": ospf_networks[i],
                            "wildcard": ospf_wildcards[i],
                            "area": ospf_areas[i],
                        }
                        for i in range(len(ospf_networks))
                    ],
                    "redistribute_connected": len(ospf_redistribute_connected) > 0,
                    "redistribute_bgp": len(ospf_redistribute_bgp) > 0,
                }

            # BGP
            bgp = None
            bgp_asns = request.form.getlist("bgp_asn[]")
            bgp_networks = request.form.getlist("bgp_network[]")
            bgp_masks = request.form.getlist("bgp_mask[]")
            bgp_neighbors = request.form.getlist("bgp_neighbor[]")
            bgp_remote_as = request.form.getlist("bgp_remote_as[]")
            bgp_address_families = request.form.getlist("bgp_address_family[]")

            if bgp_asns:
                bgp = {
                    "as_number": bgp_asns[0],
                    "neighbors": [
                        {"ip": ip, "remote_as": remote_as}
                        for ip, remote_as in zip(bgp_neighbors, bgp_remote_as)
                        if ip and remote_as
                    ],
                    "address_families": [
                        {
                            "type": af,
                            "networks": [
                                {"ip": net, "mask": mask}
                                for net, mask in zip(bgp_networks, bgp_masks)
                                if net and mask
                            ],
                        }
                        for af in bgp_address_families
                        if af
                    ],
                }

            # Attempt to generate YAML and push via Jenkins
            try:
                create_yaml_from_form_data(
                    device_id=device_id,
                    device_vendor=device_vendor,
                    interfaces=interfaces,
                    subinterfaces=subinterfaces,
                    vlans=vlans,
                    rip=rip,
                    ospf=ospf,
                    bgp=bgp,
                )
                conf_gen()
                jenkins_result = push_and_monitor_jenkins()

                if jenkins_result == "SUCCESS":
                    return render_template(
                        "configure_device.html",
                        jenkins_result="jenkins_success",
                        device_id=device_id,
                        message="✅ Jenkins pipeline succeeded!",
                    )
                else:
                    return render_template(
                        "configure_device.html",
                        jenkins_result="jenkins_failure",
                        device_id=device_id,
                        message="❌ Jenkins pipeline failed.",
                    )

            except Exception as pipeline_error:
                print("🔥 Pipeline error:", pipeline_error)
                return render_template(
                    "configure_device.html",
                    jenkins_result="jenkins_failure",
                    device_id=device_id,
                    message=str(pipeline_error),
                )

        # GET request
        return render_template("configure_device.html", jenkins_result=None)

    except Exception as e:
        print(f"Error in /configure-device: {e}")
        return render_template(
            "configure_device.html",
            jenkins_result="jenkins_failure",
            device_id="unknown",
            message=str(e),
        )

    except Exception as e:
        print(f"Error in /configure-device: {e}")
        return render_template(
            "configure_device.html",
            jenkins_result="jenkins_failure",
            device_id="unknown",
        )


@app.route("/push-config", methods=["POST"])
def push_config():
    data = request.get_json()
    device_id = data.get("device_id")

    # Run push_configuration function
    push_status = push_configuration(device_id)

    if "successfully" in push_status:
        return jsonify({"status": "success", "message": push_status})
    else:
        return jsonify({"status": "error", "message": push_status})



@app.route("/tools", methods=["GET", "POST"])
def tools():
    ping_result = None
    config_result = None
    show_result = None

    # Fetch devices dynamically
    devices = hosts_reader.get_devices()

    # Handling Ping Test
    if (
        request.method == "POST"
        and "source" in request.form
        and "destination" in request.form
    ):
        source = request.form["source"]
        destination = request.form["destination"]

        if source == "localhost":
            success, output = ping_local(destination)
        else:
            username = request.form.get("username", "root")
            password = request.form.get("password", "password")
            success, output = ping_remote(source, destination, username, password)

        if success:
            ping_result = f'<span style="color:green;">Ping successful!</span><br><pre>{output}</pre>'
        else:
            ping_result = (
                f'<span style="color:red;">Ping failed.</span><br><pre>{output}</pre>'
            )

    # Handling Golden Config Generator
    if request.method == "POST" and (
        "device" in request.form or "select_all" in request.form
    ):
        select_all = request.form.get("select_all", "off")
        hostname = request.form.get("device")

        if select_all == "on":
            filenames = generate_configs(select_all=True)
        elif hostname:
            filenames = generate_configs(select_all=False, hostname=hostname)

        if filenames:
            config_result = f"<h3>Generated Config Files:</h3><ul>"
            for file in filenames:
                config_result += f"<li>{file}</li>"
            config_result += "</ul>"

    if request.method == "POST" and (
        "selected_device" in request.form
        and (
            any(key.endswith("-dropdown") for key in request.form)
            or "command" in request.form
        )
    ):

        hostname = request.form.get("selected_device")
        selected_command = request.form.get("command", "")

        if not selected_command:
            for key in request.form:
                if key.endswith("-dropdown"):
                    selected_command = request.form[key]
                    break

        success, result = execute_show_command(hostname, selected_command)
        print(result)
        show_result = (
            f"<h3>Command Output:</h3><pre>{result}</pre>"
            if success
            else f'<span style="color:red;">Command failed: {result}</span>'
        )

    return render_template(
        "tools.html",
        ping_result=ping_result,
        config_result=config_result,
        devices=devices,
        show_result=show_result,
    )


@app.route("/ipam")
def ipam():
    """Route to display IPAM table."""
    # print(f"Rendering IPAM table with data: {ipam_reader.ipam_data}")  # Debug statement
    return render_template("ipam.html", ipam_data=ipam_reader.ipam_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    thread = Thread(target=ipam_reader.read_ipam_file, daemon=True)
    thread.start()
    app.run(host="0.0.0.0", port=5555, debug=True)
