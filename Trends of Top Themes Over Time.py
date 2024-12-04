import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/xxddzzh/PycharmProjects/Cleaned_Dataset_With_States.csv'
data = pd.read_csv(file_path)
print("TONE_Score Statistics:")
print(data['TONE_Score'].describe())

print("Extreme TONE_Score values:")
print(data[data['TONE_Score'] < -10])

valid_data = data[data['TONE_Score'] >= -10] 
print(f"Valid records after removing outliers: {valid_data.shape[0]}")
state_tone = valid_data.groupby('State')['TONE_Score'].mean().reset_index()
print("Grouped data by states:")
print(state_tone)


plt.figure(figsize=(14, 8))
plt.bar(state_tone['State'], state_tone['TONE_Score'], color='skyblue')
plt.title('Average Tone Score Across States', fontsize=16)
plt.xlabel('State', fontsize=14)
plt.ylabel('Average Tone Score', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
