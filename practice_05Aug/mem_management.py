# use join to add to lists
mymsg='line1\n'
mymsg+='line2\n'

print(mymsg)


mylist=['line1','line2']
'\n'.join(mylist)
print(mylist)
for it in mylist:
    print(it)
print(type(mylist).__name__)

#adding to string
msgstr='this %s one' %(mymsg.strip())
print(msgstr)

#using generators
def range_yield(limit):
    counter=0
    while counter<limit:
        yield counter
        counter+=1
print(sum(range_yield(100)))


#using itertools
from itertools import chain,product

def function(shape,weight):
    #print(shape,weight)
    if weight ==True:
        yield shape
    else:
        yield 0

print(list(chain.from_iterable(function(shape, weight) for weight, shape in product([True, False], range(1, 5)))))

#changing/adding to lists
#mylist=[]
oldlist=['age','gender','jobs']
'''for myword in oldlist:
      mylist.append(myword.upper())
print(mylist)
'''
mylist=list(map(str.upper,oldlist))
print(*mylist)


#profiling

import cProfile
import re
cProfile.run('re.compile("mem_management|function")')

