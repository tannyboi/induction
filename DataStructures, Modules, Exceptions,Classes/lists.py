thislist = list(['Brazil','USA','UK','Canada',1]) 
#the list constructor in the above context is optional
print(thislist)

try:
    thislist.sort()#gives sorting error between int and str
except TypeError as err:
    print("Type error ",err)
    del thislist[4]
    thislist.sort()

print(thislist) 

thislist.append("Bolivia")
print(thislist)

thislist.pop()
print(thislist)

listr = thislist.copy()
listr.reverse()
print(listr)

listr.clear()
print(listr)

del listr

try:
    print(listr)
except Exception as err:
    print(err)

thislist.append("UK")
print(thislist.count("UK"))
print(thislist.index("UK")) #returns 1st occurence
print(thislist.index("UK",3)) #returns occurence on or after index 3
try:
    print(thislist.index("UK",3,4)) #returns occurence between [3,4)
except Exception as err:
    print("for this slice ",err)
    