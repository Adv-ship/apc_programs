lst = input("Enter list elements: ").split()

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print("List after removing duplicates:", unique)
