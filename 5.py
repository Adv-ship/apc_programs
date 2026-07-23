m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))


total = m1 + m2 + m3
percentage = total / 3

if percentage >= 85:
        remark = "Excellent"
elif percentage >= 70:
        remark = "Very Good"
elif percentage >= 55:
        remark = "Good"
elif percentage >= 40:
        remark = "Average"


print(f"Total Marks: {total}")
print(f"Percentage : {percentage}")
print(f"Remark     : {remark}")
    
