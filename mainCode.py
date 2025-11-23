# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


# ---------------------------------------------------------------------
# Defined CSV file name and columns as well as colors used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------


csv_in_use = "lineCsvFile.csv"
x_axis = "x"
y_axis = "y"
color_1 = "#FF0000"

# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy as np

# ---------------------------------------------------------------------
# Defined CSV file name and columns as well as colors used in program
#  -> make the code flexible if used dataset changed
#  -> or to reuse the same function for a different file.
# ---------------------------------------------------------------------

csv_in_use = "lineCsvFile.csv"
x_axis = "x"
y_axis = "y"
color_1 = "#FF0000"


def read_line_csv():
    
    """

    Loads the csv dataset defined in 'csv_in_use'

    Returns
    -------

    pandas Dataframe -> converts csv to df containing line data

    """
    
    
    line_df = pd.read_csv(csv_in_use)
    return line_df




# opens csv file and performs linear regression

def plot_line(x = None, y = None):

    if x is None or y is None:
        df = read_line_csv()
        x = df[x_axis]
        y = df[y_axis]

    #ignoring uncecessary values
    slope, intercept, r, p, std_err = linregress(x, y)
    

    plt.plot(x, slope*x + intercept, color='r',
            label=f"Regression line\ny = {slope:.2f}x + {intercept:.2f}")

    plt.scatter(x, y, label="Data Points")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()
    plt.show() 

    # Returning values necessary for unit tests
    return slope, intercept, x, y





    #count the number of columns in csv
def count_columns_pandas(csv):


    df = pd.read_csv(csv)  
    return len(df.columns)



if __name__ == "__main__":

    # Calls function so to be used in plot_line()
    line_df = read_line_csv()
    
    #passed into plot_line() above
    x = line_df[x_axis]
    y = line_df[y_axis]
    plot_line(x, y)
    print(count_columns_pandas(csv_in_use))
    


