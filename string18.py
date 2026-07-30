s = input("Enter a string: ")

new = ""

for ch in s:
    if ch not in new:
        new = new + ch

print(new)
