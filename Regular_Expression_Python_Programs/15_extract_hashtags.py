import re

s = input("Enter social media post: ")
print(re.findall(r'#[A-Za-z0-9_]+', s))
