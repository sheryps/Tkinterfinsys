import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cursor=mydata.cursor()
#cc
def dashboard():
    dash=tk.Tk()
    dash.title('Dashboard')
    dash.geometry('1500x1000')
    #dash['bg'] = '#2f516f'
    mycanvas=tk.Canvas(dash,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(dash,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    dashframe=tk.Frame(mycanvas)
    dashframe['bg']='#2f516f'
    mycanvas.create_window((0,0),window=dashframe,anchor='nw',width=1500,height=1200)

    cid=2
    exp=0.0
    inc=0.0
    #fetching datas from accounts1 table
    ah="SELECT cid,acctype,name,balance FROM accounts1 WHERE cid= %s"
    cursor.execute(ah,[cid])
    datas=cursor.fetchall()
    for i in datas:
      if (i[0]==cid and i[3]!=0 and i[1]=='Expenses'):
        exp+=i[3]
      if (i[0]==cid and i[3]!=0 and i[1]=='other Expenses'):
        exp+=i[3]
      if (i[0]==cid and i[3]!=0 and i[1]=='Cost of Goods Sold'): 
        exp+=i[3] 
      if (i[0]==cid and i[3]!=0 and i[1]=='Income'): 
        inc+=i[3]
      if (i[0]==cid and i[3]!=0 and i[1]=='other Income'):    
        inc+=i[3]
    #fetching datas from accounts table
    ahh="SELECT cid,acctype,name,balance FROM accounts WHERE cid= %s"
    cursor.execute(ahh,[cid])
    datass=cursor.fetchall()
    for i in datass:
      if (i[0]==cid and i[3]!=0 and i[1]=='Expenses'):
        exp+=i[3]
      if (i[0]==cid and i[3]!=0 and i[1]=='other Expenses'):
        exp+=i[3]
      if (i[0]==cid and i[3]!=0 and i[1]=='Cost of Goods Sold'): 
        exp+=i[3] 
      if (i[0]==cid and i[3]!=0 and i[1]=='Income'): 
        inc+=i[3]
      if (i[0]==cid and i[3]!=0 and i[1]=='other Income'):    
        inc+=i[3]

    #fetching datas from invoice table
    label3=[]
    data3=[]
    up=0.0
    s=0.0
    ahhh="SELECT cid,grandtotal,baldue,invoicedate FROM invoice WHERE cid= %s"
    cursor.execute(ahhh,[cid])
    dataz=cursor.fetchall() 
    for i in dataz:
      if (i[0]==cid and i[2]!=0):
        up+=float(i[2])
      if (i[0]==cid and i[2]!=0):
        label3.append(i[3])
        data3.append(i[1])
        s+=i[1] 

    #fetching data from payment table xx  
    p=0.0 
    ahhhh="SELECT cid,amtreceived FROM payment WHERE cid= %s"
    cursor.execute(ahhhh,[cid])
    datazz=cursor.fetchall() 
    for i in datazz:
      if (i[0]==cid and i[1]!=0):
        p+=i[1]

    #heading frame bb
    #fetching company name from company
    comname="SELECT id,cname FROM company WHERE id= %s"
    cursor.execute(comname,[cid])
    datz=cursor.fetchone()
    headdash=tk.Frame(dashframe,bg='#243e54')
    tk.Label(headdash,text=f'{datz[1]}',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    headdash.place(relx=0.05,rely=0.03,relwidth=0.9,relheight=0.1)

    #profit and loss frame
    #y=exp-inc
    pframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(pframe,text='PROFIT AND LOSS',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    if exp>inc:
      y=exp-inc
      tk.Label(pframe,text='NET LOSS: ₹ 'f'{y}',font=('Times New Roman',16),bg='#243e54').place(relx=0.05,rely=0.2)
    elif inc>exp: 
      y=inc-exp
      tk.Label(pframe,text='NET INCOME: ₹ 'f'{y}',font=('Times New Roman',16),bg='#243e54').place(relx=0.05,rely=0.2) 
    barframe=tk.Frame(pframe,bg='#243e54')
    
   
    data = {'Income': inc,
            'Expense': exp,}

    group_data = list(data.values())
    group_names = list(data.keys())

    fig = matplotlib.figure.Figure(figsize=(5.5,1.5),dpi=80)
    abar = fig.add_subplot(111)
    fig.set_facecolor("#243e54")
    # Default Settings
    abar.barh(group_names, group_data)
    abar.set_facecolor("#2f516a")
    canvasbar = FigureCanvasTkAgg(fig, master=barframe)

    canvasbar.get_tk_widget().place(relx=0.05,rely=0,relwidth=1,relheight=1)
    canvasbar.draw()

    barframe.place(relx=0,rely=0.35,relwidth=1,relheight=0.5)
    pframe.place(relx=0.05,rely=0.2,relwidth=0.27,relheight=0.3)
   

     #Expenses frame
    expframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(expframe,text='EXPENSES: ₹ 'f'{exp}',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    expframe.place(relx=0.37,rely=0.2,relwidth=0.27,relheight=0.3)
    fig = matplotlib.figure.Figure(figsize=(2,2))
    ax = fig.add_subplot(111)



    ax.pie([exp],radius=1.4,labels=[exp]) 
    fig.set_facecolor("#243e55")
    circle=matplotlib.patches.Circle( (0,0), 1.2, color='#243e55')
    ax.add_artist(circle)

    canvas = FigureCanvasTkAgg(fig, master=expframe)
    canvas.get_tk_widget().place(relx=0,rely=0.15,relwidth=1,relheight=0.8)
    canvas.draw()

     #Bank Account frame
    bankframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(bankframe,text='BANK ACCOUNTS',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    bankframe.place(relx=0.68,rely=0.2,relwidth=0.27,relheight=0.3)

      #Income frame
    incframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(incframe,text='INCOME: ₹'f'{inc}',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    figg = matplotlib.figure.Figure(figsize=(2,2))
    ai = figg.add_subplot(111)
    ai.pie([inc],radius=1.4,labels=[inc]) 
    figg.set_facecolor("#243e55")

    canvasi = FigureCanvasTkAgg(figg, master=incframe)
    canvasi.get_tk_widget().place(relx=0,rely=0.15,relwidth=1,relheight=0.8)
    canvasi.draw()
    incframe.place(relx=0.05,rely=0.55,relwidth=0.27,relheight=0.3)

      #Invoice frame

    invframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(invframe,text='INVOICE',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    tk.Label(invframe,text='UNPAID: ₹ 'f'{up}',font=('Times New Roman',16),bg='#243e54').place(relx=0.05,rely=0.2)
    tk.Label(invframe,text='PAID: ₹ 'f'{p}',font=('Times New Roman',16),bg='#243e54').place(relx=0.05,rely=0.3)
    bframe=tk.Frame(invframe,bg='#243e54')

    data = {'Paid': p,
            'Unpaid': up,}

    group_data = list(data.values())
    group_names = list(data.keys())

    fig = matplotlib.figure.Figure(figsize=(5.5,1.5),dpi=80)
    abar = fig.add_subplot(111)
    fig.set_facecolor("#243e54")
    # Default Settings
    abar.barh(group_names, group_data)
    abar.set_facecolor("#2f516a")
    canvasinv = FigureCanvasTkAgg(fig, master=bframe)

    canvasinv.get_tk_widget().place(relx=0.05,rely=0,relwidth=1,relheight=1)
    canvasinv.draw()

    bframe.place(relx=0,rely=0.4,relwidth=1,relheight=0.5)
    invframe.place(relx=0.37,rely=0.55,relwidth=0.27,relheight=0.3)

     #Sales frame
    dict={} 
    for x in range(0,len(label3)):
      dict[label3[x]]=data3[x]     
    salesframe=tk.Frame(dashframe,bg='#243e54')
    tk.Label(salesframe,text='SALES: ₹'f'{s}',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)
    salframe=tk.Frame(salesframe,bg='#243e54')

    sdata = list(dict.values())
    snames = list(dict.keys())
    fig = matplotlib.figure.Figure(figsize=(5.5,2.5),dpi=80)
    abar = fig.add_subplot(111)
    fig.set_facecolor("#243e54")
    # Default Settings
    abar.bar(snames,sdata)
    abar.set_facecolor("#2f516a")
    canvasbar = FigureCanvasTkAgg(fig, master=salframe)

    canvasbar.get_tk_widget().place(relx=0.05,rely=0,relwidth=1,relheight=1)
    canvasbar.draw()

    salframe.place(relx=0,rely=0.35,relwidth=1,relheight=0.5)
    salesframe.place(relx=0.68,rely=0.55,relwidth=0.27,relheight=0.3)

    dash.mainloop()
dashboard()    