s = input("Enter a sentence: ")

words = s.split()

short = words[0]

for w in words:
    if len(w) < len(short):
        short = w

print("Shortest word =", short)
