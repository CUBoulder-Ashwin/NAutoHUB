import os
import csv
import time
from datetime import datetime
from easysnmp import Session

# Define the base directory paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ipam_dir = os.path.join(script_dir, "..", "IPAM")
hosts_csv = os.path.join(ipam_dir, "hosts.csv")
output_csv = os.path.join(ipam_dir, "ipam_output.csv")
check_interval = 300  # in seconds (5 minutes)

# SNMP OIDs
OID_IP = "1.3.6.1.2.1.4.20.1.1"
OID_SUBNET = "1.3.6.1.2.1.4.20.1.3"
OID_IFINDEX = "1.3.6.1.2.1.4.34.1.3.1.4"
OID_IFNAME_BASE = "1.3.6.1.2.1.2.2.1.2."


def collect_device_info(device_name, management_ip):
    """Collects interface info using SNMP."""
    community = "public"
    device_info = []

    try:
        session = Session(hostname=management_ip, community=community, version=2)

        # Step 1: Get IP → Subnet Mask
        ip_to_mask = {entry.oid_index: entry.value for entry in session.walk(OID_SUBNET)}

        # Step 2: Get IP → ifIndex
        ip_to_ifindex = {}
        for entry in session.walk(OID_IFINDEX):
            oid_parts = entry.oid_index.split(".")
            if len(oid_parts) >= 5:
                ip = ".".join(oid_parts[4:])
                ip_to_ifindex[ip] = entry.value

        # Step 3: For each IP, get ifIndex → Interface Name
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for ip, ifindex in ip_to_ifindex.items():
            try:
                if_name_oid = OID_IFNAME_BASE + str(ifindex)
                iface_entry = session.get(if_name_oid)
                iface_name = iface_entry.value
            except Exception as e:
                iface_name = f"ifIndex {ifindex}"
                print(f"Warning: Could not get interface name for {ifindex}: {e}")

            subnet_mask = ip_to_mask.get(ip, "N/A")

            device_info.append({
                "Timestamp": timestamp,
                "Device Name": device_name,
                "Interface Name": iface_name,
                "IP Address": ip,
                "Subnet Mask": subnet_mask,
            })

    except Exception as e:
        print(f"Error fetching data for {device_name} ({management_ip}): {e}")

    return device_info


def main():
    """Main function to collect and store device info."""
    while True:
        with open(hosts_csv, mode="r") as infile, open(output_csv, mode="w", newline="") as outfile:
            reader = csv.DictReader(infile)
            fieldnames = [
                "Timestamp",
                "Device Name",
                "Interface Name",
                "IP Address",
                "Subnet Mask",
            ]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                device_name = row.get("hostname")
                management_ip = row.get("management_ip")

                if not device_name or not management_ip:
                    print(f"Skipping row with missing data: {row}")
                    continue

                print(f"\nCollecting data from {device_name} ({management_ip})...")
                data = collect_device_info(device_name, management_ip)
                if data:
                    writer.writerows(data)

        print(f"\n✅ IPAM CSV updated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(check_interval)


if __name__ == "__main__":
    main()
