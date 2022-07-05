import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def viewpricelist():
    global treevv
    viewpricewin=tk.Tk()
    viewpricewin.title('View Materials')
    viewpricewin.geometry('1500x900')
    viewpricewin['bg'] = '#2f516f'
    f1=tk.Frame(viewpricewin,bg='#243e54')
    tk.Label(f1,text='PRICE LIST',bg='#243e54',font=('Times New Roman',24)).place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)
    f1.place(relx=0.1,rely=0.05,relheight=0.1,relwidth=0.8)
    f2=tk.Frame(viewpricewin,bg='#243e54')
    def searchedprice():
        searchs=serch.get()
        for item in treevv.get_children():
            treevv.delete(item) 
        if searchs!='':  
            cur.execute("SELECT priceid,productname,sku,price FROM pricelist WHERE productname LIKE %s ",(searchs,))    
            xx=cur.fetchall()
            if xx:
                for x in xx:
                    treevv.insert('', 'end',values=(x[0],x[1],x[2],x[3]))
        else:
            cur.execute("SELECT priceid,productname,sku,price FROM pricelist")
            val=cur.fetchall()
            if val:
                for x in val:
                    treevv.insert('', 'end',values=(x[0],x[1],x[2],x[3]))    
    serch=tk.Entry(f2,)
    serch.place(relx=0,rely=0,relwidth=0.2,relheight=0.07)
    search=tk.Button(f2,text='Search',bg='#243e54',font=('Times New Roman',14),command=searchedprice)
    search.place(relx=0.25,rely=0,relwidth=0.15,relheight=0.07)
    #tree
        #table view
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',background='silver',foreground='black',fieldbackground='#243e54')
    style.map('Treeview',background=[('selected','green')])
    treevv = ttk.Treeview(f2, height=20, columns=(1,2,3,4), show='headings') 
    treevv.heading(1, text='ID')
    treevv.heading(2, text='PRODUCT NAME')#headings
    treevv.heading(3, text='SKU')
    treevv.heading(4, text='PRICE')
    #treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=10, width=20,anchor=CENTER)#coloumns
    treevv.column(2, minwidth=30, width=260,anchor=CENTER)
    treevv.column(3, minwidth=30, width=160,anchor=CENTER)
    treevv.column(4, minwidth=30, width=160,anchor=CENTER)
    cur.execute("SELECT priceid,productname,sku,price FROM pricelist")
    val=cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end',values=(x[0],x[1],x[2],x[3]))
    treevv.place(relx=0,rely=0.1,relwidth=1,relheight=0.7)
    def pricelistedit():
        global editpricewin,bm
        str = treevv.focus()
        values=treevv.item(str,'values')
        b=[values[0]]
        cid=2
        cur.execute("SELECT * FROM pricelist WHERE priceid=%s",(b))
        s=cur.fetchone()
        editpricewin=tk.Toplevel(viewpricewin)
        editpricewin.title('Edit Price List')
        editpricewin.geometry('1500x700')
        editpricewin['bg'] = '#2f516f'
        frame=tk.Frame(editpricewin,bg='#243e54')
        frame.place(relx=0.15,rely=0.2,relwidth=0.7,relheight=0.4)
        tk.Label(frame,text='Product Name',bg='#243e54',font=('Times New Roman',16)).place(relx=0.2,rely=0.1)
        tk.Label(frame,text='SKU',bg='#243e54',font=('Times New Roman',16)).place(relx=0.45,rely=0.1)
        tk.Label(frame,text='PRICE',bg='#243e54',font=('Times New Roman',16)).place(relx=0.7,rely=0.1)
        pro=['Select Product']
        try:
            cur.execute("SELECT name FROM inventory WHERE cid =%s",([cid]))
            vall=cur.fetchall()    
            for row in vall:
                            pro.append(row[0])
            cur.execute("SELECT name FROM noninventory WHERE cid =%s",([cid]))
            valll=cur.fetchall()         
            for row in valll:
                pro.append(row[0])   
                cur.execute("SELECT productname FROM production WHERE cid =%s",([cid]))
                vall1=cur.fetchall()         
                for row in vall1:
                    pro.append(row[0])      
        except:
            pass
        def editpricelistprod(w):
            def clearskueditpricelist():
                sku.delete(0,END)
            clearskueditpricelist()    
            prodd=prod.get()
            cur.execute("SELECT sku FROM inventory WHERE name =%s",([prodd]))
            fet=cur.fetchone()
            cur.execute("SELECT sku FROM noninventory WHERE name =%s",([prodd]))
            fetch=cur.fetchone()
            cur.execute("SELECT sku FROM production WHERE productname =%s",([prodd]))
            fetc=cur.fetchone()
            if fet:
                sku.insert(0,fet[0])
            elif fetch:
                sku.insert(0,fetch[0])
            elif fetc:
                sku.insert(0,fetc[0]) 
        prod=ttk.Combobox(frame,values=pro)
        prod.insert(0,values[1])
        prod.bind('<<ComboboxSelected>>',editpricelistprod)
        prod.place(relx=0.2,rely=0.25,relheight=0.1,relwidth=0.2)
        sku=tk.Entry(frame)
        sku.insert(0,values[2])
        sku.place(relx=0.45,rely=0.25,relheight=0.1,relwidth=0.2)
        price=tk.Entry(frame)
        price.insert(0,values[3])
        price.place(relx=0.7,rely=0.25,relheight=0.1,relwidth=0.2)
        def savepricelistdetails():
            prodd=prod.get()
            skuu=sku.get()
            pricee=price.get()
            cur.execute("UPDATE pricelist set productname =%s, sku =%s, price =%s WHERE priceid =%s",(prodd,skuu,pricee,b[0],))
            mydata.commit()
            messagebox.showinfo('Sucessfully','Pricelist editted sucessfully')  
            editpricewin.destroy()
        tk.Button(frame,text='CREATE',bg='green',font=('Times New Roman',16),command=savepricelistdetails).place(relx=0.3,rely=0.6,relheight=0.2,relwidth=0.4)
        editpricewin.mainloop()
    edit_btn = Button(f2, text="Edit",command=pricelistedit)
    edit_btn.place(relx=0.35,rely=0.85,relheight=0.1,relwidth=0.1)
    def pricelistdelete():
        # Get selected item to Delete
        str=treevv.focus() 
        values=treevv.item(str,'values')
        b=[values[0]]
        cur.execute("DELETE FROM pricelist WHERE priceid=%s",(b))
        mydata.commit()
        treevv.delete(str)
    del_btn = Button(f2, text="Delete",command=pricelistdelete)
    del_btn.place(relx=0.5,rely=0.85,relheight=0.1,relwidth=0.1)  
    f2.place(relx=0.1,rely=0.2,relheight=0.7,relwidth=0.8)
    viewpricewin.mainloop()
viewpricelist()
