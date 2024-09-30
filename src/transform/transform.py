import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv("env_data/.env")

# Input and output directories
input_dir = os.getenv("INPUT_DIR")
output_dir = os.getenv("OUTPUT_DIR")
print(input_dir)

# Load input data
df = pd.read_csv(f"{input_dir}/frameA.csv")

# Example transformation
df['new_column'] = df['existing_column'] * 2

# Save transformed data
df.to_csv(f"{output_dir}/frameA.csv", index=False)

