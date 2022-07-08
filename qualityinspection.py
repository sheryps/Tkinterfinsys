import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
import tkinter.messagebox as MessageBox
import mysql.connector 
from tkcalendar import Calendar, DateEntry
import matplotlib.patches
from datetime import datetime, date, timedelta


mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
cur = mydata.cursor()

expense_form = tk.Tk()
expense_form.title("finsYs")
expense_form.geometry("1300x800")
expense_form['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(expense_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')


def main():

    global A
    A = tk.Tk()
    A.title('View')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'
    

    # head frame
    head = tk.LabelFrame(A, borderwidth=2, bg='#243e54')
    f = font.Font(family='Times New Roman', size=35)  # font
    lb = tk.Label(head, text='QUALITY INSPECTION', bg="#243e55", height=3,bd=2, relief="groove", font=f, width=106)
    lb['font'] = f
    lb.place(relx=0.07, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.11)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.8)
    form2_frame=tk.Frame(hd,bg='#243e54')

    def addnew():
        def addit():
            global D, qdate,sku,p_name,inspected_no,noninspected_no,inspected_by,department,qualified_products, nonqualified_products
                
            qdate = datel_input.get()
            sku = skul_input.get()
            p_name = proname_input.get()
            inspected_no = inspectedl_input.get()
            noninspected_no = noninspctqty_input.get()
            inspected_by = inspectedbyl_input.get()
            department = deptl_input.get()
            qualified_products = qualifiedl_input.get()
            nonqualified_products = nonqualifiedl_input.get()
  
            con = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="fynsystkinter", port='3307')
            cur = con.cursor()
            d='''INSERT INTO qualityinspection(qdate, sku, p_name, inspected_no, noninspected_no, inspected_by, department, qualified_products, nonqualified_products) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cur.execute(d,([qdate,sku,p_name,inspected_no,noninspected_no,inspected_by,department,qualified_products,nonqualified_products]))
                
            con.commit()
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
          
        # Get selected item to Edit
        D = tk.Toplevel(A)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        full_frame = Frame(mycanvas, width=2000, height=730, bg='#2f516a')
        mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

        heading_frame = Frame(mycanvas)
        mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
        headingfont = font.Font(family='Times New Roman', size=25,)
        credit_heading = Label(heading_frame, text="New Quality Inspection", fg='#fff',bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=106)
        credit_heading.pack(padx=0, pady=0)

        # form fields
        sub_headingfont = font.Font(family='Times New Roman', size=20,)
        form_frame = Frame(mycanvas, width=1600, height=500, bg='#243e55')
        mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

        datel = Label(form_frame, text="Date", bg='#243e55', fg='#fff')
        datel.place(x=30, y=30,)
        datel_input = StringVar()
        datel_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=datel_input)
        datel_input.place(x=30, y=50, height=40)
       
    
        skul = tk.Label(form_frame, text="SKU Number", bg='#243e55', fg='#fff')
        skul.place(x=300, y=30, height=15, width=80)
        skul_input = StringVar()
        skul_input = Entry(form_frame, width=25, bg='#2f516f', fg='#fff')
        skul_input.place(x=300, y=50, height=40)
        wrappen.pack(fill='both', expand='yes',)

        proname = Label(
            form_frame, text="Product Name", bg='#243e55', fg='#fff')
        proname.place(x=600, y=30,)
        proname_input = StringVar()
        proname_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        proname_input.place(x=600, y=50, height=40)
       
    
        inspectedl = tk.Label(form_frame, text="Inspected Quantity", bg='#243e55', fg='#fff')
        inspectedl.place(x=30, y=100, height=15, width=120)
        inspectedl_input = StringVar()
        inspectedl_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        inspectedl_input.place(x=30, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)


        noninspctqty = tk.Label(
            form_frame, text="Non-Inspected Quantity", bg='#243e55', fg='#fff')
        place_input = StringVar()
        noninspctqty.place(x=600, y=100, height=15, width=150)
        noninspctqty_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        noninspctqty_input.place(x=600, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)

        

        inspectedbyl = Label(form_frame, text="Inspected By",
                           bg='#243e55', fg='#fff')
        inspectedbyl.place(x=30, y=180,)
        inspectedbyl_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        inspectedbyl_input.place(x=30, y=210, height=40)
        wrappen.pack(fill='both', expand='yes',)
        
        deptl = tk.Label(form_frame, text="Department", bg='#243e55', fg='#fff')
        deptl.place(x=600, y=180, height=15, width=80)
        deptl_input = StringVar()
        deptl_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        deptl_input.place(x=600, y=210, height=40)
        wrappen.pack(fill='both', expand='yes',)


        qualifiedl = tk.Label(
            form_frame, text="Qualified", bg='#243e55', fg='#fff')
        place_input = StringVar()
        qualifiedl.place(x=30, y=270, height=15, width=80)
        qualifiedl_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        qualifiedl_input.place(x=30, y=290, height=40)
        wrappen.pack(fill='both', expand='yes',)

        

        nonqualifiedl = Label(form_frame, text="Non-Qualified",
                           bg='#243e55', fg='#fff')
        nonqualifiedl.place(x=600, y=270,)
        nonqualifiedl_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        nonqualifiedl_input.place(x=600, y=290, height=40)
        wrappen.pack(fill='both', expand='yes',)

        
        
        
        submit = tk.Button(form_frame, text="Save", command=addit)
        submit.place(x=580, y=400, width=100)

        D.mainloop()
         
    tk.Button(form2_frame,text = "ADD",fg="#000",font=('times new roman', 21, 'bold'),command=addnew).place(relx=0.8,rely=0.5,relwidth=0.15)
    form2_frame.place(relx=0.01,rely=0.075,relwidth=1,relheight=0.1)

    # table view

    treevv = ttk.Treeview(hd, height=7, columns=(1, 2, 3, 4, 5, 6,7,8,9,10), show='headings')
    treevv.heading(1, text='ID')  # headings
    treevv.heading(2, text='INSPECTION DATE')  # headings
    treevv.heading(3, text='SKU')
    treevv.heading(4, text='PRODUCT NAME')
    treevv.heading(5, text='INSPECTED')
    treevv.heading(6, text='NON INSPECTED')
    treevv.heading(7, text='INSPECTED BY')
    treevv.heading(8, text='DEPARTMENT')
    treevv.heading(9, text='QUALIFIED')
    treevv.heading(10, text='NON-QUALIFIED')

    treevv.column(1, minwidth=10, width=40, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=80, anchor=CENTER)
    treevv.column(3, minwidth=30, width=30, anchor=CENTER)
    treevv.column(4, minwidth=30, width=100, anchor=CENTER)
    treevv.column(5, minwidth=30, width=50, anchor=CENTER)
    treevv.column(6, minwidth=30, width=100, anchor=CENTER)
    treevv.column(7, minwidth=30, width=100, anchor=CENTER)
    treevv.column(8, minwidth=30, width=100, anchor=CENTER)
    treevv.column(9, minwidth=30, width=50, anchor=CENTER)
    treevv.column(10, minwidth=30, width=60, anchor=CENTER)
        
    cur.execute("SELECT cid,qdate,sku,p_name,inspected_no,noninspected_no,inspected_by,department,qualified_products, nonqualified_products FROM qualityinspection")
    val = cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4],x[5],x[6], x[7],x[8],x[9]))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

    def editexp():
        def changeedit():

            mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
            cur = mydata.cursor()
            global D, qdate,sku,p_name,inspected_no,noninspected_no,inspected_by,department,qualified_products, nonqualified_products
                
            qdate = datel_input.get()
            sku = skul_input.get()
            p_name = proname_input.get()
            inspected_no = inspectedl_input.get()
            noninspected_no = noninspctqty_input.get()
            inspected_by = inspectedbyl_input.get()
            department = deptl_input.get()
            qualified_products = qualifiedl_input.get()
            nonqualified_products = nonqualifiedl_input.get()
                
           
            print(qdate,sku,p_name,inspected_no,noninspected_no,inspected_by,department,qualified_products, nonqualified_products)
            # cur.execute("""UPDATE qualitycertificate SET qc_date =%s, qc_sku =%s, qc_pname =%s, qc_custumername =%s, qc_inspdate =%s  WHERE cid=%s""",[qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate, b])
            cur.execute("""UPDATE qualityinspection SET qdate =%s, sku =%s, p_name =%s, inspected_no =%s, noninspected_no =%s, inspected_by =%s, department =%s, qualified_products =%s, nonqualified_products =%s  WHERE cid=%s""", [qdate, sku, p_name, inspected_no, noninspected_no, inspected_by, department, qualified_products, nonqualified_products, b])
            mydata.commit()
            MessageBox.showinfo("Insert Status", "Updated Successfully")
            mydata.close()

        # Get selected item to Edit

        b = treevv.item(treevv.focus())["values"][0]
        print(b)
        sql='SELECT * FROM qualityinspection WHERE cid=%s'
        val=(b,)
        cur.execute(sql,val)
        s = cur.fetchone()
        D = tk.Toplevel(A)
        print(s)

        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        full_frame = Frame(mycanvas, width=2000, height=730, bg='#2f516a')
        mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

        heading_frame = Frame(mycanvas)
        mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
        headingfont = font.Font(family='Times New Roman', size=25,)
        credit_heading = Label(heading_frame, text="Edit Quality Inspection", fg='#fff',bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=106)
        credit_heading.pack(padx=0, pady=0)

        # form fields
        sub_headingfont = font.Font(family='Times New Roman', size=20,)
        form_frame = Frame(mycanvas, width=1600, height=500, bg='#243e55')
        mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

        datel = Label(form_frame, text="Date", bg='#243e55', fg='#fff')
        datel.place(x=30, y=30,)
        datel_input = StringVar()
        datel_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=datel_input)
        datel_input.place(x=30, y=50, height=40)
        try:
            datel_input.insert(0, s[1])
        except:
            pass
       
    
        skul = tk.Label(form_frame, text="SKU Number", bg='#243e55', fg='#fff')
        skul.place(x=300, y=30, height=15, width=80)
        skul_input = StringVar()
        skul_input = Entry(form_frame, width=25, bg='#2f516f', fg='#fff')
        skul_input.place(x=300, y=50, height=40)
        wrappen.pack(fill='both', expand='yes',)
        try:
            skul_input.insert(0, s[9])
        except:
            pass

        proname = Label(
            form_frame, text="Product Name", bg='#243e55', fg='#fff')
        proname.place(x=600, y=30,)
        proname_input = StringVar()
        proname_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        proname_input.place(x=600, y=50, height=40)
        try:
            proname_input.insert(0, s[2])
        except:
            pass
        
        idl = Label(
            form_frame, text="ID", bg='#243e55', fg='#fff')
        idl.place(x=1100, y=30,)
        idl_input = StringVar()
        idl_input = Entry(form_frame, width=10, bg='#2f516f', fg='#fff')
        idl_input.place(x=1100, y=50, height=40)
        try:
            idl_input.insert(0, s[0])
        except:
            pass
       
    
        inspectedl = tk.Label(form_frame, text="Inspected Quantity", bg='#243e55', fg='#fff')
        inspectedl.place(x=30, y=100, height=15, width=120)
        inspectedl_input = StringVar()
        inspectedl_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        inspectedl_input.place(x=30, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)
        try:
            inspectedl_input.insert(0, s[4])
        except:
            pass


        noninspctqty = tk.Label(
            form_frame, text="Non-Inspected Quantity", bg='#243e55', fg='#fff')
        place_input = StringVar()
        noninspctqty.place(x=600, y=100, height=15, width=150)
        noninspctqty_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        noninspctqty_input.place(x=600, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)
        try:
            noninspctqty_input.insert(0, s[5])
        except:
            pass

        

        inspectedbyl = Label(form_frame, text="Inspected By",
                           bg='#243e55', fg='#fff')
        inspectedbyl.place(x=30, y=180,)
        inspectedbyl_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        inspectedbyl_input.place(x=30, y=210, height=40)
        wrappen.pack(fill='both', expand='yes',)
        try:
            inspectedbyl_input.insert(0, s[6])
        except:
            pass
        
        deptl = tk.Label(form_frame, text="Department", bg='#243e55', fg='#fff')
        deptl.place(x=600, y=180, height=15, width=80)
        deptl_input = StringVar()
        deptl_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        deptl_input.place(x=600, y=210, height=40)
        wrappen.pack(fill='both', expand='yes',)
        try:
            deptl_input.insert(0, s[3])
        except:
            pass


        qualifiedl = tk.Label(
            form_frame, text="Qualified", bg='#243e55', fg='#fff')
        place_input = StringVar()
        qualifiedl.place(x=30, y=270, height=15, width=80)
        qualifiedl_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        qualifiedl_input.place(x=30, y=290, height=40)
        wrappen.pack(fill='both', expand='yes',)
        try:
            qualifiedl_input.insert(0, s[7])
        except:
            pass

        

        nonqualifiedl = Label(form_frame, text="Non-Qualified",
                           bg='#243e55', fg='#fff')
        nonqualifiedl.place(x=600, y=270,)
        nonqualifiedl_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        nonqualifiedl_input.place(x=600, y=290, height=40)
        wrappen.pack(fill='both', expand='yes',)
        try:
            nonqualifiedl_input.insert(0, s[8])
        except:
            pass

        
        
        
        submit = tk.Button(form_frame, text="Save", command=changeedit)
        submit.place(x=580, y=400, width=100)
        

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
