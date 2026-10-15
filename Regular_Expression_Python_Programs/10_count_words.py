import re

s = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', s)
print("Word count:", len(words))
