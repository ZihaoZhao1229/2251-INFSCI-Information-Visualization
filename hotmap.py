import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Step 1: Load the dataset
file_path = '/Users/xxddzzh/PycharmProjects/Cleaned_Dataset_With_States.csv'
data = pd.read_csv(file_path)

# Step 2: Combine all themes into a single list
all_themes = ";".join(data['THEMES'].dropna()).split(";")

# Step 3: Count the frequency of each theme
theme_counts = Counter(all_themes)

# Step 4: Create a DataFrame for the top 20 themes
theme_df = pd.DataFrame(theme_counts.most_common(20), columns=['Theme', 'Count'])

# Step 5: Plot the donut chart
plt.figure(figsize=(8, 8))
# Pie chart
wedges, texts, autotexts = plt.pie(
    theme_df['Count'],
    labels=theme_df['Theme'],
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops=dict(width=0.4)  # Make it a donut by reducing width
)

# Customize text
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=9)

# Add a title
plt.title('Top 20 Themes Distribution', fontsize=16)

# Show the chart
plt.tight_layout()
plt.show()
