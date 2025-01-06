import os
import pathlib
import subprocess
import getpass

def find_base_path():
    """Find the base path up to 'Advanced-Netman'."""
    current_dir = pathlib.Path(__file__).parent.absolute()
    base_path = current_dir
    while base_path.name != "Advanced-Netman" and base_path.parent != base_path:
        base_path = base_path.parent
    if base_path.name != "Advanced-Netman":
        raise Exception("Could not find 'Advanced-Netman' in the path hierarchy")
    return base_path

def get_service_user():
    """Determine the appropriate user for the service."""
    # Check if the script is being run as root
    if os.geteuid() == 0:
        return "root"
    else:
        # Return the current non-root user
        return getpass.getuser()

def create_service_or_timer_file(file_name, file_content):
    """Create a systemd service or timer file with elevated permissions."""
    file_path = f"/etc/systemd/system/{file_name}"
    try:
        subprocess.run(["sudo", "tee", file_path], input=file_content.encode(), check=True, stdout=subprocess.DEVNULL)
        print(f"File created successfully at {file_path}")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to create {file_name}. Make sure you have sudo privileges.")
    except Exception as e:
        print(f"An error occurred while creating {file_name}: {e}")

def deploy():
    """Deploy the services and timers."""
    try:
        subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
        print("Daemon reloaded successfully")
    except subprocess.CalledProcessError:
        print("Error: Failed to reload the daemon. Make sure you have sudo privileges.")
    except Exception as e:
        print(f"An error occurred while reloading the daemon: {e}")

    try:
        subprocess.run(["sudo", "systemctl", "enable", "password_update.service"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "device_health_check.timer"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "device_health_check.service"], check=True)
        subprocess.run(["sudo", "systemctl", "enable", "ipam.service"], check=True)
        print("Services and timers enabled successfully")
    except subprocess.CalledProcessError:
        print("Error: Failed to enable services and timers. Make sure you have sudo privileges.")
    except Exception as e:
        print(f"An error occurred while enabling services and timers: {e}")

    try:
        subprocess.run(["sudo", "systemctl", "start", "password_update.service"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "device_health_check.timer"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "device_health_check.service"], check=True)
        subprocess.run(["sudo", "systemctl", "start", "ipam.service"], check=True)
        print("Services and timers started successfully")
    except subprocess.CalledProcessError:
        print("Error: Failed to start services and timers. Make sure you have sudo privileges.")
    except Exception as e:
        print(f"An error occurred while starting services and timers: {e}")

    print("Deployment complete")

def main():
    # Find the base path dynamically
    base_path = find_base_path()

    # Determine the user for running services
    service_user = get_service_user()

    # Define services and timers
    services_and_timers = [
        {
            "file_name": "password_update.service",
            "content": f"""[Unit]
Description=Device Password Update Service

[Service]
ExecStart={base_path}/venv/bin/python {base_path}/NSOT/python-files/password_update.py
WorkingDirectory={base_path}/NSOT/python-files/
Restart=always
User={service_user}

[Install]
WantedBy=multi-user.target
"""
        },
        {
            "file_name": "device_health_check.timer",
            "content": f"""[Unit]
Description=Run Device Health Check Every Hour

[Timer]
OnCalendar=hourly
Persistent=true

[Install]
WantedBy=timers.target
"""
        },
        {
            "file_name": "device_health_check.service",
            "content": f"""[Unit]
Description=Device Health Check Service
After=network.target

[Service]
WorkingDirectory={base_path}/NSOT/python-files
ExecStart=/bin/bash -c '{base_path}/venv/bin/python {base_path}/NSOT/python-files/health_check.py'
Restart=on-failure
User={service_user}

[Install]
WantedBy=multi-user.target
"""
        },
        {
            "file_name": "ipam.service",
            "content": f"""[Unit]
Description=IPAM Python Service
After=network.target

[Service]
ExecStart={base_path}/venv/bin/python {base_path}/NSOT/python-files/ipam.py
WorkingDirectory={base_path}/NSOT
Restart=always
User={service_user}
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
"""
        }
    ]

    # Create each service or timer file
    for item in services_and_timers:
        create_service_or_timer_file(item["file_name"], item["content"])

    # Deploy the services and timers
    deploy()

if __name__ == "__main__":
    main()
