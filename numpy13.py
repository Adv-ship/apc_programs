import numpy as np

arr = np.array([45, 12, 89, 23, 7, 56, 34])

print("Original array:")
print(arr)

print("\nAscending order:")
print(np.sort(arr))

print("\nDescending order:")
print(np.sort(arr)[::-1])
