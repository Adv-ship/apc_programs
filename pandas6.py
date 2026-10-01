import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Akash"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [85, 70, 90, 65, 78]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents below 75% attendance:")
print(df[df["Attendance_Percentage"] < 75])
