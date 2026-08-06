lst = input("Enter list elements: ").split()

left = lst[1:] + lst[:1]

print("Left Rotation:", left)
