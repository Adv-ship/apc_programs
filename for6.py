x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 1
fact = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = fact * (i - 1) * i
    sum = sum + sign * (x ** i) / fact
    sign = -sign

print(sum)
