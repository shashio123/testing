import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    # Import data and set index to date column
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Clean data by filtering out top and bottom 2.5% of dataset
    df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) &
                    (df['value'] <= df['value'].quantile(0.975))]

    # Create line plot
    plt.figure(figsize=(10, 5))
    plt.plot(df_cleaned.index, df_cleaned['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    plt.show()

def draw_bar_plot():
    # Import data and set index to date column
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Extract year and month from the date
    df['year'] = df.index.year
    df['month'] = df.index.month

    # Group by year and month, calculate the mean
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Create bar plot
    fig, ax = plt.subplots(figsize=(10, 5))
    df_bar.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=[pd.to_datetime(str(i)).strftime('%B') for i in range(1, 13)])
    plt.show()

def draw_box_plot():
    # Import data and set index to date column
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Extract year and month from the date
    df['year'] = df.index.year
    df['month'] = df.index.month_name()

    # Create box plots (year-wise and month-wise)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    df['month_num'] = df['date'].dt.month
    df = df.sort_values('month_num')
    sns.boxplot(x='month', y='value', data=df, ax=axes[1],
                order=['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    plt.show()

# Call the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
