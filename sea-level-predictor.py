import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 🔹 Line of best fit (1880–2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(1880, 2051))
    plt.plot(years, res.intercept + res.slope * years, 'r')

    # 🔹 Line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g')

    # Labels & title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot
    plt.savefig("sea_level_plot.png")

    return plt.gca()