class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
#Execution!


            
mp0= Mapping(["map0","parent"])
mp1= MappingSubclass(["map1","child"])

mp0.update(["ammendable"])
try:
    mp1.update(["ammendable with parent method"])
except:
    mp1.update(["ammends"],["own"])
print(mp0.items_list,mp1.items_list)
#the items_list work with mp1 and shows values that conlict with the (k,v) tuple format

class B(Exception):
    pass
class C(B):
    pass

for c in [B,C]:
    try:
        raise c
    except C:
        print("C")
    except B:
        print("B")
        
for c in [B,C]:
    try:
        raise c
    except B:
        print("B")
    except C:
        print("C")
        
        
        
    