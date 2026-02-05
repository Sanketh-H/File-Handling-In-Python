name=['rama','amar','rita','rani','giri','veni','somu','smitha']
sal=[40000,50000,60000,55000,45000,25000,40000,60000]
dno=[11,12,13,14,15,11,12,13,14]
gender=['m','m','f','f','m','f','m','f']
elist = list(zip(name,gender,dno,sal))
flist = []
for x in elist:
    print(x)