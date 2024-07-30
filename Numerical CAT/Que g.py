import numpy as np

def trapezoidal_rule(f, a, b, n):
  """
  Approximates the definite integral of f(x) from a to b using the trapezoidal rule.

  Args:
    f: The function to integrate.
    a: The lower limit of integration.
    b: The upper limit of integration.
    n: The number of trapezoids.

  Returns:
    The approximate value of the integral.
  """

  h = (b - a) / n  # Width of each trapezoid
  x = np.linspace(a, b, n + 1)  # Equally spaced points
  y = f(x)

  # Apply the trapezoidal rule formula
  integral = h * (y[0] + y[n] + 2 * np.sum(y[1:n])) / 2

  return integral

# Example usage:
def f(x):
  return x**2

a = 0
b = 2
n = 10

result = trapezoidal_rule(f, a, b, n)
print("Approximate integral:", result)
