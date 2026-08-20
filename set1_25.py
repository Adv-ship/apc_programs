#1
s = {10, 20, 30, 40, 50}
print(s)

#2
a = [1, 2, 2, 3, 3, 4]
s = set(a)
print(s)

#3
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}

fruits.add("Papaya")
fruits.add("Guava")

print(fruits)

#4
numbers = {10, 20, 30, 40, 50}

numbers.remove(30)

print(numbers)

#5
students = {"Amit", "Rahul", "Sneha", "Priya"}

name = input("Enter name: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")

#6
    cities = {"Pune", "Mumbai", "Delhi", "Nashik"}

print("Total cities:", len(cities))

#7
languages = {"Python", "Java", "C++", "JavaScript"}

for language in languages:
    print(language)
#8
numbers = [1, 2, 2, 3, 4, 4, 5]

s = set(numbers)

print(s)

#9
a = {1, 2, 3}
b = {4, 5, 6}

print(a.union(b))

#10
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.intersection(b))

#11
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("First but not second:", a - b)
print("Second but not first:", b - a)

#12
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.symmetric_difference(b))

#13
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))

#14
a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b))

#15
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))

#16
a = {1, 2, 3}
b = {3, 2, 1}

print(a == b)

#17
student1 = {"Python", "Math", "English"}
student2 = {"Java", "Math", "English"}

print(student1.intersection(student2))

#18
sentence = input("Enter a sentence: ")

words = set(sentence.split())

print(words)

#19
morning = {"Amit", "Rahul", "Sneha"}
afternoon = {"Sneha", "Priya", "Rahul"}

print("Both:", morning & afternoon)
print("Morning only:", morning - afternoon)
print("Afternoon only:", afternoon - morning)
print("At least one:", morning | afternoon)

#20 & 21
python = {"Amit", "Rahul", "Sneha"}
java = {"Rahul", "Priya", "Sneha"}

print("Both courses:", python & java)
print("Only one course:", python ^ java)

#22
employee1 = {"Python", "Java", "SQL"}
employee2 = {"Python", "C++", "SQL"}

print("Common:", employee1 & employee2)
print("Employee 1 only:", employee1 - employee2)
print("Employee 2 only:", employee2 - employee1)
print("All skills:", employee1 | employee2)

#23
available = {"Python", "Java", "C++", "SQL"}
requested = {"Python", "SQL", "HTML"}

print("Available books:", available & requested)

#24
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)

#25
user1 = {"Amit", "Rahul", "Sneha", "Priya"}
user2 = {"Rahul", "Priya", "Kiran", "Rohit"}

print("Mutual friends:", user1 & user2)
print("User 1 only:", user1 - user2)
print("User 2 only:", user2 - user1)
print("Total unique friends:", len(user1 | user2))




