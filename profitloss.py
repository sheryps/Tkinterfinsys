import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from turtle import clear
from wsgiref.validate import validator
import matplotlib.figure
import matplotlib.patches
from tkcalendar import DateEntry
from datetime import datetime, date, timedelta
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import xcorr, yscale
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinterr')
cursor=mydata.cursor()
#cc
def profitloss():
    prlframe=tk.Tk()
    prlframe.title('Profit Loss')
    prlframe.geometry('1500x1000')
    cid=2
    #dash['bg'] = '#2f516f'
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
    tk.Label(pframe,text='PROFIT AND LOSS',font=('Times New Roman',26),bg='#243e54').place(relx=0.4,rely=0.05)
    pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

    form_frame=tk.Frame(profitlossframe,bg='#243e54')

    def menu(e):
        global dte,dtee,fromdate,todate
        toda = date.today()
        tod = toda.strftime("%Y-%m-%d")
        dropp=drop.get()
        if dropp=='Custom':            
            tk.Label(form_frame,text='From',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.45,rely=0.1)
            dte=StringVar()
            DateEntry(form_frame,textvariable=dte).place(relx=0.45,rely=0.23,relwidth=0.2,relheight=0.15)
            tk.Label(form_frame,text='To',bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.70,rely=0.1)
            dtee=StringVar()
            DateEntry(form_frame,textvariable=dtee).place(relx=0.70,rely=0.23,relwidth=0.2,relheight=0.15)
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


    def accrecifetch():
        period=drop.get()
        if period=='All dates':
            alldates() 
        elif period=='Today':
           betweendates()
        elif period=='Custom':
            global fromdate,todate
            fromdate=dte.get()
            todate=dtee.get()
        #elif period=='This month':
            #betweendates()  
       # elif period=='This financial year':
           # betweendates()         
    tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
    options=["All dates", "Custom","Today","This month","This financial year"]
    drop= ttk.Combobox(form_frame,values=options,font=16)
    drop.current(0)
    drop.bind('<<ComboboxSelected>>',menu)
    drop.place(relx=0.05,rely=0.23,relwidth=0.3,relheight=0.15)
     #buttons
    tk.Button(form_frame,text = "Run Report",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command=accrecifetch).place(relx=0.55,rely=0.5,relwidth=0.15)
    tk.Button(form_frame,text = "Back",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold')).place(relx=0.75,rely=0.5,relwidth=0.15)
    form_frame.place(relx=0.1,rely=0.08,relwidth=0.8,relheight=0.1)

    tableframe=tk.Frame(profitlossframe,bg='#243e54')
    #image
    imageframe=tk.Frame(tableframe,bg='#add8e6')
    size=(200,200)
    cv=Image.open('timeact.png').resize(size)
    ax=ImageTk.PhotoImage(cv,master=prlframe)
    ay=tk.Label(imageframe,image=ax,bg='#243e54')
    ay.place(relx=0.02,rely=0.08,relheight=0.8,relwidth=0.2)

    cursor.execute("SELECT cname FROM company WHERE id =%s",([cid]))
    h=cursor.fetchone()
    tk.Label(imageframe,text=h[0], font=('times new roman', 25, 'bold'),bg="#add8e6").place(relx=0.25,rely=0.4,relwidth=0.2)
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
    set = ttk.Treeview(contframe,height=0)
    set.place(relx=0,rely=0,relwidth=1)
    

    set['columns']= ('CUSTOMER NAME','TOTAL')
    set.column("#0", width=0,  stretch=NO)
    set.column("CUSTOMER NAME",width=820,anchor=CENTER )
    set.column("TOTAL",width=198,anchor=CENTER)


    #set.heading("#0",text="",anchor=CENTER)
    set.heading("CUSTOMER NAME",text="",anchor=CENTER )
    set.heading("TOTAL",text="TOTAL",anchor=CENTER)
    def alldates():
        tk.Label(contframe,text = "Income",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.04)
        global x,totin
        x=0.08
        print(cid)
        totin=0.0
        nme='Income'
        #cursor.execute("SELECT * FROM accounts1 WHERE acctype =%s and cid =%s",([nme,cid]))
       # val=cursor.fetchall()
       # for i in val:
                      #  tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                      #  tk.Label(contframe,text = 0,bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                      #  x=x+0.04
                     #   totin=totin+i[1]   
        #cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",([nme,cid]))
       # val=cursor.fetchall()
       # for i in val:
                     #   tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=x)
                      #  tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=x)
                      #  x=x+0.04
                      #  totin=totin+i[1]
        tk.Label(contframe,text = " Total Income",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=x)
        tk.Label(contframe,text = totin,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=x)
        tk.Label(contframe,text = " Cost of Goods Sold ",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=x+0.04)
        def costofgoodsvalue():
            nmee='Cost of Goods Sold'
            global y,gros
            tot1=0.0
            y=x+0.08
            cursor.execute("SELECT name,balance FROM accounts1 WHERE acctype =%s and cid =%s",[nmee,cid])
            val=cursor.fetchone()
            for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=y)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                    y=y+0.04
                    tot1=tot1+i[1]
            try:
                cursor.execute("SELECT name,balance FROM accounts WHERE acctype =%s and cid =%s",[nmee,cid])
                val=cursor.fetchall()
                for i in val:
                    tk.Label(contframe,text=i[0],bg="#FFFFFF",font=('times new roman', 14)).place(relx=0.08,rely=y)
                    tk.Label(contframe,text = i[1],bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.86,rely=y)
                    y=y+0.04
                    tot1=tot1+i[1]
            except:  
                pass
            gros=totin-tot1
            tk.Label(contframe,text = " Gross Profit ",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=y)
            tk.Label(contframe,text = gros,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=y)
        costofgoodsvalue()
    def betweendates():
        totalinventincome =0.0
        totalnoincome=0.0
        totalinventexpense=0.0
        totalnonexpence = 0.0
        payornot = 'openbalance'
        totalama = 0.0
        cursor.execute("SELECT grandtotal FROM bills WHERE payornot =%s and paymdate between %s and %s and cid =%s",[payornot,fromdate, todate,cid ])
        bill=cursor.fetchall()
        for i in bill:
                totalama =float(i[0])+totalama   
        try:
            cursor.execute("SELECT * FROM inventory WHERE cid =%s",([cid]))
            inventor=cursor.fetchall()
            inventor1 = []
            for i in inventor:
                inventor1.append([i[3], i[17]])   
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
        except:
            pass 
        try:#noninventory name value
            cursor.execute("SELECT * FROM noninventory WHERE cid =%s",([cid]))
            noninvento=cursor.fetchall()
            noninventor = []
            for i in noninvento:
                        noninventor.append(i[3])    
            cursor.execute("SELECT * FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ]) 
            noninvoc=cursor.fetchall() 
            for i in noninvoc:
                for j in noninventor:
                    try:
                        if i[8] == j:
                            totalnoincome += float(i[15]) 
                        cursor.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",[i[13],cid])
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[8] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[11]) * float(bq[0]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[11]) * float(bq[1]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[11]) * float(bq[2]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[11]) * float(bq[3]), 2)
                                                totalnoincome += totalcost
                                        except:
                                           pass                
                    except:
                        pass 
                    try:
                        if i[17] == j:
                            totalnoincome += float(i[22])
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[17],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[17] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[20]) * float(bq[0]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[20]) * float(bq[1]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[20]) * float(bq[2]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[20]) * float(bq[3]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                    except:
                        pass
                    try:
                        if i[24] == j:
                            totalnoincome += float(i[29])
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[24],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[24] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[27]) * float(bq[0]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[27]) * float(bq[1]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[27]) * float(bq[2]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[27]) * float(bq[3]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                    except:
                        pass
                    try:
                        if i[31] == j:
                            totalnoincome += float(i[35])
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                if i[31] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[34]) * float(bq[0]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[34]) * float(bq[1]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[34]) * float(bq[2]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[34]) * float(bq[3]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass

                    except:
                        pass  
            cursor.execute("SELECT * FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            creditnot=cursor.fetchall()
            for i in creditnot:
                for j in noninventor:
                        try:
                            if i[10] == j:
                                totalnoincome -= float(i[16])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                            xx=cursor.fetchall()                          
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[10] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[12]) * float(bq[0]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[12]) * float(bq[1]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[12]) * float(bq[2]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[12]) * float(bq[3]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass 
                        try:
                            if i[19] == j:
                                totalnoincome += float(i[24])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[19],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[19] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[21]) * float(bq[0]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[21]) * float(bq[1]), 2)
                                                totalnoincome-= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[21]) * float(bq[2]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[21]) * float(bq[3]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[25] == j:
                                totalnoincome += float(i[30])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[25],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[25] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[27]) * float(bq[0]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[27]) * float(bq[1]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[27]) * float(bq[2]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[27]) * float(bq[3]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[31] == j:
                                totalnoincome += float(i[35])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[31] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[33]) * float(bq[0]), 2)
                                                totalnoincome-= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[33]) * float(bq[1]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[33]) * float(bq[2]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[33]) * float(bq[3]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass                                   
            cursor.execute("SELECT * FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
            salesrecept=cursor.fetchall()
            for i in salesrecept:
                for j in noninventor:
                        try:
                            if i[11] == j:
                                totalnoincome += float(i[15])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[11] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[13]) * float(bq[0]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[13]) * float(bq[1]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[13]) * float(bq[2]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[13]) * float(bq[3]), 2)
                                                totalnoincome -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[20] == j:
                                totalnoincome += float(i[25])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[20],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[20] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[23]) * float(bq[0]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[23]) * float(bq[1]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[23]) * float(bq[2]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[23]) * float(bq[3]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[27] == j:
                                totalnoincome += float(i[32])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[27],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[27] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[30]) * float(bq[0]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[30]) * float(bq[1]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[30]) * float(bq[2]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[30]) * float(bq[3]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[34] == j:
                                totalnoincome += float(i[39])
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[34],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq, bprice) in zip(bundles, bundlpro, bundlqty, bundlprice):
                                    if i[34] == b:
                                        try:
                                            if j == bp[0]:
                                                totalcost = round(float(bprice[0]) * float(i[37]) * float(bq[0]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[1]:
                                                totalcost = round(float(bprice[1]) * float(i[37]) * float(bq[1]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[2]:
                                                totalcost = round(float(bprice[2]) * float(i[37]) * float(bq[2]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                                        try:
                                            if j == bp[3]:
                                                totalcost = round(float(bprice[3]) * float(i[37]) * float(bq[3]), 2)
                                                totalnoincome += totalcost
                                        except:
                                            pass
                        except:
                            pass                         
        except:
            pass  
        totalincome=totalinventincome+totalnoincome
        try:#inventory name value expense
            cursor.execute("SELECT * FROM inventory WHERE cid =%s",([cid]))
            invento=cursor.fetchall()
            inventor = []
            for i in invento:
                        inventor.append(i[3],i[16])         
            cursor.execute("SELECT * FROM invoice WHERE invoicedate between %s and %s and cid =%s",[fromdate, todate,cid ]) 
            invoc=cursor.fetchall() 
            for i in invoc:
                for j in inventor:
                    try:
                        if i[8] == j[0]:
                            totalcost = round(float(j[1]) * float(i[11]), 2)
                            totalinventexpense += totalcost
                        cursor.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",[i[13],cid])
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                if i[8] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[11]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[11]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[11]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[11]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                           pass                
                    except:
                        pass 
                    try:
                        if i[17] == j[0]:
                            totalcost = round(float(j[1]) * float(i[20]), 2)
                            totalinventexpense += totalcost
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[17],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                if i[17] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[20]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[20]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[20]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[20]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                    except:
                        pass
                    try:
                        if i[24] == j[0]:
                            totalcost = round(float(j[1]) * float(i[27]), 2)
                            totalinventexpense += totalcost
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[24],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                if i[24] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[27]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[27]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float([1]) * float(i[27]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[27]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                    except:
                        pass
                    try:
                        if i[31] == j[0]:
                            totalcost = round(float(j[1]) * float(i[34]), 2)
                            totalinventexpense += totalcost
                        cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                        xx=cursor.fetchall()
                        if xx:
                            for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                if i[31] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[34]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[34]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[34]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[34]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass

                    except:
                        pass  
            cursor.execute("SELECT * FROM credit WHERE creditdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            creditnot=cursor.fetchall()
            for i in creditnot:
                for j in inventor:
                        try:
                            if i[10] == j[0]:
                                totalcost = round(float(j[1]) * float(i[12]), 2)
                                totalinventexpense -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                            xx=cursor.fetchall()                          
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[10] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[12]) * float(bq[0]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[12]) * float(bq[1]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[12]) * float(bq[2]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[12]) * float(bq[3]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                        except:
                            pass 
                        try:
                            if i[19] == j[0]:
                                totalcost = round(float(j[1]) * float(i[21]), 2)
                                totalinventexpense -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[19],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[19] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[21]) * float(bq[0]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[21]) * float(bq[1]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[21]) * float(bq[2]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[21]) * float(bq[3]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[25] == j[0]:
                                totalcost = round(float(j[1]) * float(i[27]), 2)
                                totalinventexpense -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[25],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[25] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[27]) * float(bq[0]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[27]) * float(bq[1]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[27]) * float(bq[2]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[27]) * float(bq[3]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[31] == j[0]:
                                totalcost = round(float(j[1]) * float(i[33]), 2)
                                totalinventexpense -= totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[31],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[31] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[33]) * float(bq[0]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[33]) * float(bq[1]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[33]) * float(bq[2]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[33]) * float(bq[3]), 2)
                                                totalinventexpense -= totalcost
                                        except:
                                            pass
                        except:
                            pass                                   
            cursor.execute("SELECT * FROM salesrecpts WHERE saledate between %s and %s and cid =%s",[fromdate, todate,cid ])
            salesrecept=cursor.fetchall()
            for i in salesrecept:
                for j in inventor:
                        try:
                            if i[11] == j[0]:
                                totalcost = round(float(j[1]) * float(i[13]), 2)
                                totalinventexpense += totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[10],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[11] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[13]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[13]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[13]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[13]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[20] == j[0]:
                                totalcost = round(float(j[1]) * float(i[23]), 2)
                                totalinventexpense += totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[20],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[20] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[23]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[23]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[23]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[23]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[27] == j[0]:
                                totalcost = round(float(j[1]) * float(i[30]), 2)
                                totalinventexpense += totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[27],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[27] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[30]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[30]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[30]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[30]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                        except:
                            pass
                        try:
                            if i[34] == j[0]:
                                totalcost = round(float(j[1]) * float(i[37]), 2)
                                totalinventexpense += totalcost
                            cursor.execute("SELECT * FROM bundle WHERE name =%s cid =%s",[i[34],cid])   
                            xx=cursor.fetchall()
                            if xx:
                                for (b, bp, bq) in zip(bundles, bundlpro, bundlqty):
                                    if i[34] == b:
                                        try:
                                            if j[0] == bp[0]:
                                                totalcost = round(float(j[1]) * float(i[37]) * float(bq[0]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[1]:
                                                totalcost = round(float(j[1]) * float(i[37]) * float(bq[1]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[2]:
                                                totalcost = round(float(j[1]) * float(i[37]) * float(bq[2]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                                        try:
                                            if j[0] == bp[3]:
                                                totalcost = round(float(j[1]) * float(i[37]) * float(bq[3]), 2)
                                                totalinventexpense += totalcost
                                        except:
                                            pass
                        except:
                            pass     
        except:
            pass  
        try:#non invent expenses
            cursor.execute("SELECT * FROM noninventory WHERE cid =%s",([cid]))
            noninvento=cursor.fetchall()
            print(noninvento)
            noninventor = []
            for i in noninvento:
                        noninventor.append(i[3])              
            cursor.execute("SELECT * FROM expenses WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            expen=cursor.fetchall()
            for i in expen:
                for j in noninventor:
                        try:
                            if i[27] == j:
                                totalnonexpence += float(i[32])
                        except:
                            pass
                        try:
                            if i[33] == j:
                                totalnonexpence += float(i[38])
                        except:
                            pass
                        try:
                            if i[39] == j:
                                totalnonexpence += float(i[44])
                        except:
                            pass
                        try:
                            if i[45] == j:
                                totalnonexpence += float(i[50])
                        except:
                            pass
            cursor.execute("SELECT * FROM suplrcredit WHERE paymdate between %s and %s and cid =%s",[fromdate, todate,cid ])
            debi=cursor.fetchall()            
            for i in debi:
                for j in noninventor:
                        try:
                            if i[26] == j:
                                totalnonexpence -= float(i[31])
                        except:
                            pass
                        try:
                            if i[32] == j:
                                totalnonexpence -= float(i[37])
                        except:
                            pass
                        try:
                            if i[38] == j:
                                totalnonexpence -= float(i[43])
                        except:
                            pass
                        try:
                            if i[44] == j:
                                totalnonexpence -= float(i[49])
                        except:
                            pass
        except:
            pass 

        costofgoods = totalinventexpense
        totalnonexpences = totalnonexpence + totalama
        totaloexpense = totalnonexpences
        grosprofit = (totalinventincome + totalnoincome) - totalinventexpense
        gropro = grosprofit
        profandloss = ((totalinventincome + totalnoincome) - totalinventexpense) - (totalnonexpence + totalama)

        tk.Label(contframe,text = "Income",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.04)
        tk.Label(contframe,text = " Total Income",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=0.08)
        tk.Label(contframe,text = totalincome,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=0.08)
        tk.Label(contframe,text = " Cost of Goods Sold ",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.12)
        tk.Label(contframe,text = costofgoods,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=0.12)
        tk.Label(contframe,text = " Gross Profit ",bg="grey",font=('times new roman', 14)).place(relx=0.06,rely=0.16)
        tk.Label(contframe,text = gropro,bg="grey",font=('times new roman', 12)).place(relx=0.88,rely=0.16)
        tk.Label(contframe,text = "Expenses",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.2)
        tk.Label(contframe,text = "TOTAL EXPENSE",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.24)
        tk.Label(contframe,text = totaloexpense,bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.24) 
        tk.Label(contframe,text = "PROFIT OR LOSS",bg="#FFFFFF",font=('times new roman', 16)).place(relx=0.03,rely=0.28)
        tk.Label(contframe,text = profandloss ,bg="#FFFFFF",font=('times new roman', 12)).place(relx=0.88,rely=0.28)  
                  
    tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
   
    prlframe.mainloop()
profitloss()    