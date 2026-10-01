import numpy as np

# Create an array from 1 to 20
arr = np.arange(1, 21)

# Boolean indexing
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("Array:", arr)
print("Even numbers:", even)
print("Odd numbers:", odd)
