from enum import auto
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
import tkinter.messagebox
from tkinter.tix import AUTO
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from requests import get
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql
import pymysql
from tkinter.tix import AUTO

# def fun():#db connection
#     global mydb1,mycursor
#     mydb1=mysql.connect(
#         host='localhost',
#         user='root',
#         password='',
#         database='finsYs_tkinter'
#         )
#     mycursor = mydb1.cursor()

# def edit_payslip():  
#     def get_selected_e_product(event):
#         global earn1,dedu1
#         earr6= label1_earr6.get()
#         earr7= label1_earr7.get()
#         print(earr6)
#         print(label1_basic.get())
#         earn1 = int(basic.get()) + int(da.get()) + int(earr1.get()) + int(earr2.get()) + int(earr3.get()) + int(earr4.get())
       
#         print(earn1)
#         gros_pay = earn1 + int(label1_earr6.get()) + int(label1_earr7.get());
#         print(gros)
#         gros.set(gros_pay)
       
#         dedu1 = int(provi.get()) + int(prof.get()) + int(esi.get()) 
#         print(dedu1)
#         total_deduction = dedu1 + int(label1_dedu5.get()) + int(label1_dedu6.get())
#         tded.set(total_deduction)
#         print(tded)
        
#         gio = earn1 - dedu1;
#         net_salary = gio + int(label1_earr6.get()) + int(label1_earr7.get()) - int(label1_dedu5.get()) - int(label1_dedu6.get()) 
#         netsal.set(net_salary)
        
    
        
#     def changing_data():
#         mycursor = mydb1.cursor()
#         user_id=[6]
#         mycursor.execute("SELECT cid FROM app1_company WHERE id_id=%s",(user_id))
#         cmp1=mycursor.fetchone()      
        
#         global empname,employeenumber,desig,fper,tper,paydate,basic,da,ear1,earr1,ear2,earr2,ear3,earr3,ear4,earr4,ear5,earr5,ear6,earr6,ear7,earr7,provi,prof,esi,ded1,dedu1,ded2,dedu2,ded3,dedu3,ded4,dedu4,ded5,dedu5,ded6,dedu6,gros,tded,netsal,cid_id
#         empname=empname.get()
#         employeenumber=employeenumber.get()
#         desig=desig.get()
#         fper=fper.get()
#         tper=tper.get()
#         paydate=paydate.get()
#         basic=basic.get()
#         da=da.get()
#         ear1=ear1.get()
#         earr1=earr1.get()
#         ear2=ear2.get()
#         earr2=earr2.get()
#         ear3=ear3.get()
#         earr3=earr3.get()
#         ear4=ear4.get()
#         earr4=earr4.get()
#         ear5=ear5.get()
#         earr5=earr5.get()
#         ear6=ear6.get()
#         earr6=earr6.get()
#         ear7=ear7.get()
#         earr7=earr7.get()
#         provi=provi.get()
#         prof=prof.get()
#         esi=esi.get()
#         ded1=ded1.get()
#         # dedu1=dedu1.get()
#         ded2=ded2.get()
#         dedu2=dedu2.get()
#         ded3=ded3.get()
#         dedu3=dedu3.get()
#         ded4=ded4.get()
#         dedu4=dedu4.get()
#         ded5=ded5.get()
#         dedu5=dedu5.get()
#         ded6=ded6.get()
#         dedu6=dedu6.get()
#         gros=gros.get()
#         tded=tded.get()
#         netsal=netsal.get()
#         cid_id=cmp1[0]
        
#         mycursor.execute("UPDATE app1_payslip SET empname =%s, employeenumber =%s, desig =%s, fper =%s, tper =%s, paydate =%s, basic =%s, da =%s,ear1 =%s, earr1 =%s, ear2 =%s, earr2 =%s, ear3 =%s,earr3 =%s, ear4 =%s, earr4 =%s, ear5=%s, earr5 =%s, ear6 =%s, earr6 =%s, ear7 =%s, earr7 =%s, provi =%s, prof =%s, esi =%s, ded1 =%s, dedu1 =%s, ded2 =%s, dedu2 =%s, ded3 =%s, dedu3 =%s, ded4 =%s, dedu4 =%s, ded5 =%s, dedu5 =%s, ded6 =%s, dedu6 =%s, gros =%s, tded =%s, netsal =%s, cid_id =%s WHERE payslipid=%s"
#         ,(empname,employeenumber,desig,fper,tper,paydate,basic,da,ear1,earr1,ear2,earr2,ear3,earr3,ear4,earr4,ear5,earr5,ear6,earr6,ear7,earr7,provi,prof,esi,ded1,dedu1,ded2,dedu2,ded3,dedu3,ded4,dedu4,ded5,dedu5,ded6,dedu6,gros,tded,netsal,cid_id,data[0]))
#         mydb1.commit()
#         mydb1.close()
#         messagebox.showinfo('PaySlip edited Added')   

# fun()
# # focus_data = tree_data.focus()
# # values = tree_data.item(focus_data,'values')
# # payslip_id=[values[-1]]
# # mycursor.execute("SELECT * FROM app1_payslip WHERE payslipid=%s",(payslip_id))
# # data=mycursor.fetchone()


root = tk.Tk()
root.title("finsYs")
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")
wrappen=ttk.LabelFrame(root)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=1345,height=2500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas)
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1345,height=2400,bg='#2f516f')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#2f516f",width=100)
form_lable.place(x=0,y=0)

tit = Label(heading_frame, text="EDIT PAY SLIP", font=('times new roman', 28, 'bold'),padx=525, pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()


# global empname,employeenumber,desig,fper,tper,paydate,basic,da,ear1,earr1,ear2,earr2,ear3,earr3,ear4,earr4,ear5,earr5,ear6,earr6,ear7,earr7,provi,prof,esi,ded1,dedu1,ded2,dedu2,ded3,dedu3,ded4,dedu4,ded5,dedu5,ded6,dedu6,gros,tded,netsal
# empname=StringVar() 
# employeenumber=StringVar() 
# desig=StringVar() 
# fper=StringVar() 
# tper=StringVar() 
# paydate=StringVar() 
# basic=StringVar() 
# da=StringVar() 
# ear1=StringVar() 
# earr1=StringVar() 
# ear2=StringVar() 
# earr2=StringVar() 
# ear3=StringVar() 
# earr3=StringVar() 
# ear4=StringVar() 
# earr4=StringVar() 
# ear5=StringVar() 
# earr5=StringVar() 
# ear6=StringVar() 
# earr6=StringVar() 
# ear7=StringVar() 
# earr7=StringVar() 
# provi=StringVar() 
# prof=StringVar() 
# esi=StringVar() 
# ded1=StringVar() 
# dedu1=StringVar() 
# ded2=StringVar() 
# dedu2=StringVar() 
# ded3=StringVar() 
# dedu3=StringVar() 
# ded4=StringVar() 
# dedu4=StringVar() 
# ded5=StringVar() 
# dedu5=StringVar() 
# ded6=StringVar() 
# dedu6=StringVar() 
# gros=StringVar() 
# tded=StringVar() 
# netsal=StringVar() 

# existing_empname=data[1]
# empname.set(existing_empname)

# existing_employeenumber=data[2]
# employeenumber.set(existing_employeenumber)

# existing_desig=data[3]
# desig.set(existing_desig)

# existing_fper=data[4]
# fper.set(existing_fper)

# existing_tper=data[5]
# tper.set(existing_tper)

# existing_paydate=data[6]
# paydate.set(existing_paydate)

# existing_basic=data[7]
# basic.set(existing_basic)

# existing_da=data[8]
# da.set(existing_da)

# existing_ear1=data[9]
# ear1.set(existing_ear1)

# existing_earr1=data[10]
# earr1.set(existing_earr1)

# existing_ear2=data[11]
# ear2.set(existing_ear2)

# existing_earr2=data[12]
# earr2.set(existing_earr2)

# existing_ear3=data[13]
# ear3.set(existing_ear3)

# existing_earr3=data[14]
# earr3.set(existing_earr3)

# existing_ear4=data[15]
# ear4.set(existing_ear4)

# existing_earr4=data[16]
# earr4.set(existing_earr4)

# existing_ear5=data[17]
# ear5.set(existing_ear5)

# existing_earr5=data[18]
# earr5.set(existing_earr5)

# existing_ear6=data[19]
# ear6.set(existing_ear6)

# existing_earr6=data[20]
# earr6.set(existing_earr6)

# existing_ear7=data[21]
# ear7.set(existing_ear7)

# existing_earr7=data[22]
# earr7.set(existing_earr7)

# existing_provi=data[23]
# provi.set(existing_provi)

# existing_prof=data[24]
# prof.set(existing_prof)

# existing_esi=data[25]
# esi.set(existing_esi)

# existing_ded1=data[26]
# ded1.set(existing_ded1)

# existing_dedu1=data[27]
# dedu1.set(existing_dedu1)

# existing_ded2=data[28]
# ded2.set(existing_ded2)

# existing_dedu2=data[29]
# dedu2.set(existing_dedu2)

# existing_ded3=data[30]
# ded3.set(existing_ded3)

# existing_dedu3=data[31]
# dedu3.set(existing_dedu3)

# existing_ded4=data[32]
# ded4.set(existing_ded4)

# existing_dedu4=data[33]
# dedu4.set(existing_dedu4)

# existing_ded5=data[34]
# ded5.set(existing_ded5)

# existing_dedu5=data[35]
# dedu5.set(existing_dedu5)

# existing_ded6=data[36]
# ded6.set(existing_ded6)

# existing_dedu6=data[37]
# dedu6.set(existing_dedu6)

# existing_gros=data[38]
# gros.set(existing_gros)

# existing_tded=data[39]
# tded.set(existing_tded)

# existing_netsal=data[40]
# netsal.set(existing_netsal)



F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=30, pady=30, bd=0, fg="Black", bg="#243e55")
F.place(x=30, y=30, width=1270, height=1950)

label1=Label(F, text="MAP Creations", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=500,y=1)

label2=Label(F, text="Employee Name", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=100,y=90)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable='empname')
label2.place(x=100,y=130,height=40,width=300)

label3=Label(F, text="Employee Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=90)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable='employeenumber')
label3.place(x=450,y=130,height=40,width=300)

label4=Label(F, text="Designation", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=90)
label4=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig')
label4.place(x=800,y=130,height=40,width=300)

label2=Label(F, text="Pay Peried - From", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=100,y=190)
label2 = DateEntry(F, width= 28, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable='fper')
label2.place(x=100,y=230)

label3=Label(F, text="To", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=190)
label3 = DateEntry(F, width= 28, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable='tper')
label3.place(x=450,y=230)

label4=Label(F, text="Date of Payment", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=190)
label4 = DateEntry(F, width= 28, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable='paydate')
label4.place(x=800,y=230)

label1=Label(F, text="Salary Details", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=500,y=400)

label1=Label(F, text="Earnings", font=('times new roman', 17, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=200,y=500)

label1=Label(F, text="Basic Salary", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=40,y=580)
label1_basic=Entry(F,bg='#2f516a',fg='#fff',textvariable='basic')
label1_basic.place(x=280,y=580,height=40,width=230)
label1_basic.configure(state='disabled')

label1_da=Label(F, text="Dearance Allowance", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1_da.place(x=40,y=640)
label1_da=Entry(F,bg='#2f516a',fg='#fff',textvariable='da')
label1_da.place(x=280,y=640,height=40,width=230)
label1_da.configure(state='disabled')

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ear1')
label1.place(x=40,y=700,height=40,width=230)
label1_earr1=Entry(F,bg='#2f516a',fg='#fff',textvariable='earr1')
label1_earr1.place(x=280,y=700,height=40,width=230)
label1_earr1.configure(state='disabled')

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ear2')
label1.place(x=40,y=760,height=40,width=230)
label1_earr2=Entry(F,bg='#2f516a',fg='#fff',textvariable='earr2')
label1_earr2.place(x=280,y=760,height=40,width=230)
label1_earr2.configure(state='disabled')

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ear3')
label1.place(x=40,y=820,height=40,width=230)
label1_earr3=Entry(F,bg='#2f516a',fg='#fff',textvariable='earr3')
label1_earr3.place(x=280,y=820,height=40,width=230)
label1_earr3.configure(state='disabled')

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ear4')
label1.place(x=40,y=880,height=40,width=230)
label1_earr4=Entry(F,bg='#2f516a',fg='#fff',textvariable='earr4')
label1_earr4.place(x=280,y=880,height=40,width=230)
label1_earr4.configure(state='disabled')

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ear6')
label1.place(x=40,y=940,height=40,width=230)
# earr6.set("0")
label1_earr6=Entry(F,bg='#2f516a',fg='#fff',textvariable='earr6')
label1_earr6.place(x=280,y=940,height=40,width=230)
# label1_earr6.bind("<KeyRelease>",get_selected_e_product)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ear7')
label1.place(x=40,y=1000,height=40,width=230)
# earr7.set('0')
label1_earr7=Entry(F,bg='#2f516a',fg='#fff',textvariable='earr7')
label1_earr7.place(x=280,y=1000,height=40,width=230)
# label1_earr7.bind("<KeyRelease>",get_selected_e_product)



label1=Label(F, text="Deduction", font=('times new roman', 17, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=850,y=500)

label1=Label(F, text="Provident Fund", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=580)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='provi')
label1.place(x=940,y=580,height=40,width=230)
label1.configure(state='disabled')

label1=Label(F, text="Profession Tax", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=640)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='prof')
label1.place(x=940,y=640,height=40,width=230)
label1.configure(state='disabled')

label1=Label(F, text="ESI", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=700)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='esi')
label1.place(x=940,y=700,height=40,width=230)
label1.configure(state='disabled')

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ded5')
label1.place(x=700,y=760,height=40,width=230)
# dedu5.set("0")
label1_dedu5=Entry(F,bg='#2f516a',fg='#fff',textvariable='dedu5')
label1_dedu5.place(x=940,y=760,height=40,width=230)
# label1_dedu5.bind("<KeyRelease>",get_selected_e_product)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable='ded6')
label1.place(x=700,y=820,height=40,width=230)
# dedu6.set('0')
label1_dedu6=Entry(F,bg='#2f516a',fg='#fff',textvariable='dedu6')
label1_dedu6.place(x=940,y=820,height=40,width=230)
# label1_dedu6.bind("<KeyRelease>",get_selected_e_product)

label1=Label(F, text="Gross Pay", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1080)
label1_gros=Entry(F,bg='#2f516a',fg='#fff',textvariable='gros')
label1_gros.place(x=900,y=1080,height=40,width=270)
# label1_gros.bind("<KeyRelease>",get_selected_e_product)

label1=Label(F, text="Total Deduction", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1140)
label1_tded=Entry(F,bg='#2f516a',fg='#fff',textvariable='tded')
label1_tded.place(x=900,y=1140,height=40,width=270)
# label1_tded.bind("<KeyRelease>",get_selected_e_product)

label1=Label(F, text="Net Salary", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1200)
label1_netsal=Entry(F,bg='#2f516a',fg='#fff',textvariable='netsal')
label1_netsal.place(x=900,y=1200,height=40,width=270)
# label1_netsal.bind("<KeyRelease>",get_selected_e_product)

b1 = Button(F,text = "Update Payslip",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command='changing_data')  
b1.place(x=470,y=1350,width=300,height=40) 

wrappen.pack(fill='both',expand='yes',)




root.mainloop()



