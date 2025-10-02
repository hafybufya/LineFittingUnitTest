import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('lineEquation.csv', delimitter=',', skiprows =1)
print(data)
def equation_of_line( x_value, y_value):
    slope_m = 1
    intercept_c = 0