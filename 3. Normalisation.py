import time
start_time = time.perf_counter() # Start time measurement
import pandas as pd
import numpy as np

# Load the image matrix from an Excel file
file_path = 'mnistCS.xlsx' 
data = pd.read_excel(file_path, header=None) 

# Convert the data to a NumPy array
image_matrix = data.to_numpy()

# Normalize the matrix
# Option 1: Centering and scaling by standard deviation (Z-score normalization)
mean = np.mean(image_matrix)
std = np.std(image_matrix)
normalized_matrix = (image_matrix - mean) / std

# Option 2: Scaling between 0 and 1 (Min-Max normalization)
min_val = np.min(image_matrix)
max_val = np.max(image_matrix)
normalized_matrix_minmax = (image_matrix - min_val) / (max_val - min_val)

# Convert normalized matrix back to a DataFrame for easy saving
normalized_df = pd.DataFrame(normalized_matrix)
normalized_minmax_df = pd.DataFrame(normalized_matrix_minmax)

# Save normalized data to Excel
normalized_df.to_excel('normalized_image_zscore.xlsx', index=False, header=False)
normalized_minmax_df.to_excel('normalized_image_minmax.xlsx', index=False, header=False)

print("Normalization complete. Saved to Excel files.")

end_time = (time.perf_counter() - start_time) * 1000
print()
print (f"Computation Time for Power method for 5x5 T Matrix: {end_time} milliseconds")