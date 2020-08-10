# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:45:33 2020

@author: TANMAY MATHUR
"""


import collections as coll


#Counter
sample_cntr=coll.Counter('abcdefgabcdfrgg')
print(sample_cntr.most_common(3))

diff_test=coll.Counter(g=-2,a=3,b=1)
sample_cntr.subtract(diff_test)
print(sample_cntr)

#deque
sample_deq=coll.deque([1,2,3,4])
print(sample_deq)
sample_deq.append(5)
print(sample_deq)
sample_deq.appendleft(0)
print(sample_deq)
sample_deq.pop()
print(sample_deq)
sample_deq.popleft
print(sample_deq)

#defaultdict

sample_list_with_dup=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
dic_with_list=coll.defaultdict(list)
dic_with_set=coll.defaultdict(set)
for key,value in sample_list_with_dup:
    dic_with_list[key].append(value)
    dic_with_set[key].add(value)
print(dic_with_set,dic_with_list)

#names tuple
Color_dis=coll.namedtuple('color_dis',['r','g','b'])
clr_sample1 = Color_dis(24,100,98)
print(clr_sample1.r)
print(clr_sample1[1])
print(getattr(clr_sample1,'b'))