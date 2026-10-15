import re

n = input("Enter vehicle number: ").upper()
if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}', n):
    print("Valid vehicle number")
else:
    print("Invalid vehicle number")
