from netmiko import ConnectHandler
import csv
import os

# Dynamically set the CSV file path
current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
csv_relative_path = os.path.join(current_dir, '..', 'IPAM', 'hosts.csv')  # Relative path to the CSV file
CSV_FILE_PATH = os.path.abspath(csv_relative_path)  # Get absolute path

def get_device_credentials(hostname):
    print(f"Fetching credentials for {hostname}")
    with open(CSV_FILE_PATH, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['hostname'] == hostname:
                print(f"Found credentials for {hostname}")
                return {
                    'device_type': 'arista_eos',
                    'ip': row['management_ip'],
                    'username': row['username'],
                    'password': row['password'],
                    'secret': row['password']
                }
    print(f"No credentials found for {hostname}")
    return None

def configure_dhcp_relay(connected_device, interface, connected_ip, helper_ip):
    print(f"Configuring DHCP relay on {connected_device}")
    device_info = get_device_credentials(connected_device)
    if not device_info:
        print(f"Failed to get credentials for {connected_device}")
        return
    commands = [
        "ip dhcp relay information option", 
        "ip dhcp relay always-on",
        "ip dhcp relay all-subnets default",
        f"interface {interface}",
        "no switchport",
        f"ip address {connected_ip}",
        f"ip helper-address {helper_ip}",
        "exit"
    ]
    print(f"Commands to configure DHCP relay on {connected_device}:\n{commands}")
    try:
        ssh_conn = ConnectHandler(**device_info)
        ssh_conn.enable()
        print(f"Connected to {connected_device}. Sending configuration commands...")
        ssh_conn.send_config_set(commands)
        print(f"Successfully configured DHCP relay on {connected_device}")
        ssh_conn.disconnect()
    except Exception as e:
        print(f"Error configuring DHCP relay on {connected_device}: {e}")

def configure_dhcp_server(mac_address, dhcp_server, new_subnet, range_lower, range_upper, default_gateway, ip_address):
    print(f"Configuring DHCP server on {dhcp_server}")
    device_info = get_device_credentials(dhcp_server)
    if not device_info:
        print(f"Failed to get credentials for {dhcp_server}")
        return
    commands = [
        "configure terminal",
        f"ip dhcp relay information option",
        "dhcp server",
        f"subnet {new_subnet}",
        "reservation",
        f"mac-address {mac_address}",
        f"ipv4-address {ip_address}",
        f"range {range_lower} {range_upper}",
        f"default-gateway {default_gateway}",
        "exit"
    ]
    print(f"Commands to configure DHCP server on {dhcp_server}:\n{commands}")
    try:
        ssh_conn = ConnectHandler(**device_info)
        ssh_conn.enable()
        print(f"Connected to {dhcp_server}. Sending DHCP server configuration commands...")
        ssh_conn.send_config_set(commands)
        print(f"Successfully configured DHCP server on {dhcp_server}")
        ssh_conn.disconnect()
    except Exception as e:
        print(f"Error configuring DHCP server on {dhcp_server}: {e}")
