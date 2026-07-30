n = int(input("Enter number: "))

i = 2
prime = True

while i < n:
    if n % i == 0:
        prime = False
    i = i + 1

if prime and n > 1:
    print("Prime")
else:
    print("Not Prime")
