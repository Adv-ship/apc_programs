p = input("Enter password: ")

u = l = d = sp = 0

for ch in p:
    if ch.isupper():
        u = 1
    elif ch.islower():
        l = 1
    elif ch.isdigit():
        d = 1
    else:
        sp = 1

if len(p) >= 8 and u and l and d and sp:
    print("Valid Password")
else:
    print("Invalid Password")
