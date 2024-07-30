import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 4, 5, 4, 5])

spline = InterpolatedUnivariateSpline(x_data, y_data)
x_new = np.array([1.5, 2.5, 3.5, 4.5])
y_new = spline(x_new)

print("Interpolated values:", y_new)