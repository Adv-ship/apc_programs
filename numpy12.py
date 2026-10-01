import numpy as np

arr = np.array([10, 25, 55, 70, 40, 85, 30, 60, 45, 90])

print("Original array:")
print(arr)

arr[arr > 50] = 0

print("\nAfter replacement:")
print(arr)
