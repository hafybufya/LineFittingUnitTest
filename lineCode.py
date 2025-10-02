import numpy as np
import matplotlib.pyplot as plt

# Load CSV data (remove spaces in your CSV file first)
data = np.loadtxt('lineEquation.csv', delimiter=',')

def equation_of_line(x_value, y_value):
    slope_m = 1.85
    intercept_c = 1.22
    # Example: y = mx + c
    
    return slope_m * x_value + intercept_c

# Example usage
x = data[0]
y = data[1]
plt.plot(x, y, 'o')
plt.show()