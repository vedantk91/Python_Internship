# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:49:04 2021

@author: kelka
"""

import random

A=[]
for i in range(0,6):
    X=random.randint(1,49)
    for X in A:
        X=random.randint(1,49)
        
    A.append(X)
    
A.sort()
print("lottery numbers ",A)