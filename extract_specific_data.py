#!/usr/bin/env python3
"""
Extract Tesla and KBB data from PDFs and summarize key findings.
"""
from pathlib import Path

raw_data_dir = Path("raw_data")

print("=" * 100)
print("EXTRACTING TESLA Q1-2024 PRODUCTION & SALES FIGURES")
print("=" * 100)

# Read Tesla PDF text
tesla_txt_path = raw_data_dir / "TSLA-Q1-2024-Update.txt"
with open(tesla_txt_path, 'r') as f:
    tesla_text = f.read()

# Look for key sections
lines = tesla_text.split('\n')
print("\n✓ Searching for production and delivery figures...")

# Find lines with key metrics
key_lines = []
for i, line in enumerate(lines):
    if any(kw in line.lower() for kw in ['production', 'delivery', 'unit', 'q1', 'q2', 'q3', 'q4', '2024', '2023', '2022']):
        if len(line.strip()) > 15 and not line.startswith(' ' * 20):
            key_lines.append((i, line.strip()))

print(f"\nFound {len(key_lines)} lines with key metrics:")
print("\nFirst 50 relevant lines:")
for i, (line_num, line) in enumerate(key_lines[:50]):
    if line:
        print(f"  {line[:110]}")

# Extract specific numbers that look like production figures
import re
numbers = re.findall(r'\b(\d{3,})\b', tesla_text)
unique_numbers = sorted(set(int(n) for n in numbers if 100000 < int(n) < 10000000), reverse=True)
print(f"\nLarge numbers found (potential production/sales figures):")
print(f"  Top 20 values: {unique_numbers[:20]}")

print("\n" + "=" * 100)
print("EXTRACTING COMPETITOR DATA FROM KBB REPORT")
print("=" * 100)

kbb_txt_path = raw_data_dir / "Q1-2024-KBB-EV-Sales-Report.txt"
with open(kbb_txt_path, 'r') as f:
    kbb_text = f.read()

print("\n✓ KBB report content (first 3000 chars):")
print(kbb_text[:3000])

# Look for competitor info
print("\n✓ Searching for manufacturer names and market data...")
lines_kbb = kbb_text.split('\n')
manufacturers = ['Tesla', 'GM', 'Ford', 'VW', 'BMW', 'Audi', 'Hyundai', 'Kia', 'BYD', 'Chevrolet', 'Nissan', 'Toyota', 'Volkswagen', 'General Motors', 'Chevrolet', 'Lucid', 'Rivian', 'Mercedes', 'Porsche']

relevant_kbb = []
for line in lines_kbb:
    if any(mfr in line for mfr in manufacturers) or any(kw in line.lower() for kw in ['sales', 'market share', 'incentive', 'price', 'top', 'leader']):
        if len(line.strip()) > 15:
            relevant_kbb.append(line.strip())

print(f"\nRelevant KBB lines ({len(relevant_kbb)} total):")
for line in relevant_kbb[:40]:
    if line:
        print(f"  {line[:120]}")

print("\n" + "=" * 100)
print("DATA EXTRACTION SUMMARY")
print("=" * 100)
print("\n✓ Files successfully extracted and ready for analysis")
print("✓ Next: Parse specific Tesla Q1-2024 and annual figures")
print("✓ Next: Extract competitor breakdown and market share from KBB")
print("✓ Next: Compare with historic sales trends to identify decline drivers")
