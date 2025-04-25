import os
import yaml
from collections import defaultdict

# Final path to save the topology YAML
TOPO_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "pilot-config", "topo.yml")
)

# Custom Dumper to format 2-element endpoint lists without quotes
class NoQuotesDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

def represent_inline_endpoints(dumper, data):
    if (
        isinstance(data, list)
        and len(data) == 2
        and all(isinstance(i, str) for i in data)
    ):
        return yaml.SequenceNode(
            tag="tag:yaml.org,2002:seq",
            value=[dumper.represent_scalar("tag:yaml.org,2002:str", i, style="") for i in data],
            flow_style=True,
        )
    return dumper.represent_list(data)

yaml.add_representer(list, represent_inline_endpoints, Dumper=NoQuotesDumper)

def build_clab_topology(topo_name, devices, links):
    nodes = {}
    interface_counts = defaultdict(int)
    yaml_links = []

    # Add mgmt node first
    nodes["mgmt"] = {
        "kind": "ceos",
        "image": "ceos:4.33.2F",
        "startup-config": "~/projects/NAutoHUB/NSOT/golden_configs/goldenconfigs_mgmt.cfg",
    }
    interface_counts["mgmt"] = 0  # Initialize mgmt interface count

    has_linux_host = False  # Track if any Linux host is present

    # Add user devices
    for dev in devices:
        node = {"kind": dev["kind"], "image": dev["image"]}
        if dev["kind"].lower() == "ceos" and dev.get("config"):
            node["startup-config"] = dev["config"]
        elif dev["kind"].lower() == "linux" and dev.get("exec"):
            node["exec"] = [cmd.strip() for cmd in dev["exec"] if cmd.strip()]

        nodes[dev["name"]] = node

        if dev["kind"].lower() == "linux":
            has_linux_host = True

    # ⚡ DO NOT ADD a "host" node anymore ⚡

    # Create mgmt links only to ceos devices
    for dev in devices:
        if dev["kind"].lower() == "ceos":
            mgmt_eth = f"eth{interface_counts['mgmt'] + 1}"
            dev_eth = "eth1"
            yaml_links.append({"endpoints": [f"mgmt:{mgmt_eth}", f"{dev['name']}:{dev_eth}"]})
            interface_counts["mgmt"] += 1
            interface_counts[dev["name"]] += 1

    # Create normal user-specified links
    for dev1, dev2 in links:
        eth1 = f"eth{interface_counts[dev1] + 1}"
        eth2 = f"eth{interface_counts[dev2] + 1}"
        interface_counts[dev1] += 1
        interface_counts[dev2] += 1
        yaml_links.append({"endpoints": [f"{dev1}:{eth1}", f"{dev2}:{eth2}"]})

    # Connect mgmt to 'host' at the end (without adding host node)
    if has_linux_host:
        mgmt_eth = f"eth{interface_counts['mgmt'] + 1}"
        yaml_links.append({"endpoints": [f"mgmt:{mgmt_eth}", "host:eth1"]})
        interface_counts["mgmt"] += 1

    # Final data dict
    data = {"name": topo_name, "topology": {"nodes": nodes, "links": yaml_links}}

    # Save YAML
    os.makedirs(os.path.dirname(TOPO_PATH), exist_ok=True)
    with open(TOPO_PATH, "w") as f:
        yaml.dump(data, f, sort_keys=False, Dumper=NoQuotesDumper)

    print(f"[\u2714] YAML generated at: {TOPO_PATH}")
    return TOPO_PATH
