#!/bin/bash

set -e  # Exit on any error
echo "Pulling big files"
git lfs install
git lfs pull

echo "Building Docker images for hosts..."
sudo docker build -f Dockerfile_Hosts -t hosts:latest .

echo "Creating ceos:4.33.2F image"
sudo docker import ../NSOT/disc_images/cEOS64-lab-4.33.2F.tar.xz ceos:4.33.2F

echo "Creating netplan configs..."
sudo cp netcfg.yaml /etc/netplan/100-netcfg.yaml
sudo chmod 600 /etc/netplan/100-netcfg.yaml
echo "Applying netplan..."
sudo netplan apply

echo "Running pilot.py..."
python3 pilot.py

echo "✅ Setup complete!"

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running NAutoHUB Flask App..."
python3 ~/projects/NAutoHUB/NSOT/GUI/flask_app/nahub.py


