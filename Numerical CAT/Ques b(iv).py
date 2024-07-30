import numpy as np
from sklearn.linear_model import LinearRegression

x_data = np.array([[1], [2], [3], [4], [5]])
y_data = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(x_data, y_data)

print("Linear regression equation: y =", model.coef_[0], "x +", model.intercept_)