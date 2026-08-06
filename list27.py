salary = []

n = int(input("Enter number of employees: "))

for i in range(n):
    s = int(input("Enter salary: "))
    salary.append(s)

highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)

above50000 = 0
below30000 = 0

for i in salary:
    if i > 50000:
        above50000 += 1
    if i < 30000:
        below30000 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees earning above 50000:", above50000)
print("Employees earning below 30000:", below30000)
