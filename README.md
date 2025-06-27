# mnist-svd
Singular Value Decomposition (SVD) to the MNIST dataset for image compression
## Instructions

1. **Load and Prepare the MNIST Data**: Load the MNIST dataset (see MyLearning folder) and get familiar with the data. You may want to standardise the pixel values.

2. **Apply SVD**: Perform SVD on the image data. SVD decomposes the data matrix into three matrices: *U*, *Σ*, and *V<sup>T</sup>*. *Σ* contains the singular values in descending order, and you can truncate it to retain only a subset of the singular values.

3. **Dimensionality Reduction**: Keep a specified number of singular values (*k*) and corresponding columns of *U* and *V* to perform dimensionality reduction. This effectively reduces the dimensionality of the data.

4. **Reconstruction**: Reconstruct the compressed image data using the truncated matrices *U*, *Σ*, and *V<sup>T</sup>*.

5. **Visualization**: Create visualisations (e.g., side-by-side comparisons) to showcase the effects of PCA-based compression on the MNIST images.

6. **Choosing the right cut-off point**: Implement PCA with different variance retention thresholds (e.g., retaining 95% of variance) and compare results.

![work flow](https://github.com/user-attachments/assets/61d03a0b-865b-460a-9b3e-34f12c4f959c)

## Visual comparison of the original MNIST with the truncated MNIST
![comparison of the original with the truncated mnist](https://github.com/user-attachments/assets/bf7f7d18-8257-47bb-8061-86cafb5e5cb7)

## Data Loss % after truncation calculated using Forbenius Norm
![results](https://github.com/user-attachments/assets/53ef5583-fe71-400a-b4a7-6dede6296ec3)

