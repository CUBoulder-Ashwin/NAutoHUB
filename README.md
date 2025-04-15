# 🚀 NAutoHUB Setup Guide

This guide will help you set up the environment for the NAutoHUB website and automation stack.

---

## 📦 Prerequisites

- Ubuntu (20.04 or later)
- `git` installed
- Internet access for downloading packages

---

## 🛠️ Installation Steps

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
