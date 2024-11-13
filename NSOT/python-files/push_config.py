import csv
import os
from netmiko import ConnectHandler


def push_configuration(device_id):
    print(f"Starting configuration push for device_id: {device_id}")  # Debug statement

    csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
    print(f"Looking for CSV file at path: {csv_path}")  # Debug statement

    management_ip, username, password = None, None, None

    # Attempt to open and read the CSV file
    try:
        with open(csv_path, mode="r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["hostname"] == device_id:
                    management_ip = row["management_ip"]
                    username = row["username"]
                    password = row["password"]
                    print(
                        f"Found device in CSV with IP: {management_ip}, Username: {username}"
                    )  # Debug statement
                    break
    except FileNotFoundError:
        print("Host CSV file not found.")  # Debug statement
        return "Host CSV file not found."
    print(device_id)
    print(management_ip)
    print(username)
    print(password)
    # Check if credentials and management IP were found
    if not management_ip or not username or not password:
        print("Device credentials or management IP missing.")  # Debug statement
        return "Device credentials or management IP missing."

    # Verify the config file exists
    config_path = os.path.join(
        os.path.dirname(__file__), "..", "configs", f"{device_id}.cfg"
    )
    print(f"Looking for config file at path: {config_path}")  # Debug statement

    if not os.path.isfile(config_path):
        print("Config file not found for device.")  # Debug statement
        return "Config file not found for device."

    device = {
        "device_type": "arista_eos",
        "host": management_ip,
        "username": username,
        "password": password,
    }

    print(f"Attempting to connect to device {management_ip}...")  # Debug statement

    # Attempt to connect and push the configuration
    try:
        net_connect = ConnectHandler(**device)
        print("Connected successfully.")  # Debug statement

        output = net_connect.send_config_from_file(config_path)
        print("Configuration push output:")  # Debug statement
        print(output)  # Print command output for debugging

        net_connect.disconnect()
        print("Disconnected from device.")  # Debug statement
        return "Configuration pushed successfully."
    except Exception as e:
        print(f"Failed to push configuration: {e}")  # Debug statement
        return f"Failed to push configuration: {e}"
