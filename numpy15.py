import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Array A:")
print(A)

print("\nArray B:")
print(B)

print("\nHorizontal concatenation:")
print(np.hstack((A, B)))

print("\nVertical concatenation:")
print(np.vstack((A, B)))
