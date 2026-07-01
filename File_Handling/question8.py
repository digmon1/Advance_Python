f = open("student.txt", "r")

text = f.read()

word = input("Enter word to search: ")

if word in text:
    print("Word found.")
else:
    print("Word not found.")

f.close()