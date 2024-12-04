import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Step 1: Load data
file_path = '/Users/xxddzzh/PycharmProjects/combined_csv.csv'
data = pd.read_csv(file_path)

# Step 2: Combine all themes into a single string
# Ensure THEMES column exists and is processed
if "THEMES" in data.columns:
    themes_text = " ".join(data["THEMES"].dropna().str.replace(";", " "))

    # Step 3: Generate the word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis'
    ).generate(themes_text)

    # Step 4: Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud of Themes", fontsize=16)
    plt.show()
else:
    print("The column 'THEMES' does not exist in the dataset.")
