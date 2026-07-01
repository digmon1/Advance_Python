import csv
f=open('emp.csv',newline='', mode='w')
r=csv.writer(f)
r.writerow(['Ename','Eaddress','Email ','Contact'])

n=int(input('Enter number of employee: '))
for x in range(n):
    name=input(f'Enter employee {x+1} name:')
    address=input(f'Enter employee {x+1} address:')
    email=input(f'Enter employee {x+1} email:')
    contact=int(input(f'Enter employee {x+1} contact:'))
    r.writerow([name,address,email,contact])
    print()
f.close()
