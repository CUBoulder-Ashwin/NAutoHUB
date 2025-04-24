import yaml
import os
import csv
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "IPAM", "hosts.csv"))
TEMPLATE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "templates"))
CONFIG_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "golden_configs"))

def get_hosts_from_csv():
    hosts = []
    if os.path.exists(CSV_PATH):
        with open(CSV_PATH, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                hosts.append(row["hostname"])
    return hosts

def get_next_eth(used):
    i = 1
    while f"eth{i}" in used:
        i += 1
    return f"eth{i}"

class CompactListDumper(yaml.SafeDumper):
    def represent_sequence(self, tag, sequence, flow_style=None):
        if tag == 'tag:yaml.org,2002:seq' and all(isinstance(i, str) for i in sequence):
            return super().represent_sequence(tag, sequence, flow_style=True)
        return super().represent_sequence(tag, sequence, flow_style)

CompactListDumper.add_representer(
    list,
    lambda self, data: CompactListDumper.represent_sequence(self, 'tag:yaml.org,2002:seq', data)
)


def generate_day0_config(device_name, mgmt_ip):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("day0_config.j2")
    rendered = template.render(device_name=device_name, mgmt_ip=mgmt_ip)

    os.makedirs(CONFIG_DIR, exist_ok=True)
    config_path = os.path.join(CONFIG_DIR, f"goldenconfigs_{device_name}.cfg")
    with open(config_path, "w") as f:
        f.write(rendered)
    return config_path

def update_topology(topo_path, device_name, kind, image, config, exec_lines, mac, connect_to_list, mgmt_ip=None):
    with open(topo_path, "r") as f:
        data = yaml.safe_load(f)

    nodes = data["topology"]["nodes"]
    links = data["topology"]["links"]

    if device_name in nodes:
        print(f"[!] Device {device_name} already exists in topology.")
        return

    dev_if = defaultdict(int)

    # mgmt interface
    used_eths = {link["endpoints"][0].split(":")[1] for link in links if link["endpoints"][0].startswith("mgmt")}
    mgmt_eth = get_next_eth(used_eths)

    # auto generate config if CEOS
    if kind == "ceos" and not config and mgmt_ip:
        config = generate_day0_config(device_name, mgmt_ip)

    node_entry = {"kind": kind, "image": image}
    if kind == "ceos" and config:
        node_entry["startup-config"] = config
    elif kind == "linux" and exec_lines:
        node_entry["exec"] = [cmd.strip() for cmd in exec_lines if cmd.strip()]

    nodes[device_name] = node_entry

    # mgmt link
    dev_if[device_name] = 1
    links.append({"endpoints": [f"mgmt:{mgmt_eth}", f"{device_name}:eth1"]})

    # user links
    for target in connect_to_list:
        target_used = {
            ep.split(":")[1]
            for link in links for ep in link["endpoints"]
            if ep.startswith(f"{target}:")
        }
        target_eth = get_next_eth(target_used)
        dev_if[device_name] += 1
        this_eth = f"eth{dev_if[device_name]}"
        links.append({"endpoints": [f"{device_name}:{this_eth}", f"{target}:{target_eth}"]})

    with open(topo_path, "w") as f:
        yaml.dump(data, f, sort_keys=False, Dumper=CompactListDumper)

    print(f"[+] Added {device_name} with mgmt:{mgmt_eth} and {len(connect_to_list)} links.")
