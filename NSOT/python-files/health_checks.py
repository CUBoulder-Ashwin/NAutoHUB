import csv
import os
import time
from datetime import datetime
from easysnmp import Session
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ipam_dir = os.path.join(script_dir, "..", "IPAM")
hosts_csv = os.path.join(ipam_dir, "hosts.csv")
log_file_path = os.path.join(
    script_dir, "..", "device_health_check.log"
)

# SNMP OIDs for interface and CPU
OID_IF_NAME = "1.3.6.1.2.1.2.2.1.2"
OID_IF_STATUS = "1.3.6.1.2.1.2.2.1.8"
OID_CPU_LOAD = "1.3.6.1.4.1.9.2.1.58"


def log_to_file(message):
    """Log message with timestamp to the log file."""
    with open(log_file_path, "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {message}\n")


def fetch_health_data(device_info):
    """Fetch health data from the device using SNMP and Netmiko."""
    device_ip = device_info["management_ip"]
    device_name = device_info["hostname"]
    community = "public"  # Adjust based on your environment

    log_to_file(
        f"\nStarting health check for {device_name} ({device_ip})..."
    )

    # SNMP session
    try:
        session = Session(
            hostname=device_ip, community=community, version=2
        )
        cpu_usage = session.get(OID_CPU_LOAD).value
        interfaces = session.walk(OID_IF_NAME)
        interface_statuses = session.walk(OID_IF_STATUS)

        log_to_file(f"Device: {device_name}")
        log_to_file(f"CPU Usage: {cpu_usage}%")

        log_to_file("Neighbors (Interfaces):")
        for i, interface in enumerate(interfaces):
            status = (
                "Up" if interface_statuses[i].value == "1" else "Down"
            )
            log_to_file(f"  - {interface.value}: {status}")

    except Exception as e:
        log_to_file(f"SNMP Error for device {device_name}: {e}")

    # Netmiko session for route table and LLDP neighbors
    device_netmiko = {
        "device_type": "cisco_ios",  # Adjust based on device type
        "ip": device_ip,
        "username": device_info["username"],
        "password": device_info["password"],
        "secret": device_info["password"],
    }

    try:
        ssh_conn = ConnectHandler(**device_netmiko)
        ssh_conn.enable()

        # Fetch and log route table
        route_table = ssh_conn.send_command("show ip route")
        log_to_file("\nRoute Table:")
        log_to_file(route_table)

        # Fetch and log LLDP neighbors
        lldp_neighbors = ssh_conn.send_command("show lldp neighbors")
        log_to_file("\nLLDP Neighbors:")
        log_to_file(lldp_neighbors)

        ssh_conn.disconnect()
    except (
        NetmikoTimeoutException,
        NetmikoAuthenticationException,
    ) as e:
        log_to_file(f"SSH Error for device {device_name}: {e}")


def main():
    log_to_file("Starting health checks for all devices in CSV...\n")
    with open(hosts_csv, mode="r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            fetch_health_data(row)
            log_to_file("\n" + "-" * 50 + "\n")
            time.sleep(2)  # Optional delay between checks


if __name__ == "__main__":
    main()
