# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 15:46:29 2021

@author: kelkar
"""

x,y= input("Input two numbers").split()

if x>y:
    print("smaller number is ",y)
elif y>x:
    print("smaller number is",x)
else :
    print("Numbers are equal")