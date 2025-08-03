# R Data Processing Scripts Documentation

## File Structure
- `convert_cleaned_excel.R`: Script for converting Excel files to CSV format
- `process_ethnicity.R`: Script for processing ethnicity data (2013, 2018, 2023)
- `process_income.R`: Script for processing income data (2018, 2023)
- `process_property.R`: Script for processing property data (2013, 2018, 2023)

## Script Functionality

### convert_cleaned_excel.R
This script converts Excel files to CSV format with the following features:

1. Data Conversion
   - Converts income data Excel files (2018, 2023)
   - Converts ethnicity data Excel files (2013, 2018, 2023)
   - Converts land type data Excel file

2. Output Files
   - Income data: `Data/manual_cleaned/manual_income/income{year}_manual_cleaned.csv`
   - Ethnicity data: `Data/manual_cleaned/manual_ethnicity/ethnicity{year}_manual_cleaned.csv`
   - Land type data: `Data/manual_cleaned/manual_land_type/land_type_manual_cleaned.csv`

### process_ethnicity.R
This script processes ethnicity data with the following features:

1. Data Reading
   - Reads from `Data/manual_cleaned/manual_ethnicity/ethnicity{year}_manual_cleaned.csv`
   - Processes data for years 2013, 2018, and 2023

2. Data Processing
   - Cleans suburb names
   - Removes "Christchurch City" suffix
   - Standardizes specific suburb names
   - Calculates ethnic group percentages

3. Output Files
   - Processed file: `Data/cleaned/final_ethnicity/ethnicity_{year}.csv`

### process_income.R
This script processes income data with the following features:

1. Data Reading
   - Reads from `Data/manual_cleaned/manual_income/income{year}_manual_cleaned.csv`
   - Processes data for years 2018 and 2023

2. Data Processing
   - Cleans suburb names
   - Removes "Christchurch City" suffix
   - Standardizes specific suburb names
   - Calculates weighted median income

3. Output Files
   - Processed file: `Data/cleaned/final_income/income_{year}.csv`

### process_property.R
This script processes property data with the following features:

1. Data Reading
   - Reads from `Data/manual_cleaned/manual_property/property_selected_years_maunual_cleaned.csv`
   - Processes data for years 2013, 2018, and 2023

2. Data Processing
   - Cleans suburb names
   - Converts property values to numeric format
   - Handles scientific notation (M, K)
   - Calculates median prices and sales counts by suburb

3. Output Files
   - Processed file: `Data/cleaned/final_property/property_{year}.csv`

## Usage Instructions

1. Required R Packages:
   - dplyr
   - stringr
   - readxl
   - writexl

2. Running the Scripts:
   - First, run `convert_cleaned_excel.R` to convert Excel files to CSV
   - Then run the processing scripts in any order:
     * `process_ethnicity.R`
     * `process_income.R`
     * `process_property.R`

3. Output Files:
   - Ethnicity data: `Data/cleaned/final_ethnicity/ethnicity_{year}.csv`
   - Income data: `Data/cleaned/final_income/income_{year}.csv`
   - Property data: `Data/cleaned/final_property/property_{year}.csv`

## Important Notes
- Ensure all required packages are installed
- Verify input files exist before running
- Check for sufficient disk space and write permissions
- Existing output files will be overwritten

## Data Processing Flow
1. Data Conversion (convert_cleaned_excel.R)
   - Convert Excel files to CSV format
   - Ensure consistent file format

2. Data Processing
   - Clean and standardize suburb names
   - Handle missing values
   - Calculate required statistics
   - Generate processed files

## Data Validation
- Checks for missing values
- Validates numerical calculations
- Ensures suburb name consistency
- Verifies data completeness

## Update Log
- 2025-05-19: Documentation update
  - Added Excel to CSV conversion functionality
  - Improved data processing for multiple years
  - Updated file paths and reading methods
  - Enhanced error handling and validation
  - Updated README with comprehensive script descriptions
  - Added detailed usage instructions
  - Improved data validation documentation