#working with multiple files:
#master file and transaction file
#master file and detail file
#parent file and child file


#master file willl have unique data with id's
#transaction file uses the data of master file 

#ex. master file:101,Amar
#in trans file:
#101,2000
#101,2000


#when working with multiple file all files should have at least one common column.

#1.read all master files and create dictionary'

dfile=open("c:/sanketh_70/dep.txt")
dhead=dfile.readline()
ddata=dfile.readlines()
dfile.close()
depdict={}
for x in ddata:
    d = x.strip().split(',')
    depdict[d[0]]=d[1]
print(depdict)

#2. read the data from empfile.txt and map dno with depdict to 
#get depname

efile = open("c:/sanketh_70/emp.txt")
ehead = efile.readline()
edata = efile.readlines()
efile.close()
flist = []
for x in edata:
    #print(x)
    w = x.strip().split(',')
    #print(w)
    depname = depdict.get(w[-1])
    tup = (w[0],w[1],w[2],w[3],depname)
    flist.append(tup)
for x in flist:
    print(x)