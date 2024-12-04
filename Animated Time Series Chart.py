import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = '/Users/xxddzzh/PycharmProjects/Cleaned_Dataset_With_States.csv'
data = pd.read_csv(file_path)

# Step 2: Filter the dataset for the target theme
target_theme = 'TAX_FNCACT'  # Replace with your desired theme
filtered_data = data[data['THEMES'].str.contains(target_theme, na=False)]

# Step 3: Count occurrences of sources
source_counts = filtered_data['SOURCES'].value_counts().head(20)

# Step 4: Log transform and plot
plt.figure(figsize=(12, 8))
(source_counts + 1).apply(np.log).plot(kind='bar', color='skyblue', edgecolor='black')  # 对数变换

# Customize the plot
plt.title(f'Top 10 Sources for Theme "{target_theme}" (Log Scale)', fontsize=16)
plt.xlabel('Sources', fontsize=12)
plt.ylabel('Log Count', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

# Show the plot
plt.show()
