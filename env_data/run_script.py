import os
import subprocess
from dotenv import load_dotenv

# Load the .exc file (same as .env format)
load_dotenv(dotenv_path='env_data/.env')

# Read the environment variables
working_directory = os.getenv('wd')
script = os.getenv('script')
params = os.getenv('params')

# Change to the working directory
os.chdir(working_directory)

# Build the command
command = f"python {script} {params}"

# Execute the script with the params
try:
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Output:\n", result.stdout.decode())
    print("Errors (if any):\n", result.stderr.decode())
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e.stderr.decode()}")

