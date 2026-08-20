#1
student = {
    "roll": 84,
    "name": "Bhushan",
    "department": "CSE",
    "marks": 85
}

print(student)


#2
employee = {
    "id": 101,
    "name": "Amit",
    "salary": 30000
}

print(employee["name"])


#3
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5,
    "Eraser": 5
}

products["Bottle"] = 100

print(products)


#4
marks = {
    "Amit": 70,
    "Rahul": 80,
    "Sneha": 75
}

marks["Rahul"] = 90

print(marks)


#5
cities = {
    "Pune": 30,
    "Mumbai": 50,
    "Delhi": 40
}

cities.pop("Pune")

print(cities)


#6
employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha"
}

id = int(input("Enter employee ID: "))

if id in employees:
    print("Employee exists")
else:
    print("Employee does not exist")


#7
students = {
    "Amit": 80,
    "Rahul": 75,
    "Sneha": 90
}

print("Total:", len(students))


#8
student = {
    "name": "Amit",
    "age": 20,
    "marks": 85
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


#9
languages = {
    "Python": "Guido",
    "Java": "James",
    "C++": "Bjarne"
}

for language, creator in languages.items():
    print(language, creator)


#10
students = {}

for i in range(5):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print(students)


#11
marks = {
    "Amit": 80,
    "Rahul": 95,
    "Sneha": 75
}

name = max(marks, key=marks.get)

print("Highest:", name, marks[name])


#12
marks = {
    "Amit": 80,
    "Rahul": 95,
    "Sneha": 75
}

name = min(marks, key=marks.get)

print("Lowest:", name, marks[name])


#13
marks = {
    "Amit": 80,
    "Rahul": 90,
    "Sneha": 70
}

average = sum(marks.values()) / len(marks)

print("Average:", average)


#14
text = input("Enter string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)


#15
sentence = input("Enter sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


#16
a = {
    "A": 1,
    "B": 2
}

b = {
    "C": 3,
    "D": 4
}

a.update(b)

print(a)


#17
a = {
    "A": 1,
    "B": 2,
    "C": 3
}

b = {
    "B": 4,
    "C": 5,
    "D": 6
}

print(a.keys() & b.keys())


#18
a = {
    "A": 10,
    "B": 20,
    "C": 30
}

b = {
    "X": 20,
    "Y": 30,
    "Z": 40
}

print(a.values() & b.values())


#19
students = {
    "Amit": 80,
    "Rahul": 80,
    "Sneha": 90
}

new = {}

for key, value in students.items():
    if value not in new.values():
        new[key] = value

print(new)


#20
students = {
    "C": 80,
    "A": 90,
    "B": 70
}

for key in sorted(students):
    print(key, students[key])


#21
squares = {}

for i in range(1, 11):
    squares[i] = i * i

print(squares)


#22
squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print(squares)


#23
numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)


#24
cubes = {}

for i in range(1, 11):
    cubes[i] = i * i * i

print(cubes)


#25
students = {
    "Amit": 80,
    "Rahul": 90
}

students["Sneha"] = 85
students["Amit"] = 95
students.pop("Rahul")

name = input("Search student: ")

if name in students:
    print("Student:", students[name])
else:
    print("Student not found")

print("All students:", students)

print("Highest:", max(students.values()))

print("Average:", sum(students.values()) / len(students))


#26
employees = {
    "Amit": 40000,
    "Rahul": 60000,
    "Sneha": 55000
}

print("Highest:", max(employees.values()))
print("Lowest:", min(employees.values()))
print("Average:", sum(employees.values()) / len(employees))

for name, salary in employees.items():
    if salary > 50000:
        print("More than 50000:", name)


#27
products = {
    "Pen": 20,
    "Book": 15,
    "Bag": 5
}

products["Pencil"] = 10
products["Pen"] = 30
products.pop("Book")

name = input("Search product: ")

if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

print("Products below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name, quantity)


#28
contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234"
}

contacts["Sneha"] = "9876512345"

name = input("Search contact: ")

if name in contacts:
    print(contacts[name])
else:
    print("Contact not found")

contacts["Amit"] = "9999999999"

contacts.pop("Rahul")

print(contacts)


#29
books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

books[104] = "SQL"

id = int(input("Search book ID: "))

if id in books:
    print(books[id])
else:
    print("Book not found")

books.pop(103)

print(books)

print("Total books:", len(books))


#30
students = {
    "Amit": "CSE",
    "Rahul": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC"
}

groups = {}

for name, department in students.items():
    if department not in groups:
        groups[department] = []
    groups[department].append(name)

print(groups)


#31
words = ["cat", "dog", "apple", "ball", "sun"]

result = {}

for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print(result)


#32
numbers = [2, 4, 6, 8, 10]
target = 12

seen = {}

for number in numbers:
    if target - number in seen:
        print(target - number, number)
        break

    seen[number] = True


#33
text = input("Enter string: ")

count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

for ch in text:
    if count[ch] == 1:
        print("First unique character:", ch)
        break


#34
text = input("Enter string: ")

count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

for ch in text:
    if count[ch] > 1:
        print("First repeated character:", ch)
        break


#35
paragraph = input("Enter paragraph: ")

words = paragraph.split()
result = {}

for word in words:
    length = len(word)
    result[length] = result.get(length, 0) + 1

print(result)
