
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

#maybe an enter name of the csv function? to make it more interacting? if not just use csv that i make up 

# opens csv file and performs linear regression
def line_function():
    lineCode_pandas = pd.read_csv('lineCsvFile.csv')
    # Extract x and y
    x = lineCode_pandas['x']
    y = lineCode_pandas['y']

    #ignoring uncecessary values
    slope, intercept, _, _, _ = linregress(x, y)
    

# y = 4.07x -0.67
    plt.plot(x, slope*x + intercept, color='r',
            label=f"Regression line\ny = {slope:.2f}x + {intercept:.2f}")

    plt.scatter(x, y, label="Data Points")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()
    plt.show() #-> find a way to not have this run every unit test.
    return slope, intercept, x , y

line_function()