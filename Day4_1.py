# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:55:31 2021

@author: kelka
"""

TXT=input("Enter Text  ")
holes=0
if TXT.isupper():

 for i in TXT:
    if i=="A" or i=="P" or i=="O" or i=="R" or i=="D":
        holes=holes+1
    elif i=="B":
        holes=holes+2
    else:
        continue
 print(holes)     
else:
    print("wrong text")
     
    