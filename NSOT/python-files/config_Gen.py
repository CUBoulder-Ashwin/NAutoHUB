import os
import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import time

def generate_device_configs():
    # Set the base directory paths to NSOT level
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    yaml_file = os.path.join(base_dir, 'templates', 'devices_config.yml')
    template_dir = os.path.join(base_dir, 'templates')
    config_dir = os.path.join(base_dir, 'configs')

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    while not os.path.exists(yaml_file):
        print(f"No devices_config.yml found in {yaml_file}. Waiting for it to be created...")
        time.sleep(2)

    try:
        with open(yaml_file) as f:
            devices = yaml.safe_load(f)['devices']
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        sys.exit(1)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # Load templates
    bgp_template = env.get_template('bgp_template.j2')
    ospf_template = env.get_template('ospf_template.j2')
    rip_template = env.get_template('rip_template.j2')
    dhcp_template = env.get_template('dhcp_template.j2')
    interfaces_template = env.get_template('interfaces_template.j2')
    vlan_template = env.get_template('vlan_template.j2')

    for device in devices:
        config = ""
        clear_config = device.get('clear_config', 'no')

        # Generate interfaces config
        if 'interfaces' in device:
            if clear_config == 'yes':
                for iface in device['interfaces']:
                    config += f"no interface {iface['name']}\n"
            else:
                config += interfaces_template.render(interfaces=device['interfaces'])

        # Generate VLAN configuration
        if 'vlans' in device:
            if clear_config == 'yes':
                for vlan in device['vlans']:
                    config += f"no vlan {vlan['id']}\n"
            else:
                config += vlan_template.render(vlans=device['vlans'])

        # Generate OSPF config
        if 'ospf' in device:
            ospf_data = device['ospf']
            if clear_config == 'yes':
                config += f"no router ospf {ospf_data['process_id']}\n"
            else:
                config += ospf_template.render(
                    ospf_process=ospf_data['process_id'],
                    ospf_networks=ospf_data.get('networks', [])
                )

        # Generate BGP config
        if 'bgp' in device:
            bgp_data = device['bgp']
            if clear_config == 'yes':
                config += f"no router bgp {bgp_data['as_number']}\n"
            else:
                config += bgp_template.render(
                    bgp_as=bgp_data['as_number'],
                    bgp_networks=[
                        {'ip': net['ip']} for family in bgp_data.get('address_families', [])
                        for net in family.get('networks', [])
                    ],
                    bgp_neighbors=bgp_data.get('neighbors', [])
                )


        # Generate RIP configuration if present
        if 'rip' in device:
            rip_data = device['rip']
            if clear_config == 'yes':
                config += "no router rip\n"
            else:
                config += rip_template.render(
                    rip_version=rip_data.get('version'),
                    rip_networks=[net for net in rip_data.get('networks', [])],
                    bgp_redistribute=rip_data['redistribute'].get('bgp', False),
                    bgp_as=device.get('bgp', {}).get('as_number', ''),
                    bgp_metric=rip_data['redistribute'].get('metric', 1)
                )

        # Generate DHCP config
        if 'dhcp' in device:
            dhcp_data = device['dhcp']
            if clear_config == 'yes':
                config += "no service dhcp\n"
            else:
                config += dhcp_template.render(dhcp=dhcp_data)

        # Write the config
        filename = os.path.join(config_dir, f"{device['hostname']}.cfg")
        with open(filename, 'w') as config_file:
            config_file.write(config)

        print(f"Configuration generated for {device['hostname']} and saved as {filename}")

def conf_gen():
    generate_device_configs()
