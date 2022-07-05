
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter.tix import Select
import mysql.connector
from tkcalendar import DateEntry

#importing customer page to select the customer
def add_custom():
    import add_new_customer

#db connects here **
# def db_connection():
# global mydb,mycursor
mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        port='3308',
        database='finsys_tkinter'
        )
mycursor = mydb.cursor()
cus_name= []
#fetching customer data
customer_query="SELECT firstname FROM `app1_customer`"
mycursor.execute(customer_query)
table=mycursor.fetchall()
for a in table:
    data = (a[0])
    cus_name.append(data)
    print(data)

#select emails
def get_email(event):
    option=drop2.get()
    mail_query="SELECT * FROM `app1_customer`"
    mycursor.execute(mail_query,option)
    table2=mycursor.fetchall()
    for i in table2:
        email.set(i[9])
        biladdress.set(i[12:16])
        invnumb.set()
    print(email)

def get_invno():
    option=drop2.get()
    invquery="SELECT * FROM `app1_invoice` Where cid=%s"
    mycursor.execute(invquery,option)
    table3=mycursor.fetchall()
    for i in table3:
        invnumb.set(table3)


#select invoice no from backend
inv_no= []
#fetching invoice no
inv_query="SELECT invoiceno FROM `app1_invoice`"
mycursor.execute(inv_query)
table3=mycursor.fetchall()
for a in table3:
    data = (a[0])
    inv_no.append(data)
    print(data)

#fetching product from backend
inventory=[]
inventory_query="SELECT * FROM `app1_inventory`"
mycursor.execute(inventory_query)
table4=mycursor.fetchall()
for a in table4:
    data = (a[2])
    inventory.append(data)
    print(data)

#selecting and fetching from products
def ProSelect(event):
    selected_data=[]
    option3=product1.get()
    selected_data.append(option3)
    inventory_query2="SELECT * FROM `app1_inventory` WHERE name=%s"
    mycursor.execute(inventory_query2,selected_data)
    table5=mycursor.fetchall()
    for a in table5:
        descrip1.set(a[11])
        pricee1.set(a[12])
        print(descrip1.set())

#to save credit formdata
def save_credit_data():
        # db_connection()
        customer=cust.get()      
        mail=email.get()
        biladdr=biladdress.get() 
        creditno=creditnumber.get()
        place=placeofsup.get()
        invnum=invnumb.get()
        invperiod=inv_period.get()
        product1=pro1.get()
        product2=pro2.get()
        product3=pro3.get()
        descrip1=descript1.get()
        descrip2=descript2.get()
        descrip3=descript3.get()
        qty1=qnty1.get()
        qty2=qnty2.get()
        qty3=qnty3.get()
        price1=pricee1.get()
        price2=pricee2.get()
        price3=pricee3.get()
        total1=totall1.get()
        total2=totall2.get()
        total3=totall3.get()
        tax1=tax_1.get()
        tax2=tax_2.get()
        tax3=tax_3.get()
        sql= '''INSERT INTO app1_credit (customer,mail,biladdr,creditdate,creditno,place,invnum,invperiod,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%S,%S)''' #adding values into db
        val=(customer,mail,biladdr,creditno,place,invnum,invperiod,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3)
        # mycursor.execute(sql,[(mail),(biladdr),(creditno),(place),(invnum),(product1),(product2),(product3),(descrip1),(descrip2),(descrip3),(price1),(price2),(price3),(total1),(total2),(total3),(tax1),(tax2),(tax3)])
        mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()


#ihsdjrifjsiof
credit_form = tk.Tk()
credit_form.title("finsYs")
credit_form.geometry("1000x1000")
credit_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(credit_form)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=1600,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((0,40),window=heading_frame,anchor="nw")
headingfont=font.Font(family='Times New Roman', size=25,)
credit_heading=Label(heading_frame, text="CREDIT NOTE",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=headingfont,width=70)
credit_heading.pack()


#form fields
sub_headingfont=font.Font(family='Times New Roman', size=20,)
form_frame=Frame(mycanvas,width=1600,height=700,bg='#243e55')
mycanvas.create_window((0,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=100)
form_lable.place(x=0,y=0)
form_heading=tk.Label(form_lable, text="fin sYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=sub_headingfont,width=80)
form_heading.pack()

#declaring global variables

email=tk.StringVar()
# email.set(table2)
biladdress=tk.StringVar()
creditnumber=tk.StringVar()
placeofsup=tk.StringVar()
invnumb=tk.StringVar()
inv_period=tk.StringVar()
product1=tk.StringVar()
pro1=tk.StringVar()
pro2=tk.StringVar()
pro3=tk.StringVar()
descrip1=tk.StringVar()
descript2=tk.StringVar()
descript3=tk.StringVar()
qnty1=tk.StringVar()
qnty2=tk.StringVar()
qnty3=tk.StringVar()
pricee1=tk.StringVar()
pricee2=tk.StringVar()
pricee3=tk.StringVar()
totall1=tk.StringVar()
totall2=tk.StringVar()
totall3=tk.StringVar()
tax_1=tk.StringVar()
tax_2=tk.StringVar()
tax_3=tk.StringVar() 

title_lab=tk.Label(form_frame,text="CUSTOMER",bg='#243e55',fg='#fff')
title_lab.place(x=10,y=100,height=15,width=100)
cust=tk.StringVar()
cust.set(table)
place_input=StringVar()
drop2=ttk.Combobox(form_frame)
drop2.set("SELECT CUSTOMER")
drop2['values']=(cus_name)
drop2.bind("<<ComboboxSelected>>",get_email)
drop2.place(x=30,y=130,height=40,width=450)
wrappen.pack(fill='both',expand='yes',)

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command=add_custom,)
add_custom.place(x=505,y=130)

mailLab=Label(form_frame,text="EMAIL",bg='#243e55',fg='#fff')
mailLab.place(x=560,y=100,)
mail=Entry(form_frame,width=55,bg='#243e55',fg='#fff',textvariable=email)
mail.place(x=560,y=130,height=40)

biladdrLab=Label(form_frame,text="BILLING ADDRESS",bg='#243e55',fg='#fff')
biladdrLab.place(x=30,y=200,)
biladdr=Entry(form_frame,width=75,bg='#243e55',fg='#fff',textvariable=biladdress)
biladdr.place(x=30,y=230,height=90)

credit_note=Label(form_frame,text="CREDIT NOTE DATE",bg='#243e55',fg='#fff')
credit_note.place(x=560,y=200,)
creditno=DateEntry(form_frame,width=55,bg='#243e55',fg='#fff')
creditno.place(x=560,y=230,height=40)

place_of_supp=tk.Label(form_frame,text="PLACE OF SUPPLY",bg='#243e55',fg='#fff')
place=ttk.Combobox(form_frame,textvariable=placeofsup)
place['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
place_of_supp.place(x=20,y=330,height=15,width=100)
place.place(x=30,y=360,height=40,width=450)

invoice_period=tk.Label(form_frame,text="INVOICE PERIOD",bg='#243e55',fg='#fff')
invoice_drop=ttk.Combobox(form_frame,textvariable=inv_period)
invoice_drop['values']=("OCT2022-DEC2022","july2022-sept2022","april2022-june2022","jan2022-march2022","oct2021-dec20221","july2021-sept2021","april2021-june2021,jan2021-march2022")
invoice_period.place(x=20,y=440,height=15,width=100)
invoice_drop.place(x=30,y=460,height=40,width=450)

invoice_no=tk.Label(form_frame,text="SELECT INVOICE NO",bg='#243e55',fg='#fff')
invnum=ttk.Combobox(form_frame,textvariable=invnumb)
invnum['values']=(inv_no)
invnum.set("SELECT INVOICE NO")
invoice_no.place(x=560,y=330,height=15,width=100)
invnum.place(x=560,y=360,height=40,width=450)



#Billing session
sub_headingfont=font.Font(family='Times New Roman', size=18,)
form2_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,750),window=form2_frame,anchor="nw")

bill_heading=tk.Label(form2_frame, text="",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
bill_heading.place(x=30,y=10,)

label=tk.Label(form2_frame,text="PRODUCT/SERVICE\t\tDESCRIPTION\t\tQUANTITY\t\tPRICE\t\tTOTAL\t\tTAX\t",bg='#243e55' ,fg="white",font=('Arial',))
label.place(x=5,y=20)

#row1
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product1=ttk.Combobox(form2_frame,textvariable=product1)
product1['values']=(inventory)
product1.bind("<<ComboboxSelected>>",ProSelect)
# product1.set(a[2])
product1.set("SELECT PRODUCT")
pro.place(x=10,y=120,height=15,width=100)
product1.place(x=10,y=150,height=40,width=150)
#2
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product2=ttk.Combobox(form2_frame,textvariable=pro2)
product2['values']=("","","","")
pro.place(x=10,y=210,height=15,width=100)
product2.place(x=10,y=240,height=40,width=150)
#3
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product3=ttk.Combobox(form2_frame,textvariable=pro3)
product3['values']=("","","","")
pro.place(x=10,y=280,height=15,width=100)
product3.place(x=10,y=310,height=40,width=150)



#row 1
descript1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descrip1)
descript1.place(x=260,y=150,height=40,width=180)
#row2
descrip2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descript2)
descrip2.place(x=260,y=240,height=40,width=180)
#row3
descrip3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descript3)
descrip3.place(x=260,y=310,height=40,width=180)

#row 1
qty1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qnty1)
qty1.place(x=480,y=150,height=40,width=150)
#row2
qty2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qnty2)
qty2.place(x=480,y=240,height=40,width=150)
#row3
qty3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qnty3)
qty3.place(x=480,y=310,height=40,width=150)


#row 1
price1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=pricee1)
price1.place(x=680,y=150,height=40,width=150)
#row2
price2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=pricee3)
price2.place(x=680,y=240,height=40,width=150)
#row3
price3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=pricee3)
price3.place(x=680,y=310,height=40,width=150)

#row 1
total1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=totall1)
total1.place(x=850,y=150,height=40,width=100)
#row2
total2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=totall2)
total2.place(x=850,y=240,height=40,width=100)
#row3
total3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=totall3)
total3.place(x=850,y=310,height=40,width=100)
#row1
tax1=ttk.Combobox(form2_frame,textvariable=tax_1)
tax1['values']=("","","","")
tax1.place(x=1250,y=150,height=15,width=150)
tax1.place(x=1000,y=150,height=40,width=150)
#row2
tax2=ttk.Combobox(form2_frame,textvariable=tax_2)
tax2['values']=("","","","")
tax2.place(x=1110,y=240,height=15,width=150)
tax2.place(x=1000,y=240,height=40,width=150)
#row3
tax3=ttk.Combobox(form2_frame,textvariable=tax_3)
tax3['values']=("","","","")
tax3.place(x=1000,y=310,height=15,width=150)
tax3.place(x=1000,y=310,height=40,width=150)

##################

sub_headingfont=font.Font(family='Times New Roman', size=18,)
form3_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,1100),window=form3_frame,anchor="nw")

sub_total=Label(form3_frame,text="SUB TOTAL",bg='#243e55',fg='#fff')
sub_total.place(x=900,y=110)
sub_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff')
sub_input.place(x=1000,y=100,height=40,width=200)

tax_amount=Label(form3_frame,text="TAX AMOUNT",bg='#243e55',fg='#fff')
tax_amount.place(x=900,y=160)
tax_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff')
tax_input.place(x=1000,y=150,height=40,width=200)

grand_total=Label(form3_frame,text="GRAND TOTAL",bg='#243e55',fg='#fff')
grand_total.place(x=900,y=210)
grand_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff')
grand_input.place(x=1000,y=200,height=40,width=200)




button=tk.Button(form3_frame, text="SAVE",command=save_credit_data) 
button.place(x=1050,y=280,width=100)

credit_form.mainloop()
