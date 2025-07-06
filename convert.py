import csv
import requests
import os
from time import sleep
from random import uniform

# Config
csv_url = 'https://www.niftyindices.com/IndexConstituent/ind_nifty500list.csv'
input_file = 'stocks_raw.csv'
output_file = 'stocks_investing.csv'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/csv,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.niftyindices.com/indices/equity/ind-nifty500',
    'Accept-Language': 'en-US,en;q=0.5',
}

def download_file_if_not_exists(url, file_path, max_retries=3):
    if os.path.exists(file_path):
        print(f"📂 '{file_path}' already exists. Skipping download.")
        return

    for attempt in range(1, max_retries + 1):
        try:
            print(f"⬇️ Attempt {attempt} to download CSV...")
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"✅ Downloaded and saved as '{file_path}'.")
            return
        except requests.RequestException as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                sleep_time = round(uniform(2, 5), 2)
                print(f"🔁 Retrying in {sleep_time}s...")
                sleep(sleep_time)
            else:
                raise Exception("❌ All attempts to download the file failed.")

def convert_to_investing_format(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = ['Name', 'Symbol', 'Exchange']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for row in reader:
            name = row['Company Name'].strip()
            symbol = row['Symbol'].strip() + ".NS"
            writer.writerow({'Name': name, 'Symbol': symbol, 'Exchange': 'NSE'})

    print(f"✅ Converted data saved to '{output_path}'.")

# Main
try:
    download_file_if_not_exists(csv_url, input_file)
    convert_to_investing_format(input_file, output_file)
except Exception as e:
    print(str(e))
