

dfile=open("c:/sanketh_70/dep.txt")
dhead=dfile.readline()
ddata=dfile.readlines()
dfile.close()
depdict={}
for x in ddata:
    d = x.strip().split(',')
    depdict[d[0]]=d[1]
print(depdict)

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


wfile=open("c:/sanketh_70/empout.txt","w")
for x in flist:
    wstr=','.join(x)
    print(x)
    wfile.write(wstr+"\n")
wfile.close()