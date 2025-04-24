#!/bin/bash

set -e  # Exit on any error

echo "Building Docker images for hosts..."
sudo docker build -f Dockerfile_Hosts -t hosts:latest .

sudo docker import ../disc_images/cEOS64-lab-4.33.2F.tar ceos.4.33.2F
echo "Creating netplan configs..."
sudo cp netcfg.yaml /etc/netplan/100-netcfg.yaml
sudo chmod 600 /etc/netplan/100-netcfg.yaml
echo "Applying netplan..."
sudo netplan apply

echo "Running pilot.py..."
python3 pilot.py

# Check if user is in docker group
if groups $USER | grep -q '\bdocker\b'; then
    echo "✅ User is in the docker group."
else
    echo "❌ You are not in the 'docker' group. Adding now..."
    sudo usermod -aG docker $USER
    echo "⚠️ You must now log out and log back in (or run 'newgrp docker') for changes to take effect."
    exit 1
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running NAutoHUB Flask App..."
python3 ~/projects/NAutoHUB/NSOT/GUI/flask_app/rcn.py

echo "✅ Setup complete!"
