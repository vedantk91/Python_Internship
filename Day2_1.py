# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:48:07 2021

@author: kelka
"""
a=[]
X=input("First Word")
Y=input("Second Word")
if len(X)==len(Y):
    for i in X:
        for j in Y:
            if i==j:
                a.append(1)
                break
            else:
                
                continue
print(a)
if len(a)==len(X)==len(Y):
    if a[-1]==1:
      print("its an anagram")
    else :
        print("no")
else: 
    print("no")