import pandas as pd
import numpy as np

# Load the first matrix data from an Excel file
file_path_A = 'MNIST_N.xlsx' 
data_A = pd.read_excel(file_path_A, header=None)  # Assuming no header in Excel
matrix_A = data_A.to_numpy()

# Load the second matrix data from another Excel file
file_path_B = 'truncated_matrix_95.xlsx' 
data_B = pd.read_excel(file_path_B, header=None)
matrix_B = data_B.to_numpy()

# Step 1: Compute the Frobenius norm for both matrices
frobenius_norm_A = np.linalg.norm(matrix_A, 'fro')
frobenius_norm_B = np.linalg.norm(matrix_B, 'fro')

# Step 2: Calculate the percentage difference between the two norms
if frobenius_norm_A != 0:  # To avoid division by zero
    percentage_difference = (frobenius_norm_A - frobenius_norm_B) / frobenius_norm_A * 100
else:
    percentage_difference = float('inf')  # Handle case where the first norm is zero

# Display the results
print(f"The Frobenius norm of the normalised original matrix is: {frobenius_norm_A:.3f}")
print(f"The Frobenius norm of 95% truncated matrix is: {frobenius_norm_B:.3f}")
print(f"Data Loss: {percentage_difference:.3f}%")