import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()

print("Original 3D array:")
print(arr)

print("\nFlattened array:")
print(flat)

# Greater than 50
print("\nElements greater than 50:")
print(flat[flat > 50])

# Even numbers
print("\nEven numbers:")
print(flat[flat % 2 == 0])

# Less than average
average = np.mean(flat)

print("\nAverage:", average)

print("\nElements less than average:")
print(flat[flat < average])
