import time
start_time = time.perf_counter() # Start time measurement

import pandas as pd
import numpy as np

# Load the matrix data from an Excel file
file_path = 'mnistCSN.xlsx' 
data = pd.read_excel(file_path, header=None) 

# Convert the data to a NumPy array
matrix = data.to_numpy()

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(matrix, full_matrices=False)

# Convert S to a diagonal matrix for easier interpretation
S_matrix = np.diag(S)

# Save the results to separate Excel files if needed
pd.DataFrame(U).to_excel('U_matrix.xlsx', index=False, header=False)
pd.DataFrame(S_matrix).to_excel('S_matrix.xlsx', index=False, header=False)
pd.DataFrame(VT).to_excel('VT_matrix.xlsx', index=False, header=False)

print("SVD complete. U, S, and VT matrices saved to 'U_matrix.xlsx', 'S_matrix.xlsx', and 'VT_matrix.xlsx'.")

end_time = (time.perf_counter() - start_time) * 1000
print()
print (f"Computation Time for Power method for 5x5 T Matrix: {end_time} milliseconds")