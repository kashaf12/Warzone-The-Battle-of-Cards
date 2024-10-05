#!/bin/bash

# Generate executable script for Warzone: The Battle of Cards

# Activate virtual environment
source venv/bin/activate

# Install PyInstaller if not already installed
pip install pyinstaller

# Generate executable
pyinstaller --onefile --windowed --add-data "../static:static" ../src/main.py

# Deactivate virtual environment
deactivate

echo "Executable generated in the 'dist' directory"