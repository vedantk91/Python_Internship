# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:13:35 2021

@author: kelka
"""
p=int(input("first number"))
q=int(input("second number"))
for i in range (1, p + 1): 
    if i <= q: 	
        if p % i == 0 and q % i == 0: 
            g=i
print("The GCD number of ", p, " & ", q, " is: ", g)

 