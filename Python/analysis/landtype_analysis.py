import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .base_analysis import BaseAnalysis

class LandTypeAnalysis(BaseAnalysis):
    def analyze(self):
        """Analyze the impact of land type on housing prices"""
        # Merge 2018 and 2023 data, keeping land type and price
        landtype_price = pd.merge(
            self.data_2018[['suburb', 'median_price', 'land_type_dummy']],
            self.data_2023[['suburb', 'median_price', 'land_type_dummy']],
            on=['suburb', 'land_type_dummy'],
            suffixes=('_2018', '_2023')
        )
        # Calculate price change percentage
        landtype_price['price_change_pct'] = (
            (landtype_price['median_price_2023'] - landtype_price['median_price_2018'])
            / landtype_price['median_price_2018'] * 100
        )
        self.results = landtype_price
        return landtype_price

    def visualize(self):
        """Create visualizations for land type analysis"""
        landtype_price = self.results
        plt.figure(figsize=(16, 12))
        # 1. 2018 price distribution by land type
        plt.subplot(2, 2, 1)
        sns.boxplot(x='land_type_dummy', y='median_price_2018', data=landtype_price)
        plt.title('2018 Price Distribution by Land Type')
        plt.xlabel('Land Type (0=TC1/TC2, 1=TC2/TC3)')
        plt.ylabel('Median Price (NZD)')
        # 2. 2023 price distribution by land type
        plt.subplot(2, 2, 2)
        sns.boxplot(x='land_type_dummy', y='median_price_2023', data=landtype_price)
        plt.title('2023 Price Distribution by Land Type')
        plt.xlabel('Land Type (0=TC1/TC2, 1=TC2/TC3)')
        plt.ylabel('Median Price (NZD)')
        # 3. Price change percentage by land type
        plt.subplot(2, 2, 3)
        sns.boxplot(x='land_type_dummy', y='price_change_pct', data=landtype_price)
        plt.title('Price Change Percentage by Land Type (2018-2023)')
        plt.xlabel('Land Type (0=TC1/TC2, 1=TC2/TC3)')
        plt.ylabel('Price Change Percentage (%)')
        # 4. Median price comparison by land type
        plt.subplot(2, 2, 4)
        medians = landtype_price.groupby('land_type_dummy')[['median_price_2018','median_price_2023','price_change_pct']].median().reset_index()
        bar_width = 0.35
        plt.bar(medians['land_type_dummy']-bar_width/2, medians['median_price_2018'], width=bar_width, label='2018')
        plt.bar(medians['land_type_dummy']+bar_width/2, medians['median_price_2023'], width=bar_width, label='2023')
        plt.title('Median Price by Land Type (2018 vs 2023)')
        plt.xlabel('Land Type (0=TC1/TC2, 1=TC2/TC3)')
        plt.ylabel('Median Price (NZD)')
        plt.legend()
        plt.tight_layout()
        plt.savefig('output/visualizations/landtype_analysis/landtype_analysis.png', dpi=300, bbox_inches='tight')
        plt.close() 