#  Christchurch Suburb Property Analysis
## Christchurch Suburb Property Analysis (R + Python)

This project analyzes property price variations across Christchurch suburbs and explores how demographic factors (ethnicity), household income, and land classifications influence housing prices. The analysis spans from 2018 to 2023, providing insights into price trends and their determinants.

## Project Goals

- Clean and unify multiple datasets across years and domains
- Integrate property, income, ethnicity, and land type data at the suburb level
- Perform multi-year regression analysis to identify factors influencing property prices
- Analyze the impact of various factors on housing prices:
  * Time-based changes (2018-2023)
  * Income levels
  * Racial composition
  * Land type classifications

## 🛠️ Technologies Used

| Language | Purpose                                     |
|----------|---------------------------------------------|
| **R**    | Data cleaning and transformation of raw data |
| **Python** | Data integration, statistical modeling, and visualization |

## Project Structure

```
Data_Analysis_Project/
├── Data/                   # All datasets
│   ├── raw/               # Original downloaded files
│   ├── manual_cleaned/    # Cleaned manually
│   ├── cleaned/           # Cleaned using R scripts
│   └── integrated/        # Final merged datasets
├── R/                     # R scripts for data cleaning
│   └── README.md          # R scripts documentation
├── Python/                # Python analysis scripts
│   ├── analysis/          # Analysis modules
│   │   ├── time_analysis.py
│   │   ├── income_analysis.py
│   │   ├── racial_analysis.py
│   │   └── landtype_analysis.py
│   ├── integrate_data.py  # Data integration
│   ├── regression_statsmodels.py
│   └── main.py           # Main program
├── output/                # Analysis outputs
│   ├── visualizations/    # Analysis plots
│   └── regression_results/# Statistical results
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Analysis Workflow

### 1. **Data Preparation (R)**
- Raw data cleaning and transformation
- Scripts:
  * `process_income.R`
  * `process_ethnicity.R`
  * `process_property.R`

### 2. **Data Integration (Python)**
- Merges all datasets by suburb
- Handles missing values and data consistency
- Script: `integrate_data.py`

### 3. **Analysis Modules (Python)**
1. **Time Analysis**
   - Price changes between 2018-2023
   - Growth rate analysis
   - Suburb-level comparisons

2. **Income Analysis**
   - Income-price correlations
   - Price changes by income groups
   - Income distribution analysis

3. **Racial Analysis**
   - Racial cluster analysis
   - Price variations by racial composition
   - Correlation analysis

4. **Land Type Analysis**
   - Price distributions by land type
   - TC1/TC2 vs TC2/TC3 comparisons
   - Price change analysis

### 4. **Statistical Analysis**
- Multiple linear regression
- Model diagnostics
- Statistical summaries

## 📊 Output Structure

```
output/
├── visualizations/
│   ├── time_analysis/      # Time-based analysis plots
│   ├── income_analysis/    # Income analysis plots
│   ├── racial_analysis/    # Racial analysis plots
│   └── landtype_analysis/  # Land type analysis plots
└── regression_results/     # Statistical analysis outputs
```

##  How to Run

### 1. **Setup Environment**
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. **Run R Scripts**
```r
source("R/process_ethnicity.R")
source("R/process_income.R")
source("R/process_property.R")
```

### 3. **Run Python Analysis**
```bash
# Run complete analysis
python Python/main.py

# Or run individual components
python Python/integrate_data.py
python Python/regression_statsmodels.py
```

##  Dependencies

### Python Packages
```
graphviz==0.20.3
matplotlib==3.10.1
numpy==2.2.4
openpyxl==3.1.5
pandas==2.2.3
seaborn==0.13.2
statsmodels==0.14.4
scikit-learn==1.4.1
scipy==1.12.0
jupyter==1.0.0
tqdm==4.66.2
```

### R Packages
- tidyverse
- readxl
- writexl

##  Key Findings

1. **Time Analysis**
   - Significant price increases across most suburbs
   - Varying growth rates between different areas

2. **Income Analysis**
   - Strong correlation between income and property prices
   - Higher income areas show greater price appreciation

3. **Racial Analysis**
   - Clear patterns in price variations by racial composition
   - Different racial clusters show distinct price characteristics

4. **Land Type Analysis**
   - TC2/TC3 areas show higher prices and greater appreciation
   - Land type significantly impacts property values

##  License

This project is open-source and available under the MIT License.

##  Author

**Crystal Ma** - Master of Applied Computing
