import os
import csv
import time
from datetime import datetime
from easysnmp import Session

# Get the directory of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Dynamically locate the IPAM directory and CSV files
ipam_dir = os.path.join(script_dir, '..', 'IPAM')
hosts_csv = os.path.join(ipam_dir, 'hosts.csv')
output_csv = os.path.join(ipam_dir, 'ipam_output.csv')
check_interval = 300  # in seconds (5 minutes)

# SNMP OIDs for interface name and IP
OID_IF_NAME = '1.3.6.1.2.1.2.2.1.2'
OID_IF_IP = '1.3.6.1.2.1.4.20.1.1'
OID_IF_SUBNET = '1.3.6.1.2.1.4.20.1.3'

def collect_device_info(device_name, management_ip):
    community = 'public'  # Change to your SNMP community string
    device_info = []
    
    try:
        # Create an SNMP session
        session = Session(hostname=management_ip, community=community, version=2)
        
        # Fetch interface name, IP address, and subnet mask using SNMP
        interface_names = session.walk(OID_IF_NAME)
        ip_addresses = session.walk(OID_IF_IP)
        subnet_masks = session.walk(OID_IF_SUBNET)
        
        # Add timestamp for each entry
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        for i in range(len(interface_names)):
            device_info.append({
                'Timestamp': timestamp,
                'Device Name': device_name,
                'Interface Name': interface_names[i].value,
                'IP Address': ip_addresses[i].value if i < len(ip_addresses) else 'N/A',
                'Subnet Mask': subnet_masks[i].value if i < len(subnet_masks) else 'N/A'
            })
    except Exception as e:
        print(f"Error fetching data for {device_name} ({management_ip}): {e}")

    return device_info

def main():
    while True:
        with open(hosts_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['Timestamp', 'Device Name', 'Interface Name', 'IP Address', 'Subnet Mask']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                device_name = row['hostname']
                management_ip = row['management_ip']
                device_data = collect_device_info(device_name, management_ip)
                if device_data:
                    writer.writerows(device_data)

        print("CSV updated. Waiting for next interval.")
        time.sleep(check_interval)

if __name__ == "__main__":
    main()
