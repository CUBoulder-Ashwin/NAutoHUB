import os
import yaml
from collections import defaultdict

# Final path to save the topology YAML
TOPO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "pilot-config", "topo.yml"))

# Custom YAML dumper to format 'endpoints' inline
class CustomDumper(yaml.SafeDumper):
    def represent_list(self, data):
        if self.is_inline_list(data):
            return self.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)
        return self.represent_sequence('tag:yaml.org,2002:seq', data)

    def is_inline_list(self, data):
        # Inline only endpoints lists of exactly 2 strings
        return isinstance(data, list) and len(data) == 2 and all(isinstance(i, str) for i in data)

CustomDumper.add_representer(list, CustomDumper.represent_list)

def build_clab_topology(topo_name, devices, links):
    nodes = {}
    interface_counts = defaultdict(int)
    yaml_links = []

    for dev in devices:
        node = {
            "kind": dev["kind"],
            "image": dev["image"]
        }

        if dev["kind"] == "ceos" and dev.get("config"):
            node["startup-config"] = dev["config"]

        elif dev["kind"] == "linux" and dev.get("exec"):
            # Expecting exec as a list of strings
            node["exec"] = [cmd.strip() for cmd in dev["exec"] if cmd.strip()]

        nodes[dev["name"]] = node

    for dev1, dev2 in links:
        eth1 = f"eth{interface_counts[dev1] + 1}"
        eth2 = f"eth{interface_counts[dev2] + 1}"

        interface_counts[dev1] += 1
        interface_counts[dev2] += 1

        yaml_links.append({
            "endpoints": [f"{dev1}:{eth1}", f"{dev2}:{eth2}"]
        })

    data = {
        "name": topo_name,
        "topology": {
            "nodes": nodes,
            "links": yaml_links
        }
    }

    os.makedirs(os.path.dirname(TOPO_PATH), exist_ok=True)

    with open(TOPO_PATH, "w") as f:
        yaml.dump(data, f, sort_keys=False, Dumper=CustomDumper)

    return TOPO_PATH
