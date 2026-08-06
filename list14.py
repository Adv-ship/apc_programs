numbers = [1,2,2,3,4,4,5,6,6]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Unique Elements:", unique)
