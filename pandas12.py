import pandas as pd

attendance = {
    "Amit": 85,
    "Rahul": 70,
    "Sneha": 95,
    "Priya": 65,
    "Akash": 92
}

s = pd.Series(attendance)

print("Attendance:")
print(s)

print("\nAverage Attendance:", s.mean())

print("\nAttendance below 75:")
print(s[s < 75])

print("\nAttendance above 90:")
print(s[s > 90])

print("\nHighest Attendance:", s.max())
