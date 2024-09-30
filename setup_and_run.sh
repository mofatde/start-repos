#!/bin/bash

# Check if the repository URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <repository_url>"
    exit 1
fi

REPO_URL=$1

# Extract repo name from URL
REPO_NAME=$(basename -s .git "$REPO_URL")

rm -rf "$REPO_NAME"

# Step 1: Clone the repository
echo "Cloning repository..."
git clone "$REPO_URL"

# Check if the clone was successful
if [ $? -ne 0 ]; then
    echo "Failed to clone the repository."
    exit 1
fi

# Step 2: Navigate into the repository directory
cd "$REPO_NAME" || { echo "Failed to enter directory"; exit 1; }

echo $(ls)
# Step 3: Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv env

# Step 4: Activate the virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Step 5: Install dependencies (if there's a requirements.txt or environment.yml)
if [ -f "env_data/requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r env_data/requirements.txt
elif [ -f "env_data/environment.yml" ]; then
    echo "Installing dependencies from environment.yml..."
    conda env create -f environment.yml
else
    echo "No requirements.txt or environment.yml found. Skipping dependency installation."
fi

#exit  21
# Step 6: Run the script (assuming script runner.py is in the repo)
echo "Running the script..."
python env_data/run_script.py 

# Step 7: Deactivate the virtual environment
deactivate

