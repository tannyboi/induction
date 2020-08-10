# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:27:35 2020

@author: TANMAY MATHUR
"""

import itertools as it

#count

table_iter =  (it.count(start=3,step=3))
print('table of 3 ',list(next(table_iter) for _ in range(10)))

#product
multiplicant=[1,2,3]
multiplier=[5,6]
product_out=it.product(multiplicant,multiplier)
print('product of lists is ',*product_out)
#cycle

Inputstring=[1,2,3,4]
StringBuffer = it.cycle(Inputstring) 
SequenceRepeation = 0
SequenceStart = 0
SequenceEnd = len(Inputstring) 
  
for output in StringBuffer: 
    if(SequenceStart == 0): 
        print("Sequence % d"%(SequenceRepeation + 1))
    if(SequenceStart == SequenceEnd-1): 
          
        if(SequenceRepeation>= 3): 
            break
        else: 
            SequenceRepeation+= 1
            SequenceStart = 0
            print("\n") 
    else: 
        SequenceStart+= 1