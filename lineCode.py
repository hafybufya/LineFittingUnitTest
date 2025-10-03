import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#
#from scipy.stats import linregress
# Load CSV data (remove spaces in your CSV file first)

lineCode_pandas = pd.read_csv('lineCode_pandas.csv')
x = lineCode_pandas['x'] #y working hours
y = lineCode_pandas['y'] #y axis life expectancy


#regression stats stuff
#slope, intercept, r_value, p_value, std_err = linregress(x, y)

# fig, ax = plt.subplots()
# ax.scatter(x, y) #scatters total and divorces

# ax.set_xlabel('Average annual working hours per worker', fontsize=10)  
# ax.set_ylabel('Life expectancy at birth', fontsize=10)
# ax.plot(x, slope*x + intercept, color='r', label='Regression line \n y=-0.01x + 96.61')  #regression line
# ax.legend()
# ax.set_title('Working hours vs Life Expectancy')

# #everything here used to make regression line
# print(f" slope = {slope}, intercept = {intercept}")
# print(f" Pearson correlation = {r_value}, and p-value = {p_value}")

# #splitting the graph up because it looks like two different correlations are being shown rn dun dun dunnnnnn