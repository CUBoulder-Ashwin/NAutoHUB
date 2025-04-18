import os
import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import time


def generate_device_configs():
    # Set the base directory paths to NSOT level
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    yaml_file = os.path.join(base_dir, "templates", "devices_config.yml")
    template_dir = os.path.join(base_dir, "templates")
    config_dir = os.path.join(base_dir, "configs")

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    while not os.path.exists(yaml_file):
        print(f"No devices_config.yml found in {yaml_file}.")
        time.sleep(2)

    try:
        with open(yaml_file) as f:
            devices = yaml.safe_load(f)["devices"]
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        sys.exit(1)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    # Load templates for both Cisco and Arista
    templates = {
        "bgp": env.get_template("bgp_template.j2"),
        "ospf": env.get_template("ospf_template.j2"),
        "rip": env.get_template("rip_template.j2"),
        "dhcp": env.get_template("dhcp_template.j2"),
        "interfaces": env.get_template("interfaces_template.j2"),
        "vlan": env.get_template("vlan_template.j2"),
        # Add Cisco-specific templates
        "bgp_cisco": env.get_template("bgp_template_cisco.j2"),
        "ospf_cisco": env.get_template("ospf_template_cisco.j2"),
        "rip_cisco": env.get_template("rip_template_cisco.j2"),
        "interfaces_cisco": env.get_template("interface_template_cisco.j2"),
    }

    for device in devices:
        config = ""
        clear_config = device.get("clear_config", "no")
        device_vendor = device.get(
            "vendor", "arista"
        ).lower()  # Get vendor (Arista/Cisco)

        # Generate interfaces config
        if "interfaces" in device:
            if clear_config == "yes":
                for iface in device["interfaces"]:
                    config += f"no interface {iface['name']}\n"
            else:
                if device_vendor == "cisco":
                    config += templates["interfaces_cisco"].render(
                        interfaces=device["interfaces"]
                    )
                else:  # Default to Arista templates
                    config += templates["interfaces"].render(
                        interfaces=device["interfaces"]
                    )

        # Generate VLAN configuration
        if "vlans" in device:
            if clear_config == "yes":
                for vlan in device["vlans"]:
                    config += f"no vlan {vlan['id']}\n"
            else:
                config += templates["vlan"].render(vlans=device["vlans"])

        # Generate OSPF config
        if "ospf" in device:
            ospf_data = device["ospf"]
            if clear_config == "yes":
                config += f"no router ospf {ospf_data['process_id']}\n"
            else:
                if device_vendor == "cisco":
                    config += templates["ospf_cisco"].render(
                        ospf_process=ospf_data["process_id"],
                        ospf_networks=ospf_data.get("networks", []),
                    )
                else:
                    config += templates["ospf"].render(
                        ospf_process=ospf_data["process_id"],
                        ospf_networks=ospf_data.get("networks", []),
                    )

        # Generate BGP config
        if "bgp" in device:
            bgp_data = device["bgp"]
            if clear_config == "yes":
                config += f"no router bgp {bgp_data['as_number']}\n"
            else:
                bgp_networks = [
                    {"ip": net["ip"]}
                    for family in bgp_data.get("address_families", [])
                    for net in family.get("networks", [])
                ]
                if device_vendor == "cisco":
                    config += templates["bgp_cisco"].render(
                        bgp_as=bgp_data["as_number"],
                        bgp_networks=bgp_networks,
                        bgp_neighbors=bgp_data.get("neighbors", []),
                    )
                else:
                    config += templates["bgp"].render(
                        bgp_as=bgp_data["as_number"],
                        bgp_networks=bgp_networks,
                        bgp_neighbors=bgp_data.get("neighbors", []),
                    )

        # Generate RIP configuration if present
        if "rip" in device:
            rip_data = device["rip"]
            if clear_config == "yes":
                config += "no router rip\n"
            else:
                if device_vendor == "cisco":
                    config += templates["rip_cisco"].render(
                        rip_version=rip_data.get("version"),
                        rip_networks=rip_data.get("networks", []),
                        bgp_redistribute=rip_data["redistribute"].get("bgp", False),
                        bgp_as=device.get("bgp", {}).get("as_number", ""),
                        bgp_metric=rip_data["redistribute"].get("metric", 1),
                    )
                else:
                    config += templates["rip"].render(
                        rip_version=rip_data.get("version"),
                        rip_networks=rip_data.get("networks", []),
                        bgp_redistribute=rip_data["redistribute"].get("bgp", False),
                        bgp_as=device.get("bgp", {}).get("as_number", ""),
                        bgp_metric=rip_data["redistribute"].get("metric", 1),
                    )

        # Generate DHCP config
        if "dhcp" in device:
            dhcp_data = device["dhcp"]
            if clear_config == "yes":
                config += "no service dhcp\n"
            else:
                config += templates["dhcp"].render(dhcp=dhcp_data)

        # Write the config with '---' at the beginning
        filename = os.path.join(config_dir, f"{device['hostname']}.cfg")
        with open(filename, "w") as config_file:
            config_file.write(config)
        print(
            f"Configuration generated for {device['hostname']} and saved as {filename}"
        )


def conf_gen():
    generate_device_configs()
