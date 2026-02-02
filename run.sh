#!/bin/bash

# Run script for auto-clicker
# This script activates the virtual environment and runs the program

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found!"
    echo "Please run ./setup.sh first"
    exit 1
fi

# Activate virtual environment and run the program
source .venv/bin/activate
python auto_clicker.py
