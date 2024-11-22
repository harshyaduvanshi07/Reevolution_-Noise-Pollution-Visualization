import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data_path = 'data/noise_data_raw.csv'
noise_data = pd.read_csv(data_path)

# Display basic information about the dataset
print(noise_data.info())
print(noise_data.describe())

# Visualize noise levels by category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Noise_Level', data=noise_data)
plt.title('Noise Levels by Category in Mumbai')
plt.xlabel('Category')
plt.ylabel('Noise Level (dB)')
plt.xticks(rotation=45)
plt.savefig('visuals/noise_visualization.png')
plt.show()

# Save summary statistics to CSV
summary_stats = noise_data.groupby('Category')['Noise_Level'].describe()
summary_stats.to_csv('output/noise_summary_statistics.csv')
