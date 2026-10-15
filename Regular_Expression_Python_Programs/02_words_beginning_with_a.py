import re

s = input("Enter a sentence: ")
print(re.findall(r'\b[Aa]\w*', s))
