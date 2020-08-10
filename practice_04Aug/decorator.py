# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:37:42 2020

@author: TANMAY MATHUR
"""

def decorator_0(fxn):
    
    def inner_execution():
        print("before actual fxn runs")
        fxn()
        print("after fxn runs")
        
    return inner_execution()

def fxn():
    print("this is a demo text by the fxn")
    return 0
    
fxn = decorator_0(fxn)
print()


def decorator_1(func): 
    def inner1(*args,**kwargs): 
          
        print("before Execution") 
          
        # getting the returned value 
        returned_value = func(*args,**kwargs) 
        print("after Execution") 
          
        # returning the value to the original frame 
        return returned_value 
          
    return inner1 
  
  
# adding decorator to the function 
@decorator_1
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 
  
a, b = 1, 2
  
# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b))
        
