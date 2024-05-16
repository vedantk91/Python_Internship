# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:20:39 2021

@author: kelka
"""
import random
X=0
while X!=100:
    
 R=input("Roll Dice?  1 for Yes")
 if R=="1":
  A=random.randint(1,6)
  print(A)
  X=X+A
  
  if X==12 or X==17 or X==45 or X==64 or X==85 or X==74:
     print("OOPS Snake!")
     X=X-4
  elif X>=100:
      print("COMPLETED")
  elif X==56 or X==78 or X==8 or X==67 or X==79 or X==15:
     print("YESS Ladder")
     X=X+20
  print("Current Location")
  print(X)