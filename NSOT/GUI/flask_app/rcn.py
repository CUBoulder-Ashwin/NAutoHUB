import os
import sys
from flask import Flask, render_template, request, redirect, url_for
from jinja2 import Environment, FileSystemLoader

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to 'templates' folder at NSOT level
templates_dir = os.path.join(current_dir, '..', '..', 'templates')

# Go up two levels and into the 'python-files' directory
python_files_dir = os.path.join(current_dir, '..', '..', 'python-files')

# Add 'python-files' to the system path
sys.path.append(os.path.abspath(python_files_dir))

# Import your custom modules from 'python-files'
from ping import ping_local, ping_remote
from goldenConfig import generate_configs

app = Flask(__name__)

# Set up Jinja2 environment to load templates from 'NSOT/templates' folder
env = Environment(loader=FileSystemLoader(templates_dir))

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/dashboard")
def dashboard():
    # Embed your Grafana dashboard in the dashboard template
    return render_template("dashboard.html")

@app.route("/add-device", methods=['GET', 'POST'])
def add_device():
    if request.method == 'POST':
        device_name = request.form['device_name']
        ip_address = request.form['ip_address']
        # Add logic to handle the device configuration or database insert
        return redirect(url_for('homepage'))
    return render_template("add_device.html")

@app.route("/configure-device", methods=['GET', 'POST'])
def configure_device():
    if request.method == 'POST':
        device_id = request.form['device_id']
        router_type = request.form['router_type']

        # Fetching interface configurations
        interfaces = []
        interface_types = request.form.getlist('interface_type[]')
        interface_numbers = request.form.getlist('interface_number[]')
        interface_ips = request.form.getlist('interface_ip[]')
        interface_masks = request.form.getlist('interface_mask[]')
        switchports = request.form.getlist('switchport[]')

        # Safeguard: Ensure all lists have the same length
        max_len = max(len(interface_types), len(interface_numbers), len(interface_ips), len(interface_masks), len(switchports))

        # Fill missing fields with default values
        interface_ips += [None] * (max_len - len(interface_ips))
        interface_masks += [None] * (max_len - len(interface_masks))
        switchports += [None] * (max_len - len(switchports))

        # Build the interface list
        for i in range(max_len):
            interfaces.append({
                'type': interface_types[i],
                'number': interface_numbers[i],
                'ip': interface_ips[i] if switchports[i] != 'yes' else None,
                'mask': interface_masks[i] if switchports[i] != 'yes' else None,
                'switchport': switchports[i] == 'yes'
            })

        # Fetching OSPF configurations
        ospf_process_ids = request.form.getlist('ospf_process_id[]')
        ospf_networks = request.form.getlist('ospf_network[]')
        ospf_areas = request.form.getlist('ospf_area[]')
        ospf_redistribute_connected = request.form.getlist('ospf_redistribute_connected[]')
        ospf_redistribute_bgp = request.form.getlist('ospf_redistribute_bgp[]')

        ospf = {
            'process_ids': ospf_process_ids,
            'networks': [{'ip': ospf_networks[i], 'area': ospf_areas[i]} for i in range(len(ospf_networks))],
            'redistribute_connected': len(ospf_redistribute_connected) > 0,
            'redistribute_bgp': len(ospf_redistribute_bgp) > 0
        }

        # Fetching BGP configurations
        bgp_asns = request.form.getlist('bgp_asn[]')
        bgp_networks = request.form.getlist('bgp_network[]')
        bgp_neighbors = request.form.getlist('bgp_neighbor[]')
        bgp_remote_as = request.form.getlist('bgp_remote_as[]')
        bgp_address_families = request.form.getlist('bgp_address_family[]')

        bgp = {
            'asn': bgp_asns[0],
            'neighbors': [{'ip': bgp_neighbors[i], 'remote_as': bgp_remote_as[i]} for i in range(len(bgp_neighbors))],
            'address_families': [{'type': bgp_address_families[i], 'networks': [bgp_networks[i]]} for i in range(len(bgp_address_families))]
        }

        # Fetching VLAN configurations
        vlans = []
        vlan_ids = request.form.getlist('vlan_id[]')
        vlan_names = request.form.getlist('vlan_name[]')

        for i in range(len(vlan_ids)):
            vlans.append({
                'id': vlan_ids[i],
                'name': vlan_names[i]
            })

        # Depending on the router type, choose the correct Jinja template
        template_name = f"{router_type}_router.j2"
        template = env.get_template(template_name)

        # Render the template with the user-provided data
        configuration = template.render(
            device_id=device_id,
            interfaces=interfaces,
            ospf=ospf,
            bgp=bgp,
            vlans=vlans
        )

        # Logic to save the rendered configuration to a file
        output_dir = os.path.join(current_dir, 'configforTest')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        filename = f"{device_id}.cfg"
        with open(os.path.join(output_dir, filename), 'w') as f:
            f.write(configuration)

        return redirect(url_for('homepage'))

    return render_template("configure_device.html")



@app.route("/tools", methods=["GET", "POST"])
def tools():
    ping_result = None
    config_result = None

    # Handling Ping Test
    if request.method == "POST" and "source" in request.form and "destination" in request.form:
        source = request.form["source"]
        destination = request.form["destination"]
        
        if source == "localhost":
            success, output = ping_local(destination)
        else:
            username = request.form.get('username', 'root')
            password = request.form.get('password', 'password')
            success, output = ping_remote(source, destination, username, password)

        if success:
            ping_result = f'<span style="color:green;">Ping successful!</span><br><pre>{output}</pre>'
        else:
            ping_result = f'<span style="color:red;">Ping failed.</span><br><pre>{output}</pre>'

    # Handling Golden Config Generator
    if request.method == "POST" and ("device" in request.form or "select_all" in request.form):
        select_all = request.form.get('select_all', 'off')
        hostname = request.form.get("device")

        if select_all == 'on':
            filenames = generate_configs(select_all=True)
        elif hostname:
            filenames = generate_configs(select_all=False, hostname=hostname)

        if filenames:
            config_result = f"<h3>Generated Config Files:</h3><ul>"
            for file in filenames:
                config_result += f"<li>{file}</li>"
            config_result += "</ul>"

    return render_template("tools.html", ping_result=ping_result, config_result=config_result)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="localhost", port="8000", debug=True)
