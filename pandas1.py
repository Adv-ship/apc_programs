import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Akash"],
    "Python": [80, 65, 90, 72, 85],
    "DBMS": [75, 70, 88, 80, 78],
    "Maths": [85, 60, 92, 75, 80]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nWith Total and Average:")
print(df)

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])
