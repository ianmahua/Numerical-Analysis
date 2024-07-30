import numpy as np  

def power_iteration(A, num_simulations: int = 100):  
    b_k = np.random.rand(A.shape[1])  

    for _ in range(num_simulations):  
        # Calculate the matrix-by-vector product Av  
        b_k1 = np.dot(A, b_k)  

        # Calculate the norm  
        b_k1_norm = np.linalg.norm(b_k1)  

        # Re-normalize the vector  
        b_k = b_k1 / b_k1_norm  

    # Rayleigh quotient to estimate eigenvalue  
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)  
    
    return eigenvalue, b_k  

# Example usage  
A = np.array([[4, 1, 1],  
              [3, -1, 1],  
              [1, 2, 2]])  

eigenvalue_power, eigenvector_power = power_iteration(A)  
print("Power Iteration Eigenvalue:", eigenvalue_power)  
print("Power Iteration Eigenvector:", eigenvector_power)
