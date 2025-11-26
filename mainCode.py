# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

# ---------------------------------------------------------------------
# Defined CSV file name and columns as well as colours used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------

csv_in_use = "lineCsvFile.csv"

# X and Y axis used in plots
x_axis = "x"
y_axis = "y"

# Colors for plots
colour_1 = "#e63946"
colour_2 = "#2596be"




# ---------------------------------------------------------------------
# FUNCTION: Read CSV data into Dataframe
# ---------------------------------------------------------------------

def read_line_csv():
    
    """

    Loads the csv dataset defined in 'csv_in_use'

    Returns
    -------

    pandas Dataframe -> converts csv to df containing line data

    """
    
    # CSV converted to Df
    line_df = pd.read_csv(csv_in_use)
    
    return line_df

# ---------------------------------------------------------------------
# FUNCTION: Preforms linear regression on line_df
# ---------------------------------------------------------------------

def plot_line():

    """
    
    Reads data from line_df, performs linear regression, and plots the data with 
    a regression line. 
    
    Returns
    -------
        x         : pd.Series, x-axis values
        y         : pd.Series, y-axis values
        slope     : float, slope of the regression line
        intercept : float, intercept of the regression line  

    """

    df = read_line_csv()

    # Data extracted from pandas df
    x = df[x_axis]
    y = df[y_axis]

    # Preforming linear regression for regression line
    slope, intercept, r, p, std_err = linregress(x, y)
    
    # Plots the regression line
    plt.plot(x, slope*x + intercept, color=colour_1,
            label=f"Regression line\ny = {slope:.2f}x + {intercept:.2f}")
    
    # Plots the original data points from df
    plt.scatter(x, y, label="Data Points", color= colour_2)
    
    # X and Y axis labels
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title ("Scatter Plot with Linear Regression")

    # Displays the plot
    plt.show() 

    # Returning values necessary for unit tests
    return slope, intercept, x, y

# ---------------------------------------------------------------------
# FUNCTION: Counts number of columns in csv
# ---------------------------------------------------------------------

def count_rows_columns_pandas(csv):

    """
    
    Converts a csv into a pd.DataFrame and counts number of columns. 
    
    Paramters
    ---------
    csv : str, path of csv to be read

    Return
    ------
    len(df)         : int, number of rows in csv
    len(df.columns) : int, number of columns in csv

    """

    # Reads the csv and converts to df
    df = pd.read_csv(csv)  

    # Returns the number of columns in df
    return len(df), len(df.columns)


if __name__ == "__main__":

    line_df = read_line_csv()  # Calls function so to be used in plot_line()
    plot_line()
    rows, cols = count_rows_columns_pandas(csv_in_use)
    print(rows, cols)
