s = input("Enter string: ")

first = ""
second = ""
f1 = 0
f2 = 0

for ch in s:
    c = s.count(ch)

    if c > f1:
        second = first
        f2 = f1
        first = ch
        f1 = c

    elif c > f2 and ch != first:
        second = ch
        f2 = c

print(second)
