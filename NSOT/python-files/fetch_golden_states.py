import pandas as pd
import csv
import os
from netmiko import ConnectHandler
#from datetime import datetime

# Path to the CSV file
csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
output_directory = os.path.join(os.path.dirname(__file__), "..", "golden_states")

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Commands and headers
checks_dict = {
    "interface_brief": {
        "show ip int br": [
            "Interface",
            "IP Address",
            "Status",
            "Protocol",
            "MTU",
            "Address Owner",
        ]
    },
    "interface_status": {
        "show interfaces status": [
            "Port",
            "Name",
            "Status",
            "Vlan",
            "Duplex",
            "Speed",
            "Type",
            "Flags Encapsulation",
        ]
    },
    "ospf_neighbors": {
        "show ip ospf neighbor": [
            "Neighbor ID",
            "Instance",
            "VRF",
            "Pri",
            "State",
            "Dead Time",
            "Address",
            "Interface",
        ]
    },
}

# Dictionary to store DataFrames
dataframes = {}


def fetch_device_states(device_info):
    """
    Fetch states from the device and save them in well-formatted DataFrames.
    """
    hostname = device_info["hostname"]
    device_config = {
        "device_type": "cisco_ios",
        "host": device_info["management_ip"],
        "username": device_info["username"],
        "password": device_info["password"],
    }

    try:
        print(f"Connecting to {hostname} ({device_config['host']})...")
        connection = ConnectHandler(**device_config)

        for table_name, command_info in checks_dict.items():
            command = list(command_info.keys())[0]
            headers = command_info[command]

            output = connection.send_command(command)
            content = output

            # Split the string by newlines
            lines = content.split("\n")

            # Process the data rows
            data = []
            for line in lines[3:]:  # Skip header and separator
                if line.strip():  # Check if the line is not empty
                    parts = line.split()

                    if command == "show interfaces status":
                        # Fix the conditions where Name is empty
                        possible_status = [
                            "connected",
                            "disabled",
                            "errdisabled",
                            "inactive",
                            "no-signal",
                            "signal",
                            "notconnect",
                        ]
                        if parts[1] in possible_status:
                            parts = parts[:1] + [None] + parts[1:]

                    elif command == "show ip ospf neighbor":
                        # Fix the condition where State could be '2 WAYS/DROTHER'
                        if parts[4] == "2" and parts[5] == "WAYS/DROTHER":
                            parts = parts[:4] + ["2 WAYS/DROTHER"] + parts[6:]

                    # Fix the condition where Address Owner is empty
                    if len(parts) < len(headers):
                        parts.append(None)

                    data.append(parts)

            # Create the DataFrame using the extracted data and headers
            df = pd.DataFrame(data, columns=headers)
            dataframes.setdefault(hostname, {})[table_name] = df

        connection.disconnect()

    except Exception as e:
        print(f"Failed to fetch states for {hostname}: {e}")


def save_dataframes_to_excel():
    """
    Save each host's DataFrames into a single Excel file with separate sheets.
    """
    for hostname, tables in dataframes.items():
        file_path = os.path.join(output_directory, f"{hostname}.xlsx")
        with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
            for table_name, df in tables.items():
                df.to_excel(writer, sheet_name=table_name, index=False)
        print(f"Saved Excel file for {hostname} at {file_path}")


if __name__ == "__main__":
    devices = []
    with open(csv_path, mode="r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            devices.append(row)

    # Fetch states for each device
    for device_info in devices:
        fetch_device_states(device_info)

    # Save DataFrames to Excel files
    save_dataframes_to_excel()
