import pandas as pd
import matplotlib.pyplot as plt


file_path = '/Users/xxddzzh/PycharmProjects/Cleaned_Dataset_With_States.csv'
data = pd.read_csv(file_path)
if "THEMES" in data.columns:
    themes_split = data["THEMES"].dropna().str.split(";")
    all_themes = themes_split.explode().str.strip()  
    all_themes = all_themes[all_themes != ""]
    theme_counts = all_themes.value_counts()
    top_20_themes = theme_counts.head(20)
    plt.figure(figsize=(12, 6))
    top_20_themes.plot(kind="bar", color="skyblue")
    plt.title("Top 20 Themes By Frequency", fontsize=16)
    plt.xlabel("Themes", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

else:
    print("The column 'THEMES' does not exist in the dataset.")
