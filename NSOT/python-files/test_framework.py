import os
import csv
import json
import shutil
import time
from netmiko import ConnectHandler

# Path to the mismatches directory
mismatches_directory = os.path.join(os.path.dirname(__file__), "..", "mismatches")
csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")


# Define troubleshooting actions
def modify_mtu(connection, interface, golden_value):
    """
    Modify the MTU of a specific interface to the golden value.
    """
    print(f"Modifying MTU for {interface} to {golden_value}...")
    commands = [f"interface {interface}", f"mtu {golden_value}"]
    connection.send_config_set(commands)
    print(f"MTU for {interface} set to {golden_value}.")


def flap_interface(connection, interface):
    """
    Shut and then no shut the specific interface to clear errors or mismatches.
    """
    print(f"Flapping interface {interface}...")
    commands = [f"interface {interface}", "shutdown", "no shutdown", "end"]
    connection.send_config_set(commands)
    print(f"Interface {interface} flapped.")


def troubleshoot_device(hostname, device_config, mismatches):
    """
    Troubleshoot the device based on mismatches.
    """
    try:
        print(
            f"Connecting to {hostname} ({device_config['host']}) for troubleshooting..."
        )
        connection = ConnectHandler(**device_config)

        # Enable privileged mode if required
        connection.enable()

        # Ensure terminal length is set to 0
        connection.send_command("terminal length 0")

        for table_name, table_data in mismatches.items():
            for interface, issues in table_data.items():
                for issue, values in issues.items():
                    golden_value = values["golden"]

                    # Handle MTU adjustments
                    if issue == "MTU":
                        modify_mtu(connection, interface, golden_value)
                    # Handle interface status or protocol issues
                    elif issue in ["Status", "Protocol"]:
                        flap_interface(connection, interface)

        connection.disconnect()
    except Exception as e:
        print(f"Failed to troubleshoot {hostname}: {e}")


def get_device_info_from_csv(hostname):
    """
    Fetch device information from the IPAM/hosts.csv file based on the hostname.
    """
    with open(csv_path, mode="r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row["hostname"] == hostname:
                return {
                    "device_type": "arista_eos",
                    "host": row["management_ip"],
                    "username": row["username"],
                    "password": row["password"],
                }
    print(f"No device info found for {hostname} in {csv_path}")
    return None


# Main function
if __name__ == "__main__":
    for mismatch_file in os.listdir(mismatches_directory):
        if mismatch_file.endswith(".json"):
            hostname = mismatch_file.split(".")[0]
            file_path = os.path.join(mismatches_directory, mismatch_file)

            with open(file_path, "r") as json_file:
                mismatches = json.load(json_file)

            # Get device configuration from IPAM/hosts.csv
            device_config = get_device_info_from_csv(hostname)

            if device_config:
                troubleshoot_device(hostname, device_config, mismatches)

    # Buffer timer before ending the program
    print("Waiting for 30 seconds before cleaning up...")
    time.sleep(30)

    # Delete the mismatches directory
    try:
        shutil.rmtree(mismatches_directory)
        print(f"Deleted mismatches directory: {mismatches_directory}")
    except Exception as e:
        print(f"Failed to delete mismatches directory: {e}")
