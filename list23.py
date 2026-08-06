lst = input("Enter list elements: ").split()

for i in lst:
    if lst.count(i) > 0:
        print(i, ":", lst.count(i))
        while i in lst:
            lst.remove(i)
