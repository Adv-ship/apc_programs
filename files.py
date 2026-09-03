
# PYTHON FILE HANDLING 


# 1. Create student.txt and write details
f = open("student.txt", "w")
f.write("Name: Bhushan\nRoll:84\nBranch:CSE\nSemester:5\n")
f.close()

# 2. Display complete contents
f = open("student.txt", "r")
print("2.\n", f.read())
f.close()

# 3. Append data
f = open("student.txt", "a")
f.write("CGPA:8.5\n")
f.close()

# 4. Read line by line
f = open("student.txt", "r")
print("4.")
for line in f:
    print(line.strip())
f.close()

# 5. Count lines
f = open("student.txt", "r")
print("5. Lines =", len(f.readlines()))
f.close()

# 6. Count words
f = open("student.txt", "r")
print("6. Words =", len(f.read().split()))
f.close()

# 7. Count characters
f = open("student.txt", "r")
print("7. Characters =", len(f.read()))
f.close()

# 8. Reverse lines
f = open("student.txt", "r")
print("8.")
for line in reversed(f.readlines()):
    print(line.strip())
f.close()

# 9. Count vowels and consonants
f = open("student.txt", "r")
text = f.read().lower()
v = c = 0
for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            v += 1
        else:
            c += 1
print("9. Vowels =", v, "Consonants =", c)
f.close()

# 10. Count alphabets, digits, spaces, special chars
f = open("student.txt", "r")
text = f.read()
a = d = s = sp = 0
for ch in text:
    if ch.isalpha():
        a += 1
    elif ch.isdigit():
        d += 1
    elif ch.isspace():
        s += 1
    else:
        sp += 1
print("10.", a, d, s, sp)
f.close()

# 11. Longest word
f = open("student.txt", "r")
words = f.read().split()
longest = max(words, key=len)
print("11. Longest =", longest)
f.close()

# 12. Word frequency
f = open("student.txt", "r")
freq = {}
for w in f.read().lower().split():
    freq[w] = freq.get(w, 0) + 1
print("12.", freq)
f.close()

# 13. Search word
search = "amit"
f = open("student.txt", "r")
count = 0
for i, line in enumerate(f, 1):
    if search in line.lower():
        print("13. Found in line", i)
        count += line.lower().count(search)
print("Occurrences =", count)
f.close()

# 14. Replace word
f = open("student.txt", "r")
data = f.read()
f.close()
data = data.replace("Amit", "Rahul")
f = open("student.txt", "w")
f.write(data)
f.close()

# 15. Remove comments from Python file
src = open("sample.py", "w")
src.write("# Comment\nprint('Hello')\n")
src.close()

src = open("sample.py", "r")
des = open("new.py", "w")
for line in src:
    if not line.strip().startswith("#"):
        des.write(line)
src.close()
des.close()

# 16. Convert file to uppercase
f = open("student.txt", "r")
text = f.read()
f.close()
u = open("upper.txt", "w")
u.write(text.upper())
u.close()

# 17. Student records
f = open("students.txt", "w")
f.write("101,Amit,85\n102,Priya,92\n103,Rahul,78\n")
f.close()

f = open("students.txt", "r")
records = []
for line in f:
    r, n, m = line.strip().split(",")
    records.append((r, n, int(m)))
f.close()

print("17. Records:", records)
print("Highest =", max(records, key=lambda x: x[2]))
avg = sum(x[2] for x in records) / len(records)
print("Average =", avg)
for x in records:
    if x[2] > 80:
        print("Above 80:", x)

# 18. Employee records
f = open("emp.txt", "w")
f.write("101,Amit,IT,50000\n102,Priya,HR,60000\n103,Rahul,Sales,45000\n")
f.close()

f = open("emp.txt", "r")
emp = []
for line in f:
    i, n, dpt, sal = line.strip().split(",")
    emp.append((i, n, dpt, int(sal)))
f.close()

print("18. Highest Paid =", max(emp, key=lambda x: x[3]))
print("Average Salary =", sum(x[3] for x in emp) / len(emp))

# 19. Attendance
f = open("attendance.txt", "w")
f.write("Amit,80,100\nPriya,70,100\nRahul,90,100\n")
f.close()

f = open("attendance.txt", "r")
for line in f:
    n, p, t = line.strip().split(",")
    per = int(p) / int(t) * 100
    if per < 75:
        print("19. Below 75%:", n)
f.close()

# 20. Bank transactions
f = open("trans.txt", "w")
f.write("deposit,10000\nwithdraw,2000\ndeposit,5000\nwithdraw,1000\n")
f.close()

dep = wit = 0
largest = 0
f = open("trans.txt", "r")
for line in f:
    t, amt = line.strip().split(",")
    amt = int(amt)
    largest = max(largest, amt)
    if t == "deposit":
        dep += amt
    else:
        wit += amt
f.close()
print("20. Deposit =", dep)
print("Withdrawal =", wit)
print("Balance =", dep - wit)
print("Largest =", largest)

# 21. Book records
books = {
    "Python": True,
    "Java": False,
    "C++": True
}
print("21. Available Books")
for b in books:
    if books[b]:
        print(b)

# 22. Merge two files
a = open("a.txt", "w")
a.write("Hello\n")
a.close()

b = open("b.txt", "w")
b.write("Python\n")
b.close()

a = open("a.txt", "r")
b = open("b.txt", "r")
c = open("merge.txt", "w")
c.write(a.read())
c.write(b.read())
a.close()
b.close()
c.close()

# 23. Compare two files
a = open("a.txt", "r")
b = open("b.txt", "r")
la = a.readlines()
lb = b.readlines()

if la == lb:
    print("23. Files are identical")
else:
    print("23. Files are different")
    for i in range(min(len(la), len(lb))):
        if la[i] != lb[i]:
            print("First difference at line", i + 1)
            break

a.close()
b.close()
