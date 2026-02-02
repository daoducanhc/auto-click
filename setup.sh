#!/bin/bash

# Setup script for auto-clicker
# This script creates a virtual environment and installs dependencies

echo "================================"
echo "Auto-Clicker Setup"
echo "================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed!"
    echo "Please install Python3 first."
    exit 1
fi

echo "Python3 found: $(python3 --version)"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ -d ".venv" ]; then
    echo "Virtual environment already exists. Skipping creation."
else
    python3 -m venv .venv
    echo "Virtual environment created successfully!"
fi

# Activate virtual environment and install requirements
echo ""
echo "Installing dependencies..."
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "================================"
echo "Setup Complete!"
echo "================================"
echo ""
echo "To run the auto-clicker:"
echo "  ./run.sh"
echo ""
echo "Or manually:"
echo "  source .venv/bin/activate"
echo "  python auto_clicker.py"
echo ""
