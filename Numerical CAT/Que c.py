import numpy as np
from scipy.interpolate import interp1d

# Given data points
x = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Create a linear spline interpolator
f = interp1d(x, y, kind='linear')

# Evaluate the interpolator at x = 4.0
y_at_4 = f(4.0)

print("The value of y at x = 4.0 is:", y_at_4)