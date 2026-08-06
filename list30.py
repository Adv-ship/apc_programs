names = []
ages = []

n = int(input("Enter number of patients: "))

for i in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    names.append(name)
    ages.append(age)

print("\nPatient List")
for i in range(len(names)):
    print(names[i], "-", ages[i])

# Add Patient
name = input("\nEnter new patient name: ")
age = int(input("Enter age: "))
names.append(name)
ages.append(age)

print("\nAfter Adding Patient")
for i in range(len(names)):
    print(names[i], "-", ages[i])

# Delete Patient
delete = input("\nEnter patient name to delete: ")

if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)
    print("Patient Deleted")
else:
    print("Patient Not Found")

print("\nFinal Patient List")
for i in range(len(names)):
    print(names[i], "-", ages[i])
