import os
import unittest
from validate_ping import ping_ip


class TestNetworkAutomation(unittest.TestCase):

    def test_file_exists(self):
        print("\n" + "-" * 50)
        print("Checking Required File Existence")
        print("-" * 50)
        csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")
        self.assertTrue(os.path.exists(csv_path), f"File not found: {csv_path}")
        print(f"Found CSV file at {csv_path}\n")

    def test_ping_ip_from_csv(self):
        print("\n" + "-" * 50)
        print("Testing Ping Responses from IPs in CSV")
        print("-" * 50)

        # Specify the path directly in this function
        csv_path = os.path.join(os.path.dirname(__file__), "..", "IPAM", "hosts.csv")

        ips = []
        with open(csv_path, mode="r") as file:
            for index, line in enumerate(file):
                if index == 0:
                    continue  # Skip header row
                ip = line.strip().split(",")[3]
                ips.append(ip)

        # Ping each IP and check connectivity
        for ip in ips:
            if ip == "management_ip":
                continue  # Skip header if accidentally included
            result = ping_ip(ip)
            print(f"Ping test for IP {ip}: {'Success' if result else 'Failure'}")
            self.assertTrue(result, f"Ping failed for IP {ip}")

        print("Ping tests from CSV completed.\n")


if __name__ == "__main__":
    unittest.main()
