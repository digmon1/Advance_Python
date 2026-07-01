f = open("students.txt", "w")

for i in range(5):
    print("\nEnter Student", i + 1)

    name = input("Name: ")
    age = input("Age: ")
    sid = input("ID: ")
    email = input("Email: ")
    contact = input("Contact: ")

    f.write(name + "," + age + "," + sid + "," + email + "," + contact + "\n")

f.close()

print("\nStored Successfully!")

print("\nStudent Records")

f = open("students.txt", "r")

for line in f:
    print(line.strip())

f.close()