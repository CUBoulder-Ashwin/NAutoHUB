import os
import sys
import docker
from flask import Flask, render_template, request, redirect, url_for, jsonify
from jinja2 import Environment, FileSystemLoader
import subprocess
from threading import Thread

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
from update_topo import update_topology
from dhcp_updates import configure_dhcp_relay, configure_dhcp_server
from update_hosts import update_hosts_csv
from git_jenkins import push_and_monitor_jenkins
from push_config import push_configuration
from read_IPAM import IPAMReader 
from read_hosts import HostsReader
from clab_builder import build_clab_topology


# File path for IPAM CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IPAM_DIR = os.path.join(BASE_DIR, "..", "..", "IPAM")
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
                rows.append([
                    hostnames[i],
                    usernames[i],
                    passwords[i],
                    management_ips[i]
                ])

        if rows:
            path = write_hosts_csv(rows, append=(save_mode == "append"))
            mode_label = "Appended to" if save_mode == "append" else "Created"
            message = f"✅ {mode_label} hosts.csv with {len(rows)} new device(s)."
        else:
            message = "⚠️ No valid entries to save."

    return render_template("add_hosts.html", message=message)

@app.route("/build-topology", methods=["GET", "POST"])
def build_topology():
    if request.method == "POST":
        topo_name = request.form.get("topo_name", "custom_topo")
        devices = []
        links = []

        # Parse devices
        count = int(request.form.get("device_count", 0))
        for i in range(count):
            name = request.form.get(f"device_name_{i}")
            kind = request.form.get(f"device_kind_{i}")
            image = request.form.get(f"device_image_{i}")
            config = request.form.get(f"device_config_{i}")
            exec_lines = request.form.getlist(f"device_exec_{i}[]")

            devices.append({
                "name": name,
                "kind": kind,
                "image": image,
                "config": config,
                "exec": exec_lines
            })

        # Parse links
        link_count = int(request.form.get("link_count", 0))
        for i in range(link_count):
            dev1 = request.form.get(f"link_dev1_{i}")
            dev2 = request.form.get(f"link_dev2_{i}")
            links.append((dev1, dev2))

        # Build YAML using helper
        output_path = build_clab_topology(topo_name, devices, links)
        message = f"✅ topo.yml generated at: <code>{output_path}</code>"
        client = docker.from_env()
        images = [tag for img in client.images.list() for tag in img.tags if ":" in tag]
        return render_template("build_topology.html", docker_images=images, message=message)


    # GET mode — provide list of Docker images
    client = docker.from_env()
    images = [tag for img in client.images.list() for tag in img.tags if ":" in tag]
    return render_template("build_topology.html", docker_images=images)


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
    if request.method == "POST":
        device_name = request.form["device_name"]
        device_type = request.form["device_type"]
        device_interface = request.form["device_interface"]
        connected_device = request.form["connected_device"]
        connected_interface = request.form["connected_interface"]
        mac_address = request.form["mac_address"]
        sudo_password = request.form["sudo_password"]

        # DHCP Relay related information
        relay_toggle = request.form.get("relay_toggle")
        connected_ip = request.form.get("connected_ip")
        helper_ip = request.form.get("helper_ip")
        dhcp_server = request.form.get("dhcp_server")
        new_subnet = request.form.get("new_subnet")
        ip_address = request.form.get("ip_address")
        range_lower = request.form.get("range_lower")
        range_upper = request.form.get("range_upper")
        default_gateway = request.form.get("default_gateway")

        # Define the path to topo.yml dynamically
        topo_path = os.path.join(
            os.path.dirname(__file__), "../../../pilot-config/topo.yml"
        )

        if device_type == "router" or device_type == "switch":
            update_hosts_csv(device_name, ip_address)

        # Update topology
        update_topology(
            topo_path,
            device_name,
            device_type,
            device_interface,
            connected_device,
            connected_interface,
            mac_address,
        )

        # Prepare the deploy command
        deploy_command = (
            f"echo {sudo_password} | sudo -S containerlab destroy --all || true && "
            f"echo {sudo_password} | sudo -S containerlab deploy -t {topo_path}"
        )

        # Start the deployment and relay config in a new thread
        thread = threading.Thread(
            target=run_deployment_and_relay_config,
            args=(
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
            ),
        )
        thread.start()

    return render_template("add_device.html")


@app.route("/configure-device", methods=["GET", "POST"])
def configure_device():
    jenkins_result = None  # Default value if no job was run
    device_id = None  # Initialize device_id to None

    if request.method == "POST":
        device_id = request.form["device_id"]
        router_type = request.form["router_type"]
        device_vendor = request.form["device_vendor"]

        # Fetching interface configurations
        interfaces = []
        interface_types = request.form.getlist("interface_type[]")
        interface_numbers = request.form.getlist("interface_number[]")
        interface_ips = request.form.getlist("interface_ip[]")
        interface_masks = request.form.getlist("interface_mask[]")
        switchports = request.form.getlist("switchport[]")

        max_len = max(
            len(interface_types),
            len(interface_numbers),
            len(interface_ips),
            len(interface_masks),
            len(switchports),
        )

        interface_ips += [None] * (max_len - len(interface_ips))
        interface_masks += [None] * (max_len - len(interface_masks))
        switchports += [None] * (max_len - len(switchports))

        for i in range(max_len):
            interfaces.append(
                {
                    "type": interface_types[i],
                    "number": interface_numbers[i],
                    "ip": interface_ips[i] if switchports[i] != "yes" else None,
                    "mask": interface_masks[i] if switchports[i] != "yes" else None,
                    "switchport": switchports[i] == "yes",
                }
            )

        # Fetching OSPF configurations with wildcard masks
        ospf = None
        ospf_process_ids = request.form.getlist("ospf_process_id[]")
        ospf_networks = request.form.getlist("ospf_network[]")
        ospf_wildcards = request.form.getlist("ospf_wildcard[]")
        ospf_areas = request.form.getlist("ospf_area[]")
        ospf_redistribute_connected = request.form.getlist("ospf_redistribute_connected[]")
        ospf_redistribute_bgp = request.form.getlist("ospf_redistribute_bgp[]")

        ospf = {
            "process_ids": ospf_process_ids,
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

        # Fetching RIP configurations
        rip = None
        rip_versions = request.form.getlist("rip_version[]")
        rip_networks = request.form.getlist("rip_network[]")
        rip_redistribute_selected = request.form.get("rip_redistribute")
        rip_bgp_as = request.form.getlist("rip_bgp_as[]")
        rip_bgp_metric = request.form.getlist("rip_bgp_metric[]")

        if rip_versions:
            rip = {
                "version": rip_versions[0],
                "networks": [
                    {"ip": net} for net in rip_networks if net
                ],
            }

            if rip_redistribute_selected:
                redistribute = {}
                if rip_bgp_as and rip_bgp_as[0]:
                    redistribute["as_number"] = rip_bgp_as[0]
                if rip_bgp_metric and rip_bgp_metric[0]:
                    redistribute["metric"] = int(rip_bgp_metric[0])

                if redistribute:
                    rip["redistribute"] = redistribute

        # Fetching BGP configurations with network subnet and masks
        bgp = None
        bgp_asns = request.form.getlist("bgp_asn[]")
        bgp_networks = request.form.getlist("bgp_network[]")
        bgp_masks = request.form.getlist("bgp_mask[]")  # New mask input
        bgp_neighbors = request.form.getlist("bgp_neighbor[]")
        bgp_remote_as = request.form.getlist("bgp_remote_as[]")
        bgp_address_families = request.form.getlist("bgp_address_family[]")

        if bgp_asns:
            bgp = {
                "asn": bgp_asns[0],
                "neighbors": [
                    {"ip": ip, "remote_as": remote_as}
                    for ip, remote_as in zip(bgp_neighbors, bgp_remote_as)
                    if ip and remote_as
                ],
                "address_families": [
                    {
                        "type": af_type,
                        "networks": [
                            {"ip": net, "mask": mask}  # Include both IP and mask
                            for net, mask in zip(bgp_networks, bgp_masks)
                            if net and mask  # Ensure both IP and mask are provided
                        ],
                    }
                    for af_type in bgp_address_families
                    if af_type
                ],
            }


        # Fetching VLAN configurations
        vlans = []
        vlan_ids = request.form.getlist("vlan_id[]")
        vlan_names = request.form.getlist("vlan_name[]")

        for i in range(len(vlan_ids)):
            vlans.append({"id": vlan_ids[i], "name": vlan_names[i]})

        # Create the YAML file with collected data
        create_yaml_from_form_data(
            device_id=device_id,
            router_type=router_type,
            device_vendor=device_vendor,
            interfaces=interfaces,
            ospf=ospf,
            bgp=bgp,
            vlans=vlans,
            rip=rip,
        )
        conf_gen()

        # Run the Git push and Jenkins monitoring
        jenkins_result = push_and_monitor_jenkins()

    return render_template("configure_device.html", jenkins_result=jenkins_result, device_id=device_id)


@app.route("/push-config", methods=["POST"])
def push_config():
    data = request.get_json()
    device_id = data.get("device_id")
    
    # Run push_configuration function
    push_status = push_configuration(device_id)
    
    if "successfully" in push_status:
        return jsonify({"status": "success"})
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
        "selected_device" in request.form and (
            any(key.endswith("-dropdown") for key in request.form) or "command" in request.form
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
            f"<h3>Command Output:</h3><pre>{result}</pre>" if success else
            f'<span style="color:red;">Command failed: {result}</span>'
        )

    return render_template(
        "tools.html",
        ping_result=ping_result,
        config_result=config_result,
        devices=devices,
        show_result=show_result
    )

   


@app.route("/ipam")
def ipam():
    """Route to display IPAM table."""
    #print(f"Rendering IPAM table with data: {ipam_reader.ipam_data}")  # Debug statement
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