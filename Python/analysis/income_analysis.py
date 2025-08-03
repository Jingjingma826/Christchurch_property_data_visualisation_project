import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .base_analysis import BaseAnalysis

class IncomeAnalysis(BaseAnalysis):
    def analyze(self):
        """Analyze the impact of income on housing prices"""
        # Merge 2018 and 2023 data for income analysis
        income_price = pd.merge(
            self.data_2018[['suburb', 'median_price', 'weighted_median_income']],
            self.data_2023[['suburb', 'median_price', 'weighted_median_income']],
            on='suburb',
            suffixes=('_2018', '_2023')
        )
        # Calculate price and income changes
        income_price['price_change_pct'] = (
            (income_price['median_price_2023'] - income_price['median_price_2018']) 
            / income_price['median_price_2018'] * 100
        )
        income_price['income_change_pct'] = (
            (income_price['weighted_median_income_2023'] - income_price['weighted_median_income_2018']) 
            / income_price['weighted_median_income_2018'] * 100
        )
        # Create income groups (quartiles)
        income_price['income_group_2018'] = pd.qcut(
            income_price['weighted_median_income_2018'], 
            q=4, 
            labels=['Low', 'Medium-Low', 'Medium-High', 'High']
        )
        self.results = income_price
        return income_price

    def visualize(self):
        """Create visualizations for income analysis"""
        income_price = self.results
        plt.figure(figsize=(20, 15))
        # 1. Scatter plot of income vs price (2018)
        plt.subplot(2, 2, 1)
        sns.scatterplot(
            data=income_price,
            x='weighted_median_income_2018',
            y='median_price_2018',
            hue='income_group_2018',
            palette='viridis'
        )
        plt.title('Income vs Price Relationship (2018)')
        plt.xlabel('Weighted Median Income (NZD)')
        plt.ylabel('Median Price (NZD)')
        # 2. Scatter plot of income vs price (2023)
        plt.subplot(2, 2, 2)
        sns.scatterplot(
            data=income_price,
            x='weighted_median_income_2023',
            y='median_price_2023',
            hue='income_group_2018',
            palette='viridis'
        )
        plt.title('Income vs Price Relationship (2023)')
        plt.xlabel('Weighted Median Income (NZD)')
        plt.ylabel('Median Price (NZD)')
        # 3. Box plot of price changes by income group
        plt.subplot(2, 2, 3)
        sns.boxplot(
            data=income_price,
            x='income_group_2018',
            y='price_change_pct'
        )
        plt.title('Price Changes by Income Group (2018-2023)')
        plt.xlabel('Income Group (2018)')
        plt.ylabel('Price Change Percentage (%)')
        # 4. Correlation between income and price changes
        plt.subplot(2, 2, 4)
        sns.scatterplot(
            data=income_price,
            x='income_change_pct',
            y='price_change_pct',
            hue='income_group_2018',
            palette='viridis'
        )
        plt.title('Income Change vs Price Change (2018-2023)')
        plt.xlabel('Income Change Percentage (%)')
        plt.ylabel('Price Change Percentage (%)')
        plt.tight_layout()
        plt.savefig('output/visualizations/income_analysis/income_analysis.png', dpi=300, bbox_inches='tight')
        plt.close() 