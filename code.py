import mylib as ml
#implementation of fn_gender:
gn = input("Enter your gender :")
ng =ml.fn_gender(gn)
print(ng)




mylist = [10,100,200,1,2,89,87,65,34]
bignum =ml.fn_listbignum(mylist)
print(f"Biggest number in the list : {bignum}")






#implementation

namelist = ['manoj','sanketh','lokesh','vasanth','vismitha']
rollno = [101,102,103,104,105]
sdict = ml.fn_dict(rollno,namelist)
print(sdict)





#implementation
i = int(input("Enter a number :"))
res = ml.fn_table(i)
print(res)