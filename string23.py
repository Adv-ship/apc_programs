s = input("Enter string: ")

new = ""

count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        new = new + s[i] + str(count)
        count = 1

new = new + s[-1] + str(count)

if len(new) < len(s):
    print(new)
else:
    print(s)
