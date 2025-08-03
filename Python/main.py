import pandas as pd
from Python.analysis.property_analysis import PropertyAnalysis
from Python.analysis.income_analysis import IncomeAnalysis
from Python.analysis.ethnicity_analysis import EthnicityAnalysis
from Python.analysis.landtype_analysis import LandTypeAnalysis

def load_data():
    """Load data for analysis"""
    data_2018 = pd.read_csv("Data/Integrated/integrated_data_2018.csv")
    data_2023 = pd.read_csv("Data/Integrated/integrated_data_2023.csv")
    return data_2018, data_2023

def main():
    """Main function to run all analyses"""
    # Load data
    data_2018, data_2023 = load_data()
    
    # Property analysis
    property_analysis = PropertyAnalysis(data_2018, data_2023)
    property_analysis.analyze()
    property_analysis.visualize()
    print("Property analysis completed. Results saved to output/visualizations/property_analysis/")
    
    # Income analysis
    income_analysis = IncomeAnalysis(data_2018, data_2023)
    income_analysis.analyze()
    income_analysis.visualize()
    print("Income analysis completed. Results saved to output/visualizations/income_analysis/")
    
    # Ethnicity analysis
    ethnicity_analysis = EthnicityAnalysis(data_2018, data_2023)
    ethnicity_analysis.analyze()
    ethnicity_analysis.visualize()
    ethnicity_analysis.save_results('output/regression_results/ethnicity_models')
    print("Ethnicity analysis completed. Results saved to output/visualizations/ethnicity_analysis/")

    # Land type analysis
    landtype_analysis = LandTypeAnalysis(data_2018, data_2023)
    landtype_analysis.analyze()
    landtype_analysis.visualize()
    print("Land type analysis completed. Results saved to output/visualizations/landtype_analysis/")

if __name__ == "__main__":
    main() 