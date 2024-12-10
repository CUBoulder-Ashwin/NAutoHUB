import pandas as pd
import os
import csv
import json
import subprocess
from netmiko import ConnectHandler

# Paths
csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
golden_states_directory = os.path.join(os.path.dirname(__file__), "..", "golden_states")
output_directory = os.path.join(os.path.dirname(__file__), "..", "mismatches")
test_framework_path = os.path.join(os.path.dirname(__file__), "test_framework.py")

# Ensure output directory exists and set correct permissions
os.makedirs(output_directory, exist_ok=True)
os.chmod(
    output_directory, 0o775
)  # Read, write, execute for owner and group; read/execute for others

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


# Fetch device current state
def fetch_device_states(device_info):
    hostname = device_info["hostname"]
    device_config = {
        "device_type": "cisco_ios",
        "host": device_info["management_ip"],
        "username": device_info["username"],
        "password": device_info["password"],
    }
    current_states = {}

    try:
        print(f"Connecting to {hostname} ({device_config['host']})...")
        connection = ConnectHandler(**device_config)

        for table_name, command_info in checks_dict.items():
            command = list(command_info.keys())[0]
            headers = command_info[command]

            output = connection.send_command(command)
            lines = output.split("\n")

            data = []
            for line in lines[3:]:
                if line.strip():
                    parts = line.split()
                    if command == "show interfaces status":
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
                        if parts[4] == "2" and parts[5] == "WAYS/DROTHER":
                            parts = parts[:4] + ["2 WAYS/DROTHER"] + parts[6:]
                    if len(parts) < len(headers):
                        parts.extend([None] * (len(headers) - len(parts)))
                    data.append(parts)

            df = pd.DataFrame(data, columns=headers)
            current_states[table_name] = df

        connection.disconnect()
    except Exception as e:
        print(f"Failed to fetch states for {hostname}: {e}")
    return current_states


# Load golden states
def load_golden_states():
    golden_states_dict = {}

    for file_name in os.listdir(golden_states_directory):
        if file_name.endswith(".xlsx"):
            hostname = file_name.split(".")[0]
            file_path = os.path.join(golden_states_directory, file_name)

            golden_excel = pd.ExcelFile(file_path)
            for sheet_name in golden_excel.sheet_names:
                table_name = sheet_name
                golden_states_dict.setdefault(hostname, {})[table_name] = (
                    golden_excel.parse(sheet_name)
                )

    return golden_states_dict


# Compare golden and current states
def compare_golden_current(hostname, golden_states, current_states):
    mismatches = {}

    for table_name, command_info in checks_dict.items():
        if table_name in golden_states and table_name in current_states:
            golden_df = golden_states[table_name]
            current_df = current_states[table_name]

            golden_df.columns = golden_df.columns.str.strip()
            current_df.columns = current_df.columns.str.strip()

            for col in golden_df.columns:
                if col not in current_df.columns:
                    current_df[col] = None

            for col in current_df.columns:
                if col not in golden_df.columns:
                    golden_df[col] = None

            key_column = [golden_df.columns[0]]
            if table_name == "ospf_neighbors":
                key_column.append(golden_df.columns[-1])

            merged_df = pd.merge(
                golden_df,
                current_df,
                on=key_column,
                how="left",
                suffixes=("_golden", "_current"),
                indicator=True,
            )

            table_mismatches = {}
            for _, row in merged_df.iterrows():
                key = " - ".join(row[k] for k in key_column if k in row)
                mismatch_info = {}

                for col in golden_df.columns[1:]:
                    golden_value = row.get(f"{col}_golden")
                    current_value = row.get(f"{col}_current")

                    try:
                        if col in [
                            "Vlan",
                            "Flags Encapsulation",
                            "MTU",
                            "Instance",
                            "Pri",
                        ]:
                            golden_value = (
                                int(golden_value) if pd.notna(golden_value) else None
                            )
                            current_value = (
                                int(current_value) if pd.notna(current_value) else None
                            )
                        elif col == "Dead Time":
                            continue
                    except ValueError:
                        pass

                    golden_value = (
                        golden_value.strip()
                        if isinstance(golden_value, str)
                        else golden_value
                    )
                    current_value = (
                        current_value.strip()
                        if isinstance(current_value, str)
                        else current_value
                    )

                    if not (
                        (pd.isna(golden_value) and pd.isna(current_value))
                        or (golden_value is None and current_value is None)
                    ):
                        if golden_value != current_value:
                            mismatch_info[col] = {
                                "golden": golden_value,
                                "current": current_value,
                            }

                if mismatch_info:
                    table_mismatches[key] = mismatch_info

            if table_mismatches:
                mismatches[table_name] = table_mismatches
    return mismatches


# Save mismatches to JSON
def save_mismatches_to_json(hostname, mismatches):
    if not mismatches:
        print(f"No mismatches found for {hostname}. No file created.")
        return False

    file_path = os.path.join(output_directory, f"{hostname}.json")
    with open(file_path, "w") as json_file:
        json.dump(mismatches, json_file, indent=4)
    print(f"Mismatches saved to {file_path}")
    return True


# Clean up mismatches directory
def clean_mismatches_directory():
    for file_name in os.listdir(output_directory):
        file_path = os.path.join(output_directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print(f"Cleaned up files inside {output_directory}")


# Main function
if __name__ == "__main__":
    devices = []
    with open(csv_path, mode="r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            devices.append(row)

    golden_states_dict = load_golden_states()

    mismatches_found = False

    for device_info in devices:
        hostname = device_info["hostname"]
        current_states = fetch_device_states(device_info)

        if hostname in golden_states_dict:
            golden_states = golden_states_dict[hostname]
            mismatches = compare_golden_current(hostname, golden_states, current_states)
            if save_mismatches_to_json(hostname, mismatches):
                mismatches_found = True

    if mismatches_found:
        print("Mismatches detected. Triggering test_framework.py...")
        subprocess.run(
            [
                "/home/student/Desktop/Advanced-Netman/venv/bin/python3",
                test_framework_path,
            ]
        )
    else:
        print("No mismatches detected.")

    clean_mismatches_directory()
