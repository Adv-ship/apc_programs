ids = (101, 102, 103, 104, 105)

id = int(input("Enter ID: "))

if id in ids:
    print("Index:", ids.index(id))
else:
    print("ID not found")
