#seek(n) : moves the pointer to the nth byte

#file.seek(n)

file1 = open("c:/sanketh_70/myfile.txt")
file1.seek(20)
data = file1.read()
print(data)
file1.close()