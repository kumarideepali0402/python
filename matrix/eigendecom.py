def eigen_decomposition(matrix, iterations=100):
    size = len(matrix)
    eigenvalues = [0] * size
    eigenvectors = [[0] * size for _ in range(size)]

    # Initialize eigenvectors as identity matrix
    for i in range(size):
        eigenvectors[i][i] = 1

    # Power iteration method
    for _ in range(iterations):
        new_eigenvectors = matrix_multiply(matrix, eigenvectors)
        eigenvalues = [dot_product(new_eigenvectors[i], eigenvectors[i]) for i in range(size)]
        eigenvectors = [normalize(vector) for vector in new_eigenvectors]

    return eigenvalues, eigenvectors

# Example usage:
matrix = [[4, -2],
          [1, 1]]

eigenvalues, eigenvectors = eigen_decomposition(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
for vector in eigenvectors:
    print(vector)
In this code:

dot_product, scalar_multiply, subtract_vectors, magnitude, normalize, matrix_transpose, and matrix_multiply functions are defined for basic vector and matrix operations.
eigen_decomposition function performs eigen decomposition using the power iteration method. It iteratively multiplies the input matrix with a set of initial eigenvectors and updates the eigenvalues and eigenvectors based on the resulting values.






