# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:04:08 2019

@author: laksh
"""

for _ in range(int(input())):
    n = str(input())
    l = list(n)
    l1 = []
    for i in l:
        l1.append(int(i))
    m=l1[0]
    for i in range(1,len(l1)):
        if l1[i]<m:
            l1.remove(m)
            break
        else:
            m=l1[i]
    if len(l1)==len(l):
        l1.remove(m)
    while (len(l1) > 1 and l1[0] == 0):
        l1.remove(l1[0])
    print(*l1, sep='')