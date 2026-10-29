
import matplotlib.pyplot as plt

students = ["Amit", "Rahul", "Priya", "Sneha", "Rohit"]
marks = [70, 85, 90, 65, 80]

plt.pie(marks, labels=students, autopct="%1.1f%%")

plt.title("Student Marks - Pie Chart")

plt.show()
