# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:25:48 2020
"""

def sample_fun(*args,**kwargs):
    num = int (args[0])
    print(num**2)
    for k,v in kwargs.items():
        print(k,v)
        
sample_fun(3,x=1,y=2,z=3)



