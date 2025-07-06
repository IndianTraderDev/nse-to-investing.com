# Nifty 500 CSV Converter for Investing.com

This script automates downloading and converting Nifty 500 stock constituents into a format compatible with Investing.com's Portfolio Import.

## 🔧 Features

- Downloads Nifty 500 CSV from NSE/NiftyIndices
- Converts it to format: `"Name","Symbol","Exchange"`
- Adds `.NS` suffix for NSE compatibility
- Handles site restrictions and retries if needed
- Skips download if `stocks_raw.csv` already exists

## 📁 Output

Produces a file named `stocks_investing.csv` that can be directly uploaded to [Investing.com Portfolio Import](https://www.investing.com/portfolio-import/).

## 🛠️ Requirements

- Python 3.7+
- `requests` library

## 📦 Installation

```bash
git clone https://github.com/your-username/nifty-csv-converter.git
cd nifty-csv-converter
pip install -r requirements.txt
python convert.py
