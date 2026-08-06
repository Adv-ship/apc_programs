students = ["Amit", "Rahul", "Sneha"]

print("Total Students:", len(students))

name = input("Enter student name: ")

if name in students:
    print("Present")
else:
    print("Absent")

students.append("Priya")
students.remove("Rahul")

print("Updated List:", students)
