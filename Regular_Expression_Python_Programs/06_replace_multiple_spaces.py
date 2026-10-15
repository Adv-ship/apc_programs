import re

s = input("Enter a string: ")
print(re.sub(r' +', ' ', s))
