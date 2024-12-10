#!/bin/bash

# Ensure the script is executable
chmod +x tests.sh

# Step 1: Set PYTHONPATH
export PYTHONPATH=$(pwd)/project
echo "PYTHONPATH set to $PYTHONPATH"

# Step 2: Install required dependencies
echo "Installing required Python libraries..."
pip install --no-cache-dir -r requirements.txt

# Step 3: Run the tests
echo "Running the tests..."
python project/tests/tests.py

# Step 4: Completion message
echo "All tests executed successfully."
