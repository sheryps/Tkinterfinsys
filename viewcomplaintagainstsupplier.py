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


mydata = mysql.connector.connect(
    host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
cur = mydata.cursor()

expense_form = tk.Tk()
expense_form.title("finsYs")
expense_form.geometry("1500x1000")
expense_form['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(expense_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')


def main():

    global A, data, menu
    A = tk.Tk()
    A.title('View')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'


    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=25)  # font
    lb = tk.Label(head, text='VIEW COMPLAINT AGAINST SUPPLIER', bg="#243e55", height=2,
                  bd=5, relief="groove", font=f, width=106)
    lb['font'] = f
    lb.place(relx=0.05, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.8)
    form2_frame=tk.Frame(hd,bg='#243e54')



    def menuu(e):
        global fromdate,todate,date1,date2
        dropp=drop.get()
        toda = date.today()
        tod = toda.strftime("%Y-%m-%d") 
        if dropp=='Custom':            
            tk.Label(form2_frame,text='From',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.3,rely=0.08)
            date1 = StringVar()
            date1 = DateEntry(form2_frame, width=50, bg="#2f516f",date_pattern='y-mm-dd', textvariable=date1)
            date1.place(relx=0.3,rely=0.5,relwidth=0.2,relheight=0.5)
            tk.Label(form2_frame,text='To',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.55,rely=0.08)
            date2 = StringVar()
            date2 = DateEntry(form2_frame, width=50, bg="#2f516f",date_pattern='y-mm-dd', textvariable=date2)
            date2.place(relx=0.55,rely=0.5,relwidth=0.2,relheight=0.5)        
        elif dropp=='Today':
            fromdate = tod
            todate = tod 
        elif dropp=='This month':
            fromdate = toda.strftime("%Y-%m-01")
            todate = toda.strftime("%Y-%m-31")
          

    tk.Label(form2_frame,text="Select Date",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.08)
    options=["All dates", "Custom","Today","This month"]
    drop= ttk.Combobox(form2_frame,values=options,font=16)
    drop.current(0)
    drop.bind('<<ComboboxSelected>>',menuu)
    drop.place(relx=0.05,rely=0.5,relwidth=0.2,relheight=0.5)
        #buttons

    def clearttree():#to clear treeview
            for item in treevv.get_children():
                treevv.delete(item) 
    def dateselect():
            period=drop.get()
            if period=='All dates':
                clearttree()
                alldate()  
            elif period=='Today':
                clearttree()
                todaydate()
            elif period=='Custom':
                global fromdate,todate
                fromdate = date1.get()
                todate = date2.get()
                clearttree()
                customdate()   
            elif period=='This month':
                clearttree()
                customdate()    
                
    tk.Button(form2_frame,text = "Search",fg="#000",font=('times new roman', 16, 'bold'),command=dateselect).place(relx=0.8,rely=0.5,relwidth=0.15)
    form2_frame.place(relx=0.01,rely=0.075,relwidth=0.8,relheight=0.09)


    # table view

    treevv = ttk.Treeview(hd, height=7, columns=(
        1, 2, 3, 4, 5, 6,7,8), show='headings')
    treevv.heading(1, text='ID')  # headings
    treevv.heading(2, text='DATE')  # headings
    treevv.heading(3, text='SUPPLIER NAME')
    treevv.heading(4, text='PRODUCT NAME')
    treevv.heading(5, text='SKU')
    treevv.heading(6, text='INSPECTED QTY')
    treevv.heading(7, text='COMPLAINT QTY')
    treevv.heading(8, text='DESCRIPTION')


    # treevv.heading(7, text='Actions')
    treevv.column(1, minwidth=10, width=40, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    treevv.column(7, minwidth=30, width=140, anchor=CENTER)
    treevv.column(8, minwidth=30, width=140, anchor=CENTER)
    
    def alldate():
        cur.execute( "SELECT id,cdate,supplier_name,product_name,sku_no,inspected_qty,complaint_qty,cdescription FROM complaintagainstsupplier ")
        val = cur.fetchall()
        try:
            for x in val:
                treevv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4],x[5],x[6]))
        except:
            pass
        treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
        
    def todaydate():#today value
        print(fromdate)
        cur.execute("SELECT id,cdate,supplier_name,product_name,sku_no,inspected_qty,complaint_qty,cdescription FROM complaintagainstsupplier WHERE cdate =%s",[fromdate])
        val = cur.fetchall()
        try:
            for x in val:
                treevv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4],x[5],x[6]))
        except:
            pass
        treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
        
    def customdate():#two dates
        cur.execute("SELECT id,cdate,supplier_name,product_name,sku_no,inspected_qty,complaint_qty,cdescription FROM complaintagainstsupplier WHERE  cdate BETWEEN %s and %s ", [fromdate, todate])
        val = cur.fetchall()
        try:
                for x in val:
                    treevv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4],x[5],x[6]))
        except:
                pass
        treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
        
  
        
    cur.execute("SELECT id,cdate,supplier_name,product_name,sku_no,inspected_qty,complaint_qty,cdescription FROM complaintagainstsupplier")
    val = cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4],x[5],x[6],x[7]))   
        treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)
 

    def editexp():
        def changeedit():

            mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
            cur = mydata.cursor()
            global D, cdate, complaint_qty, inspected_qty, cdescription
            
            cdate = cdate_input.get()
            complaint_qty = complaintqty_input.get()
            inspected_qty = inspctqty_input.get()
            cdescription = cdescription_input.get()
        
            print(cdate, complaint_qty, inspected_qty, cdescription)

            cur.execute("""UPDATE complaintagainstsupplier SET cdate =%s, complaint_qty =%s, inspected_qty =%s,  cdescription =%s  WHERE id=%s""",
                        (cdate, complaint_qty, inspected_qty, cdescription, b))
            mydata.commit()
            MessageBox.showinfo("Insert Status", "Updated Successfully")
            mydata.close()
            expense_form.destroy()

      

        # Get selected item to Edit

   
        b = treevv.item(treevv.focus())["values"][0]
        print(b)
        sql='SELECT * FROM complaintagainstsupplier WHERE id=%s'
        val=(b,)
        cur.execute(sql,val)
        s = cur.fetchone()
        D = tk.Toplevel(A)
        print(s)

        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
            scrollregion=mycanvas.bbox('all')))

        full_frame = Frame(mycanvas, width=2000, height=730, bg='#2f516a')
        mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

        heading_frame = Frame(mycanvas)
        mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
        headingfont = font.Font(family='Times New Roman', size=25,)
        credit_heading = Label(heading_frame, text="Edit Complaint Against Supplier", fg='#fff',
                               bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=106)
        credit_heading.pack(padx=0, pady=0)

        # form fields
        sub_headingfont = font.Font(family='Times New Roman', size=20,)
        form_frame = Frame(mycanvas, width=1600, height=500, bg='#243e55')
        mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

        

        cd = Label(
            form_frame, text="Date", bg='#243e55', fg='#fff')
        cd.place(x=30, y=70,)
        cdate_input = StringVar()
        cdate_input = DateEntry(form_frame, width=50, bg="#2f516f", textvariable=cdate_input)
        cdate_input.place(x=30, y=100, height=40)
        try:
            cdate_input.insert(0, s[3])
        except:
            pass

    
        complaint_lab = tk.Label(form_frame, text="Complaint Quantity", bg='#243e55', fg='#fff')
        complaint_lab.place(x=30, y=160, height=15, width=150)
        place_input = StringVar()
        complaintqty_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        try:
            complaintqty_input.insert(0, s[5])
        except:
            pass
        complaintqty_input.place(x=30, y=190, height=40)
        wrappen.pack(fill='both', expand='yes',)


        inspctqty = tk.Label(
            form_frame, text="Inspected Quantity", bg='#243e55', fg='#fff')
        place_input = StringVar()
        inspctqty.place(x=30, y=240, height=15, width=150)
        inspctqty_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        try:
            inspctqty_input.insert(0, s[4])
        except:
            pass
        inspctqty_input.place(x=30, y=270, height=40)
        wrappen.pack(fill='both', expand='yes',)

        
        idll = tk.Label(
            form_frame, text="ID", bg='#243e55', fg='#fff')
        idl = Entry(form_frame, width=10, bg='#2f516f', fg='#fff')
        try:
            idl.insert(0, s[0])
        except:
            pass
        idll.place(x=530, y=200, height=15, width=20)
        idl.place(x=530, y=220, height=40, width=50)
    

        cdescription = Label(form_frame, text="Description",
                           bg='#243e55', fg='#fff')
        cdescription.place(x=530, y=70,)
        cdescription_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        try:
            cdescription_input.insert(0, s[6])
        except:
            pass
        
        cdescription_input.place(x=530, y=100, height=90)
        wrappen.pack(fill='both', expand='yes',)

        

       
        submit = tk.Button(
            form_frame, text="Save", command=changeedit)
        submit.place(x=500, y=320, width=100)

        D.mainloop()

    def delete():
        # Get selected item to Delete
        selected_item = treevv.selection()[0]
        treevv.delete(selected_item)

    edit_btn = ttk.Button(hd, text="Edit", command=editexp)
    edit_btn.place(relx=0.35, rely=0.8, relheight=0.1, relwidth=0.1)
    del_btn = ttk.Button(hd, text="Delete", command=delete)
    del_btn.place(relx=0.5, rely=0.8, relheight=0.1, relwidth=0.1)

    A.mainloop()


main()
