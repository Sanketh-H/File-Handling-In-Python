#read(n) : reads n bytes of data from the current pointer position

file1 = open("c:/sanketh_70/myfile.txt")
data = file1.read(10)
data2 = file1.read(10)
data3 = file1.read()
print(data)
print(data2)
print(data3)
file1.close()