import pandas as pd
import os

def clean_suburb_name(df):
    """Clean suburb names by removing leading and trailing whitespace"""
    df['suburb'] = df['suburb'].str.strip()
    return df

def read_ethnicity_data(year):
    """Read ethnicity data, keeping only suburb and percentage columns"""
    file_path = f"Data/cleaned/final_ethnicity/ethnicity_{year}.csv"
    df = pd.read_csv(file_path)
    df = clean_suburb_name(df)
    
    # Keep only suburb and percentage columns
    percent_columns = [col for col in df.columns if 'percent' in col or 'pct' in col]
    return df[['suburb'] + percent_columns]

def read_income_data(year):
    """Read income data for a specific year"""
    file_path = f"Data/cleaned/final_income/income_{year}.csv"
    df = pd.read_csv(file_path)
    df = clean_suburb_name(df)
    return df[['suburb', 'weighted_median_income']]

def read_land_type_data():
    """Read land type classification data"""
    file_path = "Data/manual_cleaned/manual_land_type/land_type_manual_cleaned.csv"
    df = pd.read_csv(file_path)
    df = clean_suburb_name(df)
    return df[['suburb', 'land_type_dummy']]

def read_property_data(year):
    """Read and process property data as the base dataset"""
    file_path = f"Data/cleaned/final_property/property_{year}.csv"
    df = pd.read_csv(file_path)
    df = clean_suburb_name(df)
    
    # Convert scientific notation prices to numeric
    if 'median_price' in df.columns:
        df['median_price'] = pd.to_numeric(df['median_price'], errors='coerce')
    
    # Aggregate data for duplicate suburbs
    df = df.groupby('suburb').agg({
        'year': 'first',
        'sales_count': 'sum',
        'median_price': lambda x: x.dropna().iloc[0] if not x.dropna().empty else None
    }).reset_index()
    
    return df

def integrate_data(year):
    """Integrate all datasets for a specific year"""
    # Read all datasets
    property_df = read_property_data(year)
    ethnicity_df = read_ethnicity_data(year)
    income_df = read_income_data(year)
    land_type_df = read_land_type_data()
    
    # Merge datasets using property data as the base
    merged_df = property_df.merge(ethnicity_df, on='suburb', how='inner')
    merged_df = merged_df.merge(income_df, on='suburb', how='inner')
    merged_df = merged_df.merge(land_type_df, on='suburb', how='inner')
    
    # Clean up year columns
    merged_df = merged_df.rename(columns={'year': 'year'})
    merged_df = merged_df.drop(['year_x', 'year_y'], axis=1, errors='ignore')
    
    return merged_df

def main():
    """Main function to process and integrate data for multiple years"""
    years = [2018, 2023]
    
    for year in years:
        print(f"\nProcessing data for year {year}...")
        
        # Integrate data
        integrated_df = integrate_data(year)
        
        # Save integrated data
        output_path = f"Data/integrated/integrated_data_{year}.csv"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        integrated_df.to_csv(output_path, index=False)
        
        print(f"Data for {year} has been integrated and saved to {output_path}")
        print(f"Number of suburbs in integrated data: {len(integrated_df)}")
        print("\nColumns in the integrated dataset:")
        print(integrated_df.columns.tolist())

if __name__ == "__main__":
    main() 