#file handling/working with files:

#file:file is a collection of data/information 
# stored in a secondary storage device.

#each file will be having filename for its identification and extension
#name to identify its type.

#ex: myfile.txt :(myfile is the name of the file and .txt is
#  the extension name)


#ex:.png, .py, docx,pptx,xlsx,jpeg,pdf,csv.......



#file handling functions in python : 
#read()
#readline()
#readlines()
#seek()
#open()
#close()


#steps to work with files : 
#open the file -------> read the data----->process the data---->
#close the file 


#open():
#filevariable = 
#open("pathe\filename","mode")
#opens the file from the given path and loads it to the memory

#mode:w write, a append mode, r read mode 
#by defualt mode is Read(r)


#file1=open("c:\sanketh_70\myfile.txt")
#read(): read the data from the current pointer position 
#til end of the fle and returns the data as string.

#filevariable.read()

#close():closes the opened file from and clears from the memory

#filevaribale.close()

file1 = open("c:/sanketh_70/myfile.txt")
data=file1.read()
print(data)
file1.close()