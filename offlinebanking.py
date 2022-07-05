import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
import os
import pandas as pd
import webbrowser
import mysql.connector
from tkinter import messagebox
from datetime import datetime, date, timedelta
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cursor=mydata.cursor()

off=tk.Tk()
off.title('OFFLINE BANKING')
off.geometry('1500x1000')
off['bg'] = '#2f516f'
mycanvas=tk.Canvas(off,width=1800,height=1200)
mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
yscrollbar =ttk.Scrollbar(off,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill=Y)
mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
frame=tk.Frame(mycanvas)
frame['bg']='#2f516f'
mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1200)
fra1=tk.Frame(frame,bg='#243e54')
tk.Label(fra1,text='ADD TRANSACTIONS',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
fra1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
fra2=tk.Frame(frame,bg='#243e54')

#image...
s=(400,390)
im=Image.open('trans.png').resize(s)
img=ImageTk.PhotoImage(im,master=off)
imgg=tk.Label(fra2,image=img,bg='#243e54')
imgg.place(relx=0.05,rely=0.1,relheight=0.8,relwidth=0.4)

tk.Label(fra2,text='Upload Your Bank Transactions',font=('Times New Roman',30),bg='#243e54').place(relx=0.5,rely=0.1)
tk.Label(fra2,text='1. Sign in to your bank account.',font=('Times New Roman',20),bg='#243e54').place(relx=0.53,rely=0.2)
tk.Label(fra2,text='2. Download transactions.',font=('Times New Roman',20),bg='#243e54').place(relx=0.53,rely=0.26)
tk.Label(fra2,text='3. Upload the file to Fin sYs.',font=('Times New Roman',20),bg='#243e54').place(relx=0.53,rely=0.32)

#downloading excel sheet
def download():
    webbrowser.open('https://view.officeapps.live.com/op/view.aspx?src=http%3A%2F%2Ffinsys.live%2Fstatic%2Fassets%2FExcel%2FTransaxtions.xlsx&wdOrigin=BROWSELINK')
tk.Button(fra2,text='Download Excel Sheet',font=('Times New Roman',16),bg='#243e54',command=download).place(relx=0.6,rely=0.42,relwidth=0.3)

#uploaded statements
def statements():
    st=tk.Tk()
    st.title('STATEMENTS')
    st.geometry('1500x1000')
    st['bg'] = '#2f516f'
    stframe=tk.Frame(st,bg='#243e54')
    tk.Label(stframe,text='BANK STATEMENTS',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    stframe.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    sthframe=tk.Frame(st,bg='#243e54')

      #table view
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',background='silver',foreground='black',fieldbackground='#243e54',rowheight=25)
    style.map('Treeview',background=[('selected','green')])
    stattree = ttk.Treeview(sthframe, height=9, columns=(1,2,3,4,5), show='headings') 
    stattree.heading(1, text='ID')
    stattree.heading(2, text='DATE')#headings
    stattree.heading(3, text='DESCRIPTION')
    stattree.heading(4, text='DEBIT')
    stattree.heading(5, text='CREDIT')

    stattree.column(1, minwidth=10, width=40,anchor=CENTER)#coloumns
    stattree.column(2, minwidth=30, width=140,anchor=CENTER)
    stattree.column(3, minwidth=30, width=140,anchor=CENTER)
    stattree.column(4, minwidth=30, width=140,anchor=CENTER)
    stattree.column(5, minwidth=30, width=140,anchor=CENTER)

    cursor.execute("SELECT bankstatementid,date,description,debit,credit FROM bankstatements")
    val=cursor.fetchall()
    if val:
        for x in val:
            stattree.insert('', 'end',values=(x[0],x[1],x[2],x[3],x[4]))
    def statementadd():#statement adding tkinter page
        global D,bm
        str = stattree.focus()
        values=stattree.item(str,'values')
        id=values[0]
        cid=2
        offwin=tk.Toplevel(off)
        offwin.title('ADD BANKDATA')
        offwin.geometry('1500x800')
        offwin['bg'] = '#2f516f'
        addframe=tk.Frame(offwin,bg='#243e54')

        def offlinevalues():#adding bankdata
            try:
                pay=payy.get()
                catgy=cat.get()
                catamt=float(catamount.get())
                debit=float(values[3])
                credit=float(values[4])
                if debit==0.0:#checking and assigning crdecheck
                    crdecheck='credit'
                if credit==0.0:
                    crdecheck='debit'
                toda = date.today()
                tod = toda.strftime("%Y-%m-%d")    
                #checking credit or debit
                ww='debit'
                if crdecheck=='debit':
                    deb="INSERT INTO bills (cid,paydate,paymacnt,grandtotal,payornot,payee) values(%s,%s,%s,%s,%s,%s)"
                    cursor.execute(deb,[cid, tod, catgy, catamt, ww, pay])
                    mydata.commit()
                    nam='Accounts Payable(Creditors)'
                    cursor.execute("SELECT balance FROM accounts1 WHERE name =%s and cid =%s",([nam,cid]))
                    ard=cursor.fetchone()
                    amt=ard[0]-catamt
                    cursor.execute("""UPDATE accounts1 SET balance =%s WHERE name =%s and cid =%s""",([amt,nam,cid])) 
                    mydata.commit()
                    try:
                        cursor.execute("SELECT balance FROM accounts WHERE name =%s and cid =%s",([catgy,cid]))
                        ardd=cursor.fetchone()
                        amt0=ardd[0]-catamt
                        cursor.execute("""UPDATE accounts SET balance =%s WHERE name =%s and cid =%s""",([amt0,catgy,cid])) 
                        mydata.commit()
                    except:
                        pass    
                    try:
                        cursor.execute("SELECT balance FROM accounts1 WHERE name =%s and cid =%s",([catgy,cid]))
                        ardd=cursor.fetchone()
                        amt1=ardd[0]-catamt
                        cursor.execute("""UPDATE accounts1 SET balance =%s WHERE name =%s and cid =%s""",([amt1,catgy,cid])) 
                        mydata.commit()
                        
                    except:
                        pass    
                elif crdecheck=='credit':  
                    wx='True'
                    sales="INSERT INTO salesrecpts (cid,saledate,saledeposit,salegrandtotal,offline,salename) values(%s,%s,%s,%s,%s,%s)" 
                    cursor.execute(sales,[cid, tod, catgy, catamt, wx, pay])
                    mydata.commit()
                    namm='Account Receivable(Debtors)'
                    cursor.execute("SELECT balance FROM accounts1 WHERE name =%s and cid =%s",([namm,cid]))
                    ard=cursor.fetchone()
                    amtt=ard[0]+catamt
                    cursor.execute("""UPDATE accounts1 SET balance =%s WHERE name =%s and cid =%s""",([amtt,namm,cid])) 
                    mydata.commit()
                    try:
                        cursor.execute("SELECT balance FROM accounts WHERE name =%s and cid =%s",([catgy,cid]))
                        ardd=cursor.fetchone()
                        amtt0=ardd[0]+catamt
                        cursor.execute("""UPDATE accounts SET balance =%s WHERE name =%s and cid =%s""",([amtt0,catgy,cid])) 
                        mydata.commit()
                    except:
                        pass    
                    try:
                        cursor.execute("SELECT balance FROM accounts1 WHERE name =%s and cid =%s",([catgy,cid]))
                        ardd=cursor.fetchone()
                        amtt1=ardd[0]+catamt
                        cursor.execute("""UPDATE accounts1 SET balance =%s WHERE name =%s and cid =%s""",([amtt1,catgy,cid])) 
                        mydata.commit()
                        
                    except:
                        pass 
                messagebox.showinfo('SUCESSFULL','Datas entered sucessfully',parent=offwin) 
                offwin.destroy()    
                          
            except:
                pass  
            
        def getsuppcusdata(event):#getting payee and checking database
            pay=payy.get()
            x=pay.split()
            a=x[0]
            b=x[1]
            if len(x) == 3:
                b = x[1] + " " + x[2] 
                try:
                    cursor.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cursor.fetchone()
                    if supplier:
                        list=[]
                        cursor.execute("SELECT supplier_id,title,firstname,lastname,company,state,defaultexpenceaccount FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        sup=cursor.fetchone()
                        dict = {'id': sup[0], 'title': sup[1], 'firstname': sup[2],
                        'lastname': sup[3], 'company': sup[4], 'state': sup[5],
                        'defaultexpenceaccount': sup[6]}
                        list.append(dict)
                        print(list)
                except:
                    pass   
                try:
                    cursor.execute("SELECT firstname,lastname FROM customer WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    customer=cursor.fetchone()
                    if customer:
                        list=[]
                        cursor.execute("SELECT customer_id,title,firstname,lastname,company,state FROM customer WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        cus=cursor.fetchone()
                        dict = {'id': cus[0], 'title': cus[1], 'firstname': cus[2],
                        'lastname': cus[3], 'company': cus[4], 'state': cus[5],}
                        list.append(dict)
                        print(list)
                except:
                    pass         
            else:
                try:
                    cursor.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cursor.fetchone()
                    if supplier:
                        list=[]
                        cursor.execute("SELECT supplier_id,title,firstname,lastname,company,state,defaultexpenceaccount FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        sup=cursor.fetchone()
                        dict = {'id': sup[0], 'title': sup[1], 'firstname': sup[2],
                        'lastname': sup[3], 'company': sup[4], 'state': sup[5],
                        'defaultexpenceaccount': sup[6]}
                        list.append(dict)
                except:
                    pass
                try:
                    cursor.execute("SELECT firstname,lastname FROM customer WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    customer=cursor.fetchone()
                    if customer:
                        list=[]
                        cursor.execute("SELECT customer_id,title,firstname,lastname,company,state FROM customer WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        cus=cursor.fetchone()
                        dict = {'id': cus[0], 'title': cus[1], 'firstname': cus[2],
                        'lastname': cus[3], 'company': cus[4], 'state': cus[5],}
                        list.append(dict)
                except:
                    pass   
                   
                 
        tk.Label(addframe,text='Payee',font=('Times New Roman',16),bg='#243e54').place(relx=0.05,rely=0.05)
        payy=tk.Entry(addframe,font=('Times New Roman',16))
        payy.bind('<FocusOut>',getsuppcusdata)
        payy.place(relx=0.05,rely=0.12,relwidth=0.9,relheight=0.08)

        tk.Label(addframe,text='Category*',font=('Times New Roman',16),bg='#243e54').place(relx=0.05,rely=0.28)

        def categoryvalues():#combobox values
            cursor.execute("SELECT name FROM accounts WHERE cid=%s",([cid]))
            val=cursor.fetchall()         
            for row in val:
                catval.append(row[0])
            cursor.execute("SELECT name FROM accounts1 WHERE cid=%s",([cid]))
            vl=cursor.fetchall()         
            for i in vl:
                catval.append(i[0])  
            cursor.execute("SELECT name FROM accounts WHERE cid=%s",([cid]))
            val=cursor.fetchall()       
        catval=['Deferred CGST','Deferred GST Input Credit','Deferred IGST','Deferred Krishi Kalyan Cess Input Credit'
        ,'Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit','GST Refund','Inventory Asset',
        'Krishi Kalyan Cess Refund','Prepaid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset','Undeposited Fund']
        categoryvalues()
        cat=ttk.Combobox(addframe,font=('Times New Roman',12),values=catval)
        cat.place(relx=0.05,rely=0.35,relwidth=0.9,relheight=0.08)

        tk.Label(addframe,text='Amount',font=('Times New Roman',16),bg='#243e54').place(relx=0.05,rely=0.51)
        catamount=tk.Entry(addframe,font=('Times New Roman',16))
        catamount.place(relx=0.05,rely=0.59,relwidth=0.9,relheight=0.08)

        tk.Button(addframe,text='ADD',font=('Times New Roman',16),bg='#243e54',command=offlinevalues).place(relx=0.4,rely=0.8,relwidth=0.2)

        addframe.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.6)
        offwin.mainloop()
        
    edit_btn = Button(sthframe, text="ADD",command=statementadd)
    edit_btn.place(relx=0.45,rely=0.75,relheight=0.1,relwidth=0.1)        
    stattree.place(relx=0,rely=0.05,relwidth=1,relheight=0.6)

    sthframe.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.5)
    st.mainloop()
tk.Button(fra2,text='Uploaded Statements',font=('Times New Roman',16),bg='#243e54',command=statements).place(relx=0.6,rely=0.52,relwidth=0.3)

#excel file entering
def open_file():
    global b
    file_path = filedialog.askopenfilename(filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls")))
    a=os.path.basename(file_path)
    b=os.path.abspath(file_path)
    #d=os.path.dirname(os.path.abspath(file_path))
    tk.Label(fra2,text=a,font=('Times New Roman',14),bg='#243e54').place(relx=0.5,rely=0.72,relwidth=0.2)

#excel datas to database    
def upload():
    cid=2 
    df = pd.read_excel(b)  
    for index,row in df.iterrows():
        ff="INSERT INTO bankstatements (cid,name,date,description,debit,credit) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(ff,[cid, row[0], row[1], row[2], row[3], row[4]])
        mydata.commit()
    messagebox.showinfo('SUCESSFULL','Excel sheet uploaded',parent=off)     

tk.Button(fra2,text = "Select Excel File",font=('Times New Roman',16),command=open_file,bg='#243e54').place(relx=0.5,rely=0.65,relwidth=0.2)
tk.Button(fra2,text='Upload',font=('Times New Roman',16),bg='#243e54',command=upload).place(relx=0.73,rely=0.65,relwidth=0.2)
fra2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
off.mainloop()