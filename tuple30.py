patients = (
    (101, "Amit", 25, "A+"),
    (102, "Rahul", 30, "B+"),
    (103, "Sneha", 22, "A+"),
    (104, "Priya", 28, "O+")
)


print("All Patients:")
for p in patients:
    print(p)


id = int(input("\nEnter patient ID: "))

for p in patients:
    if p[0] == id:
        print("Patient found:", p)


print("\nTotal patients:", len(patients))


blood = input("\nEnter blood group: ")

print("Patients with", blood, ":")

for p in patients:
    if p[3] == blood:
        print(p)
