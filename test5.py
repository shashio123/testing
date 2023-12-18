import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Linear regression for all data
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='All Data')

    # Linear regression for data from year 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope_recent * df['Year'] + intercept_recent, color='green', label='Since 2000')

    # Predicting sea level rise in 2050
    year_2050 = 2050
    plt.plot(year_2050, slope * year_2050 + intercept, 'o', color='red', markersize=8)
    plt.plot(year_2050, slope_recent * year_2050 + intercept_recent, 'o', color='green', markersize=8)

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save and show plot
    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    plt.show()

    # Return the plot
    return plt.gca().figure

# Call the function
draw_plot()
