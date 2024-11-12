import csv
import datetime
import subprocess
import sys

# Define the OIDs for processor load and device name
OID_PROCESSOR_LOAD = "HOST-RESOURCES-MIB::hrProcessorLoad"
OID_DEVICE_NAME = "SNMPv2-MIB::sysName.0"


# Function to get SNMP data for a specific OID
def snmp_walk(target_ip, oid):
    try:
        result = subprocess.run(
            ["snmpwalk", "-v2c", "-c", "public", target_ip, oid],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        if result.returncode != 0:
            raise Exception(f"SNMP command failed: {result.stderr}")
        return result.stdout
    except Exception as e:
        print(f"Error running snmpwalk: {e}")
        sys.exit(1)


# Function to extract processor load values from the SNMP response
def parse_processor_load(output):
    loads = []
    for line in output.strip().split("\n"):
        parts = line.split(" ")
        try:
            loads.append(int(parts[-1]))
        except ValueError:
            continue
    return loads


# Function to get the average CPU load
def get_average_cpu_load(target_ip):
    cpu_data = snmp_walk(target_ip, OID_PROCESSOR_LOAD)
    loads = parse_processor_load(cpu_data)
    return sum(loads) / len(loads) if loads else 0


# Function to get the device name from the target IP
def get_device_name(target_ip):
    device_name_output = snmp_walk(target_ip, OID_DEVICE_NAME)
    device_name = (
        device_name_output.split("=")[-1].strip().replace("STRING: ", "")
    )  # Removing 'STRING:'
    return device_name


# Function to log data to a CSV file
def log_cpu_load_to_csv(target_ip):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    average_cpu_load = get_average_cpu_load(target_ip)
    device_name = get_device_name(target_ip)

    # Write to CSV file
    with open("snmp_output.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                device_name,
                target_ip,
                f"{average_cpu_load:.2f}",
                timestamp,
            ]
        )

    # Print statement to confirm data logged
    print(
        f"Logged data for {target_ip}: CPU Utilization Average = {average_cpu_load:.2f} at {timestamp}"
    )


# Main execution
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 snmp_cpu_logs.py <target_ip>")
        sys.exit(1)

    target_ip = sys.argv[1]

    # Check if the file exists and create headers if it doesn't
    try:
        with open("snmp_output.csv", mode="x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "Device Name",
                    "Management IP",
                    "CPU Utilization Average",
                    "Timestamp",
                ]
            )
    except FileExistsError:
        pass

    # Log the CPU load data
    log_cpu_load_to_csv(target_ip)
