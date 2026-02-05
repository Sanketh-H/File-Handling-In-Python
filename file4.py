#readline() : reads the data from the current pointer position
#till end of the line and moves the pointer to the next line,
#returns the data as string.

file1 = open("c:/sanketh_70/myfile.txt")
data1 = file1.readline()
data2 = file1.readline()
file1.close()
print(data1)
print(data2)