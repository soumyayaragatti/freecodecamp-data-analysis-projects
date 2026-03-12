import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    fig, ax = plt.subplots(figsize=(10,6))
    
    # Scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # First line of best fit (all data)
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(df['Year'].min(), 2051))
    ax.plot(years, intercept + slope*years, 'r', label='Fit: All data')
    
    # Second line of best fit (2000 onwards)
    recent_df = df[df['Year'] >= 2000]
    slope2, intercept2, r2, p2, std_err2 = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    recent_years = pd.Series(range(2000, 2051))
    ax.plot(recent_years, intercept2 + slope2*recent_years, 'g', label='Fit: 2000+')
    
    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()
    
    # Return the figure
    return fig