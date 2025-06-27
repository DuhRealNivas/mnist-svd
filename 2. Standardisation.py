import time
start_time = time.perf_counter() # Start time measurement
import pandas as pd
import numpy as np

# Load the image matrix data from an Excel file
file_path = '200testC.xlsx' 
data = pd.read_excel(file_path, header=None)

# Convert the data to a NumPy array
image_matrix = data.to_numpy()

# Calculate the mean and standard deviation of the pixel values
mean_pixel_value = np.mean(image_matrix)
std_pixel_value = np.std(image_matrix)

# Standardize the image matrix by subtracting the mean and dividing by the standard deviation
standardized_matrix = (image_matrix - mean_pixel_value) / std_pixel_value

# Convert the standardized matrix back to a DataFrame for saving
standardized_df = pd.DataFrame(standardized_matrix)

# Save the standardized data to a new Excel file
standardized_df.to_excel('standardized_image_matrix.xlsx', index=False, header=False)

print("Image standardization complete. Data saved to 'standardized_image_matrix.xlsx'.")
end_time = (time.perf_counter() - start_time) * 1000
print()
print (f"Computation Time for Power method for 5x5 T Matrix: {end_time} milliseconds")
