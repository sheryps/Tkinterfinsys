from struct import pack
from textwrap import wrap
import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
import tkinter.messagebox as MessageBox
import click
import mysql.connector
from requests import request 
from tkcalendar import Calendar, DateEntry
import matplotlib.patches
from datetime import datetime, date, timedelta
from PIL import Image,ImageTk
import os
from textwrap import wrap
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter, inch



mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
cur = mydata.cursor()

expense_form = tk.Tk()
expense_form.title("New")
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
    
    head = tk.LabelFrame(A, borderwidth=1, bg='#243e54')
    f = font.Font(family='Times New Roman', size=25)  # font
    lb = tk.Label(head, text='QUALITY CERTIFICATE', bg="#243e55", height=3,bd=3, relief="groove", font=f, width=114)
    lb['font'] = f
    lb.place(relx=0.05, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.125)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.85)
    form2_frame=tk.Frame(hd,bg='#243e54')


    form2_frame.place(relx=0.01,rely=0.075,relwidth=0.8,relheight=0.09)
    
    def addnew():
        global D
        def addit():
            global date1,sku,pname,customername,inspdate

            date1 = datel_input.get()
            sku = skul_input.get()
            pname = proname_input.get()
            customername = cusname_input.get()
            inspdate  = insdate_input.get()
                    
            con = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="fynsystkinter", port='3307')
            cur = con.cursor()
            cur.execute('INSERT INTO qualitycertificate(qc_date,qc_sku,qc_pname,qc_custumername,qc_inspdate) VALUES (%s,%s,%s,%s,%s)',(date1,sku,pname,customername,inspdate))
                    
            con.commit()
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            
        # Get selected item to Edit
        D = tk.Toplevel(A)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        full_frame = Frame(mycanvas, width=2000, height=730, bg='#2f516a')
        mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

        heading_frame = Frame(mycanvas)
        mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
        headingfont = font.Font(family='Times New Roman', size=25,)
        credit_heading = Label(heading_frame, text="Create Quality Certificate", fg='#fff',bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=80)
        credit_heading.pack(padx=0, pady=0)
            # form fields
        sub_headingfont = font.Font(family='Times New Roman', size=20,)
        form_frame = Frame(mycanvas, width=1100, height=300, bg='#243e55')
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

        proname = Label(form_frame, text="Product Name", bg='#243e55', fg='#fff')
        proname.place(x=600, y=30,)
        proname_input = StringVar()
        proname_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        proname_input.place(x=600, y=50, height=40)
         
        cusname = tk.Label(form_frame, text="Customer Name", bg='#243e55', fg='#fff')
        cusname.place(x=30, y=100, height=15, width=120)
        cusname_input = StringVar()
        cusname_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
        cusname_input.place(x=30, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)

        insdate = tk.Label(form_frame, text="Inspected Date", bg='#243e55', fg='#fff')
        insdate.place(x=600, y=100, height=15, width=150)
        insdate_input = StringVar()
        insdate_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=insdate_input)
        insdate_input.place(x=600, y=130, height=40)
        wrappen.pack(fill='both', expand='yes',)

        submit = tk.Button(form_frame, text="Save", command=addit)
        submit.place(x=580, y=200, width=100)

        D.mainloop()


    def viewq():
    # table view
        
        treevv = ttk.Treeview(hd, height=7, columns=(1, 2, 3, 4, 5, 6), show='headings')
        treevv.heading(1, text='ID')  # headings
        treevv.heading(2, text='DATE')  # headings
        treevv.heading(3, text='PRODUCT NAME')
        treevv.heading(4, text='SKU')
        treevv.heading(5, text='NAME')
        treevv.heading(6, text='INSPECTION DATE')
       
        treevv.column(1, minwidth=10, width=40, anchor=CENTER)  # coloumns
        treevv.column(2, minwidth=30, width=140, anchor=CENTER)
        treevv.column(3, minwidth=30, width=140, anchor=CENTER)
        treevv.column(4, minwidth=30, width=140, anchor=CENTER)
        treevv.column(5, minwidth=30, width=140, anchor=CENTER)
        treevv.column(6, minwidth=30, width=140, anchor=CENTER)
       
       
        cur.execute("SELECT cid,qc_date,qc_sku,qc_pname,qc_custumername,qc_inspdate FROM qualitycertificate")
        val = cur.fetchall()
        if val:
            for x in val:
                treevv.insert('', 'end', values=(x[0], x[1], x[3], x[2], x[4],x[5]))
        treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

        def editexp():
            global D
            def changeedit():
    
                mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
                cur = mydata.cursor()
                global qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate
                    
                qc_date = datel_input.get()
                qc_sku = skul_input.get()
                qc_pname = proname_input.get()
                qc_customername = cusname_input.get()
                qc_inspdate   = insdate_input.get()
                    
            
                print(qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate)

                cur.execute("""UPDATE qualitycertificate SET qc_date =%s, qc_sku =%s, qc_pname =%s, qc_custumername =%s, qc_inspdate =%s  WHERE cid=%s""",[qc_date,qc_sku,qc_pname,qc_customername,qc_inspdate, b])
                mydata.commit()
                MessageBox.showinfo("Insert Status", "Updated Successfully")
                mydata.close()

            # Get selected item to Edit

            b = treevv.item(treevv.focus())["values"][0]
            print(b)
            sql='SELECT * FROM qualitycertificate WHERE cid=%s'
            val=(b,)
            cur.execute(sql,val)
            s = cur.fetchone()
            D = tk.Toplevel(A)
            print(s)

            mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

            full_frame = Frame(mycanvas, width=1400, height=800, bg='#2f516a')
            mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

            heading_frame = Frame(mycanvas)
            mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
            headingfont = font.Font(family='Times New Roman', size=25,)
            credit_heading = Label(heading_frame, text="Edit Quality Inspection", fg='#fff',bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=100)
            credit_heading.pack(padx=0, pady=0)

            # form fields
            sub_headingfont = font.Font(family='Times New Roman', size=20,)
            form_frame = Frame(mycanvas, width=1400, height=500, bg='#243e55')
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
        
            skul = Label(form_frame, text="SKU Number", bg='#243e55', fg='#fff')
            skul.place(x=300, y=30, height=15, width=80)
            skul_input = StringVar()
            skul_input = Entry(form_frame, width=25, bg='#2f516f', fg='#fff')
            skul_input.place(x=300, y=50, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                skul_input.insert(0, s[3])
            except:
                pass

            proname = Label(form_frame, text="Product Name", bg='#243e55', fg='#fff')
            proname.place(x=600, y=30,)
            proname_input = StringVar()
            proname_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
            proname_input.place(x=600, y=50, height=40)
            try:
                proname_input.insert(0, s[2])
            except:
                pass
            
            idl = Label(form_frame, text="ID", bg='#243e55', fg='#fff')
            idl.place(x=1100, y=30,)
            idl_input = StringVar()
            idl_input = Entry(form_frame, width=10, bg='#2f516f', fg='#fff')
            idl_input.place(x=1100, y=50, height=40)
            try:
                idl_input.insert(0, s[0])
            except:
                pass
        
        
            cusname = tk.Label(form_frame, text="Customer Name", bg='#243e55', fg='#fff')
            cusname.place(x=30, y=100, height=15, width=120)
            cusname_input = StringVar()
            cusname_input = Entry(form_frame, width=55, bg='#2f516f', fg='#fff')
            cusname_input.place(x=30, y=130, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                cusname_input.insert(0, s[4])
            except:
                pass


            insdate = tk.Label(
                form_frame, text="Inspected Date", bg='#243e55', fg='#fff')
            insdate_input = StringVar()
            insdate.place(x=600, y=100, height=15, width=150)
            insdate_input = DateEntry(form_frame, width=25, bg="#2f516f",date_pattern='yyyy-mm-dd', textvariable=insdate_input)
            insdate_input.place(x=600, y=130, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                insdate_input.insert(0, s[5])
            except:
                pass

            
            submit = tk.Button(form_frame, text="Save", command=changeedit)
            submit.place(x=500, y=250, width=100)
            

            D.mainloop()


        def delete():
            # Get selected item to Delete
            selected_item = treevv.selection()[0]
            treevv.delete(selected_item)
            
        def view():
            

            # Get selected item to Edit

            b = treevv.item(treevv.focus())["values"][0]
            print(b)
            sql='SELECT * FROM qualitycertificate WHERE cid=%s'
            val=(b,)
            cur.execute(sql,val)
            s = cur.fetchone()
            D = tk.Toplevel(A)
            print(s)
            

            mycanvas.configure(yscrollcommand=yscrollbar.set)
            mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

            full_frame = Frame(mycanvas, width=1500, height=1100, bg='#2f516a')
            mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

            heading_frame = Frame(mycanvas)
            mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
            headingfont = font.Font(family='Times New Roman', size=25,)
            credit_heading = Label(heading_frame, text="Quality Certificate", fg='#fff',bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=95)
            credit_heading.pack(padx=0, pady=0)

            # form fields
            form2_frame = Frame(mycanvas, width=1200, height=900, bg='#243e55')
            mycanvas.create_window((20, 150), window=form2_frame, anchor="nw")
            
            form_frame = Frame(mycanvas, width=800, height=700, bg='#fff')
            mycanvas.create_window((200, 250), window=form_frame, anchor="nw")
            
            
            tk.Button(form2_frame,text = "DOWNLOAD",fg="#000",font=('times new roman', 16, 'bold'),command=download).place(relx=0.03,rely=0.07,relwidth=0.15)

            
            
            
            F2 = LabelFrame(form_frame, font=('times new roman', 15, ),border=0, fg="Black", bg="#e5e9ec")
            F2.place(x=0, y=10, width=800, height=200)
            size=(800,210)

            ax=ImageTk.PhotoImage(Image.open('f2.png').resize(size))
           
            tk.Label(F2,image=ax,bg='#e5e9ec', border=0).place(relx=0.00,rely=-0,relheight=1,relwidth=1 )
            
            
            datel = Label(form_frame, text="Date", bg='#fff',fg='#000')
            datel.place(x=200, y=190, width=100)
            datel_input = StringVar()
            datel_input = Entry(form_frame, width=25, bg="#fff",fg='#000')
            datel_input.place(x=350, y=190, height=40)
            try:
                datel_input.insert(0, s[1])
            except:
                pass
        
            skul = Label(form_frame, text="SKU Number", bg='#fff',fg='#000')
            skul.place(x=200, y=240, width=100)
            skul_input = StringVar()
            skul_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
            skul_input.place(x=350, y=240, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                skul_input.insert(0, s[3])
            except:
                pass

            proname = Label(form_frame, text="Product Name", bg='#fff', fg='#000')
            proname.place(x=200, y=290, width=100)
            proname_input = StringVar()
            proname_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
            proname_input.place(x=350, y=290, height=40)
            try:
                proname_input.insert(0, s[2])
            except:
                pass
            
            idl = Label(form_frame, text="ID", bg='#fff', fg='#000')
            idl.place(x=200, y=340, width=100)
            idl_input = StringVar()
            idl_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
            idl_input.place(x=350, y=340, height=40)
            try:
                idl_input.insert(0, s[0])
            except:
                pass
        
        
            cusname = tk.Label(form_frame, text="Customer Name", bg='#fff', fg='#000')
            cusname.place(x=200, y=390, height=15, width=100)
            cusname_input = StringVar()
            cusname_input = Entry(form_frame, width=25, bg='#fff', fg='#000')
            cusname_input.place(x=350, y=390, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                cusname_input.insert(0, s[4])
            except:
                pass

            insdate = tk.Label(
                form_frame, text="Inspected Date", bg='#fff', fg='#000')
            place_input = StringVar()
            insdate.place(x=200, y=440, height=15, width=100)
            insdate_input = Entry(form_frame, width=25, bg="#fff",fg='#000')
            insdate_input.place(x=350, y=440, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                insdate_input.insert(0, s[5])
            except:
                pass
            
            refl = Label(form_frame, text="Material Reference", bg='#fff',fg='#000', font=('times new roman',16,'bold'))
            refl.place(x=60, y=500, width=160)
            ref_input = StringVar()
            ref1_input = Entry(form_frame, width=5, bg='#fff', fg='#000')
            ref1_input.place(x=60, y=530, height=40)
            ref2_input = Entry(form_frame, width=10, bg='#fff', fg='#000')
            ref2_input.place(x=110, y=530, height=40)
            wrappen.pack(fill='both', expand='yes',)
            try:
                ref1_input.insert(0, s[3])
                ref2_input.insert(0, s[2])
            except:
                pass
            
            note1 = tk.Label(form_frame, text="This Product Was produced In Accordance With The Guidlines And Monitored In Every Manufacturing Stage.", bg='#fff', fg='#000')
            note1.place(x=30, y=590, height=20, width=800)
            note2 = tk.Label(form_frame, text="****END****", bg='#fff', fg='#000')
            note2.place(x=30, y=620, height=20, width=800)
            
            D.mainloop()

        def download():
            path = filedialog.asksaveasfilename(initialdir=os.getcwd,title="Save File",filetypes=[('Pdf File', '*.pdf',)],defaultextension=".pdf")

            fileName = path
            documentTitle = 'Quality Certificate'
            title = 'Quality Inspection Certificate'
            pdf = canvas.Canvas(fileName, pagesize=letter)
            pdf.setTitle(documentTitle)
            
            b = treevv.item(treevv.focus())["values"][0]
            print(b)
            sql='SELECT * FROM qualitycertificate WHERE cid=%s'
            val=(b,)
            cur.execute(sql,val)
            company = cur.fetchone()
            D = tk.Toplevel(A)
            
            pdf.setFont('Helvetica',12)
            
            text=company[2]
            wraped_text="\n".join(wrap(text,30))
            htg=wraped_text.split('\n')
                
            vg=len(htg)
            size=(600,190)

            ax=Image.open('f2.png').resize(size)           
            pdf.drawInlineImage(ax, 10,580)
            pdf.rect(20,330,300,250)
            pdf.drawString(30,550, "Date:")
            pdf.drawString(30,500, "SKU Number:")
            pdf.drawString(30,450, "Product Name:")
            pdf.drawString(30,400,"Customer Name:")
            pdf.drawString(30,350,"Inspected Date:")
            
            pdf.drawString(30,300,"Material Reference:")
            pdf.drawString(15,150,"This Product Was produced In Accordance With The Guidlines And Monitored In Every Manufacturing Stage.")
            pdf.drawString(250,100,"****END****")

            sql_inv_dt='SELECT * FROM qualitycertificate WHERE cid=%s'
            val=(b,)
            cur.execute(sql_inv_dt, val)
            tre=cur.fetchall()
            x=660
            print(tre)

            for i in tre:
                                pdf.drawString(130,550,str(i[1]))
                                pdf.drawString(130,500,str(i[3]))
                                pdf.drawString(130,450,str(i[2]))
                                pdf.drawString(130,400,str(i[4]))
                                pdf.drawString(130,350,str(i[5])) 
                                
                                pdf.drawString(30,280,str(i[3])) 
                                pdf.drawString(60,280,str(i[2])) 
            pdf.save()            

        view_btn = ttk.Button(hd, text="View", command=view)
        view_btn.place(relx=0.2, rely=0.8, relheight=0.1, relwidth=0.1)
        edit_btn = ttk.Button(hd, text="Edit", command=editexp)
        edit_btn.place(relx=0.45, rely=0.8, relheight=0.1, relwidth=0.1)
        del_btn = ttk.Button(hd, text="Delete", command=delete)
        del_btn.place(relx=0.7, rely=0.8, relheight=0.1, relwidth=0.1)
        
        hd.mainloop()

    tk.Button(form2_frame,text = "ADD",fg="#000",font=('times new roman', 22, 'bold'),command=addnew).place(relx=0.2,rely=0.4,relwidth=0.3, relheight=0.9)
    tk.Button(form2_frame,text = "VIEW",fg="#000",font=('times new roman', 22, 'bold'),command=viewq).place(relx=0.7,rely=0.4,relwidth=0.3, relheight=0.9)
    A.mainloop()

main()