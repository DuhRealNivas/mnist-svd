import pandas as pd
import numpy as np

# Load the S matrix from an Excel file (diagonal matrix of singular values)
file_path = 'S_matrix.xlsx'
S_data = pd.read_excel(file_path, header=None).to_numpy()

# Extract the singular values from the diagonal
singular_values = np.diag(S_data)

# Step 1: Calculate the variance contribution of each singular value
variance_explained = singular_values ** 2
total_variance = np.sum(variance_explained)
cumulative_variance = np.cumsum(variance_explained)

# Step 2: Calculate cumulative percentage of variance explained
cumulative_percentage = cumulative_variance / total_variance * 100

# Step 3: Find the minimum number of singular values that retain 95% variance
num_singular_values = np.argmax(cumulative_percentage >= 95) + 1

# Step 4: Truncate the S matrix to keep only the required singular values
reduced_S_matrix = np.diag(singular_values[:num_singular_values])

# Save the reduced S matrix back to an Excel file if needed
pd.DataFrame(reduced_S_matrix).to_excel('reduced_S_matrix_95.xlsx', index=False, header=False)

print(f"Reduced S matrix saved with {num_singular_values} singular values to retain 95% variance.")
