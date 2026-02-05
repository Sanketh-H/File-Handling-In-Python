# function to transform m to male and f to female 

def fn_gender(gen):
    if gen == "m" or gen == "M":
        g = "Male"
    elif gen == "f" or gen == "F":
        g = "Female"
    else:
        g = "others"
    return g




#function to accept a list and return a simple data 
#task : to find the biggest number in the list 


def fn_listbignum(ilist):   #ilist is the object 
    big = 0
    for x in ilist:
        if x>big:
            big=x
    return big





#function to accept two list objects and return a dict 
#assumption : elements of list1 are keys and list2 are values


def fn_dict(list1,list2):
    newdict = {}
    for x in list(zip(list1,list2)):
        newdict[x[0]]=x[1]
    return newdict





#function to accept a number and return a list
#task : function to generate multiplication table of the given number
#store it in a list and return the list 

def fn_table(n):
    tlist = []
    for x in range(1,11):
        tlist.append(n*x)
    return tlist
