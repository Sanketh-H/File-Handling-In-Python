#create a library and create two functions for that 

#1.fn_gender() to transform m to male and F to female and 
#2 fn_dno to transform dno to deptname
#3 capitalize the name
#generate the final list as per sample:
#[(101,'Amar',50000,male,admin),.......]
#after this find the number employees in each dept name
#find total salary based dept name


def fn_gender(g):
    if g=='M' or g=='m':
        return "Male"
    elif g=='F' or g=='f':
        return "Female"
    
def fn_dno(dno):
    dno=int(dno)

    if dno==11:
        return "Admin"
    elif dno==12:
        return "HR"
    elif dno==13:
        return "IT"
    elif dno==14:
        return "Finance"
    elif dno==15:
        return "Sales"
    else:
        return "No such department"

    
file=open("c:/sanketh_70/emp.txt")

file.readline()

dept_count={}

dept_salary={}


for line in file:
    data=line.strip().split(",")

    data[1]=data[1].capitalize()

    data[3]= fn_gender(data[3])

    data[4]= fn_dno(data[4])

    print(data)

    dept=data[4]

    salary= int(data[2])

    if dept  in dept_salary:
        dept_salary[dept]=dept_salary[dept]  + salary
    else:
        dept_salary[dept]=salary


    if dept in dept_count:
        dept_count[dept]=dept_count[dept]+1
    else:
        dept_count[dept]=1
    

file.close()

print("\nEmployees in each department")
print(dept_count)

print("\nTotal salary per department")
print(dept_salary)