f = open("student.txt", "r")

text = f.read()

words = text.split()

print("Total words =", len(words))

f.close()