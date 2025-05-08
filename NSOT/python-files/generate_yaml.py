import os
import yaml


def clean_empty(data):
    """Recursively remove empty lists, dictionaries, and None values from the data."""
    if isinstance(data, dict):
        return {k: clean_empty(v) for k, v in data.items() if v not in [None, {}, []]}
    elif isinstance(data, list):
        return [clean_empty(v) for v in data if v not in [None, {}, []]]
    return data


def create_yaml_from_form(device_data, filename="devices_config.yml"):
    """Creates a YAML file from the provided device data."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    yaml_file_path = os.path.join(base_dir, "templates", filename)

    cleaned_data = clean_empty({"devices": [device_data]})

    with open(yaml_file_path, "w") as yaml_file:
        yaml_file.write("---\n")
        yaml.dump(
            cleaned_data,
            yaml_file,
            default_flow_style=False,
            sort_keys=False,
        )
    print(f"YAML file saved: {yaml_file_path}")


def build_device_data(
    device_id,
    device_vendor,
    interfaces,
    subinterfaces=None,
    ospf=None,
    bgp=None,
    vlans=None,
    rip=None,
    dhcp=None,
):
    """Builds device data structure with only non-empty fields."""
    device_data = {
        "hostname": device_id,
        "vendor": device_vendor,
        "clear_config": "no",
    }

    if interfaces:
        device_data["interfaces"] = [
            {
                "name": iface["type"] + iface["number"],
                "ip_address": iface.get("ip"),
                "subnet_mask": iface.get("mask"),
            }
            for iface in interfaces
            if iface.get("ip") and iface.get("mask")
        ]

    if subinterfaces:
        device_data["subinterfaces"] = [
            {
                "parent": sub["parent"],
                "id": sub["id"],
                "vlan": sub["vlan"],
                "ip": sub["ip"],
                "mask": sub["mask"],
            }
            for sub in subinterfaces
            if sub.get("parent")
            and sub.get("id")
            and sub.get("vlan")
            and sub.get("ip")
            and sub.get("mask")
        ]

    if vlans:
        device_data["vlans"] = [
            {"id": vlan["id"], "name": vlan["name"]}
            for vlan in vlans
            if vlan.get("id") and vlan.get("name")
        ]

    if ospf and ospf.get("process_id"):
        device_data["ospf"] = {
            "process_id": ospf["process_id"],
            "networks": [
                {
                    "ip": net["ip"],
                    "wildcard": net["wildcard"],
                    "area": net["area"],
                }
                for net in ospf["networks"]
                if net.get("ip") and net.get("wildcard") and net.get("area")
            ],
            "redistribute": {
                "connected": ospf.get("redistribute_connected", False),
                "bgp": ospf.get("redistribute_bgp", False),
            },
        }

    if bgp and bgp.get("as_number"):
        device_data["bgp"] = {
            "as_number": bgp["as_number"],
            "address_families": [
                {
                    "type": family["type"],
                    "networks": [
                        {"ip": net["ip"], "mask": net.get("mask")}
                        for net in family.get("networks", [])
                        if net.get("ip") and net.get("mask")
                    ],
                    "neighbors": [
                        {
                            "ip": neighbor["ip"],
                            "remote_as": neighbor["remote_as"],
                        }
                        for neighbor in family.get("neighbors", [])
                        if neighbor.get("ip") and neighbor.get("remote_as")
                    ],
                }
                for family in bgp.get("address_families", [])
                if family.get("type")
            ],
            "redistribute_ospf": bgp.get("redistribute_ospf", False),
            "redistribute_rip": bgp.get("redistribute_rip", False),
        }

    if rip and rip.get("version") and any(rip.get("networks")):
        device_data["rip"] = {
            "version": rip["version"],
            "networks": [net["ip"] for net in rip["networks"] if net.get("ip")],
            "redistribute": {
                "bgp": rip.get("redistribute", {}).get("bgp", False),
                "metric": rip.get("redistribute", {}).get("metric", 1),
            },
        }

    return device_data


def create_yaml_from_form_data(
    device_id,
    device_vendor,
    interfaces,
    subinterfaces=None,
    ospf=None,
    bgp=None,
    vlans=None,
    rip=None,
    dhcp=None,
):
    """Generates YAML configuration file from form data."""
    device_data = build_device_data(
        device_id,
        device_vendor,
        interfaces,
        subinterfaces,
        ospf,
        bgp,
        vlans,
        rip,
        dhcp,
    )
    create_yaml_from_form(device_data)
