import os
import pandas as pd
from netmiko import ConnectHandler

# Always locate relative to this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Assuming hosts.csv is under NSOT/IPAM/hosts.csv
csv_path = os.path.join(current_dir, "..", "..", "IPAM", "hosts.csv")

# Resolve absolute path
csv_path = os.path.abspath(csv_path)

# Load CSV once
hosts_df = pd.read_csv(csv_path)


def connect_and_run_command(device_name, command):
    """Connects to a device via SSH using Netmiko and runs a command."""
    matched_row = hosts_df[hosts_df["hostname"] == device_name]

    if matched_row.empty:
        print(f"❌ Device '{device_name}' not found in hosts.csv")
        return None

    device_info = matched_row.iloc[0]

    netmiko_device = {
        "device_type": device_info.get("device_type", "arista_eos"),
        "host": device_info["management_ip"],
        "username": device_info["username"],
        "password": device_info["password"],
    }

    try:
        print(f"🔌 Connecting to {device_name} ({netmiko_device['host']})...")
        connection = ConnectHandler(**netmiko_device)
        connection.enable()  # Enter enable mode if supported

        print(f"📡 Sending command: {command}")
        output = connection.send_command(command)

        connection.disconnect()
        return output

    except Exception as e:
        print(f"❌ Failed to connect or run command on {device_name}: {e}")
        return None
