# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:51:21 2021

@author: kelka
"""

W = input('enter  ')
L = len(W)
W = list(W) 

i = 0
j = L - 1
while (i <= j):  
              if (W[i] == W[j] == '.'): 
                  W[i] = W[j] = 'a'  
              elif W[i] != W[j]:  
                  if (W[i] == '.'):
                     W[i] = W[j]
                  elif (W[j] == '.'):
                     W[j] = W[i]
                  else: 
                     print("palindrome not possible")
              i = i + 1  
              j = j - 1 
        
print(''.join(W))