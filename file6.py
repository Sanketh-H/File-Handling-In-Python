 #task : create a text mytext.txt, type few lines
#read the file and find the biggest word in the file
#find all the words which dose not start with vowels



file=open("c:/sanketh_70/mytext.txt")
data=file.read()
print(data)
file.close()

words=data.split()
print(words)


big=words[0]
for x in words:
    # print(x)
    if len(x)>len(big):
        big=x
print(f"biggest word in the file is :{big}")


# find words that do not start with vowels
vowels = "aeiouAEIOU"
clist = []

for x in words:
    if x[0] not in vowels:
        clist.append(x)

print(f"Words not starting with vowels:{clist}")