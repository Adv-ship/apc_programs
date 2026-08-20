from array import array

# 1. append() - i
a = array('i', [10, 20, 30])
a.append(40)
print("1. append:", a)


# 2. buffer_info() - L
a = array('L', [100, 200, 300])
print("2. buffer_info:", a.buffer_info())


# 3. byteswap() - i
a = array('i', [1, 2, 3])
a.byteswap()
print("3. byteswap:", a)


# 4. count() - L
a = array('L', [100, 200, 100, 300])
print("4. count:", a.count(100))


# 5. extend() - i
a = array('i', [10, 20])
b = array('i', [30, 40])
a.extend(b)
print("5. extend:", a)


# 6. frombytes() - L
a = array('L', [100, 200])
b = array('L', [300, 400])
a.frombytes(b.tobytes())
print("6. frombytes:", a)


# 7. fromfile() - i
a = array('i', [10, 20, 30])

with open("data.bin", "wb") as f:
    a.tofile(f)

b = array('i')

with open("data.bin", "rb") as f:
    b.fromfile(f, 3)

print("7. fromfile:", b)


# 8. fromlist() - L
a = array('L', [100, 200])
a.fromlist([300, 400, 500])
print("8. fromlist:", a)


# 9. fromunicode() - u
a = array('u')
a.fromunicode("Python")
print("9. fromunicode:", a)


# 10. index() - i
a = array('i', [10, 20, 30, 40])
print("10. index:", a.index(30))


# 11. insert() - L
a = array('L', [100, 200, 400])
a.insert(2, 300)
print("11. insert:", a)


# 12. pop() - i
a = array('i', [10, 20, 30])
x = a.pop()
print("12. pop removed:", x)
print("    Remaining:", a)


# 13. remove() - L
a = array('L', [100, 200, 300, 200])
a.remove(200)
print("13. remove:", a)


# 14. reverse() - i
a = array('i', [10, 20, 30, 40])
a.reverse()
print("14. reverse:", a)


# 15. tobytes() - L
a = array('L', [100, 200, 300])
b = a.tobytes()
print("15. tobytes:", b)


# 16. tofile() - i
a = array('i', [10, 20, 30])

with open("numbers.bin", "wb") as f:
    a.tofile(f)

print("16. tofile: Data written to file")


# 17. tolist() - L
a = array('L', [100, 200, 300])
b = a.tolist()
print("17. tolist:", b)


# 18. tounicode() - u
a = array('u', ['H', 'e', 'l', 'l', 'o'])
print("18. tounicode:", a.tounicode())
