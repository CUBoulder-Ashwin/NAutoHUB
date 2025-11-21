import csv
import os
from netmiko import ConnectHandler
from config_backup import backup_running_config


def push_uploaded_config(device_id, device_vendor, config_content):
    """
    Push an uploaded configuration file directly to a device using Netmiko.

    Args:
        device_id (str): Device hostname
        device_vendor (str): Device vendor (arista, cisco, juniper)
        config_content (str): Configuration content from uploaded file

    Returns:
        tuple: (success: bool, message: str)
    """
    print(f"Starting configuration push for device_id: {device_id}")

    # Locate the CSV
    csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
    print(f"Looking for CSV file at path: {csv_path}")

    management_ip, username, password = None, None, None

    try:
        with open(csv_path, mode="r", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(f"Checking row: {row['hostname'].strip()} vs {device_id.strip()}")
                if row["hostname"].strip() == device_id.strip():
                    management_ip = row["management_ip"].strip()
                    username = row["username"].strip()
                    password = row["password"].strip()
                    print(f"Found device with IP: {management_ip}, user: {username}")
                    break
    except FileNotFoundError:
        print("Host CSV file not found.")
        return False, "Host CSV file not found."

    if not management_ip or not username or not password:
        print("Device credentials or management IP missing.")
        return False, "Device credentials or management IP missing."

    # Map vendor to Netmiko device type
    vendor_map = {
        "arista": "arista_eos",
        "cisco": "cisco_ios",
        "juniper": "juniper_junos",
    }

    device_type = vendor_map.get(device_vendor.lower())
    if not device_type:
        return False, f"Unsupported vendor: {device_vendor}"

    # Build Netmiko connection dictionary
    device = {
        "device_type": device_type,
        "host": management_ip,
        "username": username,
        "password": password,
    }

    # First, backup the current running configuration
    print(f"📦 Creating backup of current configuration for {device_id}...")
    backup_success, backup_message, backup_path = backup_running_config(device_id, device_vendor)

    if not backup_success:
        print(f"⚠️  Warning: Failed to create backup: {backup_message}")
        print("⚠️  Continuing with config push (no backup created)...")
    else:
        print(f"✅ Backup created: {backup_message}")

    print(f"Attempting to connect to device {management_ip} ({device_type})...")

    try:
        net_connect = ConnectHandler(**device)
        print("Connected successfully.")
        net_connect.enable()

        # Split configuration into commands
        config_commands = [
            line.strip()
            for line in config_content.split("\n")
            if line.strip() and not line.strip().startswith("!")
        ]

        # Send configuration commands
        output = net_connect.send_config_set(config_commands)
        print("Configuration push output:")
        print(output)

        # Save configuration
        if device_type == "arista_eos":
            save_output = net_connect.send_command("write memory")
        elif device_type in ["cisco_ios", "cisco_xe"]:
            save_output = net_connect.send_command("write memory")
        elif device_type == "juniper_junos":
            save_output = net_connect.commit()
        else:
            save_output = ""

        print(f"Save output: {save_output}")

        net_connect.disconnect()
        print("Disconnected from device.")
        return True, f"Configuration pushed successfully to {device_id}"

    except Exception as e:
        print(f"Failed to push configuration: {e}")
        return False, f"Failed to push configuration: {str(e)}"
