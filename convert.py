import csv

input_file = 'stocks_raw.csv'        # replace with your file path
output_file = 'stocks_investing.csv' # desired output CSV

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['Name', 'Symbol', 'Exchange']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    
    writer.writeheader()
    
    for row in reader:
        name = row['Company Name'].strip()
        symbol = row['Symbol'].strip() + ".NS"
        exchange = "NSE"
        
        writer.writerow({
            'Name': name,
            'Symbol': symbol,
            'Exchange': exchange
        })

print(f"✅ Converted data saved to {output_file}")
