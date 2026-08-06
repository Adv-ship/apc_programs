list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common Elements:", common)
