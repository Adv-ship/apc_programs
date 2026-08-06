score = []

for i in range(10):
    s = int(input("Enter score: "))
    score.append(s)

highest = max(score)
lowest = min(score)
total = sum(score)
average = total / len(score)

century = 0
half = 0

for i in score:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half Centuries:", half)
