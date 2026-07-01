import csv
f=open('emp.csv',newline='', mode='r')
r=csv.reader(f)
data=list(r)
for line in data:
    for word in line:
        print(word, end='\t')
    print()
f.close()