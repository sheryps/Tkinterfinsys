import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql

def fun():#db connection
    global mydb2,mycursor
    mydb2=mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='finsYs_tkinter'
        )
    mycursor = mydb2.cursor()

def add_custom():
    import addcustomer_form

    print("hellboy111")   
    global recon_data
    # global tree_data
    focus_data = tree_data.focus()
    values=tree_data.item(focus_data,'values')
    recon1_id=[values[-1]]
    mycursor.execute("SELECT * FROM app1_recon1 WHERE recon1id=%s",(recon1_id))
    data=mycursor.fetchone()
    print("hellboy")
   
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

full_frame=Frame(mycanvas,width=1345,height=2200,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas)
mycanvas.create_window((0,0),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1300,height=1900,bg='#243e55')
mycanvas.create_window((20,60),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#243e55",width=100)
form_lable.place(x=0,y=0)
fun()
mycursor.execute('select * from app1_recon1 ')
customers=mycursor.fetchall()
customers_data=[-1]
for cus in customers:
    customers_data.append(cus)

fun()
# global accounttype,endingdate,endingbalance,beginningbalance,serchar,intear,Clearbalance,difference

accounttype=StringVar(form_frame) 
endingdate=StringVar(form_frame) 
endingbalance=StringVar(form_frame)
beginningbalance=StringVar(form_frame)
serchar=StringVar(form_frame)
intear=StringVar(form_frame)
Clearbalance=StringVar(form_frame)
difference=StringVar(form_frame)

data=customers_data[-1]
print(data)


existing_accounttype=data[1]
accounttype.set(existing_accounttype)

existing_endingdate=data[4]
endingdate.set(existing_endingdate)

existing_endingbalance=data[3]
endingbalance.set(existing_endingbalance)

existing_beginningbalance=data[2]
beginningbalance.set(existing_beginningbalance)

existing_serchar=data[6]
serchar.set(existing_serchar)

existing_intear=data[9]
intear.set(existing_intear)

begbal = int(data[2])
ser = int(data[6])
inte = int(data[9])

findbalance = begbal - ser + inte
Clearbalance.set(findbalance)

difference1 = int(existing_endingbalance) - int(findbalance)
difference.set(difference1)

san_lbl = Label(form_frame, text="Reconcile", font=('times new roman', 20, 'bold'), bg="#243e55", fg="#fff")
san_lbl.place(x=500)
san_lbl = Label(form_frame, text="", font=('times new roman', 20, 'bold'), bg="#243e55", fg="#fff",textvariable=accounttype)
san_lbl.place(x=620)
san_lbl = Label(form_frame, text="Statement ending date", font=('times new roman', 11, 'bold'),width=26, bg="#243e55", fg="#fff")
san_lbl.place(x=500,y=55)
san_lbl = Label(form_frame, textvariable=endingdate, font=('times new roman', 11, 'bold'),width=26, bg="#243e55", fg="#fff")
san_lbl.place(x=500,y=75)

# Label Widget
a = Label(form_frame, bg="#243e55", fg="#fff",font=('times new roman', 10, 'bold'))
a.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.4)
san1_lbl = Label(a, textvariable=endingbalance, font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san1_lbl.grid(row=1, column=0, padx=10, pady=0, sticky='W')
san2_lbl = Label(a, text="STATEMENT ENDING BALANCE", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san2_lbl.grid(row=2, column=0, padx=10, pady=0, sticky='W')
san3_lbl = Label(a, text="-", font=('times new roman', 25, 'bold'), bg="#243e55", fg="#fff")
san3_lbl.grid(row=1, column=1, padx=10, pady=0, sticky='W')
san4_lbl = Label(a, textvariable=Clearbalance, font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san4_lbl.grid(row=1, column=2, padx=10, pady=0, sticky='W')
san5_lbl = Label(a, text="CLEARED BALANCE", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san5_lbl.grid(row=2, column=2, padx=10, pady=0, sticky='W')

a1 = Label(form_frame, bg="#243e55", fg="#fff",font=('times new roman', 10, 'bold'))
a1.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.4)
san6_lbl = Label(a1, textvariable=beginningbalance, font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san6_lbl.grid(row=1, column=0, padx=10, pady=0, sticky='W')
san7_lbl = Label(a1, text="BEGINNING BALANCE", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san7_lbl.grid(row=2, column=0, padx=10, pady=0, sticky='W')
san8_lbl = Label(a1, text="-", font=('times new roman', 25, 'bold'), bg="#243e55", fg="#fff")
san8_lbl.grid(row=1, column=1, padx=10, pady=0, sticky='W')
san9_lbl = Label(a1, textvariable=serchar, font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san9_lbl.grid(row=1, column=2, padx=10, pady=0, sticky='W')
san10_lbl = Label(a1, text="PAYMENTS", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san10_lbl.grid(row=2, column=2, padx=10, pady=0, sticky='W')
san11_lbl = Label(a1, text="+", font=('times new roman', 25, 'bold'), bg="#243e55", fg="#fff")
san11_lbl.grid(row=1, column=3, padx=10, pady=0, sticky='W')
san12_lbl = Label(a1, textvariable=intear, font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san12_lbl.grid(row=1, column=4, padx=10, pady=0, sticky='W')
san13_lbl = Label(a1, text="DEPOSITS", font=('times new roman', 13, 'bold'), bg="#243e55", fg="#fff")
san13_lbl.grid(row=2, column=4, padx=10, pady=0, sticky='W')

# Separator object
separator = ttk.Separator(form_frame, orient='vertical')
separator.place(relx=0.70, rely=0.1, relwidth=0.2, relheight=0.1)
# Label Widget
san14_lbl = Label(separator, font=('times new roman', 10, 'bold'),fg="#fff")
san14_lbl.grid(row=1, column=4, padx=10, pady=0, sticky='W')
san15_lbl = Label(separator, font=('times new roman', 10, 'bold'), fg="#fff")
san15_lbl.grid(row=2, column=4, padx=10, pady=0, sticky='W')
san16_lbl = Label(separator, textvariable=difference, font=('times new roman', 14, 'bold'), fg="#243e55")
san16_lbl.grid(row=3, column=8, padx=10, pady=0, sticky='W')
san17_lbl = Label(separator, text="DIFFERENCES", font=('times new roman', 14, 'bold'), fg="#243e55")
san17_lbl.grid(row=4, column=8, padx=10, pady=0, sticky='W')

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F.place(x=25, y=600, width=1250, height=400)

b = Button(F,text = "Payments",bg="#243e55",fg="#fff",font=('times new roman', 12, 'bold'))  
b.place(x=500,y=5,width=200,height=40) 
b = Button(F,text = "Deposits",bg="#243e55",fg="#fff",font=('times new roman', 12, 'bold'))  
b.place(x=700,y=5,width=200,height=40) 
b = Button(F,text = "All",bg="#243e55",fg="#fff",font=('times new roman', 12, 'bold'))  
b.place(x=900,y=5,width=100,height=40) 

F1 = LabelFrame(F, font=('times new roman', 15, 'bold'),fg="Black", bg="#243e55")
F1.place(x=0, y=47, width=1235, height=325)

# global tree_data
tree_data = ttk.Treeview(F1,height=13)
tree_data['show'] = 'headings'

sb = ttk.Scrollbar(F1, orient="vertical", command=tree_data.yview)
sb.grid(row=3,column=1,sticky="NS",pady=5)

tree_data.configure(yscrollcommand=sb.set)

tree_data["columns"]=("1","2","3","4","5","6","7","8")

tree_data.column("1", width=130)
tree_data.column("2", width=150)
tree_data.column("3", width=150)
tree_data.column("4", width=155)
tree_data.column("5", width=155)
tree_data.column("6", width=155)
tree_data.column("7", width=155)
tree_data.column("8", width=155)

tree_data.heading("1", text="DATE")
tree_data.heading("2", text="TYPE")
tree_data.heading("3", text="REF NO.")
tree_data.heading("4", text="ACCOUNT")
tree_data.heading("5", text="PAYEE")
tree_data.heading("6", text="MEMO")
tree_data.heading("7", text="DEPOSIT(INR)")
tree_data.heading("8", text="PAYMENT(INR)")

sql = 'SELECT edat,accounttype,recon1id,expacc,beginningbalance,serchar,intear,serchar,recon1id from app1_recon1'
mycursor.execute(sql)
treed_data=mycursor.fetchall()
total=mycursor.rowcount

for data in treed_data:
    tree_data.insert("", 'end',values=data)
    
tree_data.grid(row=3,column=0,padx=5,pady=10)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

root.mainloop()





