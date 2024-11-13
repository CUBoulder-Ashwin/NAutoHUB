import csv
import os
from netmiko import ConnectHandler


def push_configuration(device_id):
    csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
    management_ip, username, password = None, None, None

    try:
        with open(csv_path, mode="r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["hostname"] == device_id:
                    management_ip = row["management_ip"]
                    username = row["username"]
                    password = row["password"]
                    break
    except FileNotFoundError:
        return "Host CSV file not found."

    if not management_ip or not username or not password:
        return "Device credentials or management IP missing."

    config_path = os.path.join(
        os.path.dirname(__file__), "..", "configs", f"{device_id}.cfg"
    )
    if not os.path.isfile(config_path):
        return "Config file not found for device."

    device = {
        "device_type": "arista_eos",
        "host": management_ip,
        "username": username,
        "password": password,
    }

    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_from_file(config_path)
        print(output)
        net_connect.disconnect()
        return "Configuration pushed successfully."
    except Exception as e:
        return f"Failed to push configuration: {e}"
