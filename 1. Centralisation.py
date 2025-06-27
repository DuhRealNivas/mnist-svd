import time
start_time = time.perf_counter() # Start time measurement
import pandas as pd
import numpy as np

# Load the image matrix data from an Excel file
file_path = 'mnist.xlsx' 
data = pd.read_excel(file_path, header=None) 

# Convert the data to a NumPy array
image_matrix = data.to_numpy()

# Calculate the mean of the pixel values
mean_pixel_value = np.mean(image_matrix)

# Centralize the matrix by subtracting the mean from each pixel value
centralized_matrix = image_matrix - mean_pixel_value

# Convert the centralized matrix back to a DataFrame for saving
centralized_df = pd.DataFrame(centralized_matrix)

# Save the centralized data to a new Excel file
centralized_df.to_excel('centralized_image_matrix.xlsx', index=False, header=False)

print("Image centralization complete. Saved to 'centralized_image_matrix.xlsx'.")
end_time = (time.perf_counter() - start_time) * 1000
print()
print (f"Computation Time for Power method for 5x5 T Matrix: {end_time} milliseconds")