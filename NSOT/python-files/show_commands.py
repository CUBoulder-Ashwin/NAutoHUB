import csv
import os
from netmiko import ConnectHandler

CSV_FILE = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")


def find_device_info(hostname):
    with open(CSV_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["hostname"] == hostname:
                return {
                    "device_type": "arista_eos",
                    "ip": row["management_ip"],
                    "username": row["username"],
                    "password": row["password"],
                    "secret": row["password"],
                }
    return None


def execute_show_command(hostname, selected_command):
    device_info = find_device_info(hostname)
    if not device_info:
        return False, f"Device {hostname} not found in hosts.csv"

    try:
        ssh_conn = ConnectHandler(**device_info)
        ssh_conn.enable()
        output = ssh_conn.send_command(selected_command)
        ssh_conn.disconnect()
        return True, output
    except Exception as e:
        return False, str(e)
