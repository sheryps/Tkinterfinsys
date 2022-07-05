import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def pricelist():
    pricewin=tk.Tk()
    pricewin.title('ADD PRICE LIST')
    pricewin.geometry('1500x700')
    pricewin['bg'] = '#2f516f'
    cid=2
    frame=tk.Frame(pricewin,bg='#243e54')
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
    def pricelistprod(w):
        def clearskupricelist():
            sku.delete(0,END)
        clearskupricelist()    
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
    prod.bind('<<ComboboxSelected>>',pricelistprod)
    prod.place(relx=0.2,rely=0.25,relheight=0.1,relwidth=0.2)
    sku=tk.Entry(frame)
    sku.place(relx=0.45,rely=0.25,relheight=0.1,relwidth=0.2)
    price=tk.Entry(frame)
    price.place(relx=0.7,rely=0.25,relheight=0.1,relwidth=0.2)
    def savepricelistdetails():
        prodd=prod.get()
        skuu=sku.get()
        pricee=price.get()
        list="INSERT INTO pricelist (cid,productname,sku,price) VALUES (%s,%s,%s,%s)"
        cur.execute(list,[(cid),(prodd),(skuu),(pricee)])
        mydata.commit()
        messagebox.showinfo('Sucessfully','Pricelist added sucessfully')  
        pricewin.destroy()
    tk.Button(frame,text='CREATE',bg='green',font=('Times New Roman',16),command=savepricelistdetails).place(relx=0.3,rely=0.6,relheight=0.2,relwidth=0.4)
    pricewin.mainloop()
pricelist()    