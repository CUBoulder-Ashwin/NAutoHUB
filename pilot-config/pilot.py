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
    if os.geteuid() == 0:
        return "root"
    else:
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
    
    services = ["password_update.service", "device_health_check.timer", "device_health_check.service", "ipam.service", "ngrok.service"]
    for service in services:
        try:
            subprocess.run(["sudo", "systemctl", "enable", service], check=True)
            subprocess.run(["sudo", "systemctl", "start", service], check=True)
            print(f"{service} enabled and started successfully")
        except subprocess.CalledProcessError:
            print(f"Error: Failed to enable/start {service}. Make sure you have sudo privileges.")
        except Exception as e:
            print(f"An error occurred while enabling/starting {service}: {e}")

def main():
    base_path = find_base_path()
    service_user = get_service_user()

    services_and_timers = [
        {
            "file_name": "password_update.service",
            "content": f"""[Unit]
Description=Device Password Update Service

[Service]
ExecStart={base_path}/venv/bin/python {base_path}/NSOT/python-files/password_reset.py
WorkingDirectory={base_path}/NSOT/python-files/
Restart=always
User={service_user}

[Install]
WantedBy=multi-user.target
"""
        },
        {
            "file_name": "device_health_check.timer",
            "content": """[Unit]
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
        },
        {
            "file_name": "ngrok.service",
            "content": f"""[Unit]
Description=Ngrok HTTP Tunnel Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/ngrok start --all --config={base_path}/ngrok_config.yml --log={base_path}/ngrok.log
WorkingDirectory={base_path}
Restart=on-failure
User={service_user}

[Install]
WantedBy=multi-user.target
"""
        }
    ]

    for item in services_and_timers:
        create_service_or_timer_file(item["file_name"], item["content"])
    
    deploy()

if __name__ == "__main__":
    subprocess.run(["sudo", "systemctl", "enable", "jenkins"], check=True)
    subprocess.run(["sudo", "systemctl", "start", "jenkins"], check=True)
    print("Jenkins enabled and started successfully")
    main()
