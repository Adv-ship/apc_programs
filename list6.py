numbers = [25, 10, 45, 5, 30]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest Number:", largest)
print("Smallest Number:", smallest)
