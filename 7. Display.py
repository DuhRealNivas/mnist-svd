import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
mnist = pd.read_csv("truncated_matrix_95.csv")

# Set the number of rows and columns for displaying the images in a grid
nrow = 2
ncol = 5

# Define the figure size
plt.figure(figsize=(10, 5))

# Loop through each image and display it in the grid
for i in range(nrow * ncol):
    plt.subplot(nrow, ncol, i + 1)
    
    # Extract the label for the image
    label = mnist.iloc[i, 0]
    
    # Extract the pixel values 
    image = mnist.iloc[i, 1:]
    
    # Reshape the flat array of pixels into a 28x28 array
    image = np.reshape(image.values, (28, 28))
    
    # Display the image in grayscale
    plt.imshow(image, cmap='gray')
    
    # Turn off the axis for a cleaner look
    plt.axis('off')
    
    # Set the title of the subplot to show the label
    plt.title(f"Label: {label}")

# Adjust layout to avoid overlapping subplots
plt.tight_layout()

# Show the plot
plt.show()
