#!/usr/bin/env python3
"""
Extract text from PDFs and load CSV data to inspect raw content.
"""
import os
from pathlib import Path
from pypdf import PdfReader
import pandas as pd

# Set up paths
raw_data_dir = Path("raw_data")
os.makedirs(raw_data_dir, exist_ok=True)

print("=" * 80)
print("EXTRACTING TEXT FROM PDFs")
print("=" * 80)

# 1. Extract Tesla Q1 2024 Update PDF
tesla_pdf_path = raw_data_dir / "TSLA-Q1-2024-Update.pdf"
if tesla_pdf_path.exists():
    print(f"\n✓ Found: {tesla_pdf_path}")
    reader = PdfReader(tesla_pdf_path)
    print(f"  Pages: {len(reader.pages)}")
    
    # Extract first 5 pages to find production/sales data
    tesla_text = ""
    for i in range(min(5, len(reader.pages))):
        page = reader.pages[i]
        text = page.extract_text()
        tesla_text += f"\n--- PAGE {i+1} ---\n{text}"
    
    # Save extracted text
    tesla_txt_path = raw_data_dir / "TSLA-Q1-2024-Update.txt"
    with open(tesla_txt_path, "w") as f:
        f.write(tesla_text)
    print(f"  ✓ Extracted text saved to: {tesla_txt_path}")
else:
    print(f"✗ Not found: {tesla_pdf_path}")

# 2. Extract KBB Q1 2024 EV Sales Report PDF
kbb_pdf_path = raw_data_dir / "Q1-2024-KBB-EV-Sales-Report.pdf"
if kbb_pdf_path.exists():
    print(f"\n✓ Found: {kbb_pdf_path}")
    reader = PdfReader(kbb_pdf_path)
    print(f"  Pages: {len(reader.pages)}")
    
    # Extract first 3 pages for competitor/market data
    kbb_text = ""
    for i in range(min(3, len(reader.pages))):
        page = reader.pages[i]
        text = page.extract_text()
        kbb_text += f"\n--- PAGE {i+1} ---\n{text}"
    
    # Save extracted text
    kbb_txt_path = raw_data_dir / "Q1-2024-KBB-EV-Sales-Report.txt"
    with open(kbb_txt_path, "w") as f:
        f.write(kbb_text)
    print(f"  ✓ Extracted text saved to: {kbb_txt_path}")
else:
    print(f"✗ Not found: {kbb_pdf_path}")

print("\n" + "=" * 80)
print("LOADING CSV DATA")
print("=" * 80)

# 3. Load historic sales CSV
historic_csv_path = raw_data_dir / "historic_sales.csv"
if not historic_csv_path.exists():
    print(f"\n↓ Downloading historic sales CSV from GitHub...")
    import requests
    url = "https://raw.githubusercontent.com/evelynbartley/Final-Project-607/main/IEA-EV-dataEV%20salesCarsHistorical.csv"
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(historic_csv_path, "w") as f:
            f.write(response.text)
        print(f"  ✓ Downloaded: {historic_csv_path}")
    except Exception as e:
        print(f"  ✗ Failed to download: {e}")
else:
    print(f"\n✓ Found: {historic_csv_path}")

# Load and preview the CSV
try:
    df = pd.read_csv(historic_csv_path)
    print(f"\n  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"\n  Sample rows:")
    print(df.head(10))
except Exception as e:
    print(f"  ✗ Error loading CSV: {e}")

print("\n" + "=" * 80)
print("DATA EXTRACTION COMPLETE")
print("=" * 80)
