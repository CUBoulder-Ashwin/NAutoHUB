import os
import csv

class HostsReader:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.hosts_csv = os.path.join(self.base_dir, "..", "..", "IPAM", "hosts.csv")

    def get_devices(self):
        """Fetch devices dynamically from hosts.csv."""
        devices = []
        try:
            with open(self.hosts_csv, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    devices.append(row.get("hostname", "Unknown Device"))
        except FileNotFoundError:
            print(f"hosts.csv not found in {self.hosts_csv}")
        except Exception as e:
            print(f"Error reading hosts.csv: {e}")
        return devices
