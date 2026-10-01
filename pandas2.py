import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Akash"],
    "Department": ["CSE", "IT", "CSE", "HR", "IT"],
    "Salary": [45000, 60000, 75000, 52000, 48000],
    "Experience": [2, 5, 7, 4, 3]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:", df["Salary"].mean())

print("Highest Salary:", df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])
