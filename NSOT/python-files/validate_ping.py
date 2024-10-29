import subprocess

# Function to ping an IP and return True if reachable, False otherwise
def ping_ip(ip):
    try:
        # Ping the IP address with a single packet and a 1-second timeout
        output = subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return "1 received" in output or "bytes from" in output
    except subprocess.CalledProcessError:
        return False
