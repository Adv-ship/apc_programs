
# PYTHON DIRECTORY PROGRAMS



# 11. COLLEGE PROJECT
# student + faculty


print("\n===== 11. COLLEGE PROJECT =====")


# student/details.py
def student_details():
    return {
        "Name": "Amit",
        "Roll No": 101,
        "Branch": "CSE"
    }


# student/marks.py
def student_marks():
    return [80, 85, 90, 75, 88]


# faculty/details.py
def faculty_details():
    return {
        "Name": "Prof. Sharma",
        "Department": "CSE"
    }


student = student_details()
marks = student_marks()
faculty = faculty_details()

print("Student Name:", student["Name"])
print("Roll No:", student["Roll No"])
print("Branch:", student["Branch"])
print("Marks:", marks)

print("Faculty Name:", faculty["Name"])
print("Department:", faculty["Department"])



# 12. LIBRARY APPLICATION
# Books + Members + Transactions


print("\n===== 12. LIBRARY APPLICATION =====")


# Books/books.py
books = {
    101: {
        "title": "Python",
        "author": "Guido"
    },
    102: {
        "title": "Java",
        "author": "James"
    }
}


def add_book(book_id, title, author):
    books[book_id] = {
        "title": title,
        "author": author
    }


def display_books():
    for book_id, book in books.items():
        print(book_id, book["title"], book["author"])


# Members/members.py
members = {}


def add_member(member_id, name):
    members[member_id] = name


def display_members():
    for member_id, name in members.items():
        print(member_id, name)


# Transactions/transactions.py
def issue_book(book_id, member_id):
    if book_id in books and member_id in members:
        print("Book issued successfully")
    else:
        print("Book or member not found")


def return_book(book_id):
    print("Book", book_id, "returned successfully")


add_member(1, "Amit")
add_member(2, "Priya")

add_book(103, "C++", "Bjarne")

print("Books:")
display_books()

print("\nMembers:")
display_members()

print("\nTransaction:")
issue_book(101, 1)
return_book(101)



# 13. E-COMMERCE APPLICATION
# Products + Customers + Orders + Payments

print("\n===== 13. E-COMMERCE APPLICATION =====")


# Products/products.py
products = {}


def add_product(product_id, name, price):
    products[product_id] = {
        "name": name,
        "price": price
    }


def display_products():
    for pid, product in products.items():
        print(
            pid,
            product["name"],
            "Rs.", product["price"]
        )


# Customers/customers.py
customers = {}


def add_customer(customer_id, name):
    customers[customer_id] = name


def display_customers():
    for cid, name in customers.items():
        print(cid, name)


# Orders/orders.py
orders = []


def create_order(customer_id, product_id, quantity):
    order = {
        "customer": customer_id,
        "product": product_id,
        "quantity": quantity
    }

    orders.append(order)

    print("Order created successfully")


def display_orders():
    for order in orders:
        print(order)


# Payments/payments.py
def make_payment(amount):
    print("Payment of Rs.", amount, "successful")


def refund(amount):
    print("Refund of Rs.", amount)


add_product(1, "Laptop", 50000)
add_product(2, "Mouse", 1000)

add_customer(101, "Amit")
add_customer(102, "Priya")

print("Products:")
display_products()

print("\nCustomers:")
display_customers()

create_order(101, 1, 1)

print("\nOrders:")
display_orders()

make_payment(50000)
refund(1000)



# 14. HOSPITAL PROJECT
# Patient + Doctor + Billing + Medical Records


print("\n===== 14. HOSPITAL PROJECT =====")


# PatientManagement/patient.py
patients = {}


def add_patient(patient_id, name, age):
    patients[patient_id] = {
        "name": name,
        "age": age
    }


def display_patients():
    for pid, patient in patients.items():
        print(
            pid,
            patient["name"],
            patient["age"]
        )


# DoctorManagement/doctor.py
doctors = {}


def add_doctor(doctor_id, name, department):
    doctors[doctor_id] = {
        "name": name,
        "department": department
    }


def display_doctors():
    for did, doctor in doctors.items():
        print(
            did,
            doctor["name"],
            doctor["department"]
        )


# Billing/billing.py
def create_bill(consultation, medicine):
    return consultation + medicine


def display_bill(amount):
    print("Total Bill: Rs.", amount)


# MedicalRecords/records.py
records = {}


def add_record(patient_id, disease):
    records[patient_id] = disease


def display_records():
    for patient_id, disease in records.items():
        print(
            "Patient ID:",
            patient_id,
            "Disease:",
            disease
        )


# Add patient
add_patient(1, "Amit", 21)
add_patient(2, "Priya", 22)

# Add doctor
add_doctor(101, "Dr. Sharma", "Cardiology")
add_doctor(102, "Dr. Patil", "General")

# Add medical records
add_record(1, "Fever")
add_record(2, "Cold")

print("Patients:")
display_patients()

print("\nDoctors:")
display_doctors()

print("\nMedical Records:")
display_records()

# Billing
bill = create_bill(500, 1000)

print("\nBilling:")
display_bill(bill)

