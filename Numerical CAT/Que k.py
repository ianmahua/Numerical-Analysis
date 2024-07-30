import numpy as np  

def gradient_f(x, y):  
    """  
    Compute the gradient of the function f at point (x, y).  
    The function f is defined as:  
    f(x, y) = x^2 + y^2 - xy + x - y + 1.  
    """  
    df_dx = 2*x - y + 1  # Partial derivative with respect to x  
    df_dy = 2*y - x - 1  # Partial derivative with respect to y  
    return np.array([df_dx, df_dy])  

def gradient_descent(learning_rate=0.1, initial_guess=(0, 0), iterations=100):  
    """  
    Perform gradient descent to minimize the function f.  
    
    Args:  
    - learning_rate: The step size for each iteration.  
    - initial_guess: A tuple (x0, y0) for starting point.  
    - iterations: Number of iterations to perform.  
    
    Returns:  
    - (x, y): The coordinates of the local minimum found.  
    """  
    x, y = initial_guess  

    for _ in range(iterations):  
        gradient = gradient_f(x, y)  
        x -= learning_rate * gradient[0]  # Update x  
        y -= learning_rate * gradient[1]  # Update y  

    return x, y  

# Example usage  
min_x, min_y = gradient_descent()  
print(f"Minimum found at: x = {min_x}, y = {min_y}")
