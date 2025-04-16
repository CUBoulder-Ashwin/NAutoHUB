# 🚀 NAutoHUB Setup Guide

This guide walks you through setting up the NAutoHUB environment — both manually and automatically.

---

## 📦 Prerequisites

- Ubuntu 20.04+
- Git installed
- Internet connection

---

## 🛠️ Manual Setup

### 1. Jenkins & Ngrok Configuration

- Run `/NAutoHUB/pilot-config/pilot.sh` to start `ngrok.service`.
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

- Start Jenkins and retrieve the initial admin password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

- Access the Ngrok URL from `/NAutoHUB/ngrok.log`, complete Jenkins setup in browser.

### 2. GitHub Webhook

- Push this repo to your GitHub.
- Go to GitHub → **Settings > Webhooks**
- Use your Ngrok URL + `/github-webhook/`:

```text
https://<your-ngrok>.ngrok-free.app/github-webhook/
```

---

## 🤖 Automated Setup

1. Clone the repo:

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/CUBoulder-Ashwin/NAutoHUB.git
```

2. Run setup scripts:

```bash
cd NAutoHUB/pilot-config
chmod +x requirements.sh pilot.sh
./requirements.sh
./pilot.sh
```

---

## ✅ Notes

- `requirements.sh` installs Docker, Containerlab, Jenkins, Ngrok, InfluxDB, SNMP, Grafana, Java, Python packages, etc.
- `pilot.sh` deploys the initial topology with Containerlab.
- If you hit permission issues, use `sudo`.
