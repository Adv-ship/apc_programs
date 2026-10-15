import re

s = input("Enter a string: ")
print(re.sub(r'[^A-Za-z0-9 ]', '', s))
