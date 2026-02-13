#writing multiple data to the file :

name = ['rahul','sanketh','lokesh','vasanth','hemalatha']
age = [25,26,27,28,29]
salary = [50000,70000,60000,65000,70000]
elist = list(zip(name,age,salary))
wfile = open("c:/sanketh_70/new2.txt","w")
header = "Name,Age,Salary"
wfile.write(header+"\n")
for x in elist:
    tlist = [x[0],str(x[1]),str(x[2])]
    wstr = ','.join(tlist)
    print(wstr)
    wfile.write(wstr+"\n")
wfile.close()