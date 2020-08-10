d1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

for (x,y) in d1.items():
    print(x,y)

a=(0,1,2)
b='b'

d2 = dict.fromkeys(a,b)
for (x,y) in d2.items():
    print(x,y)
    
d2.update({3:'g'})
print(d2)

print(d2.setdefault(1,'f')) 
#new entry with same key not allowed, will retur alloted value
print(d2.setdefault(4,'f'))
#new entry with key 4 made, assigned value returned
