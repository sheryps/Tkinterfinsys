import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
viewpricewin=tk.Tk()
viewpricewin.title('Materials Master')
viewpricewin.geometry('1000x600')
viewpricewin['bg'] = '#2f516f'
def createmat():
    import addmaterial
def viewmat():
    import viewmaterials    
tk.Button(viewpricewin,text='CREATE',font=('Times New Roman',24),bg='#243e54',command=createmat).place(relx=0.25,rely=0.2,relwidth=0.2,relheight=0.15)
tk.Button(viewpricewin,text='VIEW',font=('Times New Roman',24),bg='#243e54',command=viewmat).place(relx=0.5,rely=0.2,relwidth=0.2,relheight=0.15)
viewpricewin.mainloop()