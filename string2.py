s = input("Enter a string: ")

v = c = d = sp = sc = 0

for ch in s:
    if ch in "AEIOUaeiou":
        v = v + 1
    elif ch.isalpha():
        c = c + 1
    elif ch.isdigit():
        d = d + 1
    elif ch == " ":
        sp = sp + 1
    else:
        sc = sc + 1

print("Vowels =", v)
print("Consonants =", c)
print("Digits =", d)
print("Spaces =", sp)
print("Special Characters =", sc)
