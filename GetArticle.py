import os
import requests
import zipfile
import pandas as pd
from datetime import datetime, timedelta

output_folder = "gdelt_data"
os.makedirs(output_folder, exist_ok=True)

base_url = "http://data.gdeltproject.org/gkg/"
start_date = datetime.strptime("20240505", "%Y%m%d")
end_date = start_date + timedelta(days=32)

urls = [
    f"{base_url}{(start_date + timedelta(days=i)).strftime('%Y%m%d')}.gkg.csv.zip"
    for i in range((end_date - start_date).days + 1)
]

def download_file(url, dest):
    response = requests.get(url)
    response.raise_for_status()  # If there is a problem during the download process, an HTTPError will be raised
    with open(dest, "wb") as f:
        f.write(response.content)

def is_valid_zip(file_path):
    try:
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            return True
    except zipfile.BadZipFile:
        return False

for url in urls:
    file_name = url.split("/")[-1]
    zip_path = os.path.join(output_folder, file_name)

    print(f"Downloading {url}...")
    try:
        download_file(url, zip_path)
        print(f"Downloaded {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        continue

    if is_valid_zip(zip_path):
        print(f"Extracting {file_name}...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(output_folder)
        print(f"Extracted {file_name}")

        os.remove(zip_path)
        print(f"Deleted {file_name}")
    else:
        print(f"{file_name} is not a valid zip file and will be deleted.")
        os.remove(zip_path)

# 找到所有 CSV 文件
csv_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith('.csv')]

# 合并所有 CSV 文件
combined_csv_path = os.path.join(output_folder, 'combined_gdelt_data.csv')
combined_csv = pd.concat([pd.read_csv(f, sep='\t', on_bad_lines='skip') for f in csv_files])
combined_csv.to_csv(combined_csv_path, index=False)

print(f"All files have been downloaded, extracted, and combined into {combined_csv_path}")

# 删除其他单独的 CSV 文件，仅保留汇总的文件
for file in csv_files:
    if file != combined_csv_path:
        os.remove(file)
        print(f"Deleted {file}")

print("All individual CSV files have been deleted, only the combined file remains.")
