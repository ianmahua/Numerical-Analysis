from scipy.integrate import quad

def f(x):
    return x**2

result, error = quad(f, 0, 2)
print("Integral of f(x) = x^2 from 0 to 2 is", result)