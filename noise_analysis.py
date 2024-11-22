import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('data/noise_data_raw.csv')

# Display the first few rows of the dataset
print(data.head())

# Calculate Leq
def calculate_leq(noise_levels):
    return 10 * np.log10(np.mean(10 ** (noise_levels / 10))

data['Leq'] = data['Noise_Level'].apply(calculate_leq)

# Calculate Noise Climate (NC)
data['NC'] = data['L10'] - data['L90']

# Calculate Noise Pollution Level (NP)
data['NP'] = data['Leq'] * 2.56 * data['std_dev']

# Save processed data
data.to_csv('data/processed_noise_data.csv', index=False)

# Summary statistics
print(data.describe())
