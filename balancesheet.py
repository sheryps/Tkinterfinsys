import tkinter as tk
from tkinter import ttk
from tkinter import *
import zlib
import matplotlib.figure
import matplotlib.patches
from datetime import datetime, date, timedelta
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from tkcalendar import DateEntry
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cursor=mydata.cursor()
#cc
def balancesheet():
    prlframe=tk.Tk()
    prlframe.title('Balance Sheet')
    prlframe.geometry('1500x1000')
    #dash['bg'] = '#2f516f'
    cid=2
    mycanvas=tk.Canvas(prlframe,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(prlframe,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    profitlossframe=tk.Frame(mycanvas)
    profitlossframe['bg']='#2f516f'
    mycanvas.create_window((0,0),window=profitlossframe,anchor='nw',width=1500,height=2200)

    pframe=tk.Frame(profitlossframe,bg='#243e54')
    tk.Label(pframe,text='BALANCE SHEET',font=('Times New Roman',26),bg='#243e54').place(relx=0.4,rely=0.05)
    pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

    form_frame=tk.Frame(profitlossframe,bg='#243e54')
    def menu1(e):
        global dte,dtee,fromdate,todate
        toda = date.today()
        tod = toda.strftime("%Y-%m-%d")
        dropp=drop.get()   
        if dropp=='Custom':            
            tk.Label(form_frame,text='From',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.45,rely=0.1)
            dte=StringVar()
            DateEntry(form_frame,textvariable=dte,date_pattern='y-mm-dd').place(relx=0.45,rely=0.23,relwidth=0.2,relheight=0.15)
            tk.Label(form_frame,text='To',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.70,rely=0.1)
            dtee=StringVar()
            DateEntry(form_frame,textvariable=dtee,date_pattern='y-mm-dd').place(relx=0.70,rely=0.23,relwidth=0.2,relheight=0.15)
        elif dropp=='Today':
            fromdate = tod
            todate = tod 
        elif dropp=='This month':
            fromdate = toda.strftime("%Y-%m-01")
            todate = toda.strftime("%Y-%m-31")
        elif dropp=='This financial year':
            if int(toda.strftime("%m")) >= 1 and int(toda.strftime("%m")) <= 3:
                pyear = int(toda.strftime("%Y")) - 1
                fromdate = f'{pyear}-03-01'
                todate = f'{toda.strftime("%Y")}-03-31'
            else:
                pyear = int(toda.strftime("%Y")) + 1
                fromdate = f'{toda.strftime("%Y")}-03-01'
                todate = f'{pyear}-03-31'  
    def balancefetch():
        period=drop.get()
        if period=='All dates':
            allbalancevalues() 
        elif period=='Today':
            contframe.destroy()
            filterbalancevalues() 
        elif period=='Custom':
            global fromdate,todate
            fromdate=dte.get()
            todate=dtee.get()
            contframe.destroy()
            filterbalancevalues()
        elif period=='This month':
            contframe.destroy()
            filterbalancevalues() 
        elif period=='This financial year':
            contframe.destroy()
            filterbalancevalues()  
    def back():
        allbalancevalues()            

    tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
    options=["All dates", "Custom","Today","This month","This financial year"]
    drop= ttk.Combobox(form_frame,values=options,font=16)
    drop.current(0)
    drop.bind('<<ComboboxSelected>>',menu1)
    drop.place(relx=0.05,rely=0.23,relwidth=0.3,relheight=0.15)
     #buttons
    tk.Button(form_frame,text = "Run Report",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command=balancefetch).place(relx=0.55,rely=0.5,relwidth=0.15)
    tk.Button(form_frame,text = "Back",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold')).place(relx=0.75,rely=0.5,relwidth=0.15)
    form_frame.place(relx=0.1,rely=0.08,relwidth=0.8,relheight=0.1)

    tableframe=tk.Frame(profitlossframe,bg='#243e54')
    #image
    imageframe=tk.Frame(tableframe,bg='#add8e6')
    size=(200,200)
    cc='barath'
    cursor.execute("SELECT image,cname FROM company WHERE cname =%s and id =%s",([cc,cid]))
    image=cursor.fetchone()
    img=image[0]
    cv=Image.open(img).resize(size)
    ax=ImageTk.PhotoImage(cv,master=prlframe)
    ay=tk.Label(imageframe,image=ax,bg='#243e54')
    ay.place(relx=0.02,rely=0.08,relheight=0.8,relwidth=0.2)
    tk.Label(imageframe,text=image[1], font=('times new roman', 25, 'bold'),bg="#add8e6").place(relx=0.25,rely=0.4,relwidth=0.2)
    imageframe.place(relx=0.05,rely=0.02,relwidth=0.9,relheight=0.15)
    #contents
    conttframe=tk.Frame(tableframe,bg='white')
    conttframe.place(relx=0.05,rely=0.17,relwidth=0.9,relheight=0.7)
    mycanvass=tk.Canvas(conttframe,width=1200,height=1200)
    mycanvass.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(conttframe,orient='vertical',command=mycanvass.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvass.configure(yscrollcommand=yscrollbar.set)
    mycanvass.bind('<Configure>',lambda e:mycanvass.configure(scrollregion=mycanvass.bbox('all')))
    contframe=tk.Frame(mycanvass)
    contframe['bg']='white'
    mycanvass.create_window((0,0),window=contframe,anchor='nw',width=1100,height=1200)
    set = ttk.Treeview(contframe,height=0)
    set.place(relx=0,rely=0,relwidth=1)

    set['columns']= ('CUSTOMER NAME','TOTAL')
    set.column("#0", width=0,  stretch=NO)
    set.column("CUSTOMER NAME",width=750,anchor=CENTER )
    set.column("TOTAL",width=198,anchor=CENTER)


    #set.heading("#0",text="",anchor=CENTER)
    set.heading("CUSTOMER NAME",text="",anchor=CENTER )
    set.heading("TOTAL",text="TOTAL",anchor=CENTER)

    tk.Label(contframe,text = "Assets",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.04)
    tk.Label(contframe,text = " Current Assets",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=0.08)
    def allbalancevalues():        #current assets database values
        def currentassets():
            global x,tott1,tott2
            current='Current Assets'
            x=0.12   
            tott1=0.0
            try:
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                        tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                        tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                        x=x+0.04
                        tott1=tott1+i[1]
            except:
                pass            

            try:
                tott2=0.0
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                    x=x+0.04
                    tott2=tott2+i[1]
            except:  
                pass
            tk.Label(contframe,text = "Bank",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
        currentassets()    
        tk.Label(contframe,text = " Account Receivable(Debtors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x+0.04)
        def AccountReceivable():
            global y
            current='Account Receivable(Debtors)'
            y=x+0.08  
            try:
                tott3=0.0
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=y)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                    y=y+0.04
                    tott3=tott3+i[1]
            except:  
                pass
            try:
                tott4=0.0
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=y)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                    y=y+0.04
                    tott4=tott4+i[1]
            except:  
                pass
            taccountsreceivable = tott3 + tott4
            tcurrentassets = tott1 + tott2 + taccountsreceivable
            tk.Label(contframe,text = " Total Account Receivable(Debtors)",bg="grey",font=('times new roman', 14)).place(relx=0.08,rely=y)
            tk.Label(contframe,text = taccountsreceivable,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y)
            tk.Label(contframe,text = " Total Current Assets",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=y+0.04)
            tk.Label(contframe,text = tcurrentassets,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.04)
            tk.Label(contframe,text = " Total Assets",bg="grey",font=('times new roman', 14)).place(relx=0.04,rely=y+0.08)
            tk.Label(contframe,text = tcurrentassets,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.08)
        AccountReceivable() 
        tk.Label(contframe,text = " Liabilities and Equity",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=y+0.12) 
        tk.Label(contframe,text = " Current Liabilities",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=y+0.16)    
        def currentLiabilities():
            global z,tliabilities
            current='Current Liabilities'
            z=y+0.20  
            try:
                tott5=0.0
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=z)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=z)
                    z=z+0.04
                    tott5=tott5+i[1]
            except:  
                pass
            try:
                tott6=0.0
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=z)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=z)
                    z=z+0.04
                    tott6=tott6+i[1]
            except:  
                pass
            tliabilities=tott5+tott6

        currentLiabilities()
        tk.Label(contframe,text = " Accounts Payable(Creditors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=z)
        def Accounts_Payable_creditors():
            global v,taccountspayable
            current='Accounts Payable(Creditors)'
            v=z+0.04 
            try:
                tott7=0.0
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=v)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=v)
                    v=v+0.04
                    tott7=tott7+i[1]
            except:  
                pass
            try:
                tott8=0.0
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=v)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=v)
                    v=v+0.04
                    tott8=tott8+i[1]
            except:  
                pass
            taccountspayable =  tott8 +  tott7
        Accounts_Payable_creditors()
        tcurrentliabilties =  tliabilities + taccountspayable
        tk.Label(contframe,text = " Total Accounts Payable(Creditors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=v)
        tk.Label(contframe,text = taccountspayable,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=v)
        tk.Label(contframe,text = " Total Current Liabilities",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=v+0.04)
        tk.Label(contframe,text = tcurrentliabilties,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=v+0.04)
        tk.Label(contframe,text = " Equity",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=v+0.08)
        def equity():
            global equityy
            w=v+0.12
            current='Equity'
            try:
                tott9=0.0
                cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=w)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=w)
                    w=w+0.04
                    tott9=tott9+i[1]
            except:  
                pass
            try:
                tott10=0.0
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([current,cid]))
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.12,rely=w)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=w)
                    w=w+0.04
                    tott10=tott10+i[1]
            except:  
                pass
            equityy=tott9+tott10
            def getothervalues():
                global proandloss
                totincome=0.0
                nme='Income'
                try:
                    cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([nme,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        totincome=totincome+i[0]
                except:  
                    pass
                try:
                    cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",([nme,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        totincome=totincome+i[0]
                except:  
                    pass
                namee='Cost of Goods Sold'
                costsold=0.0
                try:
                    cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([namee,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        costsold=costsold+i[0]
                except:  
                    pass
                try:
                    cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([namee,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        costsold=costsold+i[0]
                except:  
                    pass
                nameee='Other Income'
                otherincome=0.0
                try:
                    cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([nameee,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        otherincome=otherincome+i[0]
                except:  
                    pass
                try:
                    cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([nameee,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        otherincome=otherincome+i[0]
                except:  
                    pass
                nameee1='Expenses'
                expenses=0.0
                try:
                    cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([nameee1,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        expenses=expenses+i[0]
                except:  
                    pass
                try:
                    cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([nameee1,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        expenses=expenses+i[0]
                except:  
                    pass
                name1='Other Expenses'
                otherexpenses=0.0
                try:
                    cursor.execute("SELECT balance FROM accounts1 WHERE acctype =%s and cid =%s",([name1,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        otherexpenses=otherexpenses+i[0]
                except:  
                    pass
                try:
                    cursor.execute("SELECT balance FROM accounts WHERE acctype =%s and cid =%s",([name1,cid]))
                    val=cursor.fetchall()
                    for i in val:
                        otherexpenses=otherexpenses+i[0]
                except:  
                    pass
                proandloss = ((totincome - costsold) + otherincome) - (expenses + otherexpenses)
                tk.Label(contframe,text = " Profit for the Year",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=w)  
                tk.Label(contframe,text =proandloss,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=w)
            getothervalues()           
            tk.Label(contframe,text = " Total Equity",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=w+0.04)
            totequity = equityy + proandloss
            tk.Label(contframe,text =totequity,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=w+0.04)
            tk.Label(contframe,text = " Total Liabilities and Equity",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=w+0.08)
            tlande = tcurrentliabilties + totequity
            tk.Label(contframe,text =tlande,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=w+0.08)       
        equity() 
    allbalancevalues()
    def filterbalancevalues():
        global contframe1
        totalnoincome=0.0
        lis=[]
        totalinventincome=0.0
        totalinventasset=0.0
        totalnonexpence=0.0
        totalinventexpence=0.0
        conttframe1=tk.Frame(tableframe,bg='white')
        conttframe1.place(relx=0.05,rely=0.17,relwidth=0.9,relheight=0.7)
        mycanvass1=tk.Canvas(conttframe1,width=1200,height=1200)
        mycanvass1.place(relx=0,rely=0,relwidth=1,relheight=1)
        yscrollbar =ttk.Scrollbar(conttframe1,orient='vertical',command=mycanvass1.yview)
        yscrollbar.pack(side=RIGHT,fill=Y)
        mycanvass1.configure(yscrollcommand=yscrollbar.set)
        mycanvass1.bind('<Configure>',lambda e:mycanvass1.configure(scrollregion=mycanvass1.bbox('all')))
        contframe1=tk.Frame(mycanvass1)
        contframe1['bg']='white'
        mycanvass1.create_window((0,0),window=contframe1,anchor='nw',width=1100,height=1200)
        set = ttk.Treeview(contframe1,height=0)
        set.place(relx=0,rely=0,relwidth=1)
        set = ttk.Treeview(contframe1,height=0)
        set.place(relx=0,rely=0,relwidth=1)
        

        set['columns']= ('CUSTOMER NAME','TOTAL')
        set.column("#0", width=0,  stretch=NO)
        set.column("CUSTOMER NAME",width=820,anchor=CENTER )
        set.column("TOTAL",width=198,anchor=CENTER)


        #set.heading("#0",text="",anchor=CENTER)
        set.heading("CUSTOMER NAME",text="",anchor=CENTER )
        set.heading("TOTAL",text="TOTAL",anchor=CENTER) 
            # Account Receivable(Debtors)
        try:
            cursor.execute("SELECT * FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ])
            invoi=cursor.fetchall()
            totalardebtors = 0.0
            for i in invoi:
                    totalardebtors += float(i[16])        
            cursor.execute("SELECT * FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            creditnote=cursor.fetchall()
            for i in creditnote:
                    totalardebtors -= float(i[17])

            cursor.execute("SELECT * FROM payment WHERE paymdate between %s and %s and cid =%s" ,[fromdate, todate,cid ])
            paymen=cursor.fetchall()
            for i in paymen:
                    totalardebtors -= float(i[15])
        except:
            pass              
         # Accounts Payable(Creditors)
        try:
            totalapcreditors = 0.0
            paynot='openbalance'
            cursor.execute("SELECT * FROM bills WHERE paymdate between %s and %s and payornot =%s and cid =%s",[fromdate, todate,paynot,cid ])
            bill=cursor.fetchall()
            for b in bill:
                    totalapcreditors = totalapcreditors + float(b[58])
            cursor.execute("SELECT * FROM bills WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            bill2=cursor.fetchall()
            for b in bill2:
                if b[59] != 'openbalance' and b[59] != 'debit':
                    totalapcreditors = totalapcreditors - float(b[58])
            cursor.execute("SELECT * FROM suplrcredit WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            debit=cursor.fetchall()
            for b in debit:
                    totalapcreditors = totalapcreditors - float(b[56])
            cursor.execute("SELECT * FROM expenses WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            expence=cursor.fetchall()
            for b in expence:
                    totalapcreditors = totalapcreditors + float(b[57])
        except:
            pass            

        currentliability = [] 
        # Input CGST
        try:
            totalinpcgst = 0.0
            cursor.execute("SELECT taxamount FROM suplrcredit WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            deb=cursor.fetchall()
            for i in deb:
                    name = i[2]
                    x = name.split()
                    if len(x) == 3:
                        firstname = x[0]
                        lastname = x[1] + ' ' + x[2]
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[firstname,lastname,cid])
                        supp=cursor.fetchone()
                    else:
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[x[0],x[1],cid])
                        supp=cursor.fetchone()
                    cursor.execute("SELECT state FROM company WHERE id =%s",[cid])  
                    comp=cursor.fetchone() 
                    if supp[2]== comp[0]:
                        totalinpcgst += float(i[0]) / 2
            cursor.execute("SELECT taxamount FROM expenses WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            expen=cursor.fetchall()
            for i in expen:
                    name = i[2]
                    x = name.split()
                    if len(x) == 3:
                        firstname = x[0]
                        lastname = x[1] + ' ' + x[2]
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[firstname,lastname,cid])
                        supp=cursor.fetchone()
                    else:
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[x[0],x[1],cid])
                        supp=cursor.fetchone()
                    if supp[2]== comp[0]:
                        totalinpcgst -= float(i[0]) / 2
        except:
            pass                
        currentliability.append(['Input CGST', totalinpcgst])
        # Input SGST

        totalinpsgst = 0.0
        try:
            cursor.execute("SELECT taxamount FROM suplrcredit WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            deb=cursor.fetchall()
            for i in deb:
                    name = i[2]
                    x = name.split()
                    if len(x) == 3:
                        firstname = x[0]
                        lastname = x[1] + ' ' + x[2]
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[firstname,lastname,cid])
                        supp=cursor.fetchone()
                    else:
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[x[0],x[1],cid])
                        supp=cursor.fetchone()
                    if supp[2]== comp[0]:
                        totalinpsgst += float(i[0]) / 2
            cursor.execute("SELECT taxamount FROM expenses WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            expen=cursor.fetchall()
            for i in expen:
                    name = i[2]
                    x = name.split()
                    if len(x) == 3:
                        firstname = x[0]
                        lastname = x[1] + ' ' + x[2]
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[firstname,lastname,cid])
                        supp=cursor.fetchone()
                    else:
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[x[0],x[1],cid])
                        supp=cursor.fetchone()
                    if supp[2]== comp[0]:
                        totalinpsgst -= float(i[0]) / 2
        except:
            pass                          

        currentliability.append(['Input SGST', totalinpsgst])
        # Input IGST
        try:
            totalinpigst = 0.0
            cursor.execute("SELECT taxamount FROM suplrcredit WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            deb=cursor.fetchall()
            for i in deb:
                    name = i[2]
                    x = name.split()
                    if len(x) == 3:
                        firstname = x[0]
                        lastname = x[1] + ' ' + x[2]
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[firstname,lastname,cid])
                        supp=cursor.fetchone()
                    else:
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[x[0],x[1],cid])
                        supp=cursor.fetchone()
                    if supp[2]!= comp[0]:
                        totalinpigst -= float(i[0]) / 2
            cursor.execute("SELECT taxamount FROM expenses WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            expen=cursor.fetchall()
            for i in expen:
                    name = i[2]
                    x = name.split()
                    if len(x) == 3:
                        firstname = x[0]
                        lastname = x[1] + ' ' + x[2]
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[firstname,lastname,cid])
                        supp=cursor.fetchone()
                    else:
                        cursor.execute("SELECT firstname,lastname,state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s",[x[0],x[1],cid])
                        supp=cursor.fetchone()
                    if supp[2]!= comp[0]:
                        totalinpigst += float(i[0]) / 2
        except:
            pass                
        currentliability.append(['Input IGST', totalinpigst])

        # Output CGST
        try:
            totaloutcgst = 0.0
            cursor.execute("SELECT taxamount FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ])
            invoi=cursor.fetchall()
            for i in invoi:
                    if i[7] == comp[0]:
                        totaloutcgst += float(i[0]) / 2
            cursor.execute("SELECT taxamnt FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            creditnote=cursor.fetchall()  
            for i in creditnote:
                    if i[7] == comp[0]:
                        totaloutcgst -= float(i[0]) / 2
            cursor.execute("SELECT saletaxamount FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
            sales=cursor.fetchall()
            for i in sales:
                    if i[7] == comp[0]:
                        totaloutcgst += float(i[0]) / 2  
        except:
            pass                     
        currentliability.append(['Output CGST', totaloutcgst])  

        # Output SGST
        try:
            totaloutsgst = 0.0
            cursor.execute("SELECT taxamount FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ])
            invoi=cursor.fetchall()
            for i in invoi:
                    if i[7] == comp[0]:
                        totaloutsgst += float(i[0]) / 2
            cursor.execute("SELECT taxamnt FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            creditnote=cursor.fetchall()  
            for i in creditnote:
                    if i[7] == comp[0]:
                        totaloutsgst -= float(i[0]) / 2
            cursor.execute("SELECT saletaxamount FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
            sales=cursor.fetchall()
            for i in sales:
                    if i[7] == comp[0]:
                        totaloutsgst += float(i[0]) / 2 
        except:
            pass                      
        currentliability.append(['Output SGST', totaloutsgst])  

        # Output IGST
        try:
            totaloutigst = 0.0
            cursor.execute("SELECT taxamount FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ])
            invoi=cursor.fetchall()
            for i in invoi:
                    if i[7] != comp[0]:
                        totaloutigst += float(i[0]) / 2
            cursor.execute("SELECT taxamnt FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            creditnote=cursor.fetchall()  
            for i in creditnote:
                    if i[7] != comp[0]:
                        totaloutigst -= float(i[0]) / 2
            cursor.execute("SELECT saletaxamount FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
            sales=cursor.fetchall()
            for i in sales:
                    if i[7] != comp[0]:
                        totaloutigst += float(i[0]) / 2
        except:
            pass                       
        currentliability.append(['Output IGST', totaloutigst])   

        # Opening Balance Equity
        try:
            totalobe = 0.0   
            cursor.execute("SELECT cxq FROM inventory WHERE date between %s and %s and cid =%s",[fromdate, todate,cid ])
            inventori=cursor.fetchall()  
            for inv in inventori:
                totalobe += float(inv[0])
            cursor.execute("SELECT balfordisp FROM accounts WHERE asof between %s and %s and cid =%s",[fromdate, todate,cid ])
            accont=cursor.fetchall()   
            for a in accont:
                totalobe += float(a[0])  
        except:
            pass        

                # Ask My Accountant

        totalama = 0.0  
        payornot = 'openbalance' 
        try:
            cursor.execute("SELECT grandtotal FROM bills WHERE payornot =%s and paymdate between %s and %s and cid =%s",[payornot,fromdate, todate,cid ])
            bill=cursor.fetchall()
            for i in bill:
                    totalama =float(i[0])+totalama 
        except:
            pass   
        acclis = [] 
        acctype='Current Assets'
        try:
            cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",[acctype,cid ])
            acc=cursor.fetchall()
            for i in acc:
                if i[1] != 0.0:
                    acclis.append(i[0])
        except:
            pass                
        try:
            cursor.execute("SELECT name,cost FROM inventory WHERE cid =%s",([cid]))
            inventor=cursor.fetchall()
            inventor1 = []
            for i in inventor:
                inventor1.append([i[0], i[1]])    
        except:
            pass 
        try:
            cursor.execute("SELECT * FROM bundle WHERE cid =%s",([cid]))
            bundl=cursor.fetchall()
            bundles = []
            bundlpro = []
            bundlqty = []
            bundlprice = [] 
            for i in bundl:
                bundles.append(i[3])
                bundlpro.append([i[6], i[7], i[8], i[9]])
                bundlqty.append([i[18], i[19], i[20], i[21]])
                bundlprice.append([i[22], i[23], i[24], i[25]])
        except:
            pass        
        try:
            for i in acclis: 
            #inventory name value
                cursor.execute("SELECT invacnt FROM inventory WHERE invacnt =%s and cid =%s",[i,cid])
                inventor=cursor.fetchall()  
                cursor.execute("SELECT invacnt,cxq FROM inventory WHERE cid =%s",([cid]))
                invento=cursor.fetchall()
                totalinventasset=0.0
                for i in invento:
                    if i[0] == inventor[0]:
                        totalinventasset += i[1]
                cursor.execute("SELECT * FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ]) 
                invoc=cursor.fetchall()    
                for i in invoc:
                    for j in inventor1:
                        try:
                            if i[8] == j[0]:
                                totalcost = round(float(j[1]) * float(i[11]), 2)
                                totalinventasset -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",[i[13],cid])
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[8] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[11]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[11]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[11]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[11]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass                
                        except:
                            pass 
                        try:
                            if i[17] == j[0]:
                                totalcost = round(float(j[1]) * float(i[20]), 2)
                                totalinventasset -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[17],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[17] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[20]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[20]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[20]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[20]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                        except:
                            pass
                        try:
                            if i[24] == j[0]:
                                totalcost = round(float(j[1]) * float(i[27]), 2)
                                totalinventasset -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[24],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[24] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[27]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[27]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float([1]) * float(i[27]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[27]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                        except:
                            pass
                        try:
                            if i[31] == j[0]:
                                totalcost = round(float(j[1]) * float(i[34]), 2)
                                totalinventexpense -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[31] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[34]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[34]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[34]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[34]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass

                        except:
                            pass
                cursor.execute("SELECT * FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
                creditnot=cursor.fetchall()
                for i in creditnot:
                    for j in inventor1:
                            try:
                                if i[10] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[12]), 2)
                                    totalinventasset += totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                                xx=cursor.fetchall()                          
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[10] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[12]) * float(bq[0]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[12]) * float(bq[1]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[12]) * float(bq[2]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[12]) * float(bq[3]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                            except:
                                pass 
                            try:
                                if i[19] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[21]), 2)
                                    ttotalinventasset += totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[19],cid])   
                                xx=cursor.fetchall()
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[19] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[21]) * float(bq[0]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[21]) * float(bq[1]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[21]) * float(bq[2]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[21]) * float(bq[3]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                            except:
                                pass
                            try:
                                if i[25] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[27]), 2)
                                    totalinventasset += totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[25],cid])   
                                xx=cursor.fetchall()
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[25] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[27]) * float(bq[0]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[27]) * float(bq[1]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[27]) * float(bq[2]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[27]) * float(bq[3]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                            except:
                                pass
                            try:
                                if i[31] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[33]), 2)
                                    totalinventasset += totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                                xx=cursor.fetchall()
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[31] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[33]) * float(bq[0]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[33]) * float(bq[1]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[33]) * float(bq[2]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[33]) * float(bq[3]), 2)
                                                    totalinventasset += totalcost
                                            except:
                                                pass  
                            except:
                                pass                                              
                cursor.execute("SELECT * FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
                salesrecept=cursor.fetchall()
                for i in salesrecept:
                    for j in inventor1:
                            try:
                                if i[11] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[13]), 2)
                                    totalinventasset -= totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                                xx=cursor.fetchall()
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[11] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[13]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[13]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[13]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[13]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                            except:
                                pass
                            try:
                                if i[20] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[23]), 2)
                                    totalinventasset -= totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[20],cid])   
                                xx=cursor.fetchall()
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[20] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[23]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[23]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[23]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[23]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                            except:
                                pass
                            try:
                                if i[27] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[30]), 2)
                                    totalinventasset -= totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[27],cid])   
                                xx=cursor.fetchall()
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[27] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[30]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[30]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[30]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[30]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                            except:
                                pass
                            try:
                                if i[34] == j[0]:
                                    totalcost = round(float(j[1]) * float(i[37]), 2)
                                    totalinventasset -= totalcost
                                cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[34],cid])   
                                xx=cursor.fetchall()
                                if xx:
                                    for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                        if i[34] == b:
                                            try:
                                                if j[0] == bp[0]:
                                                    totalcost = round(float(j[1]) * float(i[37]) * float(bq[0]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[1]:
                                                    totalcost = round(float(j[1]) * float(i[37]) * float(bq[1]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[2]:
                                                    totalcost = round(float(j[1]) * float(i[37]) * float(bq[2]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                                            try:
                                                if j[0] == bp[3]:
                                                    totalcost = round(float(j[1]) * float(i[37]) * float(bq[3]), 2)
                                                    totalinventasset -= totalcost
                                            except:
                                                pass
                            except:
                                pass
                cursor.execute("SELECT * FROM expenses WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
                expen=cursor.fetchall()
                for i in expen:
                    for j in inventor1:
                            try:
                                if i[27] == j:
                                    totalcost = round(float(i[31]) * float(i[30]), 2)
                                    totalinventasset += totalcost
                            except:
                                pass
                            try:
                                if i[33] == j:
                                    totalcost = round(float(i[37]) * float(i[36]), 2)
                                    totalinventasset += totalcost
                            except:
                                pass
                            try:
                                if i[39] == j:
                                    totalcost = round(float(i[43]) * float(i[42]), 2)
                                    totalinventasset += totalcost
                            except:
                                pass
                            try:
                                if i[45] == j:
                                    totalcost = round(float(i[49]) * float(i[48]), 2)
                                    totalinventasset += totalcost
                            except:
                                pass
                cursor.execute("SELECT * FROM suplrcredit WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
                debi=cursor.fetchall()            
                for i in debi:
                    for j in inventor1:
                            try:
                                if i[26] == j:
                                    totalcost = round(float(i[30]) * float(i[29]), 2)
                                    totalinventasset -= totalcost
                            except:
                                pass
                            try:
                                if i[32] == j:
                                    totalcost = round(float(i[36]) * float(i[35]), 2)
                                    totalinventasset -= totalcost
                            except:
                                pass
                            try:
                                if i[38] == j:
                                    totalcost = round(float(i[42]) * float(i[41]), 2)
                                    totalinventasset -= totalcost
                            except:
                                pass
                            try:
                                if i[44] == j:
                                    totalcost = round(float(i[48]) * float(i[47]), 2)
                                    totalinventasset -= totalcost
                            except:
                                pass                     
        except:
            pass
        try:#inventory name value
            cursor.execute("SELECT * FROM inventory WHERE cid =%s",([cid]))
            invento=cursor.fetchall()
            inventor = []
            for i in invento:
                        inventor.append(i[3])         
            cursor.execute("SELECT * FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ]) 
            invoc=cursor.fetchall() 
            for i in invoc:
                for j in inventor:
                    try:
                        if i[8] == j:
                            totalinventincome += float(i[15]) 
                        cursor.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",[i[13],cid])
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[8] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[11]) * float(bq[0]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[11]) * float(bq[1]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[11]) * float(bq[2]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[11]) * float(bq[3]), 2)
                                                totalinventincome += totalcost
                                        except:
                                           pass                
                    except:
                        pass 
                    try:
                        if i[17] == j:
                            totalinventincome += float(i[22])
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[17],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[17] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[20]) * float(bq[0]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[20]) * float(bq[1]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[20]) * float(bq[2]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[20]) * float(bq[3]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                    except:
                        pass
                    try:
                        if i[24] == j:
                            totalinventincome += float(i[29])
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[24],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[24] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[27]) * float(bq[0]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[27]) * float(bq[1]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[27]) * float(bq[2]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[27]) * float(bq[3]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                    except:
                        pass
                    try:
                        if i[31] == j:
                            totalinventincome += float(i[35])
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[31] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[34]) * float(bq[0]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[34]) * float(bq[1]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[34]) * float(bq[2]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[34]) * float(bq[3]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass

                    except:
                        pass  
            cursor.execute("SELECT * FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            creditnot=cursor.fetchall()
            for i in creditnot:
                for j in inventor:
                        try:
                            if i[10] == j:
                                totalinventincome -= float(i[16])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                            xx=cursor.fetchall()                          
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[10] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[12]) * float(bq[0]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[12]) * float(bq[1]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[12]) * float(bq[2]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[12]) * float(bq[3]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass 
                        try:
                            if i[19] == j:
                                totalinventincome += float(i[24])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[19],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[19] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[21]) * float(bq[0]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[21]) * float(bq[1]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[21]) * float(bq[2]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[21]) * float(bq[3]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[25] == j:
                                totalinventincome += float(i[30])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[25],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[25] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[27]) * float(bq[0]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[27]) * float(bq[1]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[27]) * float(bq[2]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[27]) * float(bq[3]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[31] == j:
                                totalinventincome += float(i[35])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[31] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[33]) * float(bq[0]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[33]) * float(bq[1]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[33]) * float(bq[2]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[33]) * float(bq[3]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass                                   
            cursor.execute("SELECT * FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
            salesrecept=cursor.fetchall()
            for i in salesrecept:
                for j in inventor:
                        try:
                            if i[11] == j:
                                totalinventincome += float(i[15])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[11] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[13]) * float(bq[0]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[13]) * float(bq[1]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[13]) * float(bq[2]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[13]) * float(bq[3]), 2)
                                                totalinventincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[20] == j:
                                totalinventincome += float(i[25])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[20],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[20] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[23]) * float(bq[0]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[23]) * float(bq[1]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[23]) * float(bq[2]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[23]) * float(bq[3]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[27] == j:
                                totalinventincome += float(i[32])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[27],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[27] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[30]) * float(bq[0]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[30]) * float(bq[1]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[30]) * float(bq[2]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[30]) * float(bq[3]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[34] == j:
                                totalinventincome += float(i[39])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[34],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[34] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[37]) * float(bq[0]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[37]) * float(bq[1]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[37]) * float(bq[2]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[37]) * float(bq[3]), 2)
                                                totalinventincome += totalcost
                                        except:
                                            pass
                        except:
                            pass     
                lis = []
                try:
                    totalsaledeposit = 0.0
                    cursor.execute("SELECT saledeposit,salegrandtotal FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
                    salesrecept=cursor.fetchall()
                    print(salesrecept)
                    for s in salesrecept:
                            lis.append([s[0], s[1]])
                            totalsaledeposit += float(s[1])
                except:
                    pass 
                try:
                    totalpaydeposit = 0.0
                    cursor.execute("SELECT depto,amtapply FROM payment WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
                    payment1=cursor.fetchall()
                    print(payment1)
                    for s in payment1:
                            lis.append([s[0], s[1]])
                            totalpaydeposit += float(s[1])
                except:
                    pass 
                try:
                    totalbilldeposit = 0.0
                    cursor.execute("SELECT paymacnt,grandtotal,payornot FROM bills WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
                    bills1=cursor.fetchall()
                    for s in bills1:
                        if s[2]!='openbalance':
                            lis.append([s[0],0- s[1]])
                            totalbilldeposit -= float(s[1])
                except:
                    pass 
        except:
            pass           
        banktot = 0.0
        currenttot = 0.0
        currentlist = []
        for i in lis:
            try:
                if i[0] in acclis:
                    currentlist.append([i[0], i[1]])
                    currenttot += float(i[1])
            except:
                pass
            try:
                if i[0] not in acclis:
                    banktot += float(i[1])
            except:
                pass   
        currentlist.append(['Inventory Asset', str(totalinventasset)])  
        try:  
            cursor.execute("SELECT acctype,balfordisp FROM accounts WHERE asof between %s and %s and cid =%s",[fromdate, todate,cid ])
            accounts=cursor.fetchall() 
            for i in accounts:
                if i[0]=='3':
                    banktot += float(i[1])
        except:
            pass 
        currentliable = currentliability
        currentasset = currentlist
        asset = banktot + currenttot + \
            totalinventasset + totalardebtors

        proandloss = ((totalinventincome + totalnoincome) -totalinventexpence) - (totalnonexpence + totalama)
        equity = proandloss + totalobe
        totcliability = 0.0
        for i in currentliability:
            totcliability += float(i[1])
        totcurliability = totcliability + totalapcreditors
        totliability = totcliability + (totalapcreditors + proandloss + totalobe)
   
        tk.Label(contframe1,text = "Assets",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.04)
        tk.Label(contframe1,text = " Current Assets",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=0.08)
        x=0.12
        for i in currentasset:
            if i[1]!=0.0:
                tk.Label(contframe1,text =i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=x)
                tk.Label(contframe1,text = i[1],bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x)
                x=x+0.04
        tk.Label(contframe1,text = " Bank",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
        tk.Label(contframe1,text = banktot,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x)        
        tk.Label(contframe1,text = " Account Receivable(Debtors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x+0.04)
        tk.Label(contframe1,text = totalardebtors,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x+0.04)
        tk.Label(contframe1,text = " Total Account Receivable(Debtors)",bg="grey",font=('times new roman', 14)).place(relx=0.08,rely=x+0.08)
        tk.Label(contframe1,text =totalardebtors,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x+0.08)
        tk.Label(contframe1,text = " Total Current Assets",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=x+0.12)
        tk.Label(contframe1,text = asset,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x+0.12)
        tk.Label(contframe1,text = " Total Assets",bg="grey",font=('times new roman', 14)).place(relx=0.04,rely=x+0.16)
        tk.Label(contframe1,text = asset,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x+0.16)
        tk.Label(contframe1,text = " Liabilities and Equity",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=x+0.2) 
        tk.Label(contframe1,text = " Current Liabilities",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=x+0.24)
        y=x+0.28
        for i in currentliable:
            if i[1]!=0.0:
                tk.Label(contframe1,text =i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=y)
                tk.Label(contframe1,text = i[1],bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y)
                y=y+0.04
        tk.Label(contframe1,text = " Accounts Payable(Creditors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=y)
        tk.Label(contframe1,text = totalapcreditors,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y)
        tk.Label(contframe1,text = " Total Accounts Payable(Creditors)",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.1,rely=y+0.04)
        tk.Label(contframe1,text = totalapcreditors,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.04)
        tk.Label(contframe1,text = " Total Current Liabilities",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=y+0.08)
        tk.Label(contframe1,text = totcurliability,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.08)
        tk.Label(contframe1,text = " Equity",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=y+0.12)
        tk.Label(contframe1,text = " Profit for the Year",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=y+0.16)  
        tk.Label(contframe1,text =proandloss,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.16)
        tk.Label(contframe1,text = " Total Equity",bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.06,rely=y+0.2)
        tk.Label(contframe1,text =equity,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.2)
        tk.Label(contframe1,text = " Total Liabilities and Equity",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=y+0.24)
        tk.Label(contframe1,text =totliability,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y+0.24) 



    tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
   
   
    prlframe.mainloop()
balancesheet()   