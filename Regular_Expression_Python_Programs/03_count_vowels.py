import re

s = input("Enter a string: ")
print("Vowel count:", len(re.findall(r'[aeiouAEIOU]', s)))
