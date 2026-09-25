file = open("seek.txt", "r")

print("Starting position:", file.tell())

data = file.read(5)
print("Data:", data)

print("Current position:", file.tell())

file.seek(0)

print("After seek:", file.tell())

data = file.read(5)
print("Data:", data)

file.close()