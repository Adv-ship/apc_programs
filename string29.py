s = input("Enter sentence: ")

words = s.split()

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")
