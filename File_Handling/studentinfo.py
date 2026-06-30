def storestudentdetails():
    i=1
    f=open('studentdetails.txt','a')
    while True:
        name=input(f"Enter student{1} name: ")
        age=int(input(f"Enter student{1} age: "))
        id=int(input(f"Enter student{1} id: "))
        email=input(f"Enter student{1} Email: ")
        contact=int(input(f"Enter student{1} contact: "))
        fees=float(input(f"Enter student{1} fees: "))
        print()

        f.write(f'{id}|{age}|{email}|{contact}|{fees}\n')
        i+=1

        option = input('Do you want to add more? [yes/no]: ')
        if option.lower()=='no':
            break
    f.close()

def readstudentdetails():
    f=open('studentdetails.txt')
    data=f.readlines()
    for line in data:
        print(line,end='')