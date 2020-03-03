# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:48:31 2019

@author: laksh
"""

for _ in range(int(input())):
    n = str(input())
    l = list(n)
    l1 = []
    for i in l:
        l1.append(int(i))
    if l1.count(0) == 0:
        l1.remove(max(l1))
    else:
        m = 0
        i = 0
        while i < len(l1):
            if l1[i] != 0:
                if l1[i] > m:
                    m = l1[i]
            else:
                l1.remove(m)
                while (len(l1) > 1 and l1[0] == 0):
                    l1.remove(l1[0])
                break
            i += 1
    print(*l1, sep='')