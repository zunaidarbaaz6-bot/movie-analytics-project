"""
Movie Analytics - Main Analysis Script
Alternative to Jupyter notebook for running analysis via command line
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

def load_data(filepath='../data/movies_dataset.csv'):
    """Load the movie dataset"""
    df = pd.read_csv(filepath)
    print(f"Dataset loaded: {df.shape[0]} movies, {df.shape[1]} features")
    return df

def explore_data(df):
    """Perform basic data exploration"""
    print("\n" + "="*80)
    print("DATA EXPLORATION")
    print("="*80)
    
    print("\nDataset Info:")
    df.info()
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nBasic Statistics:")
    print(df.describe())
    
    return df

def analyze_genres(df, save_viz=True):
    """Analyze genre performance"""
    print("\n" + "="*80)
    print("GENRE ANALYSIS")
    print("="*80)
    
    genre_stats = df.groupby('genre').agg({
        'box_office_millions': ['mean', 'sum', 'count'],
        'profit_millions': 'mean',
        'roi_percentage': 'mean',
        'imdb_score': 'mean',
        'budget_millions': 'mean'
    }).round(2)
    
    genre_stats.columns = ['Avg_Box_Office', 'Total_Box_Office', 'Movie_Count', 
                           'Avg_Profit', 'Avg_ROI', 'Avg_IMDB', 'Avg_Budget']
    genre_stats = genre_stats.sort_values('Total_Box_Office', ascending=False)
    
    print(genre_stats)
    
    if save_viz:
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        genre_stats.sort_values('Total_Box_Office', ascending=True).plot(
            y='Total_Box_Office', kind='barh', ax=axes[0,0], color='skyblue', legend=False
        )
        axes[0,0].set_title('Total Box Office Revenue by Genre', fontsize=14, fontweight='bold')
        
        genre_stats.sort_values('Avg_ROI', ascending=True).plot(
            y='Avg_ROI', kind='barh', ax=axes[0,1], color='coral', legend=False
        )
        axes[0,1].set_title('Average ROI by Genre', fontsize=14, fontweight='bold')
        
        df['genre'].value_counts().plot(kind='bar', ax=axes[1,0], color='lightgreen')
        axes[1,0].set_title('Number of Movies by Genre', fontsize=14, fontweight='bold')
        
        df.boxplot(column='imdb_score', by='genre', ax=axes[1,1])
        axes[1,1].set_title('IMDB Score Distribution by Genre', fontsize=14, fontweight='bold')
        plt.suptitle('')
        
        plt.tight_layout()
        plt.savefig('../visualizations/genre_analysis.png', dpi=300, bbox_inches='tight')
        print("\nVisualization saved: ../visualizations/genre_analysis.png")
        plt.close()
    
    return genre_stats

def analyze_yearly_trends(df, save_viz=True):
    """Analyze yearly trends"""
    print("\n" + "="*80)
    print("YEARLY TRENDS ANALYSIS")
    print("="*80)
    
    yearly_stats = df.groupby('year').agg({
        'box_office_millions': ['mean', 'sum'],
        'budget_millions': 'mean',
        'profit_millions': 'mean',
        'imdb_score': 'mean',
        'title': 'count'
    }).round(2)
    
    yearly_stats.columns = ['Avg_Box_Office', 'Total_Box_Office', 
                            'Avg_Budget', 'Avg_Profit', 'Avg_IMDB', 'Movie_Count']
    
    print(yearly_stats)
    
    if save_viz:
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        yearly_stats['Total_Box_Office'].plot(ax=axes[0,0], marker='o', linewidth=2)
        axes[0,0].set_title('Total Box Office Revenue Over Years', fontsize=14, fontweight='bold')
        axes[0,0].grid(True, alpha=0.3)
        
        yearly_stats['Avg_Budget'].plot(ax=axes[0,1], marker='s', linewidth=2, color='#A23B72')
        axes[0,1].set_title('Average Budget Over Years', fontsize=14, fontweight='bold')
        axes[0,1].grid(True, alpha=0.3)
        
        yearly_stats['Movie_Count'].plot(kind='bar', ax=axes[1,0], color='#F18F01')
        axes[1,0].set_title('Number of Movies Released Per Year', fontsize=14, fontweight='bold')
        
        yearly_stats['Avg_IMDB'].plot(ax=axes[1,1], marker='d', linewidth=2, color='#6A994E')
        axes[1,1].set_title('Average IMDB Score Over Years', fontsize=14, fontweight='bold')
        axes[1,1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('../visualizations/yearly_trends.png', dpi=300, bbox_inches='tight')
        print("\nVisualization saved: ../visualizations/yearly_trends.png")
        plt.close()
    
    return yearly_stats

def analyze_studios(df, save_viz=True):
    """Analyze studio performance"""
    print("\n" + "="*80)
    print("STUDIO PERFORMANCE ANALYSIS")
    print("="*80)
    
    studio_stats = df.groupby('studio').agg({
        'box_office_millions': ['mean', 'sum'],
        'profit_millions': 'mean',
        'roi_percentage': 'mean',
        'imdb_score': 'mean',
        'title': 'count'
    }).round(2)
    
    studio_stats.columns = ['Avg_Box_Office', 'Total_Box_Office', 
                            'Avg_Profit', 'Avg_ROI', 'Avg_IMDB', 'Movie_Count']
    studio_stats = studio_stats.sort_values('Total_Box_Office', ascending=False)
    
    print(studio_stats)
    
    if save_viz:
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        studio_stats.sort_values('Total_Box_Office', ascending=True).plot(
            y='Total_Box_Office', kind='barh', ax=axes[0], color='mediumseagreen', legend=False
        )
        axes[0].set_title('Total Box Office Revenue by Studio', fontsize=14, fontweight='bold')
        
        studio_stats.sort_values('Avg_ROI', ascending=True).plot(
            y='Avg_ROI', kind='barh', ax=axes[1], color='tomato', legend=False
        )
        axes[1].set_title('Average ROI by Studio', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('../visualizations/studio_performance.png', dpi=300, bbox_inches='tight')
        print("\nVisualization saved: ../visualizations/studio_performance.png")
        plt.close()
    
    return studio_stats

def correlation_analysis(df, save_viz=True):
    """Analyze correlations between features"""
    print("\n" + "="*80)
    print("CORRELATION ANALYSIS")
    print("="*80)
    
    correlation_cols = ['budget_millions', 'box_office_millions', 'profit_millions', 
                       'imdb_score', 'runtime_minutes', 'director_experience_years']
    correlation_matrix = df[correlation_cols].corr()
    
    print(correlation_matrix)
    
    if save_viz:
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                    square=True, linewidths=1)
        plt.title('Correlation Matrix: Key Movie Metrics', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig('../visualizations/correlation_matrix.png', dpi=300, bbox_inches='tight')
        print("\nVisualization saved: ../visualizations/correlation_matrix.png")
        plt.close()
        
        # Budget analysis scatter plots
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        scatter1 = axes[0].scatter(df['budget_millions'], df['box_office_millions'], 
                                   alpha=0.6, s=50, c=df['imdb_score'], cmap='viridis')
        axes[0].set_title('Budget vs Box Office Revenue', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Budget (Millions $)')
        axes[0].set_ylabel('Box Office (Millions $)')
        plt.colorbar(scatter1, ax=axes[0], label='IMDB Score')
        
        scatter2 = axes[1].scatter(df['budget_millions'], df['roi_percentage'], 
                                   alpha=0.6, s=50, c=df['imdb_score'], cmap='plasma')
        axes[1].set_title('Budget vs ROI', fontsize=14, fontweight='bold')
        axes[1].set_xlabel('Budget (Millions $)')
        axes[1].set_ylabel('ROI (%)')
        plt.colorbar(scatter2, ax=axes[1], label='IMDB Score')
        
        plt.tight_layout()
        plt.savefig('../visualizations/budget_analysis.png', dpi=300, bbox_inches='tight')
        print("Visualization saved: ../visualizations/budget_analysis.png")
        plt.close()
    
    return correlation_matrix

def top_performers(df):
    """Display top performing movies"""
    print("\n" + "="*80)
    print("TOP PERFORMERS")
    print("="*80)
    
    print("\nTOP 10 HIGHEST GROSSING MOVIES:")
    print("-"*80)
    top_box_office = df.nlargest(10, 'box_office_millions')[
        ['title', 'genre', 'year', 'budget_millions', 'box_office_millions', 
         'profit_millions', 'imdb_score', 'studio']
    ]
    print(top_box_office.to_string(index=False))
    
    print("\n\nTOP 10 MOST PROFITABLE MOVIES (by ROI):")
    print("-"*80)
    top_roi = df.nlargest(10, 'roi_percentage')[
        ['title', 'genre', 'year', 'budget_millions', 'box_office_millions', 
         'roi_percentage', 'imdb_score', 'studio']
    ]
    print(top_roi.to_string(index=False))

def generate_summary(df):
    """Generate and save summary report"""
    print("\n" + "="*80)
    print("SUMMARY REPORT")
    print("="*80)
    
    budget_correlation = df['budget_millions'].corr(df['box_office_millions'])
    
    summary_report = {
        'Total_Movies_Analyzed': len(df),
        'Time_Period': f"{df['year'].min()}-{df['year'].max()}",
        'Total_Box_Office_Revenue': f"${df['box_office_millions'].sum():,.0f}M",
        'Average_Budget': f"${df['budget_millions'].mean():.2f}M",
        'Average_Box_Office': f"${df['box_office_millions'].mean():.2f}M",
        'Average_ROI': f"{df['roi_percentage'].mean():.2f}%",
        'Budget_BoxOffice_Correlation': f"{budget_correlation:.3f}"
    }
    
    summary_df = pd.DataFrame([summary_report]).T
    summary_df.columns = ['Value']
    summary_df.to_csv('../data/analysis_summary.csv')
    
    print(summary_df)
    print("\nSummary exported to: ../data/analysis_summary.csv")

def main():
    """Main analysis pipeline"""
    print("="*80)
    print("MOVIE INDUSTRY ANALYTICS")
    print("="*80)
    
    # Load data
    df = load_data()
    
    # Explore data
    df = explore_data(df)
    
    # Run analyses
    genre_stats = analyze_genres(df)
    yearly_stats = analyze_yearly_trends(df)
    studio_stats = analyze_studios(df)
    correlation_matrix = correlation_analysis(df)
    top_performers(df)
    generate_summary(df)
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE!")
    print("="*80)
    print("\nAll visualizations saved to ../visualizations/")
    print("Summary report saved to ../data/analysis_summary.csv")

if __name__ == "__main__":
    main()
