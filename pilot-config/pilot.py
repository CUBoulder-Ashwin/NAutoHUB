import os
import pathlib
import subprocess
import getpass


def find_base_path():
    current_dir = pathlib.Path(__file__).parent.absolute()
    base_path = current_dir
    while base_path.name != "NAutoHUB" and base_path.parent != base_path:
        base_path = base_path.parent
    if base_path.name != "NAutoHUB":
        raise Exception("Could not find 'NAutoHUB' in the path hierarchy")
    return base_path


def get_service_user():
    return "root" if os.geteuid() == 0 else getpass.getuser()


def create_service_or_timer_file(file_name, file_content):
    file_path = f"/etc/systemd/system/{file_name}"
    try:
        subprocess.run(
            ["sudo", "tee", file_path],
            input=file_content.encode(),
            check=True,
            stdout=subprocess.DEVNULL,
        )
        print(f"✅ Created: {file_path}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to create {file_name}. Do you have sudo privileges?")
    except Exception as e:
        print(f"❌ Error creating {file_name}: {e}")


def deploy():
    try:
        subprocess.run(["sudo", "systemctl", "daemon-reload"], check=True)
        print("🔁 systemd daemon reloaded")
    except subprocess.CalledProcessError:
        print("❌ Failed to reload systemd daemon.")
        return

    services = [
        "password_update.service",
        "device_health_check.timer",
        "device_health_check.service",
        "ipam.service",
        "ngrok.service",
        "gnmic_nautohub.service",
    ]

    for service in services:
        try:
            subprocess.run(["sudo", "systemctl", "enable", service], check=True)
            subprocess.run(["sudo", "systemctl", "start", service], check=True)
            print(f"✅ Enabled & started: {service}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to enable/start {service}")


def main():
    base_path = find_base_path()
    service_user = get_service_user()

    services_and_timers = [
        {
            "file_name": "password_update.service",
            "content": f"""[Unit]
Description=Device Password Update Service

[Service]
ExecStart={base_path}/pilot-config/venv/bin/python {base_path}/NSOT/python-files/password_reset.py
WorkingDirectory={base_path}/NSOT/python-files/
Restart=always
User={service_user}

[Install]
WantedBy=multi-user.target
""",
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
""",
        },
        {
            "file_name": "device_health_check.service",
            "content": f"""[Unit]
Description=Device Health Check Service
After=network.target

[Service]
WorkingDirectory={base_path}/NSOT/python-files
ExecStart=/bin/bash -c '{base_path}/pilot-config/venv/bin/python {base_path}/NSOT/python-files/health_checks.py'
Restart=on-failure
User={service_user}

[Install]
WantedBy=multi-user.target
""",
        },
        {
            "file_name": "ipam.service",
            "content": f"""[Unit]
Description=IPAM Python Service
After=network.target

[Service]
ExecStart={base_path}/pilot-config/venv/bin/python {base_path}/NSOT/python-files/ipam.py
WorkingDirectory={base_path}/NSOT
Restart=always
User={service_user}
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
""",
        },
        {
            "file_name": "ngrok.service",
            "content": f"""[Unit]
Description=Ngrok HTTP Tunnel Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/bin/ngrok start --all --config={base_path}/NSOT/misc/ngrok_config.yml --log={base_path}/NSOT/logs/ngrok.log
WorkingDirectory={base_path}
Restart=on-failure
User={service_user}

[Install]
WantedBy=multi-user.target
""",
        },
        {
            "file_name": "gnmic_nautohub.service",
            "content": f"""[Unit]
Description=gNMIc Stream Collector Service
After=network.target docker.service
Requires=docker.service

[Service]
ExecStart=/usr/local/bin/gnmic subscribe --config {base_path}/gnmic-stream.yaml
WorkingDirectory={base_path}
Restart=always
User={service_user}

[Install]
WantedBy=multi-user.target
""",
        },
    ]

    for item in services_and_timers:
        create_service_or_timer_file(item["file_name"], item["content"])

    deploy()


if __name__ == "__main__":
    subprocess.run(["sudo", "systemctl", "enable", "jenkins"], check=True)
    subprocess.run(["sudo", "systemctl", "start", "jenkins"], check=True)
    print("✅ Jenkins enabled and started")
    main()
