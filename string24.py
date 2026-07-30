s = input("Enter string: ")

max = 0
ch = ""

for i in s:
    if s.count(i) > max:
        max = s.count(i)
        ch = i

print(ch)
