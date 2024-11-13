import csv
import os
from netmiko import ConnectHandler

# Path settings
current_dir = os.path.dirname(os.path.abspath(__file__))
hosts_csv_path = os.path.join(current_dir, "..", "IPAM", "hosts.csv")
configs_dir = os.path.join(current_dir, "..", "configs")


def get_device_credentials(device_id):
    """Fetches device credentials from hosts.csv based on the device_id."""
    print(f"Fetching credentials for device_id: {device_id}")

    try:
        with open(hosts_csv_path, mode="r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["hostname"] == device_id:
                    print(f"Found device in CSV with IP: {row['management_ip']}")
                    return {
                        "device_type": "arista_eos",
                        "host": row["management_ip"],
                        "username": row["username"],
                        "password": row["password"],
                    }
    except FileNotFoundError:
        print("Hosts CSV file not found.")
        return None

    print("Device credentials or management IP missing.")
    return None


def get_configuration_commands(device_id):
    """Fetches configuration commands from a .cfg file based on the device_id."""
    config_file_path = os.path.join(configs_dir, f"{device_id}.cfg")
    print(f"Looking for config file at path: {config_file_path}")

    if not os.path.isfile(config_file_path):
        print("Config file not found for device.")
        return None

    try:
        with open(config_file_path, mode="r") as cfgfile:
            commands = cfgfile.read().splitlines()  # Reads each line as a command
            print(f"Loaded configuration commands: {commands}")
            return commands
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return None


def push_configuration(device_id):
    """Connects to the device and pushes configuration commands from a .cfg file."""
    device_info = get_device_credentials(device_id)
    if not device_info:
        return "Device credentials or management IP missing."

    commands = get_configuration_commands(device_id)
    if not commands:
        return "Configuration commands missing or file not found."

    print(f"Attempting to connect to device {device_info['host']}...")

    try:
        net_connect = ConnectHandler(**device_info)
        print("Connected successfully.")

        # Push configuration commands
        output = net_connect.send_config_set(commands, delay_factor=2)
        print("Configuration push output:")
        print(output)

        net_connect.disconnect()
        print("Disconnected from device.")
        return "Configuration pushed successfully."
    except Exception as e:
        print(f"Failed to push configuration: {e}")
        return f"Failed to push configuration: {e}"


# Run the function for a specified device ID
if __name__ == "__main__":
    device_id = "R3"  # Example device ID
    result = push_configuration(device_id)
    print(result)
