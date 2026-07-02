def storestudentsdetails():
    i = 1
    f = open('studentsdetails.txt','a')
    while True:
        name = input(f"Enter Student {i} name: ")
        age = int(input(f"Enter Student {i} age: "))
        id = int(input(f"Enter Student {i} id: "))
        email = input(f"Enter Student {i} email: ")
        contact = int(input(f"Enter Student {i} contact: "))
        fees = float(input(f"Enter Student {i} fees: "))
        print()

        f.write(f'{id}|{name}|{age}|{email}|{contact}|{fees} \n')

        i = i+1

        option = input('Do you want to add more details? [yes/no]: ')
        if option.lower() == 'no':
                break
    f.close()

def readstudentdetails():
    f = open('studentsdetails.txt')
    data = f.readlines()
    for line in data:
        print(line, end='')
    f.close()

def search_by_id():
    f = open('studentsdetails.txt')
    data = f.readlines()
    ids=int(input("Enter Students ID for search: "))
    for line in data:
        id, name, age, email, contact, fees = line.split('|')
        if int(id) == ids:
            print(f'Student Name: {name}')
            print(f'Student ID: {id}')
            print(f'Student Age: {age}')
            print(f'Student Contact: {contact}')
            print(f'Student Email: {email}')
            print(f'Student Fees: {fees}')
            break
    else:
        print("Student Not Found")
    f.close()

def editstudentdetails():
    f = open('studentsdetails.txt')
    data = f.readlines()
    f.close()

    ids = int(input("Enter Student ID to Edit: "))

    f = open('studentsdetails.txt', 'w')

    for line in data:
        id, name, age, email, contact, fees = line.strip().split('|')

        if int(id) == ids:
            print("Enter New Student Details")
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            email = input("Enter New Email: ")
            contact = input("Enter New Contact: ")
            fees = input("Enter New Fees: ")

            f.write(id + "|" + name + "|" + age + "|" + email + "|" + contact + "|" + fees + "\n")
        else:
            f.write(line)
    f.close()
    print()
    print("Info was edited succesfully !!")
    print()

def deletestudentdetails():
    f = open("studentsdetails.txt", "r")
    data = f.readlines()
    f.close()

    ids = int(input("Enter Student ID to Delete: "))

    f = open("studentsdetails.txt", "w")

    for line in data:
        id, name, age, email, contact, fees = line.split("|")

        if int(id.strip()) != ids:
            f.write(line)

    f.close()
    print()
    print("Student Details Deleted Successfully !!")
    print()

print("Students Information CRUD Operations")
print("--"*50)
while True:
    print("1. Insert Students Details")
    print("2. Display all students details")
    print("3. Search Students Details by id")
    print("4. Edit students details by id")
    print("5. Delete Students Details by id")
    print("6. Exit")
    print()
    ch=int(input("Enter your choice: "))
    if ch == 1:
        storestudentsdetails()
    elif ch == 2:
        readstudentdetails()
    elif ch == 3:
        search_by_id()
    elif ch == 4:
        editstudentdetails()
    elif ch == 5:
        deletestudentdetails()
    elif ch == 6:
        print("Thanks for using our application!!")
        exit()
    else:
        print("Invalid choice!! plz enter a valid choice!!!!!")