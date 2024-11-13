# push_config.py

import csv
import os
from netmiko import ConnectHandler


def push_configuration(device_id):
    # Step 1: Fetch the management IP, username, and password from hosts.csv
    csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
    management_ip = None
    username = None
    password = None

    print(f"Looking for device '{device_id}' in '{csv_path}'")
    with open(csv_path, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Checking row: {row}")
            if row["device_name"] == device_id:
                management_ip = row["management_ip"]
                username = row["username"]
                password = row["password"]
                print(
                    f"Found device '{device_id}' with IP: {management_ip}, Username: {username}"
                )
                break

    if not management_ip:
        print(f"Management IP not found for device {device_id}")
        return "Management IP not found for device."

    if not username or not password:
        print(f"Username or password missing for device {device_id}")
        return "Username or password missing for device."

    # Step 2: Locate the config file for the device
    config_path = os.path.join(
        os.path.dirname(__file__), "..", "configs", f"{device_id}.cfg"
    )
    print(f"Looking for config file at '{config_path}'")
    if not os.path.isfile(config_path):
        print(f"Config file not found for device {device_id}")
        return "Config file not found for device."

    # Step 3: Use Netmiko to push the config file
    device = {
        "device_type": "arista_eos",  # Adjust according to your device type
        "host": management_ip,
        "username": username,
        "password": password,
    }

    print(f"Attempting to connect to {management_ip} with username '{username}'")
    try:
        net_connect = ConnectHandler(**device)
        print(f"Connection established. Sending configuration from '{config_path}'")
        output = net_connect.send_config_from_file(config_path)
        net_connect.disconnect()
        print("Configuration pushed successfully:", output)
        return "Configuration pushed successfully."
    except Exception as e:
        print("Error pushing configuration:", e)
        return f"Failed to push configuration: {e}"
