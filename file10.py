#reading data from empfile.txt and separate header from the data

empfile = open("c:/sanketh_70/emp.txt")
header = empfile.readline()
data = empfile.readlines()
empfile.close()
totsal = 0
#print(data)
for x in data:
    #print(x)
    w=x.strip().split(',')
    print(w)
    totsal+=int(w[2])
print(f"Total Salary of the emplyees : {totsal}")




#task :
#create a library and create two functions for that
#1.fn_gender() to transform m to Male and F to female and
#2 fn_dno to transform dno to deptname
#3.capitalize the name
#generate the final list as per sample :
#[(101,'Amar',50000,Male,Admin),.....]
#after this find the number employees in each deptname
#find total salary based deptname