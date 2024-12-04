import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = '/Users/xxddzzh/PycharmProjects/Cleaned_Dataset_With_States.csv'
data = pd.read_csv(file_path)

# Step 2: Define the top 10 themes manually
themes = [
     'TAX_FNCACT', 'EPU_POLICY', 'CRISISLEX_CRISISLEXREC', 'USPEC_POLITICS_GENERAL1',
    'LEADER', 'TAX_ETHNICITY', 'UNG_FORESTS_RIVERS_OCEANS', 'SOC_POINTSOFINTEREST',
    'EDUCATION', 'WB_696_PUBLIC_SECTOR_MANAGEMENT', 'TAX_WORLDLANGUAGES',
    'MANMADE_DISASTER_IMPLIED', 'TAX_FNCACT_PRESIDENT', 'WB_621_HEALTH_NUTRITION_AND_POPULATION',
    'USPEC_POLICY1', 'GENERAL_HEALTH', 'CRISISLEX_C07_SAFETY', 'EPU_ECONOMY_HISTORIC',
    'TAX_DISEASE', 'KILL'
]

# Step 3: Filter data for the selected themes
filtered_data = data[data['THEMES'].str.contains('|'.join(themes), na=False)]

# Step 4: Extract the relevant theme for each record
filtered_data['Theme'] = filtered_data['THEMES'].str.extract(f"({'|'.join(themes)})")

# Step 5: Group data by date and theme, and calculate the average tone score
filtered_data['DATE'] = pd.to_datetime(filtered_data['DATE'])
time_series_data = filtered_data.groupby(['DATE', 'Theme'])['TONE_Score'].mean().unstack(fill_value=0)

# Step 6: Plot the streamgraph
plt.figure(figsize=(14, 8))
plt.stackplot(
    time_series_data.index,
    time_series_data.T,
    labels=time_series_data.columns,
    alpha=0.8,
    edgecolor='w'
)

# Customize the plot
plt.title('Streamgraph of Top 20 Themes Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Tone Score', fontsize=12)
plt.legend(loc='upper left', fontsize=9, title="Themes")
plt.tight_layout()

# Show the plot
plt.show()
