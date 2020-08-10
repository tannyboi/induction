# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 03:12:29 2020

@author: TANMAY MATHUR
"""

#selfdef,yield,range,xrange,irange,[for]

#selfdef non_inspace
def selfdef_non_inspace_range(num_limit):
    counter=0;
    range_list=[]
    num_limit=num_limit;
    while counter<num_limit:
        range_list.append(counter)
        counter+=1
    return range_list

print("sum of first 100 whole numbers",sum(selfdef_non_inspace_range(100)))

#custom inspace
class selfdef_inspace_range(object):
    def __init__(self,num_limit):
        self.num_limit=num_limit
        self.counter=0
    
    def __iter__(self):
        return self
    
    def __next__(self):     #compatible only with highr py versions
        return self.next()   #calls the defined next method
    
    def next(self):
        if self.counter < self.num_limit:
            curr_num,self.counter=self.counter,self.counter +1
            return curr_num
        else:
            raise StopIteration()

print("sum of first 100 whole numbers",sum(selfdef_inspace_range(100)))

#yield

def range_with_yield(num_limit):
    counter=0
    while counter < num_limit:
        yield counter
        counter+=1
print("sum of first 100 whole numbers",sum(range_with_yield(100)))

#range
print("sum of first 100 whole numbers",sum(range(100)))

#xrange
try:
    print("sum of first 100 whole numbers",sum(xrange(100)))
    print("product of the first 100 whole numbers is ",product(xrange(100)))
except:
    print("py2.x compatible function not compatible with your version")

#range generator irange
    
try:
    print("sum of first 100 whole numbers",sum([x for x in irange(100)]))
except:
    print("py2.x compatible function not compatible with your version")
    
    
#custom generators
    
def double(lst):
    return [num*2 for num in lst]
def square(lst):
    return [num**2 for num in lst]


sample_list=[1,2,3]
print(double(sample_list),square(sample_list))

    




