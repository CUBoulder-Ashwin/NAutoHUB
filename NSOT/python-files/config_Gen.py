import os
import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import time


def generate_device_configs():
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

    templates = {
        "bgp": env.get_template("bgp_template.j2"),
        "ospf": env.get_template("ospf_template.j2"),
        "rip": env.get_template("rip_template.j2"),
        "dhcp": env.get_template("dhcp_template.j2"),
        "interfaces": env.get_template("interfaces_template.j2"),
        "subinterfaces": env.get_template("subinterface_template.j2"),
        "vlan": env.get_template("vlan_template.j2"),
        "bgp_cisco": env.get_template("bgp_template_cisco.j2"),
        "ospf_cisco": env.get_template("ospf_template_cisco.j2"),
        "rip_cisco": env.get_template("rip_template_cisco.j2"),
        "interfaces_cisco": env.get_template("interfaces_template_cisco.j2"),
    }

    for device in devices:
        config = ""
        clear_config = device.get("clear_config", "no")
        vendor = device.get("vendor", "arista").lower()
        hostname = device.get("hostname")

        # Interfaces
        if "interfaces" in device:
            if clear_config == "yes":
                for iface in device["interfaces"]:
                    config += f"no interface {iface['type']}{iface['number']}\n"
            else:
                if vendor == "cisco":
                    config += templates["interfaces_cisco"].render(
                        interfaces=device["interfaces"]
                    )
                else:
                    config += templates["interfaces"].render(
                        interfaces=device["interfaces"]
                    )

        # Subinterfaces
        if "subinterfaces" in device:
            config += templates["subinterfaces"].render(
                subinterfaces=device["subinterfaces"]
            )

        # VLANs
        if "vlans" in device:
            if clear_config == "yes":
                for vlan in device["vlans"]:
                    config += f"no vlan {vlan['id']}\n"
            else:
                config += templates["vlan"].render(vlans=device["vlans"])

        # OSPF
        if "ospf" in device:
            ospf_data = device["ospf"]
            if clear_config == "yes":
                config += f"no router ospf {ospf_data['process_id']}\n"
            else:
                template_key = "ospf_cisco" if vendor == "cisco" else "ospf"
                config += templates[template_key].render(
                    ospf_process=ospf_data["process_id"],
                    ospf_networks=ospf_data.get("networks", []),
                    redistribute_connected=ospf_data.get(
                        "redistribute_connected", False
                    ),
                    redistribute_bgp=ospf_data.get("redistribute_bgp", False),
                )

        # BGP
        if "bgp" in device:
            bgp_data = device["bgp"]
            if clear_config == "yes":
                config += f"no router bgp {bgp_data['as_number']}\n"
            else:
                networks = [
                    {"ip": net["ip"], "mask": net.get("mask")}
                    for family in bgp_data.get("address_families", [])
                    for net in family.get("networks", [])
                    if net.get("ip") and net.get("mask")
                ]
                template_key = "bgp_cisco" if vendor == "cisco" else "bgp"
                config += templates[template_key].render(
                    bgp_as=bgp_data["as_number"],
                    bgp_networks=networks,
                    bgp_neighbors=bgp_data.get("neighbors", []),
                )

        # RIP
        if "rip" in device:
            rip_data = device["rip"]
            if clear_config == "yes":
                config += "no router rip\n"
            else:
                template_key = "rip_cisco" if vendor == "cisco" else "rip"
                config += templates[template_key].render(
                    rip_version=rip_data.get("version"),
                    rip_networks=rip_data.get("networks", []),
                    bgp_redistribute=rip_data.get("redistribute", {}).get("bgp", False),
                    bgp_as=device.get("bgp", {}).get("as_number", ""),
                    bgp_metric=rip_data.get("redistribute", {}).get("metric", 1),
                )

        # DHCP
        if "dhcp" in device:
            dhcp_data = device["dhcp"]
            if clear_config == "yes":
                config += "no service dhcp\n"
            else:
                config += templates["dhcp"].render(dhcp=dhcp_data)

        # Write to file
        filename = os.path.join(config_dir, f"{hostname}.cfg")
        with open(filename, "w") as config_file:
            config_file.write(config)

        print(f"Configuration generated for {hostname} and saved as {filename}")


def conf_gen():
    generate_device_configs()
