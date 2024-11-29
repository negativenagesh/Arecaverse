#!/bin/bash

# Update and install Python 3.12
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.12 python3.12-venv python3.12-distutils

# Create and activate virtual environment
python3.12 -m venv areca
source areca/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
fi

# Install dependencies if required.txt exists
if [ -f "required.txt" ]; then
  pip install -r required.txt
fi

# Confirm Python version
python --version