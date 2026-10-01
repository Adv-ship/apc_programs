import numpy as np

arr = np.arange(1, 28).reshape(3, 3, 3)

print("Original 3D array:")
print(arr)

flat = arr.flatten()

print("\nFlattened array:")
print(flat)

print("\nSum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))
