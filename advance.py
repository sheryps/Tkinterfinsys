import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
from tkinter import messagebox
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cur=mydata.cursor()
#cmt
def advance():
    def getdata():
        payy=pay.get()
        acc=account.get()
        maill=mail.get("1.0","end")
        amountt=amount.get()
        date=dte.get()
        ref=refno.get()
        memo=memo1.get("1.0","end")
        cid=2
        if acc=='':
            acn_bl.config(text='Choose account',fg='red')  
        elif len(maill)<=5:
            bl_bl.config(text='Enter Correct Address',fg='red')    
        elif amountt=='':
            mb_bl.config(text='Enter Amount',fg='red') 
        elif ref=='':
            rf_bl.config(text='Enter Reference no',fg='red') 
        elif len(memo)<=1:
            mm_bl.config(text='Enter memo',fg='red')       
        else:
            ad='''INSERT INTO advancepayment (payee,account,address,amount,paymentdate,refno,memo,cid) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
            cur.execute(ad,[(payy),(acc),(maill),(amountt),(date),(ref),(memo),(cid)])
            mydata.commit()
            print('sucessfully added')
            wn.destroy()
    wn=tk.Tk()
    wn.title('Advance Payment')
    wn.geometry('1500x1000')
    wn['bg'] = '#2f516f'

    f3=tk.Frame(wn,bg='#243e54')
    tk.Label(f3,text='Advance Payment',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    f3.place(relx=0.1,rely=0.03,relwidth=0.8,relheight=0.1)

    f4=tk.Frame(wn,bg='#243e54')

    size=(400,400)
    image=Image.open('advancepayment.png').resize(size)
    ax=ImageTk.PhotoImage(image,master=wn)
    ay=tk.Label(f4,image=ax,bg='#243e54')
    ay.place(relx=0.63,rely=0.01,relheight=0.8,relwidth=0.35)

    def payye(ent):
        o=pay.get()
        if o!='':
            p_bl.config(text='Looks Good',fg='Green')  

    tk.Label(f4,text='Payee',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.05)
    def comboinput():
        cur.execute("SELECT firstname,lastname FROM customer")
        val=cur.fetchall()         
        for row in val:
            v.append(row[0]+row[1])
        cur.execute("SELECT firstname,lastname FROM supplier")
        vl=cur.fetchall()         
        for i in vl:
            v.append(i[0]+i[1])    
    v=['Who do you Pay']
    comboinput()  
    pay=ttk.Combobox(f4,values=v)
    pay.current(0)
    pay.bind('<FocusOut>',payye)
    pay.place(relx=0.05,rely=0.1,relwidth=0.3,relheight=0.05)

    p_bl=tk.Label(f4,text='',font=('arial',11),fg='red',bg='#243e54')
    p_bl.place(relx=0.05,rely=0.15) 
    
    def axc(ent):
        o=account.get()
        if o!='':
            acn_bl.config(text='Looks Good',fg='Green')  
    tk.Label(f4,text='Bank/Credit Account',font=('times new roman', 14),bg='#2f516f').place(relx=0.38,rely=0.05)
    v=['Cash and cash equivalents','Advance Payment Asset','Deferred CGST','Deferred GST Input Credit','Deferred IGST',
    'Deferred Krishi Kalyan Cess Input Credit','Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit',
    'GST Refund','Inventory Asset','Krishi Kalyan Cess Refund','Prepaid Insurance','Service Tax Refund','TDS Receivable',
    'Uncategorised Asset','Undeposited Funds']
    account=ttk.Combobox(f4,values=v)
    account.bind('<FocusOut>',axc)
    account.place(relx=0.38,rely=0.1,relwidth=0.2,relheight=0.05)

    acn_bl=tk.Label(f4,text='',font=('arial',11),fg='red',bg='#243e54')
    acn_bl.place(relx=0.38,rely=0.15) 

    tk.Label(f4,text='Mailing Address',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.2)
    mail=tk.Text(f4)
    mail.place(relx=0.05,rely=0.25,relwidth=0.3,relheight=0.15)

    bl_bl=tk.Label(f4,text='',font=('arial',11),fg='red',bg='#243e54')
    bl_bl.place(relx=0.05,rely=0.4) 

    def valid_amount(inp):
        if inp.isdigit():
                mb_bl.config(text='Looks Good',fg='green') 
                return True          
        else:
            return False

    tk.Label(f4,text='Amount',font=('times new roman', 14),bg='#2f516f').place(relx=0.38,rely=0.2)
    amount=tk.Entry(f4)
    amount.place(relx=0.38,rely=0.25,relwidth=0.2,relheight=0.05)
    val=f4.register(valid_amount)
    amount.config(validate='key',validatecommand=(val,"%P"))

    mb_bl=tk.Label(f4,text='',font=('arial',11),fg='red',bg='#243e54')
    mb_bl.place(relx=0.38,rely=0.3)  

    tk.Label(f4,text='Payment Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.45)
    dte=StringVar()
    DateEntry(f4,textvariable=dte).place(relx=0.05,rely=0.50,relwidth=0.3,relheight=0.05)

    def valid_refno(inp):
        if inp.isdigit():
                rf_bl.config(text='Looks Good',fg='green') 
                return True          
        else:
            return False

    tk.Label(f4,text='Ref No.',font=('times new roman', 14),bg='#2f516f').place(relx=0.38,rely=0.45)
    refno=tk.Entry(f4)
    refno.place(relx=0.38,rely=0.5,relwidth=0.2,relheight=0.05)
    rf=f4.register(valid_refno)
    refno.config(validate='key',validatecommand=(rf,"%P"))

    rf_bl=tk.Label(f4,text='',font=('arial',11),fg='red',bg='#243e54')
    rf_bl.place(relx=0.38,rely=0.55)  
   

    tk.Label(f4,text='Memo',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.62)
    memo1=tk.Text(f4)
    memo1.place(relx=0.05,rely=0.69,relwidth=0.53,relheight=0.15)

    mm_bl=tk.Label(f4,text='',font=('arial',11),fg='red',bg='#243e54')
    mm_bl.place(relx=0.05,rely=0.84)  

    tk.Button(f4,text='Submit Form',font=('times new roman', 16),bg='#2f516f',command=getdata).place(relx=0.4,rely=0.9,relwidth=0.2,relheight=0.05)

    f4.place(relx=0.1,rely=0.18,relwidth=0.8,relheight=0.7)
    wn.mainloop()
advance()    