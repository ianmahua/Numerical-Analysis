import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * x**2 + b * x + c

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 4, 5, 4, 5])

popt, pcov = curve_fit(func, x_data, y_data)
print("Fitted curve: y =", popt[0], "x^2 +", popt[1], "x +", popt[2])