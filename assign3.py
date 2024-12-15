import numpy as np

# Initializing matrices
x = np.array([[1, 2], [4, 5]])

y = np.array([[7, 8], [9, 10]])



# Element-wise addition
print("The element-wise addition of matrices is:")
print(np.add(x, y))

# Element-wise subtraction
print("The element-wise subtraction of matrices is:")
print(np.subtract(x, y))

# Matrix multiplication (dot product)
print("The matrix multiplication (dot product) result is:")
print(np.dot(x, y))

# Transpose of matrix x
print("The transpose of the given matrix x is:")
print(x.T)
