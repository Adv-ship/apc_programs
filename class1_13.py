
# 1. STUDENT CLASS


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage)
        print()


s1 = Student(1, "Rahul", [80, 75, 90, 85, 70])
s2 = Student(2, "Amit", [70, 80, 75, 85, 90])

s1.display()
s2.display()



# 2. EMPLOYEE - HRA, DA AND GROSS SALARY

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        gross = self.basic_salary + hra + da

        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)
        print()


e1 = Employee(101, "Raj", 30000)
e1.calculate_salary()



# 3. RECTANGLE - AREA AND PERIMETER


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
print()



# 4. CIRCLE - AREA AND CIRCUMFERENCE


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


c = Circle(7)

print("Circle Area:", c.area())
print("Circle Circumference:", c.circumference())
print()



# 5. BOOK CLASS

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("--------------------")


b1 = Book(1, "Python", "John", 500)
b2 = Book(2, "Java", "James", 600)
b3 = Book(3, "C++", "Bjarne", 700)

b1.display()
b2.display()
b3.display()



# 6. ELECTRICITY BILL


class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):

        if self.units <= 100:
            bill = self.units * 2

        elif self.units <= 200:
            bill = (100 * 2) + ((self.units - 100) * 3)

        else:
            bill = (100 * 2) + (100 * 3) + ((self.units - 200) * 5)

        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units:", self.units)
        print("Electricity Bill:", bill)
        print()


eb = ElectricityBill(1001, "Rahul", 250)
eb.calculate_bill()



# 7. MOBILE PHONE


class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount_price(self):
        discount = self.price * 0.10
        final_price = self.price - discount

        print("Discount:", discount)
        print("Price after Discount:", final_price)
        print()


m = MobilePhone("Samsung", "S24", "128 GB", 50000)

m.display()
m.discount_price()



# 8. PATIENT

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self):
        medicine = 500
        total = self.consultation_fee + medicine

        print("Medicine Charges:", medicine)
        print("Total Bill:", total)
        print()


p = Patient(101, "Amit", 25, "Fever", 500)

p.display()
p.total_bill()



# 9. ATM MENU-DRIVEN PROGRAM

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
            print("New Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def account_details(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


# ATM object
atm = ATM(12345, "Rahul", 10000)

while True:

    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.account_details()

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid Choice")



# 10. VEHICLE RENTAL


class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self, days):
        if self.available == False:
            charge = self.rental_rate * days
            self.available = True

            print("Vehicle returned successfully")
            print("Number of Days:", days)
            print("Rental Charge:", charge)

        else:
            print("Vehicle was not rented")


v = Vehicle("MH12AB1234", "Honda City", 1500)

v.rent()
v.return_vehicle(3)



# 11. SHOPPING CART


class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart")
                return

        print("Product not found")

    def total_bill(self):
        total = 0

        for product in self.products:
            total = total + product[1]

        print("Total Bill:", total)

    def __del__(self):
        print("Shopping cart object destroyed")


cart = ShoppingCart("Rahul", 101)

cart.add_product("Pen", 20)
cart.add_product("Book", 100)
cart.add_product("Bag", 500)

cart.remove_product("Pen")

cart.total_bill()



# 12. FOOD ORDER


class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        amount = self.quantity * self.price
        tax = amount * 0.05
        total = amount + tax

        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Amount:", amount)
        print("Tax:", tax)
        print("Total Bill:", total)

    def __del__(self):
        print("Order completed")


order = FoodOrder(101, "Amit", "Pizza", 2, 250)

order.total_bill()



# 13. STUDENT RESULT


class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

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
            return "Fail"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("Student Result object destroyed")


result = StudentResult("Rahul", [85, 90, 80, 75, 88])

result.display()
