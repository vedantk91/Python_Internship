# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:11:26 2021

@author: kelka
"""

m = int(input("Number of rows : "))
n = int(input("Number of columns : "))
arr = []
# initialize the number of rows
for i in range(0,m):
    arr += [0]
# initialize the matrix
for i in range (0,m):
    arr[i] = [0]*n
for i in range (0,m):
    for j in range (0,n):
        arr[i][j] = int(input())
print ("\nThe Matrix is")
for i in range (0,m):
    for j in range (0,n):
        print(arr[i][j], end = "")
    print("\n")
k = 0; l = 0
print("Spiral Matrix : ",end = " ")
while (k < m and l < n):
    for i in range(l, n):
        print(arr[k][i], end = " ")
    k += 1
    for i in range(k, m):    
        print(arr[i][n- 1], end =" ")
    n -= 1
    if ( k < m):
        for i in range(n - 1, (l - 1), -1) :
            print(arr[m - 1][i], end = " ")  
            m -= 1
    if (l < n):
        for i in range(m - 1, k -1, -1):
            print(arr[i][l], end = " ")
        l += 1