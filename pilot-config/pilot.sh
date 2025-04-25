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

# Check if user is in docker group
if groups $USER | grep -q '\bdocker\b'; then
    echo "✅ User is in the docker group."
else
    echo "❌ You are not in the 'docker' group. Adding now..."
    sudo usermod -aG docker $USER
    echo "♻ Re-executing script in newgrp docker session..."

    # Prevent infinite loop using a flag
    exec newgrp docker <<EONG
./$(basename "$0") _docker_group_ready
EONG
    exit 0
fi

# Skip docker group check on re-entry
if [ "$1" = "_docker_group_ready" ]; then
    shift
fi


echo "✅ Setup complete!"

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running NAutoHUB Flask App..."
python3 ~/projects/NAutoHUB/NSOT/GUI/flask_app/rcn.py


