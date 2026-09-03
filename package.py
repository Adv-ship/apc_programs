

# 7. MATHUTILS PACKAGE


print("\n===== 7. MATHUTILS PACKAGE =====")

# basic.py functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# number.py functions
def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)

    return total == n


def number_palindrome(n):
    return str(n) == str(n)[::-1]


# statistics.py functions
def mean(numbers):
    return sum(numbers) / len(numbers)


def maximum(numbers):
    return max(numbers)


def minimum(numbers):
    return min(numbers)


# Basic operations
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

# Number operations
n = 153

print("Prime:", prime(n))
print("Armstrong:", armstrong(n))
print("Palindrome:", number_palindrome(n))

# Statistics
numbers = [10, 20, 30, 40, 50]

print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))



# 8. STUDENT PACKAGE
# marks.py + grade.py + attendance.py

print("\n===== 8. STUDENT PACKAGE =====")


def total_marks(marks):
    return sum(marks)


def percentage(marks):
    return sum(marks) / len(marks)


def student_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def attendance_eligible(attendance):
    return attendance >= 75


marks = [80, 85, 90, 75, 88]

total = total_marks(marks)
percent = percentage(marks)

attendance = float(input("Enter attendance percentage: "))

print("Total Marks:", total)
print("Percentage:", percent)
print("Grade:", student_grade(percent))

if attendance_eligible(attendance):
    print("Attendance: Eligible")
else:
    print("Attendance: Not Eligible")



# 9. BANKING PACKAGE
# account.py + transaction.py + loan.py


print("\n===== 9. BANKING PACKAGE =====")


def create_account(name, balance):
    return {
        "name": name,
        "balance": balance
    }


def deposit(account, amount):
    account["balance"] += amount


def withdraw(account, amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        return True
    return False


def calculate_loan(principal, rate, years):
    interest = principal * rate * years / 100
    return principal + interest


# Account creation
account = create_account("Amit", 10000)

print("Account Holder:", account["name"])
print("Initial Balance:", account["balance"])

# Deposit
deposit_amount = 5000
deposit(account, deposit_amount)

print("After Deposit:", account["balance"])

# Withdrawal
withdraw_amount = 2000

if withdraw(account, withdraw_amount):
    print("After Withdrawal:", account["balance"])
else:
    print("Insufficient Balance")

# Loan calculation
principal = 50000
rate = 8
years = 2

loan_amount = calculate_loan(principal, rate, years)

print("Loan Amount:", loan_amount)



# 10. TEXTTOOLS PACKAGE
# cleaning.py + tokenization.py + frequency.py
print("\n===== 10. TEXTTOOLS PACKAGE =====")

import string


def clean_text(text):
    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove extra spaces
    text = " ".join(text.split())

    return text


def tokenize(text):
    return text.split()


def word_frequency(words):
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


text = input("Enter text: ")

# Cleaning
cleaned = clean_text(text)

# Tokenization
words = tokenize(cleaned)

# Frequency
frequency = word_frequency(words)

print("Clean Text:", cleaned)
print("Tokens:", words)
print("Word Frequency:", frequency)
