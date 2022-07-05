
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
import mysql.connector
from tkcalendar import DateEntry

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
#fetching product from backend
inventory=[]
inventory_query="SELECT * FROM `app1_inventory`"
mycursor.execute(inventory_query)
table4=mycursor.fetchall()
for a in table4:
    data = (a[2])
    inventory.append(data)
    print(data)



def ProSelect(event):
    createsubtotal =0
    finding_tax1=0
    finding_tax2=0
    finding_tax3=0
    finding_tax4=0
    final_total=0
    selected_data=[]
    option3=product1.get()
    selected_data.append(option3)
    qty1=quantity1_input.get()
    inventory_query2="SELECT * FROM `app1_inventory` WHERE name=%s"
    mycursor.execute(inventory_query2,selected_data)
    table5=mycursor.fetchall()
    for a in table5:
        descrip1.set(a[11])
        pricee1.set(a[12])
        hsn1.set(a[3])
        saleprice=a[12]
        total1=int(saleprice)*int(qty1)
        totall1.set(total1)
        sub_total.set(total1)
    
    gst=tax_drop1.get()
    print("seslscted gst",gst)
    if gst=="18.0% GST(18%)":
        print("totla",total1)
        finding_tax1=int(total1)*(18/100)
    elif gst=="28.0% GST(28%)":
        finding_tax1=int(total1)*(28/100)
            
    elif gst=="12.0% GST(12%)":
        finding_tax1=int(total1)*(12/100)
            
    elif gst=="06.0% GST(06%)":
        finding_tax1=int(total1)*(6/100)
            
    elif gst=="05.0% GST(05%)":
        finding_tax1=int(total1)*(5/100)
            
    elif gst=="03.0% GST(03%)":
        finding_tax1=int(total1)*(3/100)
            
    elif gst=="0.25% GST(0.25%)":
        finding_tax1=int(total1)*(.25/100)
            
    else:
        finding_tax4=0
        taxamount.set(finding_tax1+finding_tax2+finding_tax3+finding_tax4)
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        taxamount.set(finding_tax)

    

#for the row of product2
def ProSelect2(event):
    selected_data=[]
    option4=product2.get()
    selected_data.append(option4)
    qty2=quantity2_input.get()
    inventory_query3="SELECT * FROM `app1_inventory` WHERE name=%s"
    mycursor.execute(inventory_query3,selected_data)
    table6=mycursor.fetchall()
    for a in table6:
        descript2.set(a[11])
        pricee2.set(a[12])
        hsn2.set(a[3])
        saleprice=a[12]
        total2=int(saleprice)*int(qty2)
        totall2.set(total2)
        sub_total.set(total2)

def ProSelect3(event):
    selected_data=[]
    option5=product3.get()
    selected_data.append(option5)
    qty3=quantity3_input.get()
    inventory_query4="SELECT * FROM `app1_inventory` WHERE name=%s"
    mycursor.execute(inventory_query4,selected_data)
    table6=mycursor.fetchall()
    for a in table6:
        descript3.set(a[11])
        pricee3.set(a[12])
        hsn3.set(a[3])
        saleprice=a[12]
        total3=int(saleprice)*int(qty3)
        totall3.set(total3)
        sub_total.set(total3)



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


def add_custom():
    import add_new_customer

cash_demo_form = tk.Tk()
cash_demo_form.title("finsYs")
cash_demo_form.geometry("1000x1000")
cash_demo_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(cash_demo_form)
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
credit_heading=Label(heading_frame, text="CASH DEMO",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=headingfont,width=70)
credit_heading.pack()

#form fields
sub_headingfont=font.Font(family='Times New Roman', size=20,)
form_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55')
mycanvas.create_window((0,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=100)
form_lable.place(x=0,y=0)
form_heading=tk.Label(form_lable, text="fin sYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=sub_headingfont,width=80)
form_heading.pack()

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
hsn1=tk.StringVar()
hsn2=tk.StringVar()
hsn3=tk.StringVar()
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
totall1.set("0")
totall2=tk.StringVar()
totall2.set("0")
totall3=tk.StringVar()
totall3.set("0")
tax_1=tk.StringVar()
tax_2=tk.StringVar()
tax_3=tk.StringVar()
sub_total=tk.StringVar()
taxamount=tk.StringVar() 

title_lab=tk.Label(form_frame,text="CUSTOMER",bg='#243e55',fg='#fff')
place_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = place_input)
drop2.set("SELECT CUSTOMER")
drop2['values']=(cus_name)
drop2.bind("<<ComboboxSelected>>",cusSelect)

title_lab.place(x=10,y=100,height=15,width=100)
drop2.place(x=30,y=130,height=40,width=450)
wrappen.pack(fill='both',expand='yes',)
add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command=add_custom)
add_custom.place(x=505,y=130)


emailL=Label(form_frame,text="EMAIL",bg='#243e55',fg='#fff')
emailL.place(x=630,y=100,)
email_input=Entry(form_frame,width=55,bg='#243e55',fg='#fff',textvariable=email)
email_input.place(x=630,y=130,height=40)

billing_ad=Label(form_frame,text="BILLING ADDRESS",bg='#243e55',fg='#fff')
billing_ad.place(x=30,y=200,)
billing_input=Entry(form_frame,width=75,bg='#243e55',fg='#fff',textvariable=biladdress)
billing_input.place(x=30,y=230,height=90)

sales_reciept_date=Label(form_frame,text="SALES RECIEPT DATE",bg='#243e55',fg='#fff')
sales_reciept_date.place(x=630,y=200,)
sales_reciept_input=DateEntry(form_frame,width=55,bg='#243e55',fg='#fff')
sales_reciept_input.place(x=630,y=230,height=40)

place_of_supp=tk.Label(form_frame,text="PLACE OF SUPPLY",bg='#243e55',fg='#fff')
place_drop=ttk.Combobox(form_frame)
place_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
place_of_supp.place(x=30,y=330,height=15,width=100)
place_drop.place(x=30,y=360,height=40,width=450)

#invoice_period=tk.Label(form_frame,text="INVOICE PERIOD",bg='#243e55',fg='#fff')
#invoice_drop=ttk.Combobox(form_frame)
#invoice_drop['values']=("OCT2022-DEC2022","","","")
#invoice_period.place(x=20,y=330,height=15,width=100)
#invoice_drop.place(x=30,y=360,height=40,width=450)
#

payment=tk.Label(form_frame,text="PAYMENT",bg='#243e55',fg='#fff')
payment_drop=ttk.Combobox(form_frame)
payment_drop['values']=("CASH","CHEQUE","CREDIT CARD","ADD NEW")
payment.place(x=20,y=420,height=15,width=100)
payment_drop.place(x=30,y=450,height=40,width=450)

sales_reciept_date=Label(form_frame,text="REFERENCE NO",bg='#243e55',fg='#fff')
sales_reciept_date.place(x=530,y=420,)
sales_reciept_input=Entry(form_frame,width=55,bg='#243e55',fg='#fff')
sales_reciept_input.place(x=530,y=450,height=40)

payment=tk.Label(form_frame,text="DEPOSIT TO",bg='#243e55',fg='#fff')
payment_drop=ttk.Combobox(form_frame)
payment_drop['values']=("DEFFERED CGST","DEFFERED GST input credit","GST refund","TDS RECIEVABLE")
payment.place(x=870,y=420,height=15,width=100)
payment_drop.place(x=880,y=450,height=40,width=450)

#Billing session
sub_headingfont=font.Font(family='Times New Roman', size=18,)
form2_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,650),window=form2_frame,anchor="nw")

bill_heading=tk.Label(form2_frame, text="",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
bill_heading.place(x=30,y=10,)

label=tk.Label(form2_frame,text="PRODUCT/SERVICE\tHSN\t\tDESCRIPTION\t\tQUANTITY\t\tPRICE\t\tTOTAL\t\tTAX\t",bg='#243e55' ,fg="white",font=('Arial',))
label.place(x=60,y=60)

#row1
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product1=ttk.Combobox(form2_frame)
product1['values']=(inventory)
product1.bind("<<ComboboxSelected>>",ProSelect)
product1.set("SELECT PRODUCT")
pro.place(x=10,y=120,height=15,width=100)
product1.place(x=60,y=150,height=40,width=150)
#2
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product2=ttk.Combobox(form2_frame)
product2['values']=(inventory)
product2.bind("<<ComboboxSelected>>",ProSelect2)
product2.set("SELECT PRODUCT")
pro.place(x=10,y=210,height=15,width=100)
product2.place(x=60,y=240,height=40,width=150)
#3
pro=tk.Label(form2_frame,text="",bg='#243e55',fg='#fff')
product3=ttk.Combobox(form2_frame)
product3['values']=(inventory)
product3.bind("<<ComboboxSelected>>",ProSelect3)
product3.set("SELECT PRODUCT")
pro.place(x=10,y=280,height=15,width=100)
product3.place(x=60,y=310,height=40,width=150)

#row 1
hsn_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=hsn1)
hsn_input.place(x=230,y=150,height=40,width=150)
#row2
hsn_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=hsn2)
hsn_input.place(x=230,y=240,height=40,width=150)
#row3
hsn_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=hsn3)
hsn_input.place(x=230,y=310,height=40,width=150)



#row 1
description_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descrip1)
description_input.place(x=400,y=150,height=40,width=150)
#row2
description_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descript2)
description_input.place(x=400,y=240,height=40,width=150)
#row3
description_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=descript3)
description_input.place(x=400,y=310,height=40,width=150)

#row 1
quantity1_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qnty1)
quantity1_input.place(x=600,y=150,height=40,width=150)
quantity1_input.bind("<KeyRelease>",ProSelect)
#row2
quantity2_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qnty2)
quantity2_input.place(x=600,y=240,height=40,width=150)
quantity2_input.bind("<KeyRelease>",ProSelect2)
#row3
quantity3_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=qnty3)
quantity3_input.place(x=600,y=310,height=40,width=150)
quantity3_input.bind("<KeyRelease>",ProSelect3)

#row 1
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=pricee1)
price_input.place(x=780,y=150,height=40,width=150)
#row2
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=pricee2)
price_input.place(x=780,y=240,height=40,width=150)
#row3
price_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=pricee3)
price_input.place(x=780,y=310,height=40,width=150)

#row 1
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=totall1)
total_input.place(x=950,y=150,height=40,width=150)
#row2
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=totall2)
total_input.place(x=950,y=240,height=40,width=150)
#row3
total_input=Entry(form2_frame,width=40,bg='#243e55',fg='#fff',textvariable=totall3)
total_input.place(x=950,y=310,height=40,width=150)
#row1
tax_drop1=ttk.Combobox(form2_frame)
tax_values=("Choose","28.0% GST(28%)","18.0% GST(18%)","12.0% GST(12%)","06.0% GST(06%)","05.0% GST(05%)","03.0% GST(03%)","0.25% GST(0.25%)","0.0% GST(0%)","Exempt GST(0%)","Out of Scope(0%)")
tax_drop1['values']=tax_values
tax_drop1.bind("<<ComboboxSelected>>",ProSelect)
tax_drop1.place(x=1130,y=150,height=40,width=150)
#row2
tax_drop2=ttk.Combobox(form2_frame)
tax_drop2['values']=tax_values
tax_drop2.bind("<<ComboboxSelected>>",ProSelect2)
tax_drop2.place(x=1130,y=240,height=40,width=150)
#row3
tax_drop3=ttk.Combobox(form2_frame)
tax_drop3['values']=tax_values
tax_drop3.bind("<<ComboboxSelected>>",ProSelect3)
tax_drop3.place(x=1130,y=310,height=40,width=150)

##################

sub_headingfont=font.Font(family='Times New Roman', size=18,)
form3_frame=Frame(mycanvas,width=1600,height=500,bg='#243e55',bd=1,relief="groove")
mycanvas.create_window((0,1100),window=form3_frame,anchor="nw")

sub_label=Label(form3_frame,text="SUB TOTAL",bg='#243e55',fg='#fff')
sub_label.place(x=900,y=110)
sub_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff',textvariable=sub_total)
sub_input.place(x=1000,y=100,height=40,width=200)

tax_amount=Label(form3_frame,text="TAX AMOUNT",bg='#243e55',fg='#fff')
tax_amount.place(x=900,y=160)
tax_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff',textvariable=taxamount)
tax_input.place(x=1000,y=150,height=40,width=200)

grand_total=Label(form3_frame,text="GRAND TOTAL",bg='#243e55',fg='#fff')
grand_total.place(x=900,y=210)
grand_input=Entry(form3_frame,width=40,bg='#243e55',fg='#fff')
grand_input.place(x=1000,y=200,height=40,width=200)

button=tk.Button(form3_frame, text="SAVE",) 
button.place(x=1050,y=280,width=100)

cash_demo_form.mainloop()
