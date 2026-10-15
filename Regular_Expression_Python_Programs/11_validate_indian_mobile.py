import re

n = input("Enter mobile number: ")
if re.fullmatch(r'[6-9]\d{9}', n):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
