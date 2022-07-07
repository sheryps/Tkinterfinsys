import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
from datetime import datetime, date, timedelta
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def salespayments():  
    def getpaymenvalues():
        a=estcus.get()
        c=invno.get()
        d=estdate.get()
        e=paymet.get()
        f=drop1accounttype.get()
        g=label44amountrec.get()
        h=label44tabpayment.get()
        i=label44amountapply.get()
        j=label44amountcredit.get()
        cur.execute("UPDATE payment SET paymdate =%s,paymethod =%s,invno =%s, acctype =%s, payamount =%s, amtapply =%s,amtreceived =%s,amtcredit =%s WHERE paymentid =%s",(d,e,c,f,h,i,g,j,v))
        mydata.commit()
        estwin.destroy()    

    estwin=tk.Tk()
    estwin.title('Payments')
    estwin.geometry('1500x1000')
    estwin['bg'] = '#2f516f'
    cid=2
    mycanvas=tk.Canvas(estwin,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(estwin,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1500)
    hf1=tk.Frame(frame,bg='#243e54')
    tk.Label(hf1,text='Receive Payments',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    hf1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.05)
    hf2=tk.Frame(frame,bg='#243e54')
            #customer
    tk.Label(hf2,text='Fin sYs',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.02)     
    def salespaymentscusinput():
        try:
                cur.execute("SELECT firstname,lastname FROM customer")
                val=cur.fetchall()         
                for row in val:
                    tm.append(row[0]+row[1])   
        except:
            pass              
    tm=['Select Customer']
    salespaymentscusinput()      
    tk.Label(hf2,text='Customer',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.11) 
    estcus=ttk.Combobox(hf2,font=('times new roman', 12),values=tm)
    def get_mail(event):
        global v
        def des():
            label44tabdescription.delete(0,END)
            email.delete(0,END)
            label44tabduedate.delete(0,END)
            label44taboriginalamount.delete(0,END)
            label44tabopenbalance.delete(0,END)
        des()
        option=estcus.get()
        x = option.split(" ", 1)
        print("boy",option)
        # mycursor.execute("SELECT * FROM app1_customer where firstname=%s and lastname=%s",(x[0],x[1]))
        # table1=mycursor.fetchone()
        # email.set(table1[9])
            # billto.set(i[12:17])
        
        cur.execute("SELECT descrip,email,duedate,orgamt,openbal,paymentid FROM payment where customer=%s ",([option]))
        table2=cur.fetchone() 
        email.insert(0,table2[1])
        label44tabduedate.insert(0,table2[2])
        label44tabdescription.insert(0,table2[0])
        label44taboriginalamount.insert(0,table2[3])
        label44tabopenbalance.insert(0,table2[4])
        v=table2[5]
    estcus.bind('<<ComboboxSelected>>',get_mail)
    estcus.place(relx=0.05,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Button(hf2,text='+',font=(14)).place(relx=0.26,rely=0.15,relwidth=0.025,relheight=0.03)
    tk.Label(hf2,text='Email',font=('times new roman', 14),bg='#2f516f').place(relx=0.30,rely=0.11)
    email=tk.Entry(hf2)
    email.place(relx=0.3,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Label(hf2,text='Find by invoice number',font=('times new roman', 14),bg='#2f516f').place(relx=0.55,rely=0.11)
    invno=tk.Entry(hf2)
    invno.place(relx=0.55,rely=0.15,relwidth=0.2,relheight=0.03)
    toda = date.today()
    to = toda.strftime("%Y-%m-%d")
    tk.Label(hf2,text='Payment Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.2)
    estdate=tk.Entry(hf2)
    estdate.insert(0,to)
    estdate.place(relx=0.05,rely=0.24,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text='Payment Method',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.29)

    def pmethod(event):
        global add,label44add
        p = paymet.get()
        print(p)
        
        if p == 'Add New':
            def wer(n):
                cc=label44add.get()
                paymet.delete(0,END)
                paymet.insert(0,label44add.get())
            add=StringVar()    
            label44add=Entry(hf2,bg='#2f516a',fg='#fff',textvariable=add, font=('times new roman', 11, 'bold'))
            label44add.place(relx=0.05,rely=0.37,relwidth=0.2,relheight=0.03)
            label44add.bind("<KeyRelease>",wer)
        if p!='Add New':
            label44add['state']='disabled'   
    met=['Cash','Cheque','Credit Card','Add New']
    paymet=ttk.Combobox(hf2,values=met)
    paymet.current(0)
    paymet.bind('<<ComboboxSelected>>',pmethod)
    paymet.place(relx=0.05,rely=0.33,relwidth=0.2,relheight=0.03) 
    tk.Label(hf2,text="Deposit To",font=('times new roman', 14),bg='#2f516f').place(relx=0.55,rely=0.2)
    drop1accounttype=ttk.Combobox(hf2,textvariable='accounttype')
    drop1accounttype['values']=("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund")
    drop1accounttype.place(relx=0.55,rely=0.24,relwidth=0.2,relheight=0.03) 
    def deffadd():
        def getpayaccvalues():
            global cb
            try:
                actype=cm1.get()
                name=nameinput.get()
                dettype=l.get()
                dec=descriptioninput.get()
                act=cb.get()
                tax=nb.get()

                d='INSERT INTO accounts (acctype,detype,name,description,gst,deftaxcode,cid) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(d,[(actype),(dettype),(name),(dec),(act),(tax),(cid)])
                mydata.commit()
            except:
                pass
            drop1accounttype.insert(0,name)
            add.destroy()
        global add,cb
        add = tk.Toplevel(estwin)
        add.title('Add Account')
        add.geometry('1000x800')
        add['bg'] = '#2f516f'
        
        uid=[4]
        acc_heading= Label(add, text="ACCOUNT CREATE",bd=0,relief="groove",bg='#2f516f', fg='#fff',height=2,pady=2,width=100)
        acc_heading.pack()
        hd1 = tk.Frame(add,width=900,height=650)
        hd1['bg'] = '#243e54'
        hd1.place(relx=0.05, rely=0.1)

            # font

        tk.Label(hd1, text='Account Type', bg='#243e54', fg="#fff",font=(
            'times new roman', 14)).place(relx=0.04, rely=0.05)
        value=['Bank','Current Assests']    
        cm1 =ttk.Combobox(hd1,values=value)
        cm1.place(relx=0.04, rely=0.10, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Name', bg='#243e54', fg="#fff",font=(
            'times new roman', 14)).place(relx=0.5, rely=0.05)
        nameinput = StringVar()
        fnameinput = tk.Entry(hd1, textvariable=nameinput,bg="#3E505C",fg="#fff")

        fnameinput.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.065)


        def detype(g):
            def dtl():
                fnameinput.delete(0,END)
            ok=l.get()
            print("ctc",ok)
            dtl()
            fnameinput.insert(0,l.get())

        tk.Label(hd1, text='Detail Type',fg="#fff", font=('times new roman', 14),
                    bg='#243e54').place(relx=0.04, rely=0.2)           
        def combopinput():
            cur.execute("SELECT itemname FROM itemmodel")
            val=cur.fetchall()         
            for row in val:
                itemvalue.append(row[0]) 
        itemvalue=[]           
        combopinput()                 
        l =ttk.Combobox(hd1,values=itemvalue)
        
        l.place(relx=0.04, rely=0.25, relwidth=0.4, relheight=0.065)

        tk.Label(hd1, text='Description',fg="#fff", font=('times new roman', 14),
                    bg='#243e54').place(relx=0.5, rely=0.2)
        descriptioninput = StringVar()
        co = tk.Entry(hd1, textvariable=descriptioninput,bg="#3E505C",fg="#fff")
        #co.insert(1, s[4])
        co.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.065)

        message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
        text_box = Text(hd1,bg="#3E505C",fg="#fff")
        text_box.place(relx=0.04, rely=0.35, relwidth=0.4, relheight=0.3)
        text_box.insert('end', message)
        text_box.config(state='disabled')

        # subaccountinput="Deffered_CGST"
        typeinput = StringVar()
        def activator():
            global cb
            bal=['Deferred CGST','Deferred GST Input Credit','Deferred Krishi Kalyan Cess',
            'Input Credit','Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit',
            'GST Refund','Inventory Asset','Paid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset',
            'Accumulated Depreciation','Buildings and Improvements','Furniture and Equipment','Land','Leasehold Improvements',
            'CGST Payable','CST Payable','CST Suspense','GST Payable','GST Suspense','IGST Payable','Input CGST','Input CGST Tax RCM',
            'Input IGST','Input IGST Tax RCM','Input Krishi Kalyan Cess','Input Krishi Kalyan Cess RCM','Input Service Tax',
            'Input Service Tax RCM','Input VAT 14%','Input VAT 4%','Input VAT 5%','Krishi Kalyan Cess Payable','Krishi Kalyan Cess Suspense',
            'Output CGST','Output CGST Tax RCM','Output CST 2%','Output IGST','Output IGST Tax RCM','Output Krishi Kalyan Cess',
            'Output Krishi Kalyan Cess DCM','Output Service Tax','Output Service Tax RCM','Output SGST','Output SGST Tax RCM',
            'Output VAT 14%','Output VAT 4%','Output VAT 5%','Service Tax Payable','Service Tax Suspense','SGST Payable','Swachh Bharat Cess Payable',
            'TDS Payable','VAT Payable','VAT Suspense','Opening Balance','Equity']

            cb=ttk.Combobox(hd1,values=bal)
            cb.place(relx=0.5,rely=0.43,relwidth=0.4,relheight=0.065)
        ch=IntVar()
        Checkbutton(hd1, text = "Is sub-account ",bg='#243e54',font=('times new roman', 12),command=activator,variable=ch).place(relx=0.50,rely=0.35)    
        
        

        tk.Label(hd1, text='Default Tax Code', font=('times new roman', 14),fg="#fff",
                    bg='#243e54').place(relx=0.5, rely=0.5)
        defaulttaxcodeinput = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                                '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
        nb = ttk.Combobox(hd1, values=defaulttaxcodeinput)

        nb.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.065)

    
        sub = tk.Button(hd1, text='Create', font=15, bg='#243e54',fg="#fff",width=40,command=getpayaccvalues).place(relx=0.28, rely=0.8)
    tk.Button(hf2,text='+',font=(14),command=deffadd).place(relx=0.755,rely=0.24,relwidth=0.025,relheight=0.03)
    def key_press(event):
        def dec():
            label4amount.delete(0,END)
            label44tabpayment.delete(0,END)
            label44amountapply.delete(0,END)
        # dec()   
        act=label44amountrec.get()
        print("wowo",act)
        dec()
        label4amount.insert(0,label44amountrec.get())
        label44tabpayment.insert(0,label44amountrec.get())
        label44amountapply.insert(0,label44amountrec.get())
    Label(hf2, text="Amount Recieved", font=('times new roman', 14),bg='#2f516f').place(relx=0.72,rely=0.32) 
    label44amountrec=Entry(hf2,font=('times new roman', 11))
    label44amountrec.place(relx=0.72,rely=0.35,relwidth=0.2,relheight=0.03) 
    label44amountrec.bind('<KeyRelease>',key_press)

    Label(hf2, text="AMOUNT RECIEVED", font=('times new roman', 12), bd=12,bg='#2f516f').place(relx=0.72,rely=0.40) 
    label4amount=Entry(hf2, font=('times new roman',11))
    label4amount.place(relx=0.72,rely=0.45,relwidth=0.2,relheight=0.03) 

    label4=Label(hf2, text="#", font=('times new roman', 12,'bold'), bd=12, bg='#2f516f')
    label4.place(relx=0.05,rely=0.55)
    tk.Label(hf2,text='1',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.62,relwidth=0.05,relheight=0.03)   

    label4=Label(hf2, text="DESCRIPTION", font=('times new roman', 12,'bold'), bd=12, bg='#2f516f')
    label4.place(relx=0.12,rely=0.55)
    label44tabdescription=Entry(hf2,font=('times new roman', 11))
    label44tabdescription.place(relx=0.12,rely=0.62,relwidth=0.15,relheight=0.03)

    label4=Label(hf2, text="DUE DATE", font=('times new roman', 12, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.29,rely=0.55)
    label44tabduedate=Entry(hf2,font=('times new roman', 11, 'bold'))
    label44tabduedate.place(relx=0.29,rely=0.62,relwidth=0.15,relheight=0.03)

    label4=Label(hf2, text="ORIGINAL AMOUNT", font=('times new roman', 12,'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.46,rely=0.55)
    label44taboriginalamount=Entry(hf2, font=('times new roman', 11))
    label44taboriginalamount.place(relx=0.46,rely=0.62,relwidth=0.15,relheight=0.03)

    label4=Label(hf2, text="OPEN BALANCE", font=('times new roman', 12, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.64,rely=0.55)
    label44tabopenbalance=Entry(hf2,font=('times new roman', 11))
    label44tabopenbalance.place(relx=0.64,rely=0.62,relwidth=0.12,relheight=0.03)

    label4=Label(hf2, text="PAYMENT", font=('times new roman', 12, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.80,rely=0.55)
    label44tabpayment=Entry(hf2, font=('times new roman', 11, 'bold'))
    label44tabpayment.place(relx=0.80,rely=0.62,relwidth=0.12,relheight=0.03)

    label4=Label(hf2, text="Amount to Apply", font=('times new roman', 14, 'bold'), bd=12, bg="#2f516f")
    label4.place(relx=0.60,rely=0.70)
    label44amountapply=Entry(hf2, font=('times new roman', 11, 'bold'))
    label44amountapply.place(relx=0.75,rely=0.70,relwidth=0.15,relheight=0.04)

    label4=Label(hf2, text="Amount to Credit", font=('times new roman', 14, 'bold'), bd=12,bg="#2f516f" )
    label4.place(relx=0.60,rely=0.77)
    label44amountcredit=Entry(hf2,font=('times new roman', 11, 'bold'))
    label44amountcredit.place(relx=0.75,rely=0.77,relwidth=0.15,relheight=0.04)

    tk.Button(hf2,text='Save',bg="#2f516f",font=('times new roman', 14, 'bold'),command=getpaymenvalues).place(relx=0.65,rely=0.9,relwidth=0.1,relheight=0.05)

    hf2.place(relx=0.1,rely=0.12,relwidth=0.8,relheight=0.7)
    estwin.mainloop()   
salespayments()    