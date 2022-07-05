
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkcalendar import DateEntry
import mysql.connector


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


#invetory data
mycursor.execute("SELECT * FROM app1_inventory WHERE cid_id=%s")
inventory_data=mycursor.fetchall()

#bundle data
mycursor.execute("SELECT * FROM app1_bundle WHERE cid_id=%s")
bundle_data=mycursor.fetchall()

#noninventor data
mycursor.execute("SELECT * FROM app1_noninventory WHERE cid_id=%s")
noninventory_data=mycursor.fetchall()

#service data
mycursor.execute("SELECT * FROM app1_service WHERE cid_id=%s")
services_data=mycursor.fetchall()

#fetching product datas from database
def get_selected_product(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4,final_total
        createsubtotal =0
        finding_tax1=0
        finding_tax2=0
        finding_tax3=0
        finding_tax4=0
        final_total=0
        selected_product=[]
        product=product1.get()
        quantity=quantity_input1.get()
        selected_product.append(product)
        for product in inventory_data:
            product_details="SELECT * FROM app1_inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn.set(i[4])
                desc.set(i[11])
                price.set(i[12])
                sale_price=i[12]
                tota_price=int(sale_price)*int(quantity)
                total.set(tota_price)
        for product in noninventory_data:
            product_details="SELECT * FROM app1_noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn.set(i[4])
                desc.set(i[7])
                price.set(i[8])
                sale_price=i[8]
                tota_price=int(sale_price)*int(quantity)
                total.set(tota_price) 
        
        for product in bundle_data:
            product_details="SELECT * FROM app1_bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn.set(i[4])
                desc.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                price.set(sale_price)
                
                tota_price=int(sale_price)*int(quantity)
                total.set(tota_price)   
        createsubtotal=int(total.get())+int(total2.get())+int(total3.get())
        subtotal.set(createsubtotal)
        #get selected gst then find tax amount thenset it 
        gst=tax_drop1.get()

        if gst=="18.0% GST(18%)":
            print("totla",tota_price)
            finding_tax1=int(tota_price)*(18/100)
        elif gst=="28.0% GST(28%)":
            finding_tax1=int(tota_price)*(28/100)
            
        elif gst=="12.0% GST(12%)":
            finding_tax1=int(tota_price)*(12/100)
            
        elif gst=="06.0% GST(06%)":
            finding_tax1=int(tota_price)*(6/100)
            
        elif gst=="05.0% GST(05%)":
            finding_tax1=int(tota_price)*(5/100)
            
        elif gst=="03.0% GST(03%)":
            finding_tax1=int(tota_price)*(3/100)
            
        else:
            finding_tax1=0
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        taxamount.set(finding_tax)
        
        if taxamount==None:
            final_total=0
            grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            grand.set(final_total)
        # amount_recieved=amt_received_input.get()
        # balancedue=final_total-int(amount_recieved)
        # balance.set(balancedue)

mydb.commit()
mydb.close()


delay_form = tk.Tk()
delay_form.title("finsYs")
delay_form.geometry("1000x1000")
delay_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(delay_form)
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
credit_heading=Label(heading_frame, text="DELAYED CHARGE",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=headingfont,width=70)
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

global select_customer,email,invoice_date,terms,Due_date,billto,invno,cmpname,cpmemail,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,taxamount,grand,amt_received,balance

select_customer=StringVar()
email=StringVar()
product=StringVar()
desc=StringVar()
qty=StringVar()
price=StringVar()
total=StringVar()
total.set("0")
tax=StringVar()
subtotal=StringVar()
taxamount=StringVar()
taxamount.set("0")
grand=StringVar()
grand.set("0")

title_lab=tk.Label(form_frame,text="CUSTOMER",bg='#243e55',fg='#fff')
place_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = place_input)
drop2.set("SELECT CUSTOMER")
drop2['values']=(cus_name)
title_lab.place(x=10,y=200,height=15,width=100)
drop2.place(x=30,y=230,height=40,width=450)
wrappen.pack(fill='both',expand='yes',)


delayed_charge_date=Label(form_frame,text="DELAYED CHARGE DATE",bg='#243e55',fg='#fff')
delayed_charge_date.place(x=30,y=300,)
delayed_input=DateEntry(form_frame,width=55,bg='#243e55',fg='#fff')
delayed_input.place(x=30,y=330,height=40,width=450)



#invoice_period=tk.Label(form_frame,text="INVOICE PERIOD",bg='#243e55',fg='#fff')
#invoice_drop=ttk.Combobox(form_frame)
#invoice_drop['values']=("OCT2022-DEC2022","","","")
#invoice_period.place(x=20,y=330,height=15,width=100)
#invoice_drop.place(x=30,y=360,height=40,width=450)

#Billing session
sub_headingfont=font.Font(family='Times New Roman', size=18,)
form2_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,650),window=form2_frame,anchor="nw")

bill_heading=tk.Label(form2_frame, text="",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
bill_heading.place(x=30,y=10,)

label=tk.Label(form2_frame,text="PRODUCT/SERVICE\t\tDESCRIPTION\t\tQUANTITY\t\tRATE\t\tTOTAL\t\tTAX\t",bg='#243e55' ,fg="white",font=('Arial',))
label.place(x=60,y=60)

#row1
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product_drop1=ttk.Combobox(form2_frame)
product1=[]
for proinv in inventory_data: 
    if proinv[-1] == cmp1[0] :
        inv_data=proinv[2]
        product1.append(inv_data)

for proinv in noninventory_data: 
    if proinv[-1] == cmp1[0] :
        noninv_data=proinv[2]
        product1.append(noninv_data)

for proinv in bundle_data: 
    if proinv[-1] == cmp1[0] :
        bundleinv_data=proinv[2]
        product1.append(bundleinv_data)
            
product_drop1['values']=product1
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
product3=ttk.Combobox(form2_frame)
product3['values']=("","","","")
pro.place(x=10,y=280,height=15,width=100)
product3.place(x=60,y=310,height=40,width=150)




#row 1
description_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
description_input1.place(x=320,y=150,height=40,width=150)
#row2
description_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
description_input2.place(x=320,y=240,height=40,width=150)
#row3
description_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
description_input3.place(x=320,y=310,height=40,width=150)

#row 1
quantity_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input1.place(x=530,y=150,height=40,width=150)
#row2
quantity_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input2.place(x=530,y=240,height=40,width=150)
#row3
quantity_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
quantity_input3.place(x=530,y=310,height=40,width=150)


#row 1
price_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input1.place(x=720,y=150,height=40,width=150)
#row2
price_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input2.place(x=720,y=240,height=40,width=150)
#row3
price_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
price_input3.place(x=720,y=310,height=40,width=150)

#row 1
total_input1=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input1.place(x=890,y=150,height=40,width=150)
#row2
total_input2=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input2.place(x=890,y=240,height=40,width=150)
#row3
total_input3=Entry(form2_frame,width=40,bg='#243e55',fg='#fff')
total_input3.place(x=890,y=310,height=40,width=150)
#row1
tax_drop1=ttk.Combobox(form2_frame)
tax_drop1['values']=()
tax_drop1.place(x=1050,y=150,height=40,width=150)
#row2
tax2=ttk.Combobox(form2_frame)
tax2['values']=("","","","")
tax2.place(x=1050,y=240,height=40,width=150)
#row3
tax3=ttk.Combobox(form2_frame)
tax3['values']=("","","","")
tax3.place(x=1050,y=310,height=40,width=150)

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

button=tk.Button(form3_frame, text="SAVE",) 
button.place(x=1050,y=280,width=100)

delay_form.mainloop()
