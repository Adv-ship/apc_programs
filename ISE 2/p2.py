students = []
grades = []


def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))

    students.append(name)
    grades.append(grade)

    print("Student added successfully!")


def update_grade():
    name = input("Enter student name: ")

    if name in students:
        index = students.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
        print("Grade updated successfully!")
    else:
        print("Student not found.")


def remove_student():
    name = input("Enter student name: ")

    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully!")
    else:
        print("Student not found.")


def display_average():
    if len(grades) == 0:
        print("No grades available.")
    else:
        average = sum(grades) / len(grades)
        print("Average grade:", average)


def display_highest_lowest():
    if len(grades) == 0:
        print("No grades available.")
    else:
        highest = max(grades)
        lowest = min(grades)

        highest_index = grades.index(highest)
        lowest_index = grades.index(lowest)

        print("Highest grade:", highest, "-", students[highest_index])
        print("Lowest grade:", lowest, "-", students[lowest_index])


def display_students():
    if len(students) == 0:
        print("No students available.")
    else:
        print("\nStudent List:")
        for i in range(len(students)):
            print(students[i], "-", grades[i])


# Main menu
while True:
    
    print("1. Add new student")
    print("2. Update grade")
    print("3. Remove student")
    print("4. Display all students")
    print("5. Display average grade")
    print("6. Display highest and lowest grade")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_grade()

    elif choice == "3":
        remove_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        display_average()

    elif choice == "6":
        display_highest_lowest()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
