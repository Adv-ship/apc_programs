import re

s = input("Enter student details (Name: Rahul, Roll: 84, Marks: 90): ")
name = re.search(r'Name:\s*(\w+)', s)
roll = re.search(r'Roll:\s*(\d+)', s)
marks = re.search(r'Marks:\s*(\d+)', s)

if name and roll and marks:
    print("Name:", name.group(1))
    print("Roll number:", roll.group(1))
    print("Marks:", marks.group(1))
else:
    print("Invalid format")
