import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime, date, timedelta
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from tkcalendar import DateEntry
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cursor=mydata.cursor()
#cc
def accrecivabales():
    prlframe=tk.Tk()
    prlframe.title('Account Receivables')
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
    tk.Label(pframe,text='A/R AGEING SUMMARY REPORT',font=('Times New Roman',26),bg='#243e54').place(relx=0.4,rely=0.05)
    pframe.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.05)

    form_frame=tk.Frame(profitlossframe,bg='#243e54')

    def menuuu(e):
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
    tk.Label(form_frame,text="Report Period",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold')).place(relx=0.05,rely=0.1)
    options=["All dates", "Custom","Today","This month","This financial year"]
    drop= ttk.Combobox(form_frame,values=options,font=16)
    drop.current(0)
    drop.bind('<<ComboboxSelected>>',menuuu)
    drop.place(relx=0.05,rely=0.23,relwidth=0.3,relheight=0.15)
     #buttons
    def cleartree():#to clear treeview
        for item in treevv.get_children():
            treevv.delete(item) 
    def accrecifetch():
        period=drop.get()
        if period=='All dates':
            cleartree()
            accrevalldates()  
        elif period=='Today':
            cleartree()
            accrevtoday() 
        elif period=='Custom':
            global fromdate,todate
            fromdate=dte.get()
            todate=dtee.get()
            cleartree()
            customvalues()   
        elif period=='This month':
            cleartree()
            customvalues()    
        elif period=='This financial year':
            cleartree()
            customvalues()      
    tk.Button(form_frame,text = "Run Report",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command=accrecifetch).place(relx=0.55,rely=0.5,relwidth=0.15)
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
    mycanvass=tk.Canvas(conttframe,width=1200,height=800)
    mycanvass.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(conttframe,orient='vertical',command=mycanvass.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvass.configure(yscrollcommand=yscrollbar.set)
    mycanvass.bind('<Configure>',lambda e:mycanvass.configure(scrollregion=mycanvass.bbox('all')))
    contframe=tk.Frame(mycanvass)
    contframe['bg']='white'
    mycanvass.create_window((0,0),window=contframe,anchor='nw',width=1100,height=2200)
    #table view
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',background='silver',foreground='white',fieldbackground='white')
    treevv = ttk.Treeview(contframe, height=10, columns=(1,2,3,4,5,6,7,8), show='headings') 
    treevv.heading(1, text='CUSTOMER NAME')
    treevv.heading(2, text='TRANSACTION TYPE')#headings
    treevv.heading(3, text='CURRENT')
    treevv.heading(4, text='0-30')
    treevv.heading(5, text='30-60')
    treevv.heading(6, text='60-90')
    treevv.heading(7, text='90 AND OVER')
    treevv.heading(8, text='TOTAL')

    treevv.column(1, minwidth=10, width=120,anchor=CENTER)#coloumns
    treevv.column(2, minwidth=30, width=130,anchor=CENTER)
    treevv.column(3, minwidth=30, width=100,anchor=CENTER)
    treevv.column(4, minwidth=30, width=100,anchor=CENTER)
    treevv.column(5, minwidth=30, width=100,anchor=CENTER)
    treevv.column(6, minwidth=30, width=100,anchor=CENTER)
    treevv.column(7, minwidth=30, width=100,anchor=CENTER)
    treevv.column(8, minwidth=30, width=100,anchor=CENTER)         
    treevv.place(relx=0,rely=0,relwidth=1)  
    def accrevalldates():#all dates
        cursor.execute("SELECT customername, SUM(baldue) FROM invoice WHERE cid=%s GROUP BY customername",([cid]))
        vall=cursor.fetchall()
        trans='Invoice Balance Due'
        try:
            for i in vall:
                treevv.insert('', 'end',values=(i[0],trans,i[1],0,0,0,0,i[1]))
        except:
            pass 
        transs='Credit Note' 
        cursor.execute("SELECT customer,SUM(grndtot) FROM credit WHERE cid =%s GROUP BY customer",([cid]))
        val=cursor.fetchall()   
        try:
            for j in val:
                treevv.insert('', 'end',values=(j[0],transs,j[1],0,0,0,0,j[1]))
        except:
            pass          
    tableframe.place(relx=0.1,rely=0.19,relwidth=0.8,relheight=0.7)
    def accrevtoday():#today values
        cursor.execute("SELECT customername,SUM(baldue) FROM invoice WHERE invoicedate =%s and cid =%s GROUP BY customername",(fromdate,cid))
        vall=cursor.fetchall()
        trans='Invoice Balance Due'
        try:
            for i in vall:
                treevv.insert('', 'end',values=(i[0],trans,i[1],0,0,0,0,i[1]))
        except:
            pass 
        transs='Credit Note' 
        cursor.execute("SELECT customer,SUM(grndtot) FROM credit WHERE creditdate =%s and cid =%s GROUP BY customer",(fromdate,cid))
        val=cursor.fetchall()   
        try:
            for j in val:
                treevv.insert('', 'end',values=(j[0],transs,j[1],0,0,0,0,j[1]))
        except:
            pass 
    def customvalues():#other values
        cursor.execute("SELECT customername,SUM(baldue) FROM invoice WHERE invoicedate BETWEEN %s and %s and cid =%s GROUP BY customername",(fromdate,todate,cid))
        vall=cursor.fetchall()
        trans='Invoice Balance Due'
        try:
            for i in vall:
                    treevv.insert('', 'end',values=(i[0],trans,i[1],0,0,0,0,i[1]))
        except:
            pass  
        transs='Credit Note' 
        cursor.execute("SELECT customer,SUM(grndtot) FROM credit WHERE creditdate BETWEEN %s and %s and cid =%s GROUP BY customer",(fromdate,todate,cid))
        val=cursor.fetchall()   
        try:
            for j in val:
                treevv.insert('', 'end',values=(j[0],transs,j[1],0,0,0,0,j[1]))
        except:
            pass          
   
    prlframe.mainloop()
accrecivabales()   