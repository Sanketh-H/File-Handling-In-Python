#working on file with tabular data (data arranged in rows and columns)
#table or matrix

empfile = open("c:/sanketh_70/emp.txt")
data = empfile.readlines()
empfile.close()
#print(data)
for x in data:
    print(x)
    # print(type(x))