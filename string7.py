s = input("Enter a string: ")

new = ""

for ch in s:
    if ch != " ":
        new = new + ch

print(new)
