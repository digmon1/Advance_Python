f=open('abc.txt')
data=f.readlines()
for x in data:
    print(x, end="")
print(type(data))
f.close()