from zipfile import ZipFile
f=ZipFile('test.zip','r')
name=f.namelist()
print(name)
for x in name:
    print(f'file name: {x}')
    f1=open(x,'r')
    data=f1.read()
    print(data)
    print('--'*30)
    print()
    f1.close()
print('Zip file created successfully')