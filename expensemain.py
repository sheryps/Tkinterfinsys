import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
import tkinter.font as font
import tkinter.messagebox as MessageBox
import mysql.connector 
from tkcalendar import Calendar, DateEntry


mydata = mysql.connector.connect(
    host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
cur = mydata.cursor()

expense_form = tk.Tk()
expense_form.title("finsYs")
expense_form.geometry("1500x1000")
expense_form['bg'] = '#2f516a'
wrappen = ttk.LabelFrame(expense_form)
mycanvas = Canvas(wrappen)
mycanvas.pack(side=LEFT, fill="both", expand="yes")
yscrollbar = ttk.Scrollbar(wrappen, orient='vertical', command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill='y')


def main():

    global A, data, menu
    A = tk.Tk()
    A.title('Expenses')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'


    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Times New Roman', size=25)  # font
    lb = tk.Label(head, text='EXPENSES', bg="#243e55", height=2,
                  bd=5, relief="groove", font=f, width=106)
    lb['font'] = f
    lb.place(relx=0.05, rely=0.2)
    head.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

    # contents frame
    hd = tk.Frame(A, bg='#243e54')
    hd.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
    # ff = font.Font(family='Times New Roman', size=15)  # font
    # bt = tk.Button(hd, text='New Transaction',
    #                command="", bg='#243e54')
    # bt['font'] = ff
    # bt.place(relx=0.85, rely=0.05)



    def selected(event):
        select_pro=[]
        menu=product_drop5.get()
        select_pro.append(menu)
        print(menu)
        if menu == 'Expenses':
            import expenses
        elif menu == 'Payment':
            import payment
        elif menu == 'Debit Note ':
            import debitnote
        else:
            import expensemain
    pr1 = "Expenses", "Payment", "Debit Note ", "Expenses Main"
    product_drop5=ttk.Combobox(hd,font=('times new roman', 10, 'bold'), )
    product_drop5.set("New Transaction")
    product_drop5['values']=pr1
    product_drop5.bind("<<ComboboxSelected>>",selected)
    product_drop5.place(x=900,y=10,height=40,width=200)


    # table view

    treevv = ttk.Treeview(hd, height=7, columns=(
        1, 2, 3, 4, 5, 6), show='headings')
    treevv.heading(1, text='ID')  # headings
    treevv.heading(2, text='DATE')  # headings
    treevv.heading(3, text='TYPE')
    treevv.heading(4, text='PAYEE')
    treevv.heading(5, text='TAX')
    treevv.heading(6, text='AMOUNT')
    # treevv.heading(7, text='Actions')
    treevv.column(1, minwidth=10, width=40, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    cur.execute(
        "SELECT id,payment_date,etype,payee,tax,grandtotal FROM expensesmain")
    val = cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end', values=(
                x[0], x[1], x[2], x[3], x[4], x[5]))
    treevv.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

    def editexp():
        def changeedit():

            mydata = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
            cur = mydata.cursor()
            global D, refno, payee, payment_date, payment_method, payment_account, supplier, mailaddress, category1, category2, category3, categorydescription1, categorydescription2, categorydescription3, categoryquantity1, categoryquantity2, categoryquantity3, categoryprice1, categoryprice2, categoryprice3, categorytotal1, categorytotal2, categorytotal3, product1, product2, product3, productdescription1, productdescription2, productdescription3, hsn1, hsn2, hsn3, productquantity1, productquantity2, productquantity3, productprice1, productprice2, productprice3, producttotal1, producttotal2, producttotal3, producttax1, producttax2, producttax3, subtotal, tax, grandtotal
            refno = drop1.get()
            payee = drop2.get()
            payment_date = paymentdate_input.get()
            payment_method = drop3.get()
            payment_account = drop4.get()
            supplier = drop5.get()
            mailaddress = billing_input.get()
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

            # con = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='fynsystkinter', port='3307')
            # cur = con.cursor()
            # d = '''UPDATE expensesmain SET(id,refno, payee, payment_date, payment_method, payment_account, supplier, mailaddress,category1 ,category2, category3, categorydescription1  , categorydescription2 
            #                 , categorydescription3, categoryquantity1 , categoryquantity2 ,categoryquantity3, categoryprice1 , categoryprice2 , categoryprice3, categorytotal1 , categorytotal2 , categorytotal3, product1 , product2 , product3, productdescription1 , productdescription2 , productdescription3, hsn1 , hsn2 , hsn3, productquantity1 , productquantity2 , productquantity3, productprice1  , productprice2 ,productprice3, producttotal1  , producttotal2 , producttotal3, producttax1  ,  producttax2 ,producttax3, subtotal,tax,grandtotal) VALUES (%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)  WHERE id=%d'''
            # cur.execute(d, [(id),(refno), (payee), (payment_date),  (payment_method),(payment_account),(supplier),(mailaddress) (category1), (category2), (category3), (categorydescription1), (categorydescription2), (categorydescription3), (categoryquantity1), (categoryquantity2), (categoryquantity3), (categoryprice1), (categoryprice2), (categoryprice3), (categorytotal1), (categorytotal2), (categorytotal3), (product1), (product2),
            #             (product3), (productdescription1), (productdescription2), (productdescription3), (hsn1), (hsn2), (hsn3), (productquantity1), (productquantity2), (productquantity3), (productprice1), (productprice2), (productprice3), (producttotal1), (producttotal2), (producttotal3), (producttax1),  (producttax2), (producttax3), (subtotal),  (tax), (grandtotal)])
            # con.commit()
            
            
            print(refno, payee, payment_date, payment_method, payment_account, supplier, mailaddress, category1, category2, category3, categorydescription1, categorydescription2, categorydescription3, categoryquantity1, categoryquantity2,
                  categoryquantity3, categoryprice1, categoryprice2, categoryprice3, categorytotal1, categorytotal2, categorytotal3, product1, product2, product3, productdescription1, productdescription2, productdescription3, hsn1, hsn2, hsn3, productquantity1, productquantity2, productquantity3, productprice1, productprice2, productprice3, producttotal1, producttotal2, producttotal3, producttax1, producttax2, producttax3, subtotal, tax, grandtotal)

            cur.execute("""UPDATE expensesmain SET refno =%s, payee =%s, payment_date =%s, payment_method =%s, payment_account =%s, supplier =%s, mailaddress =%s, category1 =%s, category2 =%s, category3 =%s,categorydescription1 =%s, categorydescription2 =%s,categorydescription3 =%s, categoryquantity1 =%s, categoryquantity2 =%s, categoryquantity3 =%s, categoryprice1 =%s, categoryprice2 =%s, categoryprice3 =%s, categorytotal1 =%s, categorytotal2 =%s, categorytotal3 =%s, product1 =%s, product2 =%s, product3 =%s,productdescription1 =%s, productdescription2 =%s,productdescription3 =%s, hsn1 =%s, hsn2 =%s, hsn3 =%s, productquantity1 =%s, productquantity2 =%s, productquantity3 =%s, productprice1 =%s, productprice2 =%s, productprice3 =%s, producttotal1=%s  , producttotal2=%s , producttotal3=%s, producttax1=%s  ,  producttax2=%s ,producttax3=%s, subtotal=%s,tax =%s,grandtotal=%s WHERE id=%s""",
                        ( refno, payee, payment_date, payment_method, payment_account, supplier, mailaddress, category1, category2, category3, categorydescription1, categorydescription2, categorydescription3, categoryquantity1, categoryquantity2, categoryquantity3, categoryprice1, categoryprice2, categoryprice3, categorytotal1, categorytotal2, categorytotal3, product1, product2, product3, productdescription1, productdescription2, productdescription3, hsn1, hsn2, hsn3, productquantity1, productquantity2, productquantity3, productprice1, productprice2, productprice3, producttotal1, producttotal2, producttotal3, producttax1,  producttax2, producttax3, subtotal, tax, grandtotal, b))
            mydata.commit()
            MessageBox.showinfo("Insert Status", "Updated Successfully")
            mydata.close()
            expense_form.destroy()

      

        # Get selected item to Edit

   
        b = treevv.item(treevv.focus())["values"][0]
        print(b)
        sql='SELECT * FROM expensesmain WHERE id=%s'
        val=(b,)
        cur.execute(sql,val)
        s = cur.fetchone()
        D = tk.Toplevel(A)
        print(s)

        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
            scrollregion=mycanvas.bbox('all')))

        full_frame = Frame(mycanvas, width=2000, height=1950, bg='#2f516a')
        mycanvas.create_window((0, 0), window=full_frame, anchor="nw")

        heading_frame = Frame(mycanvas)
        mycanvas.create_window((0, 40), window=heading_frame, anchor="nw")
        headingfont = font.Font(family='Times New Roman', size=25,)
        credit_heading = Label(heading_frame, text="EXPENSES", fg='#fff',
                               bg='#243e55', height=2, bd=5, relief="groove", font=headingfont, width=106)
        credit_heading.pack(padx=0, pady=0)

        # form fields
        sub_headingfont = font.Font(family='Times New Roman', size=20,)
        form_frame = Frame(mycanvas, width=1600, height=600, bg='#243e55')
        mycanvas.create_window((0, 150), window=form_frame, anchor="nw")

        title_lab = tk.Label(form_frame, text="Ref No.",
                             bg='#243e55', fg='#fff')
        place_input = StringVar()
        drop1 = ttk.Combobox(form_frame)
        drop1['values'] = ("REF1 REF2 REF3 REF4")
        try:
            drop1.insert(0, s[2])
        except:
            pass
        
        title_lab.place(x=10, y=20, height=15, width=100)
        drop1.place(x=30, y=40, height=40, width=450)
        wrappen.pack(fill='both', expand='yes',)

        title_lab = tk.Label(form_frame, text="PAYEE", bg='#243e55', fg='#fff')
        place_input = StringVar()
        drop2 = ttk.Combobox(form_frame)
        drop2['values'] = ("PAYEE1 PAYEE2 PAYEE3 PAYEE4")
        try:
            drop2.insert(0, s[3])
        except:
            pass
        
        
        title_lab.place(x=10, y=100, height=15, width=100)
        drop2.place(x=30, y=130, height=40, width=450)
        wrappen.pack(fill='both', expand='yes',)

        pd = Label(
            form_frame, text="Payment Date", bg='#243e55', fg='#fff')
        pd.place(x=30, y=200,)
        paymentdate_input = StringVar()
        payment_input = DateEntry(form_frame, width=49, bg="#2f516f", textvariable=paymentdate_input)
        payment_input.place(x=30, y=230, height=40)

        payment_input.insert(0, s[4])

    
        payment_method_lab = tk.Label(
            form_frame, text="Payment Method", bg='#243e55', fg='#fff')
        payment_method_lab.place(x=530, y=100, height=15, width=100)
        place_input = StringVar()
        drop3 = ttk.Combobox(form_frame)
        drop3['values'] = ("Cash Cheque Debit_Card Credit_Card")
        try:
            drop3.insert(0, s[6])
        except:
            pass
        
        drop3.place(x=530, y=130, height=40, width=450)

        payment_account_lab = tk.Label(
            form_frame, text="Payment account", bg='#243e55', fg='#fff')
        place_input = StringVar()
        drop4 = ttk.Combobox(form_frame)
        drop4['values'] = ("Acc1 Acc2 Acc3 Acc4")
        try:
            drop4.insert(0, s[5])
        except:
            pass
        
        payment_account_lab.place(x=530, y=200, height=15, width=120)
        drop4.place(x=530, y=230, height=40, width=450)
        wrappen.pack(fill='both', expand='yes',)

        title_lab = tk.Label(form_frame, text="Supplier",
                             bg='#243e55', fg='#fff')
        place_input = StringVar()
        title_lab.place(x=530, y=20, height=15, width=60)
        drop5 = ttk.Combobox(form_frame)
        drop5['values'] = ("Select Supplier")
        try:
            drop5.insert(0, s[8])
        except:
            pass
        
        
        idll = tk.Label(
            form_frame, text="ID", bg='#243e55', fg='#fff')
        idl = Entry(form_frame, width=10, bg='#2f516f', fg='#fff')
        try:
            idl.insert(0, s[0])
        except:
            pass
        idll.place(x=480, y=290, height=15, width=120)
        idl.place(x=530, y=320, height=40, width=50)
        

        drop5.place(x=530, y=40, height=40, width=450)
        wrappen.pack(fill='both', expand='yes',)

        billing_ad = Label(form_frame, text="Maling Address",
                           bg='#243e55', fg='#fff')
        billing_ad.place(x=30, y=290,)
        billing_input = Entry(form_frame, width=50, bg='#2f516f', fg='#fff')
        try:
            billing_input.insert(0, s[7])
        except:
            pass
        
        billing_input.place(x=30, y=320, height=90)
        wrappen.pack(fill='both', expand='yes',)

        amount = Label(form_frame, text="AMOUNT", bg='#243e55', fg='#fff')
        amount.place(x=1130, y=200,)

        digit = font.Font(family='Times New Roman', size=35,)
        digit = Label(form_frame, text="0.00",
                      bg='#243e55', font=digit, fg='#fff')
        digit.place(x=1130, y=250,)

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
        cpro_drop1['values'] = (
            "Category 1", "Category 2", "Catefory 3", "Category 4")
        try:
            cpro_drop1.insert(0, s[9])
        except:
            pass
        
        pro.place(x=50, y=120, height=15, width=150)
        cpro_drop1.place(x=50, y=150, height=40, width=200)

        # 2
        pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
        cpro_drop2 = ttk.Combobox(form2_frame)
        cpro_drop2['values'] = (
            "Category 1", "Category 2", "Catefory 3", "Category 4")
        try:
            cpro_drop2.insert(0, s[10])
        except:
            pass
        pro.place(x=50, y=210, height=15, width=150)
        cpro_drop2.place(x=50, y=240, height=40, width=200)
        # 3
        pro = tk.Label(form2_frame, text="", bg='#243e55', fg='#fff')
        cpro_drop3 = ttk.Combobox(form2_frame)
        cpro_drop3['values'] = (
            "Category 1", "Category 2", "Catefory 3", "Category 4")
        try:
            cpro_drop3.insert(0, s[11])
        except:
            pass
        pro.place(x=50, y=280, height=15, width=150)
        cpro_drop3.place(x=50, y=310, height=40, width=200)

        # row 1
        discription_input1 = Entry(
            form2_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            discription_input1.insert(0, s[12])
        except:
            pass
        discription_input1.place(x=350, y=150, height=40, width=200)
        # row2
        discription_input2 = Entry(
            form2_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            discription_input2.insert(0, s[13])
        except:
            pass
        discription_input2.place(x=350, y=240, height=40, width=200)
        # row3
        discription_input3 = Entry(
            form2_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            discription_input3.insert(0, s[14])
        except:
            pass
        discription_input3.place(x=350, y=310, height=40, width=200)

        # row 1
        quantity_input1 = Entry(
            form2_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            quantity_input1.insert(0, s[15])
        except:
            pass
        quantity_input1.place(x=650, y=150, height=40, width=200)
        # row2
        quantity_input2 = Entry(
            form2_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            quantity_input2.insert(0, s[16])
        except:
            pass
        quantity_input2.place(x=650, y=240, height=40, width=200)
        # row3
        quantity_input3 = Entry(
            form2_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            quantity_input3.insert(0, s[17])
        except:
            pass
        quantity_input3.place(x=650, y=310, height=40, width=200)

        # row 1
        price_input1 = Entry(form2_frame, width=40, bg='#2f516f',
                             fg='#fff')
        try:
            price_input1.insert(0, s[18])
        except:
            pass
        price_input1.place(x=950, y=150, height=40, width=150)
        # row2
        price_input2 = Entry(form2_frame, width=40, bg='#2f516f',
                             fg='#fff')
        try:
            price_input2.insert(0, s[19])
        except:
            pass
        price_input2.place(x=950, y=240, height=40, width=150)
        # row3
        price_input3 = Entry(form2_frame, width=40, bg='#2f516f',
                             fg='#fff')
        try:
            price_input3.insert(0, s[20])
        except:
            pass
        price_input3.place(x=950, y=310, height=40, width=150)

        # row 1
        ctotal_input1 = Entry(form2_frame, width=40, bg='#2f516f',
                              fg='#fff', )
        try:
            ctotal_input1.insert(0, s[21])
        except:
            pass
        ctotal_input1.place(x=1200, y=150, height=40, width=100)
        # row2
        ctotal_input2 = Entry(form2_frame, width=40, bg='#2f516f',
                              fg='#fff')
        try:
            ctotal_input2.insert(0, s[22])
        except:
            pass
        ctotal_input2.place(x=1200, y=240, height=40, width=100)
        # row3
        ctotal_input3 = Entry(form2_frame, width=40, bg='#2f516f',
                              fg='#fff')
        try:
            ctotal_input3.insert(0, s[23])
        except:
            pass
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
        prod_drop1['values'] = (
            "Product 1", "Product 2", "Product 3", "Product 4")
        try:
            prod_drop1.insert(0, s[24])
        except:
            pass
        prod.place(x=50, y=120, height=15, width=150)
        prod_drop1.place(x=50, y=150, height=40, width=175)
        # 2
        prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
        prod_drop2 = ttk.Combobox(form4_frame)
        prod_drop2['values'] = (
            "Product 1", "Product 2", "Product 3", "Product 4")
        try:
            prod_drop2.insert(0, s[25])
        except:
            pass
        prod.place(x=50, y=210, height=15, width=150)
        prod_drop2.place(x=50, y=240, height=40, width=175)
        # 3
        prod = tk.Label(form4_frame, text="", bg='#243e55', fg='#fff')
        prod_drop3 = ttk.Combobox(form4_frame)
        prod_drop3['values'] = (
            "Product 1", "Product 2", "Product 3", "Product 4")
        try:
            prod_drop3.insert(0, s[26])
        except:
            pass
        prod.place(x=50, y=280, height=15, width=150)
        prod_drop3.place(x=50, y=310, height=40, width=175)

        # row 1
        description_input1 = Entry(
            form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            description_input1.insert(0, s[27])
        except:
            pass
        description_input1.place(x=380, y=150, height=40, width=200)
        # row2
        description_input2 = Entry(
            form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            description_input2.insert(0, s[28])
        except:
            pass
        description_input2.place(x=380, y=240, height=40, width=200)
        # row3
        description_input3 = Entry(
            form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            description_input3.insert(0, s[29])
        except:
            pass
        description_input3.place(x=380, y=310, height=40, width=200)

        # row 1
        hsn_input1 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            hsn_input1.insert(0, s[30])
        except:
            pass
        hsn_input1.place(x=250, y=150, height=40, width=100)
        # row2
        hsn_input2 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            hsn_input2.insert(0, s[31])
        except:
            pass
        hsn_input2.place(x=250, y=240, height=40, width=100)
        # row3
        hsn_input3 = Entry(form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            hsn_input3.insert(0, s[32])
        except:
            pass
        hsn_input3.place(x=250, y=310, height=40, width=100)

        # row 1
        pquantity_input1 = Entry(
            form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            pquantity_input1.insert(0, s[33])
        except:
            pass
        pquantity_input1.place(x=610, y=150, height=40, width=200)
        # row2
        pquantity_input2 = Entry(
            form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            pquantity_input2.insert(0, s[34])
        except:
            pass
        pquantity_input2.place(x=610, y=240, height=40, width=200)
        # row3
        pquantity_input3 = Entry(
            form4_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            pquantity_input3.insert(0, s[35])
        except:
            pass
        pquantity_input3.place(x=610, y=310, height=40, width=200)

        # row 1
        pprice_input1 = Entry(form4_frame, width=40,
                              bg='#2f516f', fg='#fff')
        try:
            pprice_input1.insert(0, s[36])
        except:
            pass
        pprice_input1.place(x=840, y=150, height=40, width=150)
        # row2
        pprice_input2 = Entry(form4_frame, width=40,
                              bg='#2f516f', fg='#fff')
        try:
            pprice_input2.insert(0, s[37])
        except:
            pass
        pprice_input2.place(x=840, y=240, height=40, width=150)
        # row3
        pprice_input3 = Entry(form4_frame, width=40,
                              bg='#2f516f', fg='#fff')
        try:
            pprice_input3.insert(0, s[38])
        except:
            pass
        pprice_input3.place(x=840, y=310, height=40, width=150)

        # row 1
        ptotal_input1 = Entry(form4_frame, width=40, bg='#2f516f',
                              fg='#fff')
        try:
            ptotal_input1.insert(0, s[39])
        except:
            pass
        ptotal_input1.place(x=1020, y=150, height=40, width=100)
        # row2
        ptotal_input2 = Entry(form4_frame, width=40, bg='#2f516f',
                              fg='#fff')
        try:
            ptotal_input2.insert(0, s[40])
        except:
            pass
        
        ptotal_input2.place(x=1020, y=240, height=40, width=100)
        # row3
        ptotal_input3 = Entry(form4_frame, width=40, bg='#2f516f',
                              fg='#fff')
        try:
            ptotal_input3.insert(0, s[41])
        except:
            pass
        ptotal_input3.place(x=1020, y=310, height=40, width=100)
        # row1
        taxpro_drop1 = ttk.Combobox(form4_frame)
        taxpro_drop1['values'] = ("10", "18", "20", "30")
        try:
            taxpro_drop1.insert(0, s[42])
        except:
            pass
        pro.place(x=1150, y=150, height=15, width=150)
        taxpro_drop1.place(x=1150, y=150, height=40, width=200)
        # row2
        taxpro_drop2 = ttk.Combobox(form4_frame)
        taxpro_drop2['values'] = ("10", "18", "20", "30")
        try:
            taxpro_drop2.insert(0, s[43])
        except:
            pass
        pro.place(x=1150, y=240, height=15, width=150)
        taxpro_drop2.place(x=1150, y=240, height=40, width=200)
        # row3
        taxpro_drop3 = ttk.Combobox(form4_frame)
        taxpro_drop3['values'] = ("10", "18", "20", "30")
        try:
            taxpro_drop1.insert(0, s[44])
        except:
            pass
        pro.place(x=1150, y=310, height=15, width=150)
        taxpro_drop3.place(x=1150, y=310, height=40, width=200)

        ##################

        sub_headingfont = font.Font(family='Times New Roman', size=18,)
        form3_frame = Frame(mycanvas, width=1600, height=500,
                            bg='#243e55', bd=1, relief="groove")
        mycanvas.create_window((0, 1500), window=form3_frame, anchor="nw")

        sub_total = Label(form3_frame, text="SUB TOTAL",
                          bg='#243e55', fg='#fff')
        sub_total.place(x=1000, y=110)
        sub_input = Entry(form3_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            sub_input.insert(0, s[45])
        except:
            pass
        sub_input.place(x=1150, y=100, height=40, width=200)

        tax_amount = Label(form3_frame, text="TAX AMOUNT",
                           bg='#243e55', fg='#fff')
        tax_amount.place(x=1000, y=160)
        tax_input = Entry(form3_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            tax_input.insert(0, s[46])
        except:
            pass
        tax_input.place(x=1150, y=150, height=40, width=200)

        grand_total = Label(
            form3_frame, text="GRAND TOTAL", bg='#243e55', fg='#fff')
        grand_total.place(x=1000, y=210)
        grand_input = Entry(form3_frame, width=40, bg='#2f516f', fg='#fff')
        try:
            grand_input.insert(0, s[47])
        except:
            pass
        grand_input.place(x=1150, y=200, height=40, width=200)

        submit = tk.Button(
            form3_frame, text="Submit Form", command=changeedit)
        submit.place(x=1150, y=280, width=100)

        D.mainloop()

    def delete():
        # Get selected item to Delete
        selected_item = treevv.selection()[0]
        treevv.delete(selected_item)

    edit_btn = ttk.Button(hd, text="Edit", command=editexp)
    edit_btn.place(relx=0.35, rely=0.8, relheight=0.1, relwidth=0.1)
    del_btn = ttk.Button(hd, text="Delete", command=delete)
    del_btn.place(relx=0.5, rely=0.8, relheight=0.1, relwidth=0.1)

    A.mainloop()


main()
