import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
import tkinter.messagebox as MessageBox
# import click
import mysql.connector 
from tkcalendar import Calendar, DateEntry
# import matplotlib.patches
from datetime import datetime, date, timedelta


expense_form = tk.Tk()
wrappen = ttk.LabelFrame(expense_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")


def main():
        global A

        global data, menu
        A = tk.Tk()
        A.title('View')
        A.geometry('1350x800')
        A['bg'] = '#2f516f'


        # head frame
        head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
        f = font.Font(family='Times New Roman', size=25)  # font
        lb = tk.Label(head, text='NEW COMPLAINT AGAINST SUPPLIER', bg="#243e55", height=2,
                    bd=5, relief="groove", font=f, width=106)
        lb['font'] = f
        lb.place(relx=0.05, rely=0.2)
        head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

        # contents frame
        hd = tk.Frame(A, bg='#243e54')
        hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.8)



    
        
        def submit():

                global D, cdate,supplier_name,product_name,inspected_qty,complaint_qty,cdescription
                
                cdate = cdate_input.get()
                supplier_name = supname_input.get()
                product_name =proname_input.get()
                inspected_qty =inspctqty_input.get()
                complaint_qty = complaintqty_input.get()
                cdescription = cdescription_input.get()
            

            
                
                
                con =  mydata = mysql.connector.connect(host="127.0.0.1", user="root",
                            password="", database="fynsystkinter", port='3307')
                cur = con.cursor()
                d='''INSERT INTO complaintagainstsupplier(cdate,supplier_name,product_name,inspected_qty,complaint_qty,cdescription ) VALUES (%s,%s,%s,%s,%s,%s)'''
                cur.execute(d,[(cdate),(supplier_name),(product_name),(inspected_qty),(complaint_qty),(cdescription) ])
                
                con.commit()
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                expense_form.destroy()

        # Get selected item to Edit

   

        supname = Label(hd, text="Supplier Name", bg='#243e55', fg='#fff')
        supname.place(x=30, y=30,)
        supname_input = StringVar()
        supname_input = Entry(hd, width=50, bg='#2f516f', fg='#fff')
        supname_input.place(x=30, y=50, height=40)
       
    
        proname = tk.Label(hd, text="Product Name", bg='#243e55', fg='#fff')
        proname.place(x=530, y=30, height=15, width=120)
        place_input = StringVar()
        proname_input = Entry(hd, width=50, bg='#2f516f', fg='#fff')
        proname_input.place(x=530, y=50, height=40)
        wrappen.pack(fill='both', expand='yes',)

        cd = Label(
            hd, text="Date", bg='#243e55', fg='#fff')
        cd.place(x=30, y=100,)
        cdate_input = StringVar()
        cdate_input = DateEntry(hd, width=50, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=cdate_input)
        cdate_input.place(x=30, y=130, height=40)
       
    
        complaint_lab = tk.Label(hd, text="Complaint Quantity", bg='#243e55', fg='#fff')
        complaint_lab.place(x=530, y=100, height=15, width=120)
        place_input = StringVar()
        complaintqty_input = Entry(hd, width=25, bg='#2f516f', fg='#fff')
        complaintqty_input.place(x=530, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)


        inspctqty = tk.Label(
            hd, text="Inspected Quantity", bg='#243e55', fg='#fff')
        place_input = StringVar()
        inspctqty.place(x=780, y=100, height=15, width=120)
        inspctqty_input = Entry(hd, width=25, bg='#2f516f', fg='#fff')
        inspctqty_input.place(x=780, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)

        

        cdescription = Label(hd, text="Description",
                           bg='#243e55', fg='#fff')
        cdescription.place(x=30, y=180,)
        cdescription_input = Entry(hd, width=50, bg='#2f516f', fg='#fff')
        cdescription_input.place(x=30, y=210, height=90)
        wrappen.pack(fill='both', expand='yes',)

        

       
        submit = tk.Button(
            hd, text="Save", command=submit)
        submit.place(x=500, y=320, width=100)

        A.mainloop()
        
        


main()
