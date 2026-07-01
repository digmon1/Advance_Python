f = open("student.txt", "r")

text = f.read().lower()

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Total vowels =", count)

f.close()