#readlines() : reads all the data from the file and returns the data
#as list, each line will be the list element.

#filevariable.readlines()

file1 = open("c:/sanketh_70/myfile.txt")
data = file1.readlines()
file1.close()
#print(data)
for x in data:
#     print(x)
    print(x.strip())



    #task : create a text mytext.txt, type few lines
#read the file and find the biggest word in the file
#find all the words which dose not start with vowels