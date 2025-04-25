# 🚀 NAutoHUB Setup Guide

This guide walks you through setting up the NAutoHUB

---

## 📦 Prerequisites

- Ubuntu 20.04+
- Git installed
- Internet connection (LOL)

---

## 🤖 Automated Setup

1. Clone the repo:

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/CUBoulder-Ashwin/NAutoHUB.git
```

2. Create executables:

```bash
cd NAutoHUB/pilot-config
chmod +x requirements.sh pilot.sh
```

3. `requirements.sh` installs Docker, Containerlab, InfluxDB, Grafana, Ngrok, Java, Jenkins and Python packages like snmp-mibs, easysnmp, netmiko, flask etc.

```bash
./requirements.sh
```

4. `pilot.sh`,
   - creates docker images necessary
   - creates managment network interfaces and add routes for the containerlabs
   - runs an example containerlab topology
   - creates crafted services like ipam, snmp, ngrok, device health checks, etc
   - initiates the frontend

```bash
./pilot.sh
```

---

## 🛠️ Manual Setup (Optional) 

### 1. Jenkins & Ngrok Configuration

- Get your [Ngrok auth token](https://dashboard.ngrok.com/get-started/your-authtoken) and paste it into `/NAutoHUB/ngrok_config.yml`:

```yaml
version: "2"
agent:
  authtoken: <your_token>
  region: us
tunnels:
  jenkins:
    addr: 8080
    proto: http
```
- Restart the service

  ```bash
  sudo systemctl restart ngrok.service
  
- Retrieve the initial admin password from jenkins service:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

- Access the Ngrok URL from `/NAutoHUB/ngrok.log`, complete Jenkins setup in browser.

### 2. GitHub Webhook

- Push this repo to GitHub.
- Go to GitHub → **Settings > Webhooks**
- Use your Ngrok URL + `/github-webhook/`:

```text
https://<your-ngrok>.ngrok-free.app/github-webhook/
```

---

## ✅ Troubleshooting

- If you're running into permission errors or your WSL Ubuntu user can't run sudo, it likely means your user isn't in the sudoers group. 

Run the following in Command Prompt or PowerShell as Administrator:

```bash
  wsl -u root
  usermod -aG sudo <your_wsl_username>
```
