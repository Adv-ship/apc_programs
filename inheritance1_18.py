
# 1. EMPLOYEE - MANAGER

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


m = Manager(101, "Rahul", 50000, "IT")
m.display_manager()



# 2. VEHICLE - CAR


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self):
        discount = self.price * 0.10
        return self.price - discount

    def display_car(self):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.discounted_price())


car = Car("Honda", "City", "Petrol", 1000000)
car.display_car()



# 3. MULTIPLE INHERITANCE - ACADEMIC + SPORTS


class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, name, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)
        self.name = name

    def performance(self):
        total = self.marks + self.points
        print("Name:", self.name)
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", total)


s = Student("Amit", 80, 15)
s.performance()



# 4. PERSONAL + PROFESSIONAL DETAILS


class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class EmployeeDetails(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e = EmployeeDetails("Raj", 25, 101, "Developer", 50000)
e.display()



# 5. MULTILEVEL INHERITANCE
# Person -> Student -> ResearchStudent


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class StudentPerson(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(StudentPerson):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide:", self.guide)


rs = ResearchStudent(
    "Rahul", 24, 101, "M.Tech",
    "Artificial Intelligence", "Dr. Sharma"
)

rs.display()



# 6. BANK ACCOUNT - MULTILEVEL INHERITANCE


class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display_details(self):
        self.display()
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


p = PremiumSavingsAccount(12345, 50000, 5, "Free Insurance")
p.display_details()


# 7. SHAPE - CIRCLE, RECTANGLE, TRIANGLE


class Shape:
    def display_name(self):
        print("This is a shape")


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class RectangleShape(Shape):
    def area(self, length, breadth):
        return length * breadth


class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height


c = Circle()
print("Circle Area:", c.area(5))

r = RectangleShape()
print("Rectangle Area:", r.area(10, 5))

t = Triangle()
print("Triangle Area:", t.area(10, 5))



# 8. EMPLOYEE - MANAGER, DEVELOPER, TESTER


class EmployeeSalary:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class ManagerSalary(EmployeeSalary):
    def salary(self):
        return self.basic_salary + 15000


class Developer(EmployeeSalary):
    def salary(self):
        return self.basic_salary + 10000


class Tester(EmployeeSalary):
    def salary(self):
        return self.basic_salary + 5000


manager = ManagerSalary(1, "Raj", 50000)
developer = Developer(2, "Amit", 40000)
tester = Tester(3, "Ravi", 30000)

print("Manager Salary:", manager.salary())
print("Developer Salary:", developer.salary())
print("Tester Salary:", tester.salary())



# 9. HIERARCHICAL + MULTIPLE INHERITANCE
# Person -> Student
# Person -> Faculty
# Student + Faculty -> TeachingAssistant


class PersonBase:
    def __init__(self, name):
        self.name = name


class StudentBase(PersonBase):
    def student_details(self):
        print("Student:", self.name)


class FacultyBase(PersonBase):
    def faculty_details(self):
        print("Faculty:", self.name)


class TeachingAssistant(StudentBase, FacultyBase):
    def display(self):
        print("Teaching Assistant:", self.name)


ta = TeachingAssistant("Rahul")
ta.display()



# 10. VEHICLE - CAR, BIKE - SPORTSCAR, ELECTRICBIKE


class VehicleBase:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class CarBase(VehicleBase):
    def car_method(self):
        print("This is a car")


class BikeBase(VehicleBase):
    def bike_method(self):
        print("This is a bike")


class SportsCar(CarBase):
    def speed(self):
        print("Sports Car has high speed")


class ElectricBike(BikeBase):
    def battery(self):
        print("Electric Bike has a battery")


sc = SportsCar("BMW")
sc.display()
sc.car_method()
sc.speed()

eb = ElectricBike("Ola")
eb.display()
eb.bike_method()
eb.battery()



# 11. STUDENT - RESULT


class StudentResult:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(StudentResult):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def display_result(self):
        total = sum(self.marks)
        percentage = total / 3

        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


result = Result(101, "Amit", "CSE", [80, 75, 90])
result.display_result()



# 12. PRODUCT - ELECTRONIC PRODUCT


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self):
        discount = self.price * 0.10
        return self.price - discount

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Original Price:", self.price)
        print("Final Price:", self.final_price())


ep = ElectronicProduct(
    101, "Laptop", 60000, "HP", "2 Years"
)

ep.display()



# 13. MULTIPLE INHERITANCE - PRINTER + SCANNER

class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class MultifunctionDevice(Printer, Scanner):
    def use_device(self):
        self.print_document()
        self.scan_document()


device = MultifunctionDevice()
device.use_device()



# 14. MULTIPLE INHERITANCE - CAMERA + PHONE


class Camera:
    def take_photo(self):
        print("Photo taken")


class Phone:
    def make_call(self):
        print("Making phone call")


class Smartphone(Camera, Phone):
    def use_phone(self):
        self.take_photo()
        self.make_call()


smartphone = Smartphone()
smartphone.use_phone()



# 15. MULTILEVEL INHERITANCE
# Person -> Student -> ResearchStudent


class Person15:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student15(Person15):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent15(Student15):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide:", self.guide)


rstudent = ResearchStudent15(
    "Amit", 24, 10, "M.Tech",
    "Machine Learning", "Dr. Patil"
)

rstudent.display()



# 16. MULTILEVEL INHERITANCE
# Person -> Student -> ResearchStudent

class Person16:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student16(Person16):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent16(Student16):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide:", self.guide)


r = ResearchStudent16(
    "Ravi", 25, 20, "M.Tech",
    "Deep Learning", "Dr. Sharma"
)

r.display()



# 17. ANIMAL - DOG, CAT, COW


class Animal:
    def eat(self):
        print("Animal eats food")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


dog = Dog()
dog.eat()
dog.sound()

cat = Cat()
cat.eat()
cat.sound()

cow = Cow()
cow.eat()
cow.sound()



# 18. PERSON - DOCTOR, PATIENT, SURGEON, RESEARCHER

class Person18:
    def __init__(self, name):
        self.name = name


class Doctor(Person18):
    def doctor_work(self):
        print(self.name, "is a doctor")


class Patient(Person18):
    def patient_work(self):
        print(self.name, "is a patient")


class Surgeon(Doctor, Patient):
    def surgery(self):
        print(self.name, "performs surgery")


class MedicalResearcher(Doctor, Patient):
    def research(self):
        print(self.name, "does medical research")


surgeon = Surgeon("Dr. Rahul")
surgeon.surgery()

researcher = MedicalResearcher("Dr. Amit")
researcher.research()
