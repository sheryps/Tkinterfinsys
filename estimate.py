

import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
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
        database='finsYs_tkinter'
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

def cusSelect(event):
    fname=[]
    option2=drop2.get()
    fname.append(option2)
    cus_query="SELECT * FROM `app1_customer` WHERE firstname=%s"
    mycursor.execute(cus_query,fname)
    table1=mycursor.fetchall()
    for a in table1:
        email.set(a[10])
        biladdress.set(a[12:17])
        # print(descrip1.set())

#to save estimate formdata
def save_estimate_data():
        # customer=cust.get()
        # mail=email.get()    
        # biladdr=biladdress.get() 
        # creditno=creditnumber.get()
        # place=placeofsup.get()
        # invnum=invnumb.get()
        # invperiod=inv_period.get()
        # product1=pro1.get()
        # product2=pro2.get()
        # product3=pro3.get()
        # descrip1=descript1.get()
        # descrip2=descript2.get()
        # descrip3=descript3.get()
        # qty1=qnty1.get()
        # qty2=qnty2.get()
        # qty3=qnty3.get()
        # price1=pricee1.get()
        # price2=pricee2.get()
        # price3=pricee3.get()
        # total1=totall1.get()
        # total2=totall2.get()
        # total3=totall3.get()
        # tax1=tax_1.get()
        # tax2=tax_2.get()
        # tax3=tax_3.get()
        # sql= '''INSERT INTO app1_credit (customer,mail,biladdr,creditdate,creditno,place,invnum,invperiod,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%S,%S)''' #adding values into db
        # val=(customer,mail,biladdr,creditno,place,invnum,invperiod,product1,descrip1,qty1,price1,tax1,total1,product2,descrip2,qty2,price2,tax2,total2,product3,descrip3,qty3,price3,total3,tax3)
        # # mycursor.execute(sql,[(mail),(biladdr),(creditno),(place),(invnum),(product1),(product2),(product3),(descrip1),(descrip2),(descrip3),(price1),(price2),(price3),(total1),(total2),(total3),(tax1),(tax2),(tax3)])
        # mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()


estimate_form = tk.Tk()
estimate_form.title("finsYs")
estimate_form.geometry("1000x1000")
estimate_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(estimate_form)
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
credit_heading=Label(heading_frame, text="ESTIMATE",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=headingfont,width=70)
credit_heading.pack()

#form fields
sub_headingfont=font.Font(family='Times New Roman', size=20,)
form_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55')
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
estimate_input=tk.StringVar()
estimate_input=tk.StringVar()
placeofsup=tk.StringVar()
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
cust=tk.StringVar()
# cust.set(table)
place_input=StringVar()
drop2=ttk.Combobox(form_frame)
drop2.set("SELECT CUSTOMER")
drop2['values']=(cus_name)
drop2.bind("<<ComboboxSelected>>",cusSelect)
title_lab.place(x=10,y=100,height=15,width=100)
drop2.place(x=30,y=130,height=40,width=450)
wrappen.pack(fill='both',expand='yes',)

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command=add_custom,)
add_custom.place(x=505,y=130)


emailL=Label(form_frame,text="EMAIL",bg='#243e55',fg='#fff')
emailL.place(x=550,y=100,)
email_input=Entry(form_frame,width=55,bg='#243e55',fg='#fff',textvariable = email)
# email.set()
email_input.place(x=550,y=130,height=40)

billing_ad=Label(form_frame,text="BILLING ADDRESS",bg='#243e55',fg='#fff')
billing_ad.place(x=30,y=200,)
biladdress_input=Entry(form_frame,width=75,bg='#243e55',fg='#fff',textvariable = biladdress)
biladdress_input.place(x=30,y=230,height=90)

estimate_date=Label(form_frame,text="ESTIMATE DATE",bg='#243e55',fg='#fff')
estimate_date.place(x=550,y=200,)
estimate_input=DateEntry(form_frame,width=55,bg='#243e55',fg='#fff')
estimate_input.place(x=550,y=230,height=40)

expiration_date=Label(form_frame,text="EXPIRATION DATE",bg='#243e55',fg='#fff')
expiration_date.place(x=950,y=200,)
estimate_input=DateEntry(form_frame,width=55,bg='#243e55',fg='#fff')
estimate_input.place(x=950,y=230,height=40)

place_of_supp=tk.Label(form_frame,text="PLACE OF SUPPLY",bg='#243e55',fg='#fff')
place_drop=ttk.Combobox(form_frame)
place_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
place_of_supp.place(x=30,y=330,height=15,width=100)
place_drop.place(x=30,y=360,height=40,width=450)



#Billing session
sub_headingfont=font.Font(family='Times New Roman', size=18,)
form2_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,650),window=form2_frame,anchor="nw")

bill_heading=tk.Label(form2_frame, text="",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
bill_heading.place(x=30,y=10,)

label=tk.Label(form2_frame,text="PRODUCT/SERVICE\tHSN\t\tDESCRIPTION\t\tQUANTITY\t\tRATE\t\tTOTAL\t\tTAX\t",bg='#243e55' ,fg="white",font=('Arial',))
label.place(x=60,y=60)

#row1
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product1=ttk.Combobox(form2_frame)
product1['values']=("","","","")
pro.place(x=10,y=120,height=15,width=100)
product1.place(x=60,y=150,height=40,width=150)
#2
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product2=ttk.Combobox(form2_frame)
product2['values']=("","","","")
pro.place(x=10,y=210,height=15,width=100)
product2.place(x=60,y=240,height=40,width=150)
#3
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=10,y=280,height=15,width=100)
pro_drop.place(x=60,y=310,height=40,width=150)

#row 1
hsn_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
hsn_input.place(x=230,y=150,height=40,width=150)
#row2
hsn_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
hsn_input.place(x=230,y=240,height=40,width=150)
#row3
hsn_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
hsn_input.place(x=230,y=310,height=40,width=150)



#row 1
discription_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription_input.place(x=400,y=150,height=40,width=150)
#row2
discription_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription_input.place(x=400,y=240,height=40,width=150)
#row3
discription_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
discription_input.place(x=400,y=310,height=40,width=150)

#row 1
quantity_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input.place(x=600,y=150,height=40,width=150)
#row2
quantity_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input.place(x=600,y=240,height=40,width=150)
#row3
quantity_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input.place(x=600,y=310,height=40,width=150)


#row 1
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input.place(x=780,y=150,height=40,width=150)
#row2
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input.place(x=780,y=240,height=40,width=150)
#row3
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input.place(x=780,y=310,height=40,width=150)

#row 1
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input.place(x=950,y=150,height=40,width=150)
#row2
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input.place(x=950,y=240,height=40,width=150)
#row3
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input.place(x=950,y=310,height=40,width=150)
#row1
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=1250,y=150,height=15,width=150)
pro_drop.place(x=1130,y=150,height=40,width=150)
#row2
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=1110,y=240,height=15,width=150)
pro_drop.place(x=1130,y=240,height=40,width=150)
#row3
pro_drop=ttk.Combobox(form2_frame)
pro_drop['values']=("","","","")
pro.place(x=1000,y=310,height=15,width=150)
pro_drop.place(x=1130,y=310,height=40,width=150)

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

button=tk.Button(form3_frame, text="SAVE",command=save_estimate_data) 
button.place(x=1050,y=280,width=100)

estimate_form.mainloop()
