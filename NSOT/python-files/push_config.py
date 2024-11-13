# push_config.py

import csv
import os
from netmiko import ConnectHandler


def push_configuration(device_id):
    # Step 1: Fetch the management IP from hosts.csv
    csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
    management_ip = None
    with open(csv_path, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["device_name"] == device_id:
                management_ip = row["management_ip"]
                break

    if not management_ip:
        print(f"Management IP not found for device {device_id}")
        return "Management IP not found for device."

    # Step 2: Locate the config file for the device
    config_path = os.path.join(
        os.path.dirname(__file__), "..", "configs", f"{device_id}.cfg"
    )
    if not os.path.isfile(config_path):
        print(f"Config file not found for device {device_id}")
        return "Config file not found for device."

    # Step 3: Use Netmiko to push the config file
    device = {
        "device_type": "cisco_ios",  # Adjust according to your device type
        "host": management_ip,
        "username": "your_username",  # Replace with actual credentials
        "password": "your_password",
    }

    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_from_file(config_path)
        net_connect.disconnect()
        print("Configuration pushed successfully:", output)
        return "Configuration pushed successfully."
    except Exception as e:
        print("Error pushing configuration:", e)
        return f"Failed to push configuration: {e}"
