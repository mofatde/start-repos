import pandas as pd
import numpy as np
import os

# Generate example data for frameA
df = pd.DataFrame({
    'existing_column': np.random.randint(0, 100, size=100)
})

# Save to .input directory
os.makedirs('input', exist_ok=True)
df.to_csv('input/frameA.csv', index=False)

