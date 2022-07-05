
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import tkinter.font as font
from unicodedata import category
import mysql.connector as mysql
from tkcalendar import Calendar, DateEntry



debit_form = tk.Tk()
debit_form.title("finsYs")
debit_form.geometry("1500x1000")
debit_form['bg'] = "#badc57"
wrappen = ttk.LabelFrame(debit_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')


def submit():
    etype = "Debit Note"

    supplier = drop2.get()
    mailaddress = billing_input.get()
    payment_date = payment_drop.get()

    category1 = cpro_drop1.get()
    category2 = cpro_drop2.get()
    category3 = cpro_drop3.get()
    categorydescription1 = discription_input1.get()
    categorydescription2 = discription_input2.get()
    categorydescription3 = discription_input3.get()
    categoryquantity1 = quantity_input1.get()
    categoryquantity2 = quantity_input2.get()
    categoryquantity3 = quantity_input3.get()
    categoryprice1 = price_input1.get()
    categoryprice2 = price_input2.get()
    categoryprice3 = price_input3.get()
    categorytotal1 = ctotal_input1.get()
    categorytotal2 = ctotal_input2.get()
    categorytotal3 = ctotal_input3.get()
    product1 = prod_drop1.get()
    product2 = prod_drop2.get()
    product3 = prod_drop3.get()
    productdescription1 = description_input1.get()
    productdescription2 = description_input2.get()
    productdescription3 = description_input3.get()
    hsn1 = hsn_input1.get()
    hsn2 = hsn_input2.get()
    hsn3 = hsn_input3.get()
    productquantity1 = pquantity_input1.get()
    productquantity2 = pquantity_input2.get()
    productquantity3 = pquantity_input3.get()
    productprice1 = pprice_input1.get()
    productprice2 = pprice_input2.get()
    productprice3 = pprice_input3.get()
    producttotal1 = ptotal_input1.get()
    producttotal2 = ptotal_input2.get()
    producttotal3 = ptotal_input3.get()
    producttax1 = taxpro_drop1.get()
    producttax2 = taxpro_drop2.get()
    producttax3 = taxpro_drop3.get()
    subtotal = sub_input.get()
    tax = tax_input.get()
    grandtotal = grand_input.get()

    con = mysql.connect(host="127.0.0.1", user="root",
                        password="", database="fynsystkinter", port='3307')
    cur = con.cursor()
    d = '''INSERT INTO expensesmain(etype,supplier , payment_date , mailaddress, category1 ,category2, category3, categorydescription1  , categorydescription2 
                    , categorydescription3, categoryquantity1 , categoryquantity2 ,categoryquantity3, categoryprice1 , categoryprice2 , categoryprice3, categorytotal1 , categorytotal2 , categorytotal3, product1 , product2 , product3, productdescription1 , productdescription2 , productdescription3, hsn1 , hsn2 , hsn3, productquantity1 , productquantity2 , productquantity3, productprice1  , productprice2 ,productprice3, producttotal1  , producttotal2 , producttotal3, producttax1  ,  producttax2 ,producttax3, subtotal,tax,grandtotal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cur.execute(d, [(etype), (supplier), (payment_date), (mailaddress), (category1), (category2), (category3), (categorydescription1), (categorydescription2), (categorydescription3), (categoryquantity1), (categoryquantity2), (categoryquantity3), (categoryprice1), (categoryprice2), (categoryprice3), (categorytotal1), (categorytotal2), (categorytotal3), (product1), (product2),
                (product3), (productdescription1), (productdescription2), (productdescription3), (hsn1), (hsn2), (hsn3), (productquantity1), (productquantity2), (productquantity3), (productprice1), (productprice2), (productprice3), (producttotal1), (producttotal2), (producttotal3), (producttax1),  (producttax2), (producttax3), (subtotal),  (tax), (grandtotal)])
    con.commit()
    MessageBox.showinfo("Insert Status", "Inserted Successfully")
    debit_form.destroy()


mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
    scrollregion=mycanvas.bbox('all')))

full_frame = Frame(mycanvas, width=2000, height=2000, bg='#2f516a')
mycanvas.create_window((0, 0), window=full_frame, anchor="nw")


heading_frame = Frame(mycanvas)
mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
headingfont = font.Font(family='Times New Roman', size=25,)
credit_heading = Label(heading_frame, text="Debit Note", fg='#fff',
                       bg="#243e55", height=2, bd=5, relief="groove", font=headingfont, width=106)
credit_heading.pack(padx=0, pady=0)

# form fields
sub_headingfont = font.Font(family='Times New Roman', size=20,)
form_frame = Frame(mycanvas, width=1400, height=500, bg='#243e55')
mycanvas.create_window((0, 150), window=form_frame, anchor="nw")
form_lable = tk.Label(form_frame, bg='#243e55', width=100)
form_lable.place(x=2, y=5)
form_heading = tk.Label(form_lable, text="finsYs", fg='#fff', bg='#243e55',
                        height=2, bd=1, relief="groove", font=sub_headingfont, width=125)
form_heading.pack()

title_lab = tk.Label(form_frame, text="Supplier", bg='#243e55', fg='#fff')
place_input = StringVar()
drop2 = ttk.Combobox(form_frame, textvariable=place_input)

drop2['values'] = ("Select Supplier")

title_lab.place(x=30, y=100, height=15, width=60)
drop2.place(x=30, y=130, height=40, width=450)
wrappen.pack(fill='both', expand='yes',)


billing_ad = Label(form_frame, text="Maling Address", bg='#243e55', fg='#fff')
billing_ad.place(x=30, y=200,)
billing_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
billing_input.place(x=30, y=230, height=90)


payment_period = tk.Label(
    form_frame, text="Payment Date", bg='#243e55', fg='#fff')
payment_period.place(x=30, y=330, height=15, width=100)

# payment_drop = ttk.Combobox(form_frame)
#  DateEntry(debit_form, width=16, bg="#2f516f", bd=2)
payment_drop = DateEntry(form_frame, width=49, bg="#2f516f", bd=2)
payment_drop.place(x=30, y=360, height=40)


# CATEGORY DETAILS
sub_headingfont = font.Font(family='Times New Roman', size=18,)
form2_frame = Frame(mycanvas, width=1600, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 650), window=form2_frame, anchor="nw")

bill_heading = tk.Label(form2_frame, text="Catgory Details", fg='#fff',
                        bg='#243e55', height=2, font=sub_headingfont, width=15)
bill_heading.place(x=30, y=0,)

label = tk.Label(form2_frame, text="CATEGORY\t\t\tDESCRIPTION\t\t\tNOT APPLICABLE\t\t\tPRICE\t\t\tTOTAL\t\t",
                 bg='#243e55', fg="white", font=('Arial', 15))
label.place(x=120, y=50)

# row1
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
cpro_drop1 = ttk.Combobox(form2_frame)
cpro_drop1['values'] = ("Category 1", "Category 2", "Catefory 3", "Category 4")
pro.place(x=50, y=120, height=15, width=150)
cpro_drop1.place(x=50, y=150, height=40, width=200)
# 2
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
cpro_drop2 = ttk.Combobox(form2_frame)
cpro_drop2['values'] = ("Category 1", "Category 2", "Catefory 3", "Category 4")
pro.place(x=50, y=210, height=15, width=150)
cpro_drop2.place(x=50, y=240, height=40, width=200)
# 3
pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
cpro_drop3 = ttk.Combobox(form2_frame)
cpro_drop3['values'] = ("Category 1", "Category 2", "Catefory 3", "Category 4")
pro.place(x=50, y=280, height=15, width=150)
cpro_drop3.place(x=50, y=310, height=40, width=200)


# row 1
discription_input1 = Entry(form2_frame, width=40, bg='#2f516f', fg='#fff')
discription_input1.place(x=350, y=150, height=40, width=200)
# row2
discription_input2 = Entry(form2_frame, width=40, bg='#2f516f', fg='#fff')
discription_input2.place(x=350, y=240, height=40, width=200)
# row3
discription_input3 = Entry(form2_frame, width=40, bg='#2f516f', fg='#fff')
discription_input3.place(x=350, y=310, height=40, width=200)

# row 1
quantity_input1 = Entry(form2_frame, width=40, bg='#2f516f', fg='#fff')
quantity_input1.place(x=650, y=150, height=40, width=200)
# row2
quantity_input2 = Entry(form2_frame, width=40, bg='#2f516f', fg='#fff')
quantity_input2.place(x=650, y=240, height=40, width=200)
# row3
quantity_input3 = Entry(form2_frame, width=40, bg='#2f516f', fg='#fff')
quantity_input3.place(x=650, y=310, height=40, width=200)


# def mulc(self, event):
#     ctotal_input1.delete(0, 'end')
#     price_input1 = int(price_input1.get())
#     quantity_input1 = int(quantity_input1.get())
#     resultc1 = price_input1*quantity_input1
#     ctotal_input2.insert(END, str(resultc1))
#     ctotal_input2.delete(0, 'end')
#     price_input2 = int(price_input2.get())
#     quantity_input2 = int(quantity_input2.get())
#     resultc2 = price_input2*quantity_input2
#     ctotal_input2.insert(END, str(resultc2))
#     ctotal_input3.delete(0, 'end')
#     price_input3 = int(price_input3.get())
#     quantity_input3 = int(quantity_input3.get())
#     resultc3 = price_input3*quantity_input3
#     ctotal_input3.insert(END, str(resultc3))


# row 1
price_input1 = Entry(form2_frame, width=40, bg='#2f516f',
                     fg='#fff')
price_input1.place(x=950, y=150, height=40, width=150)
# row2
price_input2 = Entry(form2_frame, width=40, bg='#2f516f',
                     fg='#fff')
price_input2.place(x=950, y=240, height=40, width=150)
# row3
price_input3 = Entry(form2_frame, width=40, bg='#2f516f',
                     fg='#fff')
price_input3.place(x=950, y=310, height=40, width=150)

# row 1
ctotal_input1 = Entry(form2_frame, width=40, bg='#2f516f',
                      fg='#fff', )
ctotal_input1.place(x=1200, y=150, height=40, width=100)
# row2
ctotal_input2 = Entry(form2_frame, width=40, bg='#2f516f',
                      fg='#fff')
ctotal_input2.place(x=1200, y=240, height=40, width=100)
# row3
ctotal_input3 = Entry(form2_frame, width=40, bg='#2f516f',
                      fg='#fff')
ctotal_input3.place(x=1200, y=310, height=40, width=100)


##################


# ITEM DETAILS
sub_headingfont = font.Font(family='Times New Roman', size=18,)
form4_frame = Frame(mycanvas, width=1500, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 1100), window=form4_frame, anchor="nw")

bill_heading = tk.Label(form4_frame, text="Item Details", fg='#fff',
                        bg='#243e55', height=2, font=sub_headingfont, width=15)
bill_heading.place(x=30, y=0,)

label = tk.Label(form4_frame, text="PRODUCT/SERVICE\tHSN\t\tDESCRIPTION\t\t  QUANTITY\t\t  PRICE\t\t     TOTAL\t\t\t     TAX(%)\t\t",
                 bg='#243e55', fg="white", font=('Arial', 15))
label.place(x=60, y=60)

# row1
prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
prod_drop1 = ttk.Combobox(form4_frame)
prod_drop1['values'] = ("Product 1", "Product 2", "Product 3", "Product 4")
prod.place(x=50, y=120, height=15, width=150)
prod_drop1.place(x=50, y=150, height=40, width=175)
# 2
prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
prod_drop2 = ttk.Combobox(form4_frame)
prod_drop2['values'] = ("Product 1", "Product 2", "Product 3", "Product 4")
prod.place(x=50, y=210, height=15, width=150)
prod_drop2.place(x=50, y=240, height=40, width=175)
# 3
prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
prod_drop3 = ttk.Combobox(form4_frame)
prod_drop3['values'] = ("Product 1", "Product 2", "Product 3", "Product 4")
prod.place(x=50, y=280, height=15, width=150)
prod_drop3.place(x=50, y=310, height=40, width=175)


# row 1
description_input1 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
description_input1.place(x=380, y=150, height=40, width=200)
# row2
description_input2 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
description_input2.place(x=380, y=240, height=40, width=200)
# row3
description_input3 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
description_input3.place(x=380, y=310, height=40, width=200)

# row 1
hsn_input1 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
hsn_input1.place(x=250, y=150, height=40, width=100)
# row2
hsn_input2 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
hsn_input2.place(x=250, y=240, height=40, width=100)
# row3
hsn_input3 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
hsn_input3.place(x=250, y=310, height=40, width=100)

# row 1
pquantity_input1 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
pquantity_input1.place(x=610, y=150, height=40, width=200)
# row2
pquantity_input2 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
pquantity_input2.place(x=610, y=240, height=40, width=200)
# row3
pquantity_input3 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
pquantity_input3.place(x=610, y=310, height=40, width=200)


# row 1
pprice_input1 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
pprice_input1.place(x=840, y=150, height=40, width=150)
# row2
pprice_input2 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
pprice_input2.place(x=840, y=240, height=40, width=150)
# row3
pprice_input3 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
pprice_input3.place(x=840, y=310, height=40, width=150)


# def mulc(self, event):
#     ptotal_input1.delete(0, 'end')
#     pprice_input1 = int(pprice_input1.get())
#     pquantity_input1 = int(pquantity_input1.get())
#     resultp1 = pprice_input1*pquantity_input1
#     ptotal_input1.insert(END, str(resultp1))

#     ptotal_input2.delete(0, 'end')
#     pprice_input2 = int(pprice_input2.get())
#     pquantity_input2 = int(pquantity_input2.get())
#     resultp2 = pprice_input2*pquantity_input2
#     ptotal_input2.insert(END, str(resultp2))

#     ptotal_input3.delete(0, 'end')
#     pprice_input3 = int(pprice_input3.get())
#     pquantity_input3 = int(pquantity_input3.get())
#     resultp3 = pprice_input3*pquantity_input3
#     ptotal_input3.insert(END, str(resultp3))


# row 1
ptotal_input1 = Entry(form4_frame, width=40, bg='#2f516f',
                      fg='#fff')
ptotal_input1.place(x=1020, y=150, height=40, width=100)
# row2
ptotal_input2 = Entry(form4_frame, width=40, bg='#2f516f',
                      fg='#fff')
ptotal_input2.place(x=1020, y=240, height=40, width=100)
# row3
ptotal_input3 = Entry(form4_frame, width=40, bg='#2f516f',
                      fg='#fff')
ptotal_input3.place(x=1020, y=310, height=40, width=100)
# row1
taxpro_drop1 = ttk.Combobox(form4_frame)
taxpro_drop1['values'] = ("10", "18", "20", "30")
pro.place(x=1150, y=150, height=15, width=150)
taxpro_drop1.place(x=1150, y=150, height=40, width=200)
# row2
taxpro_drop2 = ttk.Combobox(form4_frame)
taxpro_drop2['values'] = ("10", "18", "20", "30")
pro.place(x=1150, y=240, height=15, width=150)
taxpro_drop2.place(x=1150, y=240, height=40, width=200)
# row3
taxpro_drop3 = ttk.Combobox(form4_frame)
taxpro_drop3['values'] = ("10", "18", "20", "30")
pro.place(x=1150, y=310, height=15, width=150)
taxpro_drop3.place(x=1150, y=310, height=40, width=200)


##################


sub_headingfont = font.Font(family='Times New Roman', size=18,)
form3_frame = Frame(mycanvas, width=1600, height=500,
                    bg='#243e55', bd=1, relief="groove")
mycanvas.create_window((0, 1500), window=form3_frame, anchor="nw")

sub_total = Label(form3_frame, text="SUB TOTAL", bg='#243e55', fg='#fff')
sub_total.place(x=1000, y=110)
sub_input = Entry(form3_frame, width=40, bg='#2f516f', fg='#fff')
sub_input.place(x=1150, y=100, height=40, width=200)

tax_amount = Label(form3_frame, text="TAX AMOUNT", bg='#243e55', fg='#fff')
tax_amount.place(x=1000, y=160)
tax_input = Entry(form3_frame, width=40, bg='#2f516f', fg='#fff')
tax_input.place(x=1150, y=150, height=40, width=200)

grand_total = Label(form3_frame, text="GRAND TOTAL", bg='#243e55', fg='#fff')
grand_total.place(x=1000, y=210)
grand_input = Entry(form3_frame, width=40, bg='#2f516f', fg='#fff')
grand_input.place(x=1150, y=200, height=40, width=200)

submit = tk.Button(form3_frame, text="Submit Form", command=submit)
submit.place(x=1150, y=280, width=100)

debit_form.mainloop()
