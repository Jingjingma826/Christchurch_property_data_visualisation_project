import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .base_analysis import BaseAnalysis

class PropertyAnalysis(BaseAnalysis):
    def analyze(self):
        """Analyze price changes over time (2018-2023)"""
        price_change = self._calculate_price_change()
        self.results = price_change
        return price_change

    def visualize(self):
        """Create visualizations for time analysis"""
        price_change = self.results
        plt.figure(figsize=(20, 15))
        # 1. Bar plot of top 10 suburbs by price increase
        plt.subplot(2, 2, 1)
        sns.barplot(data=price_change.head(10), x='price_change_pct', y='suburb')
        plt.title('Top 10 Suburbs by Price Increase (2018-2023)')
        plt.xlabel('Price Change Percentage (%)')
        plt.ylabel('Suburb')
        # 2. Distribution of price changes
        plt.subplot(2, 2, 2)
        bins = range(-20, 200, 20)
        plt.hist(price_change['price_change_pct'], bins=bins, edgecolor='black')
        plt.title('Distribution of Price Changes (2018-2023)')
        plt.xlabel('Price Change Percentage (%)')
        plt.ylabel('Number of Suburbs')
        plt.grid(True, linestyle='--', alpha=0.7)
        # 3. Box plot comparison of 2018 and 2023 prices
        plt.subplot(2, 2, 3)
        years_data = pd.DataFrame({
            '2018': self.data_2018['median_price'],
            '2023': self.data_2023['median_price']
        })
        sns.boxplot(data=years_data)
        plt.title('Price Distribution Comparison (2018 vs 2023)')
        plt.ylabel('Price (NZD)')
        # 4. Scatter plot of 2018 vs 2023 prices
        plt.subplot(2, 2, 4)
        plt.scatter(self.data_2018['median_price'], self.data_2023['median_price'], 
                   alpha=0.5, c='blue', label='Suburb Prices')
        max_price = max(max(self.data_2018['median_price']), max(self.data_2023['median_price']))
        plt.plot([0, max_price], [0, max_price], 'r--', label='No Change Line')
        plt.title('Price Comparison Scatter Plot (2018 vs 2023)')
        plt.xlabel('2018 Price (NZD)')
        plt.ylabel('2023 Price (NZD)')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('output/visualizations/property_analysis/property_analysis.png', dpi=300, bbox_inches='tight')
        plt.close() 