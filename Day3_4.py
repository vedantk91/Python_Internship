# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:03:58 2021

@author: kelka
"""

def spiral(x, y, z): 
   
    k = 0
    l = 0
    while (k < x and l < y): 
 
        for i in range(l, y): 
            print(a[k][i], end=" ") 

        k += 1

        for i in range(k, y): 
            print(a[i][y-1], end=" ") 

        y -= 1

        if (k < x): 

            for i in range(y - 1, (l - 1), -1): 
                print(a[x- 1][i], end=" ") 

            x -= 1

        if (l < y): 
            for i in range(x - 1, k - 1, -1): 
                print(z[i][l], end=" ") 

            l += 1
 
a = [[1, 2, 3, 4], 
     [12, 13, 14, 5], 
     [11, 16, 15, 6],
     [10, 9, 8, 7]] 

r = 4
c = 4

spiral(r, c, a)