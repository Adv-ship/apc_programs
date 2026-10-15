import re

s = input("Enter a sentence: ")
print(re.findall(r'\b(\w+)\s+\1\b', s, re.IGNORECASE))
