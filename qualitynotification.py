import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
import tkinter.messagebox as MessageBox
import click
import mysql.connector 
from tkcalendar import Calendar, DateEntry
import matplotlib.patches
from datetime import datetime, date, timedelta


def main():

    global A, data, menu
    A = tk.Tk()
    A.title('View')
    A.geometry('1400x800')
    A['bg'] = '#2f516f'


    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=25)  # font
    lb = tk.Label(head, text='QUALITY NOTIFICATION', bg="#243e55", height=2,bd=3, relief="groove", font=f, width=75)
    lb['font'] = f
    lb.place(relx=0.05, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=1)

  
    def select(event):
        select_pro=[]
        menu=product_drop4.get()
        select_pro.append(menu)
        print(menu)
        if menu == 'Customer Complaints':
            import createcustomercomplaints
        elif menu == 'Complaint Against Supplier':
            import createcomplaintagainstsupplier
        elif menu == 'Material Error':
            import creatematerialerror
        else:
            import qualitynotification
    p1 = Label(hd, text="Create Complaints", bg='#243e55', fg='#fff',font=('times new roman', 28, 'bold'))
    p1.place(x=290, y=200,)
    pr1 = "Customer Complaints", "Complaint Against Supplier", "Material Error"
    product_drop4=ttk.Combobox(hd,font=('times new roman', 28, 'bold'), )
    product_drop4.set("Create")
    product_drop4['values']=pr1
    product_drop4.bind("<<ComboboxSelected>>",select)
    product_drop4.place(x=300,y=300,height=40,width=200)
    
    
    def selected2(event):
        select_pro=[]
        menu=product_drop5.get()
        select_pro.append(menu)
        print(menu)
        if menu == 'Customer Complaints':
            import viewcustomercomplaints
        elif menu == 'Complaint Against Supplier':
            import viewcomplaintagainstsupplier
        elif menu == 'Material Error':
            import viewmaterialerror
        else:
            import qualitynotification
    p1 = Label(hd, text="View Complaints", bg='#243e55', fg='#fff',font=('times new roman', 28, 'bold'))
    p1.place(x=590, y=200,)
    pr1 = "Customer Complaints", "Complaint Against Supplier", "Material Error"
    product_drop5=ttk.Combobox(hd,font=('times new roman', 28, 'bold'), )
    product_drop5.set("View")
    product_drop5['values']=pr1
    product_drop5.bind("<<ComboboxSelected>>",selected2)
    product_drop5.place(x=600,y=300,height=40,width=200)

    A.mainloop()


main()
