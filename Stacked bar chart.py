import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/xxddzzh/PycharmProjects/Cleaned_Dataset_With_States.csv'
data = pd.read_csv(file_path)

themes = [
    'TAX_FNCACT', 'EPU_POLICY', 'CRISISLEX_CRISISLEXREC', 'USPEC_POLITICS_GENERAL1',
    'LEADER', 'TAX_ETHNICITY', 'UNG_FORESTS_RIVERS_OCEANS', 'SOC_POINTSOFINTEREST',
    'EDUCATION', 'WB_696_PUBLIC_SECTOR_MANAGEMENT', 'TAX_WORLDLANGUAGES',
    'MANMADE_DISASTER_IMPLIED', 'TAX_FNCACT_PRESIDENT', 'WB_621_HEALTH_NUTRITION_AND_POPULATION',
    'USPEC_POLICY1', 'GENERAL_HEALTH', 'CRISISLEX_C07_SAFETY', 'EPU_ECONOMY_HISTORIC',
    'TAX_DISEASE', 'KILL'
]

filtered_data = data[data['THEMES'].str.contains('|'.join(themes), na=False)]
filtered_data['Theme'] = filtered_data['THEMES'].str.extract(f"({'|'.join(themes)})")

source_theme_counts = (
    filtered_data.groupby(['SOURCES', 'Theme'])
    .size()
    .unstack(fill_value=0)
    .head(15)  
)

source_theme_counts.plot(
    kind='bar',
    stacked=True,
    figsize=(14, 8),
    colormap='tab20',  
    edgecolor='black'
)

plt.title('Stacked Bar Chart of Themes by Sources', fontsize=16)
plt.xlabel('Sources', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.legend(title='Themes', fontsize=10, loc='upper right')
plt.tight_layout()

plt.show()
