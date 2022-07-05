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
        A.geometry('1350x800')
        A['bg'] = '#2f516f'
        wrappen = ttk.LabelFrame(A)
        mycanvas = Canvas(wrappen)
        mycanvas.pack(side=LEFT, fill="both", expand="yes")


        # head frame
        head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
        f = font.Font(family='Times New Roman', size=25)  # font
        lb = tk.Label(head, text='NEW CUSTOMER COMPLAINT', bg="#243e55", height=3,bd=1, relief="groove", font=f, width=75)
        lb['font'] = f
        lb.place(relx=0.05, rely=0.2)
        head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

        # contents frame
        hd = tk.Frame(A, bg='#243e54')
        hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)



    
        
        def submit():

               
                global D, cdate, complaint_qty, cdescription
                
                cdate = cdate_input.get()
                complaint_qty = complaintqty_input.get()
                cdescription = cdescription_input.get()
                invoiceno = invoice_input.get()
            

            
                
                
                con = mysql.connector.connect(host="127.0.0.1", user="root",
                            password="", database="fynsystkinter", port='3307')
                cur = con.cursor()
                d='''INSERT INTO customercomplaint(cdate,invoiceno,cdescription,complaint_qty) VALUES (%s,%s,%s,%s)'''
                cur.execute(d,[(cdate),(invoiceno),(cdescription),(complaint_qty)])
                
                con.commit()
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                A.destroy()

        # Get selected item to Edit

   

        
        

        cd = Label(
            hd, text="Date", bg='#243e55', fg='#fff')
        cd.place(x=350, y=70,)
        cdate_input = StringVar()
        cdate_input = DateEntry(hd, width=50, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=cdate_input)
        cdate_input.place(x=350, y=100, height=40)
        

    
        invoice_lab = tk.Label(hd, text="Invoice Number", bg='#243e55', fg='#fff')
        invoice_lab.place(x=350, y=160, height=15, width=120)
        place_input = StringVar()
        invoice_input = Entry(hd, width=50, bg='#2f516f', fg='#fff')
        invoice_input.place(x=350, y=190, height=40)
        wrappen.pack(fill='both', expand='yes',)

        complaint_lab = tk.Label(hd, text="Complaint Quantity", bg='#243e55', fg='#fff')
        complaint_lab.place(x=350, y=230, height=15, width=130)
        place_input = StringVar()
        complaintqty_input = Entry(hd, width=50, bg='#2f516f', fg='#fff')
        complaintqty_input.place(x=350, y=260, height=40)
        wrappen.pack(fill='both', expand='yes',)


    
        cdescription = Label(hd, text="Description",
                           bg='#243e55', fg='#fff')
        cdescription.place(x=350, y=310,)
        cdescription_input = Entry(hd, width=50, bg='#2f516f', fg='#fff')
        cdescription_input.place(x=350, y=330, height=90)
        wrappen.pack(fill='both', expand='yes',)

        

       
        submit = tk.Button(
            hd, text="Save", command=submit)
        submit.place(x=700, y=450, width=100)



        A.mainloop()


main()
