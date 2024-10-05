#!/bin/bash

# Setup script for Warzone: The Battle of Cards environment

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r ../requirements.txt

echo "Environment setup complete. Activate it with 'source venv/bin/activate'"