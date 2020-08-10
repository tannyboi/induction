# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:41:32 2020

@author: TANMAY MATHUR
"""


def factorial(num_for_factorial):
    if(num_for_factorial<=1):
        return 1
    return num_for_factorial*factorial(num_for_factorial-1)

print(factorial(5))
print(factorial(-3))