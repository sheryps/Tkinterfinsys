import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font


def add_custom():
    import addcustomer_form

editinvoice_form = tk.Tk()
editinvoice_form.title("finsYs")
editinvoice_form.geometry("5000x2000")
editinvoice_form['bg']='#2f516a'
wrappen=ttk.LabelFrame(editinvoice_form)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=2500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")


heading_frame=Frame(mycanvas)
mycanvas.create_window((150,40),window=heading_frame,anchor="nw")
invoice_heading= tk.Label(heading_frame, text="INVOICE.1001",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
invoice_heading.pack()

#form fields

form_frame=Frame(mycanvas,width=1600,height=1900,bg='#243e55')
mycanvas.create_window((150,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=50)
form_lable.place(x=0,y=0)
form_heading=tk.Label(form_lable, text="FinsYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
form_heading.pack()




select_customer_lab=tk.Label(form_frame,text="Select Customer",bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = select_customer_input)

drop2['values']=("Select-Options")

select_customer_lab.place(x=30,y=200,height=15)
drop2.place(x=30,y=230,height=40,width=335)
wrappen.pack(fill='both',expand='yes',)

add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=2,command=add_custom)
add_custom.place(x=370,y=230)

email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
email_lab.place(x=500,y=200,)
email_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
email_input.place(x=500,y=230,height=40)

invoice_date_lab=Label(form_frame,text="Invoice Date",bg='#243e55',fg='#fff')
invoice_date_lab.place(x=30,y=300,)
invoice_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
invoice_date_input.place(x=30,y=330,height=40)

terms_lab=Label(form_frame,text="Terms",bg='#243e55',fg='#fff')
terms_lab.place(x=500,y=300,)
terms_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
terms_input.place(x=500,y=330,height=40)

Due_date_lab=Label(form_frame,text="Due Date",bg='#243e55',fg='#fff')
Due_date_lab.place(x=970,y=300,height=40)
Due_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
Due_date_input.place(x=970,y=330,height=40)

billto_lab=Label(form_frame,text="Bill To",bg='#243e55',fg='#fff')
billto_lab.place(x=30,y=400,)
billto_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
billto_input.place(x=30,y=430,height=150)

invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
invno_lab.place(x=500,y=400,)
invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
invno_input.place(x=500,y=430,height=40)

place_of_supply=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')
place_input=StringVar()
drop2=ttk.Combobox(form_frame,textvariable = place_input)
drop2['values']=("Kerala","Karnataka","Tamilnadu")
place_of_supply.place(x=30,y=600,)
drop2.place(x=30,y=630,height=40,width=335)

# table form

#col-1
product_lab=Label(form_frame,text="PRODUCT / SERVICES",bg='#243e55',fg='#fff')
product_lab.place(x=100,y=730,)
product_input1=StringVar()
product_drop1=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop1['values']=(" ")
product_drop1.place(x=70,y=780,height=40,width=200)

product_input2=StringVar()
product_drop2=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop2['values']=(" ")
product_drop2.place(x=70,y=850,height=40,width=200)

product_input3=StringVar()
product_drop3=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop3['values']=(" ")
product_drop3.place(x=70,y=930,height=40,width=200)

product_input4=StringVar()
product_drop4=ttk.Combobox(form_frame,textvariable = product_input1)
product_drop4['values']=(" ")
product_drop4.place(x=70,y=1000,height=40,width=200)

#col-2

hsn_lab=Label(form_frame,text="HSN",bg='#243e55',fg='#fff')
hsn_lab.place(x=350,y=730,)

hsn_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input1.place(x=300,y=780,height=40)

hsn_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input2.place(x=300,y=850,height=40)

hsn_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input3.place(x=300,y=930,height=40)

hsn_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
hsn_input4.place(x=300,y=1000,height=40)

#col-3

desc_lab=Label(form_frame,text="DESCRIPTION",bg='#243e55',fg='#fff')
desc_lab.place(x=550,y=730,)

desc_input1=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input1.place(x=500,y=780,height=40)

desc_input2=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input2.place(x=500,y=850,height=40)

desc_input3=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input3.place(x=500,y=930,height=40)

desc_input4=Entry(form_frame,width=25,bg='#2f516a',fg='#fff')
desc_input4.place(x=500,y=1000,height=40)

#col-4
qty_lab=Label(form_frame,text="QUANTITY",bg='#243e55',fg='#fff')
qty_lab.place(x=800,y=730,)

qty_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
qty_input1.place(x=750,y=780,height=40)

qty_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
qty_input2.place(x=750,y=850,height=40)

qty_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
qty_input3.place(x=750,y=930,height=40)

qty_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
qty_input4.place(x=750,y=1000,height=40)

#col-5
price_lab=Label(form_frame,text="PRICE",bg='#243e55',fg='#fff')
price_lab.place(x=1000,y=730,)

price_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input1.place(x=950,y=780,height=40)

price_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input2.place(x=950,y=850,height=40)

price_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input3.place(x=950,y=930,height=40)

price_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
price_input4.place(x=950,y=1000,height=40)

#col-6
total_lab=Label(form_frame,text="TOTAL",bg='#243e55',fg='#fff')
total_lab.place(x=1200,y=730,)

total_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
total_input1.place(x=1150,y=780,height=40)

total_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
total_input2.place(x=1150,y=850,height=40)

total_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
total_input3.place(x=1150,y=930,height=40)

total_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff')
total_input4.place(x=1150,y=1000,height=40)

#ocol-7
tax_lab=Label(form_frame,text="TAX (%)",bg='#243e55',fg='#fff')
tax_lab.place(x=1400,y=730,)

tax_input1=StringVar()
tax_drop1=ttk.Combobox(form_frame,textvariable = tax_input1)
tax_drop1['values']=(" ")
tax_drop1.place(x=1350,y=780,height=40,width=200)

tax_input2=StringVar()
tax_drop2=ttk.Combobox(form_frame,textvariable = tax_input2)
tax_drop2['values']=(" ")
tax_drop2.place(x=1350,y=850,height=40,width=200)

tax_input3=StringVar()
tax_drop3=ttk.Combobox(form_frame,textvariable = tax_input3)
tax_drop3['values']=(" ")
tax_drop3.place(x=1350,y=930,height=40,width=200)

tax_input4=StringVar()
tax_drop4=ttk.Combobox(form_frame,textvariable = tax_input4)
tax_drop4['values']=(" ")
tax_drop4.place(x=1350,y=1000,height=40,width=200)





subtotal_lab=Label(form_frame,text="Sub Total",bg='#243e55',fg='#fff')
subtotal_lab.place(x=970,y=1200,height=40)
subtotal_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
subtotal_input.place(x=1100,y=1200,height=40)

tax2_lab=Label(form_frame,text="Tax Amount",bg='#243e55',fg='#fff')
tax2_lab.place(x=970,y=1300,height=40)
tax2_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
tax2_input.place(x=1100,y=1300,height=40)

grand_lab=Label(form_frame,text="Grand Total",bg='#243e55',fg='#fff')
grand_lab.place(x=970,y=1400,height=40)
grand_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
grand_input.place(x=1100,y=1400,height=40)

amt_received_lab=Label(form_frame,text="Amount Received",bg='#243e55',fg='#fff')
amt_received_lab.place(x=970,y=1500,height=40)
amt_received_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
amt_received_input.place(x=1100,y=1500,height=40)

balance_lab=Label(form_frame,text="Balance Due",bg='#243e55',fg='#fff')
balance_lab.place(x=970,y=1600,height=40)
balance_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff')
balance_input.place(x=1100,y=1600,height=40)

submit_button=Button(form_frame,text="Save",background="#2f516a", foreground="white",width=20,height=2)

submit_button.place(x=1150,y=1700)
font=('Times', 15)
notice_lab=Label(form_frame,text="Notice :",bg='#243e55',fg='#808080',font=('Times', 15))
notice_lab.place(x=30,y=1800,)

note_lab=Label(form_frame,text="Fin sYs Terms and Conditions Apply ",bg='#243e55',fg='#808080',)
note_lab.place(x=30,y=1825,)
note2_lab=Label(form_frame,text="Invoice was created on a computer and is valid without the signature and seal.  ",bg='#243e55',fg='#808080',)
note2_lab.place(x=30,y=1850,)


editinvoice_form.mainloop()