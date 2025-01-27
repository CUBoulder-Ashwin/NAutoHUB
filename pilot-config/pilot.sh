#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Import the hosts and webserver dockers
echo "Building Docker images for hosts and webserver..."
sudo docker build -f pilot-config/Dockerfile_Hosts -t hosts:latest .
sudo docker build -f pilot-config/Dockerfile_WebServer -t server:latest .

# # Add the netcfg file to /etc/netplan and apply
# echo "Creating netplan configs..."
# sudo cp pilot-config/netcfg.yaml /etc/netplan/02-netcfg.yaml
# sudo chmod 600 /etc/netplan/02-netcfg.yaml
# echo "Applying netplan..."
# sudo netplan apply

#Create management network
echo "Creating management network..."
sudo ip link add eth0 type dummy
sudo ip link add link eth0 name eth0.100 type vlan id 100
sudo ip addr add 10.0.101.200/24 dev eth0.100
sudo ip link set eth0 up
sudo ip link set eth0.100 up
sudo ip route add 10.0.100.0/24 via 10.0.101.100 dev eth0.100


# Create a virtual environment and activate it
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install required libraries
echo "Installing dependencies..."
sudo apt-get update
sudo apt-get install -y libsnmp-dev snmp-mibs-downloader gcc python3-dev
sudo apt install -y python3-pip yq
pip install easysnmp netmiko flask requests

# Deploy the clab topo.yml file
echo "Deploying container lab topology..."
sudo clab deploy -t pilot-config/topo.yml

# Run pilot.py
echo "Running pilot.py..."
python3 pilot-config/pilot.py

#Running NAutoHUB
echo "Running NAutoHUB"
python3 NSOT/GUI/flask_app/rcn.py



echo "Setup complete!"
