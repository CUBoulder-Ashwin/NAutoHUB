import os
import subprocess
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

def ping_local(destination):
    """Ping locally and return success or failure."""
    try:
        print(f"Starting local ping to {destination}")
        output = subprocess.check_output(["ping", "-c", "3", destination], stderr=subprocess.STDOUT, universal_newlines=True)
        print("Local ping successful")
        return True, output
    except subprocess.CalledProcessError as e:
        print("Local ping failed")
        return False, e.output

def ping_remote(source, destination, username, password, device_type="arista_eos"):
    """Ping from remote source using SSH and Netmiko."""
    device = {
        'device_type': device_type,
        'ip': source,
        'username': username,
        'password': password,
        'session_log': 'netmiko_session.log'  # Logs session output for debugging
    }

    try:
        print(f"Attempting to connect to {source} with username: {username}")
        # Establish SSH connection using Netmiko
        ssh_conn = ConnectHandler(**device)
        print(f"Login successful to {source}")

        # Go to enable mode
        print(f"Switching to enable mode on {source}")
        ssh_conn.enable()

        # Execute the ping command remotely
        print(f"Starting ping test from {source} to {destination}")
        command = f"ping {destination}"
        output = ssh_conn.send_command(command)
        
        print("Ping test completed, disconnecting SSH")
        ssh_conn.disconnect()

        # Check if ping was successful
        if "0% packet loss" in output:
            print(f"Ping test successful from {source} to {destination}")
            return True, output
        else:
            print(f"Ping test failed from {source} to {destination}")
            return False, output
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as e:
        print(f"SSH connection failed to {source}. Error: {str(e)}")
        return False, str(e)
