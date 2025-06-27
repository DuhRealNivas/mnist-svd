import pandas as pd
import numpy as np

# Load the matrices from Excel files
matrix1 = pd.read_excel('U_matrix_95.xlsx', header=None).to_numpy()
matrix2 = pd.read_excel('S_matrix_95.xlsx', header=None).to_numpy()
matrix3 = pd.read_excel('VT_matrix_95.xlsx', header=None).to_numpy()

# Perform matrix multiplication
# First multiply matrix1 and matrix2, then multiply the result with matrix3
result_matrix = np.dot(np.dot(matrix1, matrix2), matrix3)

# Convert the result back to a DataFrame for easy export
result_df = pd.DataFrame(result_matrix)

# Save the result to a new Excel file
result_df.to_excel('truncated_matrix_95.xlsx', index=False, header=False)

print("Matrix multiplication complete. Result saved to 'truncated_matrix_95.xlsx'.")
