# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:39:53 2021

@author: kelka
"""

a=[]

x=1
while x!=0 :
    x=int(input("enter a number"))
    if x!=0 :
        a.append(x)
a.sort()
print(a)
for i in a:
    print(i)
    