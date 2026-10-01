import numpy as np

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Matrix:")
print(A)

print("\nFirst row:")
print(A[0])

print("\nLast column:")
print(A[:, -1])

print("\nDiagonal elements:")
print(np.diag(A))

print("\nSecond and third rows:")
print(A[1:3])
