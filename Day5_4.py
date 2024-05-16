# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:20:11 2021

@author: kelka
"""

import turtle
turtle.bgcolor("green")


sr=turtle.Turtle()


dot_distance=25
sr.setposition(-200,200)

def spiral(m,n):
    k=0
    l=0
    f=0
    sr.color("black")
    while(k<m and l<n):
        if f==1:
            sr.right(90)
        for i in range(l,n):
            sr.forward(dot_distance)
        k+=1
        f=1
        sr.right(90)
        for i in range(k,m):
            sr.forward(dot_distance)
        n-=1
        sr.right(90)
        if(k<m):
            for i in range(n-1,l-1,-1):
                sr.forward(dot_distance)
            m-=1
        sr.right(90)

        if(l<n):
            for i in range(m-1,k-1,-1):
                sr.forward(dot_distance)
            l+=1


spiral(20,20)


turtle.done()