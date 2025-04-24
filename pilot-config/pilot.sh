#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Import the hosts and webserver dockers
echo "Building Docker images for hosts and webserver..."
sudo docker build -f Dockerfile_Hosts -t hosts:latest .
#sudo docker build -f Dockerfile_WebServer -t server:latest .

# # Add the netcfg file to /etc/netplan and apply
echo "Creating netplan configs..."
sudo cp netcfg.yaml /etc/netplan/100-netcfg.yaml
sudo chmod 600 /etc/netplan/100-netcfg.yaml
echo "Applying netplan..."
sudo netplan apply

# Deploy the clab topo.yml file
# echo "Deploying container lab topology..."
# sudo clab deploy -t ceos-example.yaml

# Run pilot.py
echo "Running pilot.py..."
python3 pilot.py

#Running NAutoHUB
echo "Running NAutoHUB"
source venv/bin/activate
python3 ~/projects/NAutoHUB/NSOT/GUI/flask_app/rcn.py


echo "Setup complete!"
