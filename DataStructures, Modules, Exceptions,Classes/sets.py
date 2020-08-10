thisset = set({'Brazil','USA','UK','Canada',1}) 
#the list constructor in the above context is optional
print(thisset)



thisset.update({"Bolivia"})
print(thisset)

thisset.pop()
print(thisset)

thisset.add("UK") # same as update with {"US"}
print(thisset) #no duplicate entries allowed

set2 = {x for x in range(10)}
set3 = thisset.union(set2)
print(set3)

set4 = { x for x in range(15) if x>=5}
print(set4)

setdiff = set4.difference(set3)
setdiffsym= set4.symmetric_difference(set3)
print(setdiff)
print(setdiffsym)   
print(setdiff.isdisjoint(setdiffsym)) 
print(setdiff.isdisjoint(set3))

tuple1 =tuple(set4)
print(tuple1)
try: 
    tuple1[0]='0' #immutable
except Exception as err:
    print(type(err).__name__, err)

