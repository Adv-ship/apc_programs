
# PYTHON MODULES AND PACKAGES

# 1. CALCULATOR MODULE


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("\n===== 1. CALCULATOR =====")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))



# 2. STUDENT MODULE
def student_total(marks):
    return sum(marks)

def student_percentage(marks):
    return sum(marks) / len(marks)

def student_grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "F"


print("\n===== 2. STUDENT =====")

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

total = student_total(marks)
percentage = student_percentage(marks)

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", student_grade(percentage))



# 3. NUMBER UTILITIES MODULE


def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def number_palindrome(n):
    return str(n) == str(n)[::-1]


def armstrong(n):
    digits = str(n)
    total = 0

    for digit in digits:
        total += int(digit) ** len(digits)

    return total == n


def perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


print("\n===== 3. NUMBER UTILITIES =====")

n = int(input("Enter number: "))

print("Prime:", prime(n))
print("Palindrome:", number_palindrome(n))
print("Armstrong:", armstrong(n))
print("Perfect:", perfect(n))



# 4. STRING UTILITIES MODULE


def count_vowels(s):
    count = 0

    for ch in s.lower():
        if ch in "aeiou":
            count += 1

    return count


def reverse_string(s):
    return s[::-1]


def string_palindrome(s):
    return s == s[::-1]


def word_count(s):
    return len(s.split())


def remove_spaces(s):
    return s.replace(" ", "")


print("\n===== 4. STRING UTILITIES =====")

s = input("Enter string: ")

print("Vowels:", count_vowels(s))
print("Reverse:", reverse_string(s))
print("Palindrome:", string_palindrome(s))
print("Word Count:", word_count(s))
print("Without Spaces:", remove_spaces(s))



# 5. SALARY MODULE


def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    return basic + hra + da


def deductions(gross):
    return gross * 0.10


def net_salary(gross, deduction):
    return gross - deduction


print("\n===== 5. SALARY =====")

basic = float(input("Enter basic salary: "))

gross = gross_salary(basic)
deduction = deductions(gross)
net = net_salary(gross, deduction)

print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)



# 6. RECURSIVE MODULE


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)


def decimal_to_binary(n):
    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)


print("\n===== 6. RECURSIVE FUNCTIONS =====")

n = int(input("Enter number: "))

print("Factorial:", factorial(n))
print("Fibonacci:", fibonacci(n))
print("Sum of Digits:", sum_digits(n))

if n == 0:
    print("Binary: 0")
else:
    print("Binary:", decimal_to_binary(n))


