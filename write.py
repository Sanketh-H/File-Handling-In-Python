#writing data to the file :

#for writing data to the file we need to open the file in 
#w mode or a mode.

#w : write : when we open the file in write mode, it will
#check for the file in the given path, if the file is present
#then it will overwrite the file, otherwise it will create a new file.

#a : append : when we open the file in append mode, it will
#check for the file in the given path, if the file is present
#then it will add data to the file, otherwise it will create a new file.

#write() : is used to write data the file
#filevariable.write(string)

#writing input data to the file :

wfile = open("c:/sanketh_70/new1.txt","w")
header = "name,age,salary"
wfile.write(header+"\n")
name = input("Enter name :")
age = int(input("Enter age :"))
salary = int(input("Enter Salary :"))
tlist = [name,str(age),str(salary)]
wstr = ','.join(tlist)
print(wstr)
wfile.write(wstr+"\n")
wfile.close()