import os
import pathlib
import subprocess

def find_base_path():
    """Find the base path up to 'Advanced-Netman'."""
    current_dir = pathlib.Path(__file__).parent.absolute()
    base_path = current_dir
    while base_path.name != "Advanced-Netman" and base_path.parent != base_path:
        base_path = base_path.parent
    if base_path.name != "Advanced-Netman":
        raise Exception("Could not find 'Advanced-Netman' in the path hierarchy")
    return base_path

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

def main():
    # Find the base path dynamically
    base_path = find_base_path()

    # Define services and timers
    services_and_timers = [
        {
            "file_name": "password_update.service",
            "content": f"""[Unit]
Description=Device Password Update Service

[Service]
ExecStart={base_path}/venv/bin/python {base_path}/NSOT/GUI/flask_app/password_update.py
WorkingDirectory={base_path}/NSOT/python-files/
Restart=always

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
User=student
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
"""
        }
    ]

    # Create each service or timer file
    for item in services_and_timers:
        create_service_or_timer_file(item["file_name"], item["content"])

if __name__ == "__main__":
    main()
