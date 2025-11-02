# Tesla EV Market Analysis - Project Overview

**Status**: Initial Findings Complete ✅  
**Last Updated**: November 2, 2025

## Quick Start

### View the Analysis
1. **Main Report**: `REPORT_INITIAL_FINDINGS.md` - comprehensive findings with tables & recommendations
2. **Jupyter Notebook**: `analysis.ipynb` - interactive data exploration and charts
3. **Summary Visualizations**: `plots/SUMMARY_KEY_FINDINGS.png` - executive dashboard

### Run the Analysis

```bash
# Activate virtual environment
source .venv/bin/activate

# Run Jupyter Lab
python -m jupyter lab

# Or run Python scripts directly
python extract_and_load.py
python extract_specific_data.py
python create_summary_viz.py
```

## Project Structure

```
tesla-ev-market-analysis/
├── .venv/                          # Python virtual environment (60+ packages)
├── raw_data/
│   ├── TSLA-Q1-2024-Update.pdf    # Tesla investor relations Q1-2024
│   ├── TSLA-Q1-2024-Update.txt    # Extracted text from PDF
│   ├── Q1-2024-KBB-EV-Sales-Report.pdf  # Kelley Blue Book sales data
│   ├── Q1-2024-KBB-EV-Sales-Report.txt  # Extracted text from PDF
│   └── historic_sales.csv         # Global EV sales 2010-2022 (IEA data)
├── plots/
│   ├── 01_global_bev_sales.png    # Global BEV trend 2010-2022
│   ├── 02_global_vs_usa_sales.png # Global vs USA market comparison
│   ├── 03_regional_trends.png     # Top 8 markets regional trends
│   └── SUMMARY_KEY_FINDINGS.png   # Executive summary dashboard
├── analysis.ipynb                  # Interactive Jupyter notebook
├── extract_and_load.py            # PDF extraction and data loading script
├── extract_specific_data.py       # Tesla & competitor data extraction
├── create_summary_viz.py          # Summary visualization generation
├── requirements.txt               # Python dependencies (frozen versions)
├── REPORT_INITIAL_FINDINGS.md    # Comprehensive analysis report
└── README.md                      # This file
```

## Key Findings Summary

### Question: Why are Tesla's EV sales and prices declining despite market growth?

### Answer: Market Maturation + Competitive Disruption

**Tesla Q1-2024 Performance:**
- Sales: **140,187 units (-13.3% YoY)**
- Market share (USA): **51.3% (down from 61.7% Q1-23)**
- Operating margin: **5.5% (down from 10.9%)**
- Free cash flow: **-$2.5B**

**Market Context:**
- Global BEV growth: **+59% (2021-22)**, 4.6M → 7.3M units
- USA BEV growth: **+70% (2021-22)**, 470k → 800k units
- Global CAGR 2010-22: **~60% annually**

### Four Hypotheses - All Validated:

| Hypothesis | Status | Evidence |
|-----------|--------|----------|
| **Competition Growing** | ✅ CRITICAL | Ford +86%, Mercedes +66%, BMW +62% (Q1-24) |
| **Price Wars Active** | ✅ HIGH | 3 price cuts in 12 mo; margins halved |
| **Inventory Buildup** | ✅ HIGH | $2.7B inventory increase Q1; -$2.5B FCF |
| **Charging Gaps** | ✅ MEDIUM | 51k stations in USA; underserved rural areas |

### Market Structure Shift:

**Wave 1 Buyers (Saturating - Tesla's core market):**
- Early adopters, premium segment, tech enthusiasts
- Tesla: 65-70% share

**Wave 2 Buyers (Growing - Mainstream, price-sensitive):**
- Value conscious, feature focused, comparing options
- Ford Mach-E, Hyundai Ioniq 5, Kia EV9, BMW i4
- Tesla: 40-50% share (declining)

## Data Sources

1. **Global EV Historic Sales**: GitHub IEA dataset (2010-2022)
   - 834 rows, 8 columns
   - Covers 35+ countries, BEV & PHEV vehicles

2. **Tesla Q1-2024 Update**: Tesla IR PDF
   - Production, delivery, financial metrics
   - Operating margin, cash flow data

3. **KBB Q1-2024 EV Sales Report**: Kelley Blue Book PDF
   - USA market sales by brand & model
   - YoY growth rates, market share
   - Competitor breakdown

4. **CNET EV Charging Article**: Infrastructure snapshot
   - 51,000 public charging stations in USA
   - Regional distribution analysis

## Methodology

### Data Cleaning
- Loaded 834 CSV records into pandas DataFrames
- Filtered for World + USA BEV sales only
- Pivot tables for year-over-year analysis
- Calculated CAGR and growth rates

### Analysis
- Comparative trend analysis (Tesla vs. competitors)
- Market share calculations and erosion tracking
- Hypothesis testing against available evidence
- Regional market analysis

### Visualizations
- Line plots: Global and regional sales trends
- Bar charts: Competitor growth comparison
- Market share stacked bar charts
- Summary dashboard: 6-panel executive view

## Limitations & Next Steps

### Current Limitations
- Global data only through 2022 (2024 market snapshot USA only)
- Limited pricing data (qualitative, not quantitative)
- No incentive impact quantification by state
- No regression modeling (correlation vs. causation)

### Recommended Next Steps
1. **Regression Analysis**: Price elasticity, competition effect, incentive impact
2. **Pricing Correlation**: Correlate price cuts with volume changes
3. **Real-time Tracking**: 2024-2025 quarterly updates
4. **Incentive Quantification**: By state, dealer, manufacturer
5. **Profitability Analysis**: Margin impact by model, region
6. **Forecast Modeling**: 2025-2026 market share projections

## Tools & Technologies

- **Python 3.13**: Core analysis language
- **Pandas**: Data manipulation and pivot tables
- **Matplotlib & Seaborn**: Visualization
- **Jupyter Lab**: Interactive notebook environment
- **PDF Extraction**: PyPDF library
- **Other**: NumPy, scikit-learn (for future regression models)

## Contact & Questions

For questions about methodology, data, or findings, refer to:
- `REPORT_INITIAL_FINDINGS.md` for detailed analysis
- `analysis.ipynb` for interactive exploration
- `plots/SUMMARY_KEY_FINDINGS.png` for executive summary

---

**Analysis By**: Tesla EV Market Analysis Project  
**Date**: November 2, 2025  
**Status**: Initial Findings Published | Full Report Pending
