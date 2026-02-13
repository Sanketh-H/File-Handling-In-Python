#task :
#create a library and create two functions for that
#1.fn_gender() to transform m to Male and F to female and
#2 fn_dno to transform dno to deptname
#3.capitalize the name
#generate the final list as per sample :
#[(101,'Amar',50000,Male,Admin),.....]
#after this find the number employees in each deptname
#find total salary based deptname

#Function 1 : transform  m to male and f to female

def fn_gender(g):
    if g == "m" or g=="M":
        return "male"
    elif g=="f" or g=="F":
        return "female"
    

   
   # Function 2: transfer department number to department name 
    def fn_dno(dno):
        if dno=="11":
            return "Accounting"
        elif dno=="12":
            return "research"
        elif dno=="13":
            return "Sales"
        elif dno=="14":
            return "operations"
        elif dno=="15":
            return "field"
        else:
            return "Unknown department"