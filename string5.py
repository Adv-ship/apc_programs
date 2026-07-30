s = input("Enter a string: ")

u = 0
l = 0

for ch in s:
    if ch.isupper():
        u = u + 1
    elif ch.islower():
        l = l + 1

print("Uppercase =", u)
print("Lowercase =", l)
