import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class BaseAnalysis:
    def __init__(self, data_2018, data_2023):
        """
        Initialize base analysis class
        Args:
            data_2018: DataFrame containing 2018 data
            data_2023: DataFrame containing 2023 data
        """
        self.data_2018 = data_2018
        self.data_2023 = data_2023
        self.results = {}
        
        # Set default visualization parameters
        plt.style.use('seaborn')
        
        # Set color scheme
        self.colors = {
            '2018': '#4B8BBE',  # Soft blue
            '2023': '#E74C3C',  # Soft red
            'trend_2018': '#2C3E50',  # Dark blue trend line
            'trend_2023': '#C0392B'   # Dark red trend line
        }
    
    def analyze(self):
        """Base analysis method to be implemented by subclasses"""
        raise NotImplementedError
    
    def visualize(self):
        """Base visualization method to be implemented by subclasses"""
        raise NotImplementedError
    
    def save_results(self, output_path):
        """Save analysis results to file"""
        raise NotImplementedError
    
    def _calculate_price_change(self):
        """Calculate price changes between 2018 and 2023"""
        price_change = pd.merge(
            self.data_2018[['suburb', 'median_price']],
            self.data_2023[['suburb', 'median_price']],
            on='suburb',
            suffixes=('_2018', '_2023')
        )
        
        price_change['price_change_pct'] = (
            (price_change['median_price_2023'] - price_change['median_price_2018']) 
            / price_change['median_price_2018'] * 100
        )
        
        return price_change.sort_values('price_change_pct', ascending=False) 