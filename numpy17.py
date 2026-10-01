import numpy as np

marks = np.array([45, 67, 89, 56, 78, 92, 34, 71, 85, 63,
                  49, 95, 58, 76, 88, 42, 69, 81, 55, 73])

average = np.mean(marks)

print("Marks:")
print(marks)

print("\nClass average:", average)

print("\nMarks above average:")
print(marks[marks > average])
