# Christchurch Property Analysis Project - Python Module

This repository contains Python scripts for analyzing property prices in Christchurch, New Zealand, focusing on the relationship between property prices and various demographic, economic, and land type factors.

## Project Structure

```
Python/
├── analysis/                    # Analysis modules
│   ├── base_analysis.py        # Base analysis class
│   ├── property_analysis.py    # Time-based analysis
│   ├── income_analysis.py      # Income analysis
│   ├── ethnicity_analysis.py   # Ethnicity composition analysis
│   └── landtype_analysis.py    # Land type analysis
├── integrate_data.py           # Data integration script
├── regression_statsmodels.py   # Statistical analysis
├── main.py                     # Main program entry
└── README.md                   # This documentation
```

## Analysis Modules

### 1. Property Analysis (`property_analysis.py`)
- Analyzes price changes between 2018 and 2023
- Generates visualizations showing:
  * Price change trends
  * Suburb-level comparisons
  * Growth rate distributions

### 2. Income Analysis (`income_analysis.py`)
- Examines relationship between income and property prices
- Features:
  * Income-price correlations
  * Price changes by income groups
  * Income distribution analysis

### 3. Ethnicity Analysis (`ethnicity_analysis.py`)
- Analyzes impact of ethnicity composition on property prices
- Includes:
  * Ethnicity cluster analysis
  * Price variations by ethnicity composition
  * Correlation analysis between ethnicity percentages and prices

### 4. Land Type Analysis (`landtype_analysis.py`)
- Investigates influence of land type on property prices
- Analyzes:
  * Price distributions by land type (TC1/TC2 vs TC2/TC3)
  * Price changes across land types
  * Median price comparisons

## Data Integration

### Overview
The `integrate_data.py` script combines multiple datasets:
- Property sales data
- Demographic information
- Income statistics
- Land type classifications

### Data Sources
1. **Property Data**: Suburb-level sales information
2. **Ethnicity Data**: Demographic composition percentages
3. **Income Data**: Weighted median income by suburb
4. **Land Type Data**: Land classification indicators

## Statistical Analysis

### Regression Analysis (`regression_statsmodels.py`)
- Multiple linear regression analysis
- Features analyzed:
  * Demographic percentages
  * Income levels
  * Land type classification
- Outputs:
  * Regression coefficients
  * Model diagnostics
  * Statistical summaries

## Output Structure

```
output/
├── visualizations/
│   ├── property_analysis/
│   ├── income_analysis/
│   ├── ethnicity_analysis/
│   └── landtype_analysis/
└── regression_results/
    └── ethnicity_models/
```

## Usage

1. **Run Complete Analysis**
```bash
python main.py
```

2. **Individual Analysis**
```bash
python regression_statsmodels.py  # For regression analysis
```

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- statsmodels
- scikit-learn
- scipy
- jupyter
- tqdm

## Notes

- All analyses are performed at the suburb level
- Results include both statistical summaries and visualizations
- Outputs are organized by analysis type in the output directory
- Comprehensive documentation is available in the main README.md 