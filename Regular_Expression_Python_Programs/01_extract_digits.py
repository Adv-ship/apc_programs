import re

s = input("Enter a string: ")
print(re.findall(r'\d', s))
