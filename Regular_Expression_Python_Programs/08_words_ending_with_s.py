import re

s = input("Enter a sentence: ")
print(re.findall(r'\b\w+s\b', s, re.IGNORECASE))
