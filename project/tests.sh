#!/bin/bash

# Grant execute permissions for this script
chmod +x run_pipeline.sh

# Step 1: Install required Python libraries
echo "Installing required Python libraries..."
pip install --no-cache-dir -r requirements.txt

# Step 2: Run the pipeline
echo "Running the test cases..."
python ./tests.py

# Step 3: Completion message
echo "Pipeline execution complete."
