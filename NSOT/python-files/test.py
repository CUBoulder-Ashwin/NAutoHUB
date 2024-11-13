from netmiko import ConnectHandler

# Example connection details
device = {
    "device_type": "arista_eos",
    "host": "10.0.101.3",
    "username": "admin",
    "password": "admin",
}

# Path to the configuration file
config_file_path = "/home/student/Desktop/Advanced-Netman/NSOT/configs/R3.cfg"

# Establish a connection and push configuration
try:
    net_connect = ConnectHandler(**device)
    print("Connected successfully.")
    net_connect.enable()
    output = net_connect.send_config_from_file(config_file=config_file_path)
    print("Configuration push output:")
    print(output)
    net_connect.disconnect()
except Exception as e:
    print(f"Failed to push configuration: {e}")
