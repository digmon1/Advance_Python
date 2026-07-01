def storestudentdetails():
    i = 1

    with open('studentdetails.txt', 'a') as f:
        while True:
            name = input(f"Enter student {i} name: ")
            age = int(input(f"Enter student {i} age: "))
            id = int(input(f"Enter student {i} ID: "))
            email = input(f"Enter student {i} Email: ")
            contact = int(input(f"Enter student {i} Contact: "))
            fees = float(input(f"Enter student {i} Fees: "))
            print()

            
            f.write(f"{id}|{name}|{age}|{email}|{contact}|{fees}\n")

            i += 1

            option = input("Do you want to add more? (yes/no): ")
            if option.lower() == "no":
                break


def readstudentdetails():
    with open('studentdetails.txt', 'r') as f:
        data = f.readlines()

    print("\nStudent Details")
    print("-" * 60)

    for line in data:
        id, age, name, email, contact, fees = line.strip().split('|')

        print(f"ID      : {id}")
        print(f"Name    : {name}")
        print(f"Age     : {age}")
        print(f"Email   : {email}")
        print(f"Contact : {contact}")
        print(f"Fees    : {fees}")
        print("-" * 60)


def search_by_id():
    with open('studentdetails.txt', 'r') as f:
        data = f.readlines()

    ids = int(input("Enter Student ID to search: "))
    found = False

    for line in data:
        id, name, age, email, contact, fees = line.strip().split('|')

        if int(id) == ids:
            found = True
            print("\nStudent Found")
            print("-" * 30)
            print(f"ID      : {id}")
            print(f"Name    : {name}")
            print(f"Age     : {age}")
            print(f"Email   : {email}")
            print(f"Contact : {contact}")
            print(f"Fees    : {fees}")
            break

    if not found:
        print("Student ID not found!")

print('Students information CRUD Operations')
print('-' * 40)
print()
while True:
    print("1. Insert Student Details")
    print("2. Display Student Details")
    print("3. Search Student by ID")
    print("4. Edit student details by ID")
    print("5. Delete student details by ID")
    print("6. Exit")
    print()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        storestudentdetails()
    elif choice == 2:
        readstudentdetails()
    elif choice == 3:
        search_by_id()
    elif choice ==6:
        print("Thanks for using our program!")
        exit()
    else:
        print("Invalid choice! Please try again.")

storestudentdetails()
print()
readstudentdetails()
print()
search_by_id()