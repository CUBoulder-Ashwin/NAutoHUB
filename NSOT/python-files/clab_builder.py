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
            value=[
                dumper.represent_scalar("tag:yaml.org,2002:str", i, style="")
                for i in data
            ],
            flow_style=True,
        )
    return dumper.represent_list(data)


yaml.add_representer(list, represent_inline_endpoints, Dumper=NoQuotesDumper)


def build_clab_topology(topo_name, devices, links):
    nodes = {}
    interface_counts = defaultdict(int)
    yaml_links = []

    for dev in devices:
        node = {"kind": dev["kind"], "image": dev["image"]}

        if dev["kind"] == "ceos" and dev.get("config"):
            node["startup-config"] = dev["config"]
        elif dev["kind"] == "linux" and dev.get("exec"):
            node["exec"] = [cmd.strip() for cmd in dev["exec"] if cmd.strip()]

        nodes[dev["name"]] = node

    for dev1, dev2 in links:
        eth1 = f"eth{interface_counts[dev1] + 1}"
        eth2 = f"eth{interface_counts[dev2] + 1}"
        interface_counts[dev1] += 1
        interface_counts[dev2] += 1

        yaml_links.append({"endpoints": [f"{dev1}:{eth1}", f"{dev2}:{eth2}"]})

    data = {"name": topo_name, "topology": {"nodes": nodes, "links": yaml_links}}

    os.makedirs(os.path.dirname(TOPO_PATH), exist_ok=True)

    with open(TOPO_PATH, "w") as f:
        yaml.dump(data, f, sort_keys=False, Dumper=NoQuotesDumper)

    print(f"[\u2714] YAML generated at: {TOPO_PATH}")
    return TOPO_PATH
