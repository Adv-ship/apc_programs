import pandas as pd

salary = {
    "Amit": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Priya": 52000,
    "Akash": 48000
}

s = pd.Series(salary)

print("Series:")
print(s)

print("\nHighest Salary:", s.max())
print("Lowest Salary:", s.min())
print("Average Salary:", s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])
