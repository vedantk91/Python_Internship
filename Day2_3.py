    # -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 12:29:44 2021

@author: kelka
"""
 
def change(para):
   
 para[0].upper()
 X= para.replace(" i ", " I ")

 loc=X.find(".")
 X=X.replace(X[loc+1],X[loc+1].upper())

 loc=X.find("!")
 X=X.replace(X[loc+1],X[loc+1].upper())

 loc=X.find("?")
 X=X.replace(X[loc+1],X[loc+1].upper())
 print(X)
 
para=input("a paragraph   ")  
change(para)

