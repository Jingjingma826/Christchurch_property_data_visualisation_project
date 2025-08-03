import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from .base_analysis import BaseAnalysis

class EthnicityAnalysis(BaseAnalysis):
    def __init__(self, data_2018, data_2023):
        super().__init__(data_2018, data_2023)
        self.ethnicity_cols = [
            'european_pct', 'maori_pct', 'pacific_peoples_pct', 
            'asian_pct', 'middle_eastern_latin_american_african_pct', 
            'new_zealander_pct'
        ]
    
    def analyze(self):
        """Analyze racial composition impact on housing prices"""
        # Prepare data for clustering
        ethnicity_data_2018 = self.data_2018[self.ethnicity_cols].copy()
        ethnicity_data_2023 = self.data_2023[self.ethnicity_cols].copy()
        
        # Standardize the data
        scaler = StandardScaler()
        ethnicity_data_scaled_2018 = scaler.fit_transform(ethnicity_data_2018)
        ethnicity_data_scaled_2023 = scaler.transform(ethnicity_data_2023)
        
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=4, random_state=42)
        self.data_2018['ethnicity_cluster'] = kmeans.fit_predict(ethnicity_data_scaled_2018)
        self.data_2023['ethnicity_cluster'] = kmeans.predict(ethnicity_data_scaled_2023)
        
        # Calculate cluster centers
        cluster_centers_array = scaler.inverse_transform(kmeans.cluster_centers_)
        # Create DataFrame directly from array
        cluster_centers = pd.DataFrame(cluster_centers_array, columns=self.ethnicity_cols)
        
        # Prepare data for merging
        data_2018_subset = self.data_2018[['suburb', 'median_price', 'ethnicity_cluster'] + self.ethnicity_cols].copy()
        data_2023_subset = self.data_2023[['suburb', 'median_price', 'ethnicity_cluster'] + self.ethnicity_cols].copy()
        
        # Add suffixes to all columns except 'suburb'
        data_2018_subset = data_2018_subset.rename(columns={
            col: f"{col}_2018" for col in data_2018_subset.columns if col != 'suburb'
        })
        data_2023_subset = data_2023_subset.rename(columns={
            col: f"{col}_2023" for col in data_2023_subset.columns if col != 'suburb'
        })
        
        # Merge 2018 and 2023 data for analysis
        ethnicity_price = pd.merge(
            data_2018_subset,
            data_2023_subset,
            on='suburb'
        )
        
        # Calculate price changes
        ethnicity_price['price_change_pct'] = (
            (ethnicity_price['median_price_2023'] - ethnicity_price['median_price_2018']) 
            / ethnicity_price['median_price_2018'] * 100
        )
        
        # Save results
        self.results = {
            'ethnicity_price': ethnicity_price,
            'cluster_centers': cluster_centers
        }
        
        return self.results
    
    def visualize(self):
        """Create visualizations for racial analysis"""
        ethnicity_price = self.results['ethnicity_price']
        
        plt.figure(figsize=(20, 25))
        
        # Define racial groups for visualization
        ethnicity_groups = {
            'European': 'european_pct',
            'Asian': 'asian_pct',
            'Maori': 'maori_pct',
            'Pacific Peoples': 'pacific_peoples_pct',
            'Middle Eastern/Latin American/African': 'middle_eastern_latin_american_african_pct',
            'New Zealander': 'new_zealander_pct'
        }
        
        for idx, (group_name, col_name) in enumerate(ethnicity_groups.items(), 1):
            plt.subplot(3, 2, idx)
            
            # Plot 2018 data
            plt.scatter(ethnicity_price[f'{col_name}_2018'] * 100, 
                       ethnicity_price['median_price_2018'] / 1000000,
                       alpha=0.7, label='2018', color=self.colors['2018'], s=120,
                       edgecolor='white', linewidth=1)
            
            # Plot 2023 data
            plt.scatter(ethnicity_price[f'{col_name}_2023'] * 100,
                       ethnicity_price['median_price_2023'] / 1000000,
                       alpha=0.7, label='2023', color=self.colors['2023'], s=120,
                       edgecolor='white', linewidth=1)
            
            # Add trend lines
            z_2018 = np.polyfit(ethnicity_price[f'{col_name}_2018'] * 100, 
                               ethnicity_price['median_price_2018'] / 1000000, 1)
            p_2018 = np.poly1d(z_2018)
            plt.plot(sorted(ethnicity_price[f'{col_name}_2018'] * 100),
                    p_2018(sorted(ethnicity_price[f'{col_name}_2018'] * 100)),
                    color=self.colors['trend_2018'], linestyle='--', alpha=0.8, linewidth=2)
            
            z_2023 = np.polyfit(ethnicity_price[f'{col_name}_2023'] * 100,
                               ethnicity_price['median_price_2023'] / 1000000, 1)
            p_2023 = np.poly1d(z_2023)
            plt.plot(sorted(ethnicity_price[f'{col_name}_2023'] * 100),
                    p_2023(sorted(ethnicity_price[f'{col_name}_2023'] * 100)),
                    color=self.colors['trend_2023'], linestyle='--', alpha=0.8, linewidth=2)
            
            # Set title and labels
            plt.title(f'{group_name} Percentage vs. Housing Price (2018 vs 2023)', 
                     fontsize=12, pad=15)
            plt.xlabel(f'{group_name} Population Percentage (%)', fontsize=10)
            plt.ylabel('Median Housing Price (Million NZD)', fontsize=10)
            plt.legend(fontsize=10)
            plt.grid(True, linestyle='--', alpha=0.3)
            
            # Add correlation coefficients
            corr_2018 = ethnicity_price[f'{col_name}_2018'].corr(ethnicity_price['median_price_2018'])
            corr_2023 = ethnicity_price[f'{col_name}_2023'].corr(ethnicity_price['median_price_2023'])
            plt.text(0.05, 0.95, 
                    f'2018 Correlation: {corr_2018:.2f}\n2023 Correlation: {corr_2023:.2f}',
                    transform=plt.gca().transAxes,
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'),
                    fontsize=9)
        
        plt.tight_layout()
        plt.savefig('output/visualizations/ethnicity_analysis/ethnicity_analysis.png', 
                    dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
    
    def save_results(self, output_path):
        """Save analysis results to file"""
        # Save cluster statistics
        cluster_stats = self.results['ethnicity_price'].groupby('ethnicity_cluster_2018').agg({
            'price_change_pct': ['mean', 'std', 'count'],
            'european_pct_2018': 'mean',
            'asian_pct_2018': 'mean',
            'maori_pct_2018': 'mean'
        })
        
        # Save results to CSV
        cluster_stats.to_csv(f'{output_path}/cluster_statistics.csv')
        self.results['cluster_centers'].to_csv(f'{output_path}/cluster_centers.csv') 