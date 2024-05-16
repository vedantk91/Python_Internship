# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 09:03:29 2021

@author: kelka
"""


from tkinter import *
from tkinter import messagebox


def loginpage():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("warning","Blank Not allowed")


    elif (uname == "omkar" and password == "12345"):

        messagebox.showinfo("", "Login Success")
        root.destroy()

    else:
        messagebox.showinfo("", "Incorrent Username and Password")


root = Tk()
root.title("Login")
root.geometry("350x350")
global e1
global e2

Label(root, text="UserName").place(x=10, y=10)
Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=loginpage, height=3, width=13).place(x=10, y=100)

root.mainloop()