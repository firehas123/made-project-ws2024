#!/bin/bash

echo "Current directory: $(pwd)"

# Ensure the script is executable
chmod +x tests.sh

# Step 1: Set PYTHONPATH
export PYTHONPATH=$(pwd)/project
echo "PYTHONPATH set to $PYTHONPATH"

# Step 2: Install required dependencies
echo "Installing required Python libraries..."
pip install --no-cache-dir -r ./project/requirements.txt

# Step 3: Run the tests
echo "Running the tests..."
pytest ./project/tests.py -v

# Step 4: Completion message
echo "All tests executed successfully."
