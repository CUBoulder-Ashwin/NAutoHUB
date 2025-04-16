# 🚀 NAutoHUB Setup Guide

This guide will help you set up the environment for the NAutoHUB website and automation stack.

---

## 📦 Prerequisites

- Ubuntu (20.04 or later)
- `git` installed
- Internet access for downloading packages

---


## Manual setup

1. **GitHub webhook for jenkins pipeline**
   - `pilot.sh` creates and starts a service called `ngrok.service`
   - For this service to run properly, you need an auth token added to the `/NAutoHUB/ngrok_config.yml`
   - You can get this token by simply accessing this link [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) and creating an account.
   - Copy the token and paste it in the yaml
     
     ```bash
      ---
      version: "2"
      authtoken:  -------> paste here
      region: us
      tunnels:
        jenkins:
          addr: 8080
          proto: http

---

## Automated setup

1. **Create a `projects` folder and clone the repo:**

   ```bash
   mkdir -p ~/projects
   cd ~/projects
   git clone https://github.com/CUBoulder-Ashwin/NAutoHUB.git

2. **Navigate to the setup directory:**

   ```bash
   cd ~/projects/NAutoHUB/pilot-config
   
3. **Make the requirements script executable and run it:**

   ```bash
   chmod +x requirements.sh
   ./requirements.sh

4. **Make the pilot script executable and run it:**

   ```bash
   chmod +x pilot.sh
   ./pilot.sh

---

## ✅ Notes

- Make sure you run all commands from a terminal (Ubuntu or WSL).
- `requirements.sh` sets up everything: Docker, Containerlab, InfluxDB, Grafana, Ngrok, Jenkins, Java, SNMP tools, and Python dependencies.
- `pilot.sh` initializes your project environment. This runs an example topo.yaml file present in the `NAutoHUB/pilot-config`.
- If you get permission errors, try prefixing commands with `sudo`.
