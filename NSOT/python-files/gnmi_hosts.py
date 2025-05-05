import csv
import yaml
import os


def update_gnmic_yaml_from_hosts():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ipam_dir = os.path.join(script_dir, "..", "IPAM")
    gnmi_path = os.path.join(script_dir, "..", "..")

    hosts_csv = os.path.join(ipam_dir, "hosts.csv")
    gnmic_yaml = os.path.join(gnmi_path, "gnmic-stream.yaml")

    # Load current gnmic config
    with open(gnmic_yaml, "r") as f:
        config = yaml.safe_load(f)

    # Overwrite the 'targets' section from hosts.csv
    config["targets"] = {}

    with open(hosts_csv, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            hostname = row["hostname"]
            mgmt_ip = row["management_ip"]
            config["targets"][hostname] = {"address": f"{mgmt_ip}:6030"}

    # Write the updated gnmic YAML
    with open(gnmic_yaml, "w") as f:
        yaml.dump(config, f, sort_keys=False)
