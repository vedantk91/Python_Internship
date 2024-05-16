# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 09:15:51 2021

@author: kelka
"""

A=[]
n=int(input("no of songs "))
for i in range(0,n):
    L=int(input("Length of the song"))
    A.append(L)
P1=int(input("position of computing paradox "))
L1=int(input("length of computing paradox "))
A.insert(P1, L1)
A.sort()
loc=A.index(L1)
print(A)
print("position of comuting paradox",loc)
    