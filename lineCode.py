
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
# Load CSV data (remove spaces in your CSV file first)

lineCode_pandas = pd.read_csv('lineCsvFile.csv')
# Extract x and y
x = lineCode_pandas['x']
y = lineCode_pandas['y']

slope, intercept, r_value, p_value, std_err = linregress(x, y)

plt.plot(x, slope*x + intercept, color='r',
         label=f"Regression line\ny = {slope:.2f}x + {intercept:.2f}")

plt.scatter(x, y, label="Data Points")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()


