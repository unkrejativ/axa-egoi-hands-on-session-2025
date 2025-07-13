import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

def calculate_age_from_birthdate(date_series):
    """
    Calculates the age in years for reference date 2025-07-16 for a pandas series with birth dates.
    
    Parameters:
    - date_series: pd.Series in datetime64[ns]
    
    Returns:
    - pd.Series age in years
    """
    reference_date = pd.Timestamp('2025-07-16')
    birth_dates = pd.to_datetime(date_series)
    
    # Check if the birthday has not yet occurred this year
    not_had_birthday = ( (birth_dates.dt.month > reference_date.month) | 
                         ((birth_dates.dt.month == reference_date.month) & (birth_dates.dt.day > reference_date.day)) )
    
    age = reference_date.year - birth_dates.dt.year - not_had_birthday.astype(int)
    
    return age.astype(int)

def scatter_plot(df, x, y):
    """
    Creates a scatter plot for the given DataFrame columns.
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data.
    x (str): The column name to be used for the x-axis.
    y (str): The column name to be used for the y-axis.
    Returns:
    None: Displays the scatter plot.
    Notes:
    - The x-axis and y-axis are labeled with the respective column names.
    - The y-axis is configured to display integer values only.
    """
    
    plt.scatter(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{x} vs. {y}')
    plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))
    plt.show()