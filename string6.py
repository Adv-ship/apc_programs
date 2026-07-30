s = input("Enter a string: ")
a = input("Enter character to replace: ")
b = input("Enter new character: ")

new = ""

for ch in s:
    if ch == a:
        new = new + b
    else:
        new = new + ch

print(new)
