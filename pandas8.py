import pandas as pd

marks = {
    "Amit": 80,
    "Rahul": 65,
    "Sneha": 90,
    "Priya": 72,
    "Akash": 85
}

s = pd.Series(marks)

print("Series:")
print(s)

print("\nMarks of Amit:")
print(s["Amit"])

print("\nMaximum Marks:", s.max())
print("Minimum Marks:", s.min())
print("Average Marks:", s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])
