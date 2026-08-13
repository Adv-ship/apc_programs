t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

common = ()

for n in t1:
    if n in t2:
        common = common + (n,)

print("Common elements:", common)
