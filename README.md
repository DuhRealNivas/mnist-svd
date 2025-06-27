# mnist-svd
Singular Value Decomposition (SVD) to the MNIST dataset for image compression
## Instructions

1. **Load and Prepare the MNIST Data**: Load the MNIST dataset (see MyLearning folder) and get familiar with the data. You may want to standardise the pixel values.

2. **Apply SVD**: Perform SVD on the image data. SVD decomposes the data matrix into three matrices: *U*, *Σ*, and *V<sup>T</sup>*. *Σ* contains the singular values in descending order, and you can truncate it to retain only a subset of the singular values.

3. **Dimensionality Reduction**: Keep a specified number of singular values (*k*) and corresponding columns of *U* and *V* to perform dimensionality reduction. This effectively reduces the dimensionality of the data.

4. **Reconstruction**: Reconstruct the compressed image data using the truncated matrices *U*, *Σ*, and *V<sup>T</sup>*.

5. **Visualization**: Create visualisations (e.g., side-by-side comparisons) to showcase the effects of PCA-based compression on the MNIST images.

6. **Choosing the right cut-off point**: Implement PCA with different variance retention thresholds (e.g., retaining 95% of variance) and compare results.
