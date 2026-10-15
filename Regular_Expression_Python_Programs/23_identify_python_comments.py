import re

s = input("Enter Python source line(s): ")
print(re.findall(r'^\s*#.*$', s, re.MULTILINE))
