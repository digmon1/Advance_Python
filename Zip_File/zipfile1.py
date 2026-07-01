from zipfile import ZipFile
f=ZipFile('test.zip','w')
f.write('f1.txt')
f.write('f2.txt')
f.write('f3.txt')
print('Zip file created successfully')