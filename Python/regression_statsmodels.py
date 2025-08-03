import pandas as pd
import statsmodels.api as sm
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Create output directory
os.makedirs('output/regression_results', exist_ok=True)

def load_data(year):
    """Load integrated data for a specific year and handle missing values"""
    file_path = f"Data/integrated/integrated_data_{year}.csv"
    df = pd.read_csv(file_path)
    
    # Print missing value information
    print(f"\nMissing value information for {year}:")
    missing_info = df.isnull().sum()
    print(missing_info[missing_info > 0])
    
    # Print suburbs with missing values
    if df.isnull().any().any():
        print("\nSuburbs with missing values:")
        for col in df.columns:
            if df[col].isnull().any():
                missing_subs = df[df[col].isnull()]['suburb'].tolist()
                print(f"Missing {col} for suburbs: {missing_subs}")
    
    df = df.dropna()
    return df

def plot_regression_diagnostics(model, year, X, y):
    """Generate regression diagnostic plots"""
    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    plt.suptitle(f'Regression Diagnostics for {year}', fontsize=16, y=1.02)
    
    # 1. Predicted vs Actual values
    predicted = model.predict(X)
    axes[0, 0].scatter(y, predicted, alpha=0.5)
    axes[0, 0].plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
    axes[0, 0].set_xlabel('Actual Values', fontsize=12)
    axes[0, 0].set_ylabel('Predicted Values', fontsize=12)
    axes[0, 0].set_title('Predicted vs Actual Values', fontsize=14, pad=10)
    axes[0, 0].tick_params(axis='both', which='major', labelsize=10)
    
    # 2. Residuals vs Predicted values
    residuals = y - predicted
    axes[0, 1].scatter(predicted, residuals, alpha=0.5)
    axes[0, 1].axhline(y=0, color='r', linestyle='--')
    axes[0, 1].set_xlabel('Predicted Values', fontsize=12)
    axes[0, 1].set_ylabel('Residuals', fontsize=12)
    axes[0, 1].set_title('Residuals vs Predicted Values', fontsize=14, pad=10)
    axes[0, 1].tick_params(axis='both', which='major', labelsize=10)
    
    # 3. Residuals histogram
    sns.histplot(residuals, kde=True, ax=axes[1, 0])
    axes[1, 0].set_xlabel('Residuals', fontsize=12)
    axes[1, 0].set_ylabel('Frequency', fontsize=12)
    axes[1, 0].set_title('Residuals Distribution', fontsize=14, pad=10)
    axes[1, 0].tick_params(axis='both', which='major', labelsize=10)
    
    # 4. Q-Q plot
    sm.qqplot(residuals, line='45', ax=axes[1, 1])
    axes[1, 1].set_title('Q-Q Plot', fontsize=14, pad=10)
    axes[1, 1].tick_params(axis='both', which='major', labelsize=10)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save figure with high DPI for better quality
    plt.savefig(f'output/regression_results/regression_diagnostics_{year}.png', dpi=300, bbox_inches='tight')
    plt.close()

def run_statsmodels_regression(df, year):
    """Perform regression analysis using statsmodels and save results"""
    features = [
        'european_pct', 'maori_pct', 'pacific_peoples_pct',
        'asian_pct', 'middle_eastern_latin_american_african_pct',
        'weighted_median_income', 'land_type_dummy'
    ]
    X = df[features]
    y = df['median_price']
    X = sm.add_constant(X)  # Add intercept term
    model = sm.OLS(y, X).fit()
    
    # Save regression results as text
    with open(f'output/regression_results/statsmodels_summary_{year}.txt', 'w') as f:
        f.write(model.summary().as_text())
    
    # Save regression coefficients as CSV
    summary_df = model.summary2().tables[1]
    summary_df.to_csv(f'output/regression_results/statsmodels_coefficients_{year}.csv')
    
    # Generate diagnostic plots
    plot_regression_diagnostics(model, year, X, y)
    
    print(f"Statsmodels regression analysis results for {year} have been saved to output/regression_results/")
    return model

def main():
    """Main function to run regression analysis for multiple years"""
    for year in [2018, 2023]:
        print(f"\nRunning Statsmodels regression analysis for {year}...")
        df = load_data(year)
        print(f"Number of rows after cleaning: {len(df)}")
        model = run_statsmodels_regression(df, year)
        print(model.summary())

if __name__ == "__main__":
    main() 