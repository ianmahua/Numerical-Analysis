import numpy as np

def f(x):
    return x**2

def derivative(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2.0 * h)

x = 2.0
print("Derivative of f(x) = x^2 at x =", x, "is", derivative(f, x))