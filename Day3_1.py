# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:48:25 2021

@author: kelka
"""

S=input("rating")
S=float(S)
if S==0.6:
    print("performance is Meritorious")
elif S==0.4:
    print("performance is Acceptable")
elif S==0.0:
    print("performance is Unacceptable")
else:
    print("invalid")

    
print("your raise is",S*2400,"$")