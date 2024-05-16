# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:16:17 2021

@author: kelka
"""
X=1000
Finalp=0

while X!=0:
    X=(input("Age"))
    if X==" ":
        break
    else:
        X=int(X)
        if X<2:
         S=0
        elif 3<X<12:
         S=14
        elif X>65:
         S=18
        else :
         S=23
    Finalp=Finalp+S
print("Final Price is rs",Finalp)