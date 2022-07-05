import tkinter as tk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
import mysql.connector
from tkinter import *
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def delayedcharge():  
    win=tk.Tk()
    win.title('Sales Records')
    win.geometry('1500x1000')
    win['bg'] = '#2f516f'
    cid=2
    mycanvas=tk.Canvas(win,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(win,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1200)
    hf1=tk.Frame(frame,bg='#243e54')
    tk.Label(hf1,text='DELAYED CHARGE',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    hf1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)
    hf2=tk.Frame(frame,bg='#243e54')
            #customer
    tk.Label(hf2,text='Customer',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.11) 
    global subtot,amount,taxamt,taxamt2,taxamt3,taxamt4
    subtot=0.0
    amount=0.0
    taxamt=0.0
    taxamt2=0.0
    taxamt3=0.0
    taxamt4=0.0
    def delaycusinput():
        try:
                cur.execute("SELECT firstname,lastname FROM customer")
                val=cur.fetchall()         
                for row in val:
                    tm.append(row[0]+row[1])   
        except:
            pass              
    tm=['Select Customer']
    delaycusinput()     
    timecus=ttk.Combobox(hf2,values=tm,font=(6))
    timecus.place(relx=0.05,rely=0.15,relwidth=0.2,relheight=0.03)
    tk.Button(hf2,text='+',font=(14)).place(relx=0.26,rely=0.15,relwidth=0.025,relheight=0.03)

    tk.Label(hf2,text='Delayed charge date',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.2) 
    deldate=StringVar()
    DateEntry(hf2,textvariable=deldate,date_pattern='y-mm-dd').place(relx=0.05,rely=0.25,relwidth=0.2,relheight=0.03) 
    def product1getitems(t):
        prodd=prod.get()
        cur.execute("SELECT description FROM inventory WHERE name =%s",([prodd]))
        fet=cur.fetchone()
        cur.execute("SELECT descr FROM noninventory WHERE name =%s",([prodd]))
        fetch=cur.fetchone()
        if fet:
            desc.insert(0,fet[0])
        elif fetch:
            desc.insert(0,fetch[0])  
        def delayedsupplierstate1():
            prod1=prod.get()
            x=prod1.split()
            a=x[0]
            b=x[1]
            if len(x) == 3:
                b = x[1] + " " + x[2] 
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
            else:
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
        list=[] 
        try:
            cur.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",([prod1,cid]))
            bundleobject=cur.fetchone() 
            if bundleobject:
                bundledict={'item':'bundle','bundleid':bundleobject[0],'name':bundleobject[3],'hsn':bundleobject[4],'description':bundleobject[3],
                'salesprice':bundleobject[34],'cost':0,'tax':0,'product1':bundleobject[6],'product2':bundleobject[7],'product3':bundleobject[8],'product4':bundleobject[39],
                'hsn1':bundleobject[10],'hsn2':bundleobject[11],'hsn3':bundleobject[12],'hsn4':bundleobject[31],'description1':bundleobject[14],'description2':bundleobject[15],
                'description3':bundleobject[16],'description4':bundleobject[17],'qty1':bundleobject[18],'qty2':bundleobject[19],'qty3':bundleobject[20],'qty4':bundleobject[21],
                'price1':bundleobject[22],'price2':bundleobject[23],'price3':bundleobject[24],'price4':bundleobject[25],'total1':bundleobject[26],'total2':bundleobject[27]
                ,'total3':bundleobject[28],'total4':bundleobject[29],'tax1':bundleobject[30],'tax2':bundleobject[31],'tax3':bundleobject[32],'tax4':bundleobject[33]}
                try:
                    bundledict['place']= delayedsupplierstate1() 
                except:
                    pass 
                list.append(bundledict)   
            cur.execute("SELECT * FROM inventory WHERE name =%s and cid =%s",([prod1,cid]))
            inventoryobject=cur.fetchone() 
            if inventoryobject:
                inventorydict = {'item': 'inventory', 'inventoryid': inventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],
                         'date': inventoryobject[9], 'stockalrt': inventoryobject[10],
                         'invacnt': inventoryobject[11],
                         'description': inventoryobject[12], 'salesprice': inventoryobject[13],
                         'incomeacnt': inventoryobject[14],
                         'tax': inventoryobject[15], 'purchaseinfo': inventoryobject[16],
                         'cost': inventoryobject[17],
                         'expacnt': inventoryobject[18], 'purtax': inventoryobject[19],
                         'revcharge': inventoryobject[20],
                         'presupplier': inventoryobject[21]}
                try:
                    inventorydict['place'] = delayedsupplierstate1()
                except:
                    pass 
                list.append(inventorydict)
            cur.execute("SELECT * FROM noninventory WHERE name =%s and cid =%s",([prod1,cid]))
            noninventoryobject=cur.fetchone() 
            if noninventoryobject:
                noninventorydict = {'item': 'noninventory', 'inventoryid': noninventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],'description': inventoryobject[9],
                          'salesprice': inventoryobject[10],'tax': inventoryobject[12],
                          'cost': inventoryobject[14],'purtax': inventoryobject[16],}
                try:
                    noninventorydict['place'] = delayedsupplierstate1()
                except:
                    pass
                list.append(noninventorydict)      
            cur.execute("SELECT * FROM service WHERE name =%s and cid =%s",([prod1,cid]))
            serviceobject=cur.fetchone() 
            if serviceobject:
                servicedict = {'item': 'service', 'serviceid': serviceobject[0],
                       'name': serviceobject[3], 'sku': serviceobject[4],
                       'hsn': serviceobject[5], 'unit': serviceobject[6], 'categ': serviceobject[7],
                       'description': serviceobject[8], 'salesprice': serviceobject[9],
                       'income': serviceobject[10], 'initialqty': '',
                       'tax': serviceobject[11], 'abatement': serviceobject[12],
                       'sertype': serviceobject[14]}  
                try:
                    servicedict['place'] = delayedsupplierstate1()
                except:
                     pass
                list.append(servicedict)  
            else:
                notany = {'item': 'notany', 'name': ' ',
                  'sku': ' ', 'hsn': ' ',
                  'unit': 0,
                  'category': ' ', 'initialqty': 0,
                  'description': ' ', 'cost': 0,
                  'salesprice': 0,
                  'tax': 0, 'purtax': 0}
                list.append(notany)               
        except:
            pass            


    tk.Label(hf2,text='#',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.3)
    tk.Label(hf2,text='PRODUCT/SERVICES',font=('times new roman', 14),bg='#2f516f').place(relx=0.1,rely=0.3)
            #first row
    tk.Label(hf2,text='1',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.35)
    pro=['Select Product']
    try:
                cur.execute("SELECT name,description FROM inventory WHERE cid =%s",([cid]))
                vall=cur.fetchall() 
                print(vall)      
                for row in vall:
                        pro.append(row[0])
                cur.execute("SELECT name,descr FROM noninventory WHERE cid =%s",([cid]))
                valll=cur.fetchall()         
                for row in valll:
                    pro.append(row[0])    
                #cur.execute("SELECT name FROM bundle WHERE cid =%s",([cid]))
                #vall1=cur.fetchall()         
                #for row in vall1:
                   # pro.append(row[0]) 
                   # hs.append(row[1])   
                    #ds.append(row[2])           
    except:
                pass
            
    prod=ttk.Combobox(hf2,values=pro,font=(8))
    prod.bind('<<ComboboxSelected>>',product1getitems)
    prod.place(relx=0.1,rely=0.35,relwidth=0.16,relheight=0.04)
    tk.Label(hf2,text='DESCRIPTION',font=('times new roman', 14),bg='#2f516f').place(relx=0.28,rely=0.3)
    desc=tk.Entry(hf2,font=(8))
    desc.place(relx=0.28,rely=0.35,relwidth=0.11,relheight=0.04)
        

    def totalvalues(t):      
        global subtot,clear_total,tot
        def clear_text():
            total.delete(0, END) 
        def clear_total():
            sub.delete(0,END)  
        tot=0.0    
        q=float(quan1.get())
        r=float(rate1.get())
        tot=tot + (q*r)
        subtot=subtot+tot
        clear_text()
        total.insert(0,tot)
        clear_total()
        sub.insert(0,subtot) 

    quan1=IntVar()    
    tk.Label(hf2,text='QTY',font=('times new roman', 14),bg='#2f516f').place(relx=0.41,rely=0.3,relwidth=0.1)
    qty=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan1,font=(8))
    qty.bind('<FocusIn>',totalvalues)
    qty.place(relx=0.41,rely=0.35,relwidth=0.1,relheight=0.04)
    tk.Label(hf2,text='RATE',font=('times new roman', 14),bg='#2f516f').place(relx=0.53,rely=0.3,relwidth=0.1)
    rate1=IntVar()
    rate=tk.Spinbox(hf2,textvariable=rate1,from_=0,to=2147483647,font=(8))
    rate.bind('<FocusIn>',totalvalues)
    rate.place(relx=0.53,rely=0.35,relwidth=0.1,relheight=0.04)
    tk.Label(hf2,text='TOTAL',font=('times new roman', 14),bg='#2f516f').place(relx=0.66,rely=0.3,relwidth=0.1)

    total=tk.Entry(hf2,font=(8))
    total.place(relx=0.66,rely=0.35,relwidth=0.1,relheight=0.04)

    def taxxvalue(y):
        global taxamt,clear_totalamount,taxamt2,taxamt4,taxamt3,amount
        tx=0.0
        def clear_tax():
            taxamount.delete(0,END)   
        def clear_totalamount():
            totalamount.delete(0,END)                 
        taxvalue=tax.get()
        if taxvalue=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue=='0.0% GST(0%)':
            tval=0.00
        elif taxvalue=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue=='Out of Scope(0%)':
            tval=0.00                                      
        tx=tot*tval
        taxtot=0.0
        if taxamt==0:
                taxtot=round(taxtot+tx,2)
        else:
                taxtot=round(tx,2)
        taxamt=taxtot    
        clear_tax()
        taxamount.insert(0,taxamt+taxamt2+taxamt3+taxamt4)
        clear_totalamount()
        amount=round(subtot+taxamt+taxamt2+taxamt3+taxamt4,2)
        totalamount.insert(0,amount)

    tk.Label(hf2,text='TAX',font=('times new roman', 14),bg='#2f516f').place(relx=0.78,rely=0.3,relwidth=0.1)
    taxval=['28.0% GST(28%)','18.0% GST(18%)','12.0% GST(12%)','06.0% GST(06%)','05.0% GST(05%)','03.0% GST(03%)',
                                                    '0.25% GST(0.25%)','0.0% GST(0%)','Exempt GST(0%)','Out of Scope(0%)']                                           
    tax=ttk.Combobox(hf2,values=taxval)
    tax.bind('<<ComboboxSelected>>',taxxvalue)
    tax.place(relx=0.78,rely=0.35,relwidth=0.1,relheight=0.04)
        #second row    
    tk.Label(hf2,text='2',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.42)
    def product2getitems(t):
        prodd=prod1.get()
        cur.execute("SELECT description FROM inventory WHERE name =%s",([prodd]))
        fet=cur.fetchone()
        cur.execute("SELECT descr FROM noninventory WHERE name =%s",([prodd]))
        fetch=cur.fetchone()
        if fet:
            desc1.insert(0,fet[0])
        elif fetch:
            desc1.insert(0,fetch[0])  
        def delayedsupplierstate2():
            prodd2=prod1.get()
            x=prodd2.split()
            a=x[0]
            b=x[1]
            if len(x) == 3:
                b = x[1] + " " + x[2] 
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
            else:
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
        list=[] 
        try:
            cur.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",([prod1,cid]))
            bundleobject=cur.fetchone() 
            if bundleobject:
                bundledict={'item':'bundle','bundleid':bundleobject[0],'name':bundleobject[3],'hsn':bundleobject[4],'description':bundleobject[3],
                'salesprice':bundleobject[34],'cost':0,'tax':0,'product1':bundleobject[6],'product2':bundleobject[7],'product3':bundleobject[8],'product4':bundleobject[39],
                'hsn1':bundleobject[10],'hsn2':bundleobject[11],'hsn3':bundleobject[12],'hsn4':bundleobject[31],'description1':bundleobject[14],'description2':bundleobject[15],
                'description3':bundleobject[16],'description4':bundleobject[17],'qty1':bundleobject[18],'qty2':bundleobject[19],'qty3':bundleobject[20],'qty4':bundleobject[21],
                'price1':bundleobject[22],'price2':bundleobject[23],'price3':bundleobject[24],'price4':bundleobject[25],'total1':bundleobject[26],'total2':bundleobject[27]
                ,'total3':bundleobject[28],'total4':bundleobject[29],'tax1':bundleobject[30],'tax2':bundleobject[31],'tax3':bundleobject[32],'tax4':bundleobject[33]}
                try:
                    bundledict['place']= delayedsupplierstate2() 
                except:
                    pass 
                list.append(bundledict)   
            cur.execute("SELECT * FROM inventory WHERE name =%s and cid =%s",([prod1,cid]))
            inventoryobject=cur.fetchone() 
            if inventoryobject:
                inventorydict = {'item': 'inventory', 'inventoryid': inventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],
                         'date': inventoryobject[9], 'stockalrt': inventoryobject[10],
                         'invacnt': inventoryobject[11],
                         'description': inventoryobject[12], 'salesprice': inventoryobject[13],
                         'incomeacnt': inventoryobject[14],
                         'tax': inventoryobject[15], 'purchaseinfo': inventoryobject[16],
                         'cost': inventoryobject[17],
                         'expacnt': inventoryobject[18], 'purtax': inventoryobject[19],
                         'revcharge': inventoryobject[20],
                         'presupplier': inventoryobject[21]}
                try:
                    inventorydict['place'] = delayedsupplierstate2()
                except:
                    pass 
                list.append(inventorydict)
            cur.execute("SELECT * FROM noninventory WHERE name =%s and cid =%s",([prod1,cid]))
            noninventoryobject=cur.fetchone() 
            if noninventoryobject:
                noninventorydict = {'item': 'noninventory', 'inventoryid': noninventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],'description': inventoryobject[9],
                          'salesprice': inventoryobject[10],'tax': inventoryobject[12],
                          'cost': inventoryobject[14],'purtax': inventoryobject[16],}
                try:
                    noninventorydict['place'] = delayedsupplierstate2()
                except:
                    pass
                list.append(noninventorydict)      
            cur.execute("SELECT * FROM service WHERE name =%s and cid =%s",([prod1,cid]))
            serviceobject=cur.fetchone() 
            if serviceobject:
                servicedict = {'item': 'service', 'serviceid': serviceobject[0],
                       'name': serviceobject[3], 'sku': serviceobject[4],
                       'hsn': serviceobject[5], 'unit': serviceobject[6], 'categ': serviceobject[7],
                       'description': serviceobject[8], 'salesprice': serviceobject[9],
                       'income': serviceobject[10], 'initialqty': '',
                       'tax': serviceobject[11], 'abatement': serviceobject[12],
                       'sertype': serviceobject[14]}  
                try:
                    servicedict['place'] = delayedsupplierstate2()
                except:
                     pass
                list.append(servicedict)  
            else:
                notany = {'item': 'notany', 'name': ' ',
                  'sku': ' ', 'hsn': ' ',
                  'unit': 0,
                  'category': ' ', 'initialqty': 0,
                  'description': ' ', 'cost': 0,
                  'salesprice': 0,
                  'tax': 0, 'purtax': 0}
                list.append(notany)               
        except:
            pass            
            #third row
    tk.Label(hf2,text='1',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.35)
    def product3getitems(t):
        prodd=prod3.get()
        cur.execute("SELECT description FROM inventory WHERE name =%s",([prodd]))
        fet=cur.fetchone()
        cur.execute("SELECT descr FROM noninventory WHERE name =%s",([prodd]))
        fetch=cur.fetchone()
        if fet:
            desc3.insert(0,fet[0])
        elif fetch:
            desc3.insert(0,fetch[0])  
        def delayedsupplierstate3():
            prodd3=prod3.get()
            x=prodd3.split()
            a=x[0]
            b=x[1]
            if len(x) == 3:
                b = x[1] + " " + x[2] 
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
            else:
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
        list=[] 
        try:
            cur.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",([prod1,cid]))
            bundleobject=cur.fetchone() 
            if bundleobject:
                bundledict={'item':'bundle','bundleid':bundleobject[0],'name':bundleobject[3],'hsn':bundleobject[4],'description':bundleobject[3],
                'salesprice':bundleobject[34],'cost':0,'tax':0,'product1':bundleobject[6],'product2':bundleobject[7],'product3':bundleobject[8],'product4':bundleobject[39],
                'hsn1':bundleobject[10],'hsn2':bundleobject[11],'hsn3':bundleobject[12],'hsn4':bundleobject[31],'description1':bundleobject[14],'description2':bundleobject[15],
                'description3':bundleobject[16],'description4':bundleobject[17],'qty1':bundleobject[18],'qty2':bundleobject[19],'qty3':bundleobject[20],'qty4':bundleobject[21],
                'price1':bundleobject[22],'price2':bundleobject[23],'price3':bundleobject[24],'price4':bundleobject[25],'total1':bundleobject[26],'total2':bundleobject[27]
                ,'total3':bundleobject[28],'total4':bundleobject[29],'tax1':bundleobject[30],'tax2':bundleobject[31],'tax3':bundleobject[32],'tax4':bundleobject[33]}
                try:
                    bundledict['place']= delayedsupplierstate3() 
                except:
                    pass 
                list.append(bundledict)   
            cur.execute("SELECT * FROM inventory WHERE name =%s and cid =%s",([prod1,cid]))
            inventoryobject=cur.fetchone() 
            if inventoryobject:
                inventorydict = {'item': 'inventory', 'inventoryid': inventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],
                         'date': inventoryobject[9], 'stockalrt': inventoryobject[10],
                         'invacnt': inventoryobject[11],
                         'description': inventoryobject[12], 'salesprice': inventoryobject[13],
                         'incomeacnt': inventoryobject[14],
                         'tax': inventoryobject[15], 'purchaseinfo': inventoryobject[16],
                         'cost': inventoryobject[17],
                         'expacnt': inventoryobject[18], 'purtax': inventoryobject[19],
                         'revcharge': inventoryobject[20],
                         'presupplier': inventoryobject[21]}
                try:
                    inventorydict['place'] = delayedsupplierstate3()
                except:
                    pass 
                list.append(inventorydict)
            cur.execute("SELECT * FROM noninventory WHERE name =%s and cid =%s",([prod1,cid]))
            noninventoryobject=cur.fetchone() 
            if noninventoryobject:
                noninventorydict = {'item': 'noninventory', 'inventoryid': noninventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],'description': inventoryobject[9],
                          'salesprice': inventoryobject[10],'tax': inventoryobject[12],
                          'cost': inventoryobject[14],'purtax': inventoryobject[16],}
                try:
                    noninventorydict['place'] = delayedsupplierstate3()
                except:
                    pass
                list.append(noninventorydict)      
            cur.execute("SELECT * FROM service WHERE name =%s and cid =%s",([prod1,cid]))
            serviceobject=cur.fetchone() 
            if serviceobject:
                servicedict = {'item': 'service', 'serviceid': serviceobject[0],
                       'name': serviceobject[3], 'sku': serviceobject[4],
                       'hsn': serviceobject[5], 'unit': serviceobject[6], 'categ': serviceobject[7],
                       'description': serviceobject[8], 'salesprice': serviceobject[9],
                       'income': serviceobject[10], 'initialqty': '',
                       'tax': serviceobject[11], 'abatement': serviceobject[12],
                       'sertype': serviceobject[14]}  
                try:
                    servicedict['place'] = delayedsupplierstate3()
                except:
                     pass
                list.append(servicedict)  
            else:
                notany = {'item': 'notany', 'name': ' ',
                  'sku': ' ', 'hsn': ' ',
                  'unit': 0,
                  'category': ' ', 'initialqty': 0,
                  'description': ' ', 'cost': 0,
                  'salesprice': 0,
                  'tax': 0, 'purtax': 0}
                list.append(notany)               
        except:
            pass                    
    prod1=ttk.Combobox(hf2,values=pro,font=(8))
    prod1.bind('<<ComboboxSelected>>',product2getitems)
    prod1.place(relx=0.1,rely=0.42,relwidth=0.16,relheight=0.04)
    desc1=tk.Entry(hf2,font=(8))
    desc1.place(relx=0.28,rely=0.42,relwidth=0.11,relheight=0.04)
    def total1values(tt):
            global tot2,subtot
            def clear_text1():
                total2.delete(0, END) 
            tot2=0.0
            q2=float(quan2.get())
            r2=float(rate2.get())
            tot2=tot2 + (q2*r2)
            subtot=subtot+tot2
            clear_text1()
            total2.insert(0,tot2) 
            clear_total()
            sub.insert(0,subtot) 
    quan2=IntVar()    
    rate2=IntVar()
    qty2=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan2,font=(8))
    qty2.bind('<FocusIn>',total1values)
    qty2.place(relx=0.41,rely=0.42,relwidth=0.1,relheight=0.04)  
    rat2=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=rate2,font=(8))
    rat2.bind('<FocusIn>',total1values)
    rat2.place(relx=0.53,rely=0.42,relwidth=0.1,relheight=0.04)

    total2=tk.Entry(hf2,font=(8))
    total2.place(relx=0.66,rely=0.42,relwidth=0.1,relheight=0.04)
    #tax 2
    def taxxvalue1(y):
        global taxamt,taxamt2,taxamt3,taxamt4,amount
        tx1=0.0
        def clear_tax():
            taxamount.delete(0,END)  
              
        taxvalue1=tax1.get()
        if taxvalue1=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue1=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue1=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue1=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue1=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue1=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue1=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue1=='0.0% GST(0%)':    
            tval=0.00   
        elif taxvalue1=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue1=='Out of Scope(0%)':
            tval=0.00                                   
        tx1=tot2*tval
        taxtot1=0.0
        if taxamt2==0:
                taxtot1=round(taxtot1+tx1,2)
        else:
                taxtot1=round(tx1,2)       
        clear_tax()
        taxamt2=taxtot1
        taxamount.insert(0,taxamt4+taxamt3+taxamt2+taxamt)
        clear_totalamount()
        amount=round(subtot+taxamt+taxamt2+taxamt3+taxamt4,2)
        totalamount.insert(0,amount)
    tax1=ttk.Combobox(hf2,values=taxval)
    tax1.bind('<<ComboboxSelected>>',taxxvalue1)
    tax1.place(relx=0.78,rely=0.42,relwidth=0.1,relheight=0.04)
        #third row 
    tk.Label(hf2,text='3',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.49)     
    prod3=ttk.Combobox(hf2,values=pro,font=(8))
    prod3.bind('<<ComboboxSelected>>',product3getitems)
    prod3.place(relx=0.1,rely=0.49,relwidth=0.16,relheight=0.04)
    desc3=tk.Entry(hf2,font=(8))
    desc3.place(relx=0.28,rely=0.49,relwidth=0.11,relheight=0.04)
    def total3values(tt):
            global tot3,subtot
            def clear_text3():
                total3.delete(0, END)
            tot3=0.0
            q3=float(quan3.get())
            r3=float(rate3.get())
            tot3=tot3 + (q3*r3)
            subtot=subtot+tot3
            clear_text3()
            total3.insert(0,tot3) 
            clear_total()
            sub.insert(0,subtot) 
    quan3=IntVar()    
    rate3=IntVar()
    qty3=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan3,font=(8))
    qty3.bind('<FocusIn>',total3values)
    qty3.place(relx=0.41,rely=0.49,relwidth=0.1,relheight=0.04)  
    rat3=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=rate3,font=(8))
    rat3.bind('<FocusIn>',total3values)
    rat3.place(relx=0.53,rely=0.49,relwidth=0.1,relheight=0.04)

    total3=tk.Entry(hf2,font=(8))
    total3.place(relx=0.66,rely=0.49,relwidth=0.1,relheight=0.04)

    #tax 3
    def taxxvalue2(y):
        global taxamt,taxamt2,taxamt3,taxamt4,amount
        tx2=0.0
        def clear_tax():
            taxamount.delete(0,END)
              
        taxvalue2=tax3.get()
        if taxvalue2=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue2=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue2=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue2=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue2=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue2=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue2=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue2=='0.0% GST(0%)':
            tval=0.00  
        elif taxvalue2=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue2=='Out of Scope(0%)':
            tval=0.00                                    
        tx2=tot3*tval
        taxtot2=0.0
        if taxamt3==0:
                taxtot2=round(taxtot2+tx2,2)
        else:
                taxtot2=round(tx2,2)       
        clear_tax()
        taxamt3=taxtot2
        taxamount.insert(0,taxamt4+taxamt3+taxamt2+taxamt)
        clear_totalamount()
        amount=round(subtot+taxamt+taxamt2+taxamt3+taxamt4,2)
        totalamount.insert(0,amount)
    tax3=ttk.Combobox(hf2,values=taxval)
    tax3.bind('<<ComboboxSelected>>',taxxvalue2)
    tax3.place(relx=0.78,rely=0.49,relwidth=0.1,relheight=0.04)
        #fourth row
    tk.Label(hf2,text='4',font=('times new roman', 14),bg='#2f516f').place(relx=0.05,rely=0.56)
    def product4getitems(t):
        prodd=prod4.get()
        cur.execute("SELECT description FROM inventory WHERE name =%s",([prodd]))
        fet=cur.fetchone()
        cur.execute("SELECT descr FROM noninventory WHERE name =%s",([prodd]))
        fetch=cur.fetchone()
        if fet:
            desc4.insert(0,fet[0])
        elif fetch:
            desc4.insert(0,fetch[0])  
        def delayedsupplierstate4():
            prodd4=prod4.get()
            x=prodd4.split()
            a=x[0]
            b=x[1]
            if len(x) == 3:
                b = x[1] + " " + x[2] 
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
            else:
                try:
                    cur.execute("SELECT firstname,lastname FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                    supplier=cur.fetchone()
                    if supplier:
                        cur.execute("SELECT state FROM supplier WHERE firstname =%s and lastname =%s and cid =%s ",([a,b,cid]))
                        supobject=cur.fetchone()
                        payeeplace=supobject[0]
                except:
                    pass
        list=[] 
        try:
            cur.execute("SELECT * FROM bundle WHERE name =%s and cid =%s",([prod1,cid]))
            bundleobject=cur.fetchone() 
            if bundleobject:
                bundledict={'item':'bundle','bundleid':bundleobject[0],'name':bundleobject[3],'hsn':bundleobject[4],'description':bundleobject[3],
                'salesprice':bundleobject[34],'cost':0,'tax':0,'product1':bundleobject[6],'product2':bundleobject[7],'product3':bundleobject[8],'product4':bundleobject[39],
                'hsn1':bundleobject[10],'hsn2':bundleobject[11],'hsn3':bundleobject[12],'hsn4':bundleobject[31],'description1':bundleobject[14],'description2':bundleobject[15],
                'description3':bundleobject[16],'description4':bundleobject[17],'qty1':bundleobject[18],'qty2':bundleobject[19],'qty3':bundleobject[20],'qty4':bundleobject[21],
                'price1':bundleobject[22],'price2':bundleobject[23],'price3':bundleobject[24],'price4':bundleobject[25],'total1':bundleobject[26],'total2':bundleobject[27]
                ,'total3':bundleobject[28],'total4':bundleobject[29],'tax1':bundleobject[30],'tax2':bundleobject[31],'tax3':bundleobject[32],'tax4':bundleobject[33]}
                try:
                    bundledict['place']= delayedsupplierstate4() 
                except:
                    pass 
                list.append(bundledict)   
            cur.execute("SELECT * FROM inventory WHERE name =%s and cid =%s",([prod1,cid]))
            inventoryobject=cur.fetchone() 
            if inventoryobject:
                inventorydict = {'item': 'inventory', 'inventoryid': inventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],
                         'date': inventoryobject[9], 'stockalrt': inventoryobject[10],
                         'invacnt': inventoryobject[11],
                         'description': inventoryobject[12], 'salesprice': inventoryobject[13],
                         'incomeacnt': inventoryobject[14],
                         'tax': inventoryobject[15], 'purchaseinfo': inventoryobject[16],
                         'cost': inventoryobject[17],
                         'expacnt': inventoryobject[18], 'purtax': inventoryobject[19],
                         'revcharge': inventoryobject[20],
                         'presupplier': inventoryobject[21]}
                try:
                    inventorydict['place'] = delayedsupplierstate4()
                except:
                    pass 
                list.append(inventorydict)
            cur.execute("SELECT * FROM noninventory WHERE name =%s and cid =%s",([prod1,cid]))
            noninventoryobject=cur.fetchone() 
            if noninventoryobject:
                noninventorydict = {'item': 'noninventory', 'inventoryid': noninventoryobject[0],
                         'name': inventoryobject[3], 'sku': inventoryobject[4], 'hsn': inventoryobject[5],
                         'unit': inventoryobject[6], 'category': inventoryobject[7],
                         'initialqty': inventoryobject[8],'description': inventoryobject[9],
                          'salesprice': inventoryobject[10],'tax': inventoryobject[12],
                          'cost': inventoryobject[14],'purtax': inventoryobject[16],}
                try:
                    noninventorydict['place'] = delayedsupplierstate4()
                except:
                    pass
                list.append(noninventorydict)      
            cur.execute("SELECT * FROM service WHERE name =%s and cid =%s",([prod1,cid]))
            serviceobject=cur.fetchone() 
            if serviceobject:
                servicedict = {'item': 'service', 'serviceid': serviceobject[0],
                       'name': serviceobject[3], 'sku': serviceobject[4],
                       'hsn': serviceobject[5], 'unit': serviceobject[6], 'categ': serviceobject[7],
                       'description': serviceobject[8], 'salesprice': serviceobject[9],
                       'income': serviceobject[10], 'initialqty': '',
                       'tax': serviceobject[11], 'abatement': serviceobject[12],
                       'sertype': serviceobject[14]}  
                try:
                    servicedict['place'] = delayedsupplierstate4()
                except:
                     pass
                list.append(servicedict)  
            else:
                notany = {'item': 'notany', 'name': ' ',
                  'sku': ' ', 'hsn': ' ',
                  'unit': 0,
                  'category': ' ', 'initialqty': 0,
                  'description': ' ', 'cost': 0,
                  'salesprice': 0,
                  'tax': 0, 'purtax': 0}
                list.append(notany)               
        except:
            pass       
    prod4=ttk.Combobox(hf2,values=pro,font=(8))
    prod4.bind('<<ComboboxSelected>>',product4getitems)
    prod4.place(relx=0.1,rely=0.56,relwidth=0.16,relheight=0.04)
    desc4=tk.Entry(hf2,font=(8))
    desc4.place(relx=0.28,rely=0.56,relwidth=0.11,relheight=0.04)
    def total4values(tt):
            global tot4,subtot
            def clear_text4():
                total4.delete(0, END)
            tot4=0.0
            q4=float(quan4.get())
            r4=float(rate4.get())
            tot4=tot4 + (q4*r4)
            subtot=subtot+tot4
            clear_text4()
            total4.insert(0,tot4)
            clear_total()
            sub.insert(0,subtot) 
    quan4=IntVar()    
    rate4=IntVar()
    qty4=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=quan4,font=(8))
    qty4.bind('<FocusIn>',total4values)
    qty4.place(relx=0.41,rely=0.56,relwidth=0.1,relheight=0.04)  
    rat4=tk.Spinbox(hf2,from_=0,to=2147483647,textvariable=rate4,font=(8))
    rat4.bind('<FocusIn>',total4values)
    rat4.place(relx=0.53,rely=0.56,relwidth=0.1,relheight=0.04)

    total4=tk.Entry(hf2,font=(8))
    total4.place(relx=0.66,rely=0.56,relwidth=0.1,relheight=0.04)
        #tax 4
    def taxxvalue3(y):
        global taxamt,taxamt2,taxamt3,taxamt4,amount
        tx3=0.0
        def clear_tax():
            taxamount.delete(0,END)
              
        taxvalue3=tax4.get()
        if taxvalue3=='28.0% GST(28%)':
            tval=0.28
        elif taxvalue3=='18.0% GST(18%)':
            tval=0.18
        elif taxvalue3=='12.0% GST(12%)':
            tval=0.12
        elif taxvalue3=='06.0% GST(06%)':
            tval=0.06 
        elif taxvalue3=='05.0% GST(05%)':
            tval=0.05
        elif taxvalue3=='03.0% GST(03%)':
            tval=0.03
        elif taxvalue3=='0.25% GST(0.25%)':
            tval=0.025
        elif taxvalue3=='0.0% GST(0%)':
            tval=0.00 
        elif taxvalue3=='Exempt GST(0%)':
            tval=0.00 
        elif taxvalue3=='Out of Scope(0%)':
            tval=0.00     
        tx3=tot4*tval
        taxtot3=0.0
        if taxamt4==0:
                taxtot3=round(taxtot3+tx3,2)
        else:
                taxtot3=round(tx3,2)       
        clear_tax()
        taxamt4=taxtot3
        taxamount.insert(0,taxamt4+taxamt3+taxamt2+taxamt)
        clear_totalamount()
        amount=round(subtot+taxamt+taxamt2+taxamt3+taxamt4,2)
        totalamount.insert(0,amount)
    
    tax4=ttk.Combobox(hf2,values=taxval)
    tax4.bind('<<ComboboxSelected>>',taxxvalue3)
    tax4.place(relx=0.78,rely=0.56,relwidth=0.1,relheight=0.04)


    tk.Label(hf2,text='Sub Total',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.65,relwidth=0.1,relheight=0.05)
    sub=tk.Entry(hf2,font=('times new roman', 16))
    sub.place(relx=0.82,rely=0.65,relheight=0.05,relwidth=0.12)
    tk.Label(hf2,text='Tax Amount',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.71,relwidth=0.1,relheight=0.05)
    taxamount=tk.Entry(hf2,font=('times new roman', 16))
    taxamount.place(relx=0.82,rely=0.71,relheight=0.05,relwidth=0.12)
    tk.Label(hf2,text='Grand Total',font=('times new roman', 16),bg='#2f516f').place(relx=0.7,rely=0.77,relwidth=0.1,relheight=0.05)
    totalamount=tk.Entry(hf2,font=('times new roman', 16))
    totalamount.place(relx=0.82,rely=0.77,relheight=0.05,relwidth=0.12)
    def delayedchargesave():
        cust=timecus.get()
        date=deldate.get()
        delayedchargeno='1000'
        prodorser=prod.get()
        descr=desc.get()
        qtyy=quan1.get()
        raty1=rate1.get()
        tax11=tax.get()
        taxamount=taxamt+taxamt+taxamt3+taxamt4
        totaly=total.get()
        prodoser1=prod1.get()
        descr1=desc1.get()
        qtyy2=quan2.get()
        raty2=rate2.get()
        tax22=tax1.get()
        totaly2=total2.get()
        prodorser2=prod3.get()
        descp2=desc3.get()
        qtyy3=quan3.get()
        raty3=rate3.get()
        totaly3=total3.get()
        tax33=tax3.get()
        prodorser3=prod4.get()
        descp3=desc4.get()
        qtyy4=quan4.get()
        raty4=rate4.get()
        totaly4=total4.get()
        tax44=tax4.get()
        dlych='''INSERT INTO delayedcharge (cid,customer,delayedchargedate,delayedchargeno,prodorser,description,qty,rate,tax,total,prodorser1,
        description1,qty1,rate1,total1,tax1,prodorser2,description2,qty2,rate2,total2,tax2,prodorser3,description3,qty3,rate3,total3,tax3,
        taxamount,subtotal,grandtotal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cur.execute(dlych,[(cid),(cust),(date),(delayedchargeno),(prodorser),(descr),(qtyy),(raty1),(tax11),(totaly),(prodoser1),
        (descr1),(qtyy2),(raty2),(totaly2),(tax22),(prodorser2),(descp2),(qtyy3),(raty3),(totaly3),(tax33),(prodorser3),(descp3),(qtyy4),(raty4),(totaly4),(tax44),
        (taxamount),(subtot),(amount)])
        mydata.commit()
        win.destroy()
    tk.Button(hf2,text='Save',font=('times new roman', 16),bg='#2f516f',command=delayedchargesave).place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.05)
    hf2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.7)
    win.mainloop()   
delayedcharge()    
     