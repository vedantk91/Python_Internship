# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:19:58 2021

@author: kelka
"""

X=float(input("x coordinate"))
Y=float(input("y coordinate"))
dist1=0
Dist=0
X2=X
Y2=Y
while X2!=None:
    X1=X2
    Y1=Y2
    X2=input("x coordinate")
    if X2==" ":
        break
    X2=float(X2)
    Y2=float(input("y coordinate"))
    dist1=((Y2-Y1)**2+(X2-X1)**2)**0.5
    print("Distance from previous point")
    print(dist1)
    Dist=Dist+dist1
    print("Total Distance till now")
    print(Dist)
print("Final Perimeter")
print(Dist)
    
    

    