#!/bin/bash

set -e

echo "[1/12] Removing old Docker components..."
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
    sudo apt-get remove -y $pkg || true
done

echo "[2/12] Setting up Docker repository and installing Docker..."
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu   $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

echo "[3/12] Installing Containerlab..."
curl -sL https://containerlab.dev/setup | sudo -E bash -s "all"

echo "[4/12] Setting up InfluxDB repository and installing influxdb2..."
curl -s https://repos.influxdata.com/influxdata-archive.key -o influxdata-archive.key
echo "943666881a1b8d9b849b74caebf02d3465d6beb716510d86a39f6c8e8dac7515  influxdata-archive.key" | sha256sum --check -
cat influxdata-archive.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive.gpg] https://repos.influxdata.com/ubuntu jammy stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
sudo apt-get update && sudo apt-get install -y influxdb2
sudo systemctl enable --now influxdb

echo "[5/12] Installing Grafana..."
sudo apt-get install -y apt-transport-https software-properties-common wget
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install -y grafana
sudo systemctl enable --now grafana-server

echo "[6/12] Installing Ngrok..."
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc > /dev/null
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt-get update && sudo apt-get install -y ngrok

echo "[7/12] Installing Java (OpenJDK 17)..."
sudo apt-get install -y fontconfig openjdk-17-jre
java -version

echo "[8/12] Installing Jenkins..."
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update && sudo apt-get install -y jenkins
sudo systemctl enable --now jenkins

echo "[9/12] Setting up Python environment and SNMP tools..."
sudo apt install -y python3.12-venv
python3 -m venv venv
source venv/bin/activate


echo "[10/12] Installing tools..."
sudo apt-get update
sudo apt-get install -y libsnmp-dev snmp snmpd snmptrapd snmp-mibs-downloader gcc python3-dev syslog-ng
sudo add-apt-repository universe -y
sudo download-mibs
sudo apt install telegraf
sudo apt install git-lfs
sudo apt install gnmic


sudo apt install -y python3-pip netplan.io
sudo systemctl enable systemd-networkd
sudo systemctl start systemd-networkd

echo "[11/12] Installing Python packages from requirements.txt..."
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
REQ_FILE="${SCRIPT_DIR}/requirements.txt"

if [[ -f "$REQ_FILE" ]]; then
    pip install -r "$REQ_FILE"
else
    echo "❗ requirements.txt not found in $SCRIPT_DIR. Skipping Python dependency installation."
fi

echo "[12/12] Fixing permissions so Jenkins can access venv..."
sudo chmod o+rx $HOME
sudo chmod o+rx $HOME/projects
sudo chmod o+rx $HOME/projects/NAutoHUB
sudo chmod o+rx $HOME/projects/NAutoHUB/pilot-config
sudo chmod -R o+rx $HOME/projects/NAutoHUB/pilot-config/venv
sudo usermod -aG docker $USER
newgrp docker

echo "✅ All tools and packages have been successfully installed."