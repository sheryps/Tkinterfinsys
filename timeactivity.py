import tkinter as tk
from xml.dom.minicompat import StringTypes
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
cur=mydata.cursor()
#sherryag
def time():
    def getdetails():
        date=timedate.get()
        name=timename.get()
        cus=timecus.get()
        checkbill=timebill.get()
        bill=timbill.get()
        timecheck=time.get()
        starttime=hr.get()+':'+min.get()
        endtime=eh.get()+':'+em.get()
        ttime=timeh.get()+':'+timem.get()
        text=timetext.get("1.0","end")
        tg='''INSERT INTO timeactivity (timdate,timname,timcus,timcheck,timebill,timecheckk,timestart,timeend,tyme,timedes) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cur.execute(tg,[(date),(name),(cus),(checkbill),(bill),(timecheck),(starttime),(endtime),(ttime),(text)])
        #print(date,name,cus,checkbill,bill,timecheck,starttime,endtime,ttime,text)
        mydata.commit()
        win.destroy()
    win=tk.Tk()
    win.title('Time Activity')
    win.geometry('1500x1000')
    win['bg'] = '#2f516f'
    f1=tk.Frame(win,bg='#243e54')
    tk.Label(f1,text='Time Activity',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
    f1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    f2=tk.Frame(win,bg='#243e54')
    size=(400,500)
    ax=ImageTk.PhotoImage(Image.open('time.png').resize(size))
    tk.Label(f2,image=ax,bg='#243e54').place(relx=0.05,rely=0.05,relheight=0.8,relwidth=0.2)

    tk.Label(f2,text='Date',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.1)
    timedate=StringVar()
    DateEntry(f2,textvariable=timedate).place(relx=0.3,rely=0.16,relwidth=0.3,relheight=0.05)

    tk.Label(f2,text='Name',font=('times new roman', 14),bg='#2f516f').place(relx=0.65,rely=0.1)
    timename=StringVar()
    tk.Entry(f2,textvariable=timename).place(relx=0.65,rely=0.16,relwidth=0.3,relheight=0.05)

    tk.Label(f2,text='Customer',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.25)   
    def comboinput():
        cur.execute("SELECT firstname,lastname FROM customer")
        val=cur.fetchall()         
        for row in val:
            tm.append(row[0]+row[1])
    global tm  
    tm=['Select Customer']
    comboinput()     
    timecus=ttk.Combobox(f2,values=tm)
    timecus.current(0)  
    timecus.place(relx=0.3,rely=0.31,relwidth=0.65,relheight=0.05)
    
    tk.Label(f2,text='Billable(/hr)',font=('times new roman', 12),bg='#2f516f').place(relx=0.3,rely=0.4)
    bl=['Yes','No']
    timebill=ttk.Combobox(f2,values=bl)
    timebill.place(relx=0.38,rely=0.4,relwidth=0.18,relheight=0.05)
    print(timebill.get())

    timbill=StringVar()
    tk.Entry(f2,textvariable=timbill).place(relx=0.58,rely=0.4,relwidth=0.18,relheight=0.05)

    tk.Label(f2,text='Enter start and end time',font=('times new roman', 12),bg='#2f516f').place(relx=0.3,rely=0.5)
    time=ttk.Combobox(f2,values=bl)
    time.place(relx=0.43,rely=0.5,relwidth=0.05,relheight=0.05)

    tk.Label(f2,text='Start time',font=('times new roman', 12),bg='#2f516f').place(relx=0.55,rely=0.5)
    hr=StringVar()
    min_sb = tk.Spinbox(f2,from_=0,to=23,wrap=True,state="readonly",textvariable=hr).place(relx=0.61,rely=0.5,relwidth=0.05,relheight=0.05)
    min=StringVar()
    sec_sb = tk.Spinbox(f2,from_=0,to=59,wrap=True,state="readonly",textvariable=min).place(relx=0.66,rely=0.5,relwidth=0.05,relheight=0.05)

    tk.Label(f2,text='Endtime',font=('times new roman', 12),bg='#2f516f').place(relx=0.72,rely=0.5)
    eh=StringVar()
    em=StringVar()
    emin_sb = tk.Spinbox(f2,from_=0,to=23,wrap=True,state="readonly",textvariable=eh).place(relx=0.77,rely=0.5,relwidth=0.05,relheight=0.05)
    esec_sb = tk.Spinbox(f2,from_=0,to=59,wrap=True,state="readonly",textvariable=em).place(relx=0.82,rely=0.5,relwidth=0.05,relheight=0.05)

    tk.Label(f2,text='Time',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.58)
    timeh=StringVar()
    timem=StringVar()
    temin_sb = tk.Spinbox(f2,from_=0,to=23,wrap=True,state="readonly",textvariable=timeh).place(relx=0.3,rely=0.65,relwidth=0.325,relheight=0.05)
    tsec_sb = tk.Spinbox(f2,from_=0,to=59,wrap=True,state="readonly",textvariable=timem).place(relx=0.625,rely=0.65,relwidth=0.3,relheight=0.05)

    tk.Label(f2,text='Description',font=('times new roman', 14),bg='#2f516f').place(relx=0.3,rely=0.71)
    timetext=tk.Text(f2)
    timetext.place(relx=0.3,rely=0.78,relwidth=0.65,relheight=0.1)
    
    tk.Button(f2,text='Submit Form',font=('times new roman', 16),bg='#2f516f',command=getdetails).place(relx=0.45,rely=0.92,relwidth=0.2,relheight=0.05)
    f2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.7)
    win.mainloop()
time()    