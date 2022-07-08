import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox as MessageBox
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql
import pymysql

def fun():#db connection
    global mydb2,mycursor
    mydb2=mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='finsys_tkinter1'
        )
    mycursor = mydb2.cursor()
    



def add_recon1():
    print("hai")
    # fun()
    global accounttype,beginningbalance,endingbalance,endingdate,edat,serchar,expacc,idat1,intear,incacc
    accounttype=accounttype.get()
    beginningbalance=beginningbalance.get()
    endingbalance=endingbalance.get()
    endingdate=endingdate.get()
    edat=edat.get()
    serchar=serchar.get()
    expacc=expacc.get()
    idat1=idat1.get()
    intear=intear.get()
    incacc=incacc.get()
    cid_id=1
    sql="INSERT INTO app1_recon1 (accounttype,beginningbalance,endingbalance ,endingdate,edat,serchar,expacc ,idat1 ,intear ,incacc,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
    val=(accounttype,beginningbalance,endingbalance,endingdate,edat,serchar,expacc,idat1,intear,incacc,cid_id)
    mycursor.execute(sql, val)
    mydb2.commit()
    mydb2.close()
    tkinter.messagebox.showinfo("ADD", "Record entered successfully")
      
    import tkinter as tk
    # from tkinter import *
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
        # import addcustomer_form
        fun()
        print("hellboy111")   
        global recon_data
        # global tree_data
        focus_data = tree_data.focus()
        values=tree_data.item(focus_data,'values')
        recon1_id=[values[-1]]
        mycursor.execute("SELECT * FROM app1_recon1 WHERE recon1id=%s",(recon1_id))
        data=mycursor.fetchone()
        print("hellboy")
    
    shell = tk.Toplevel(root)
    shell.title("finsYs")
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    shell.geometry("%dx%d" %(width,height))
    shell.configure(bg="#2f516f")
    wrappen=ttk.LabelFrame(shell)
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
    customers_data=[]
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
    print("wild")
    print(customers_data[-1])
    print(data)
    print("wild")

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
    print('melc')
    print(data[2])
    print('melc')
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

    sql = 'SELECT edat,accounttype,recon1id,expacc,beginningbalance,endingbalance,intear,serchar,recon1id from app1_recon1'
    mycursor.execute(sql)
    treed_data=mycursor.fetchall()
    total=mycursor.rowcount

    for data in treed_data:
        tree_data.insert("", 'end',values=data)
        
    tree_data.grid(row=3,column=0,padx=5,pady=10)

    wrappen.pack(fill='both',expand='yes',)

    wrappen.pack(fill='both',expand='yes',)

    wrappen.pack(fill='both',expand='yes',)

    shell.mainloop()





    
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
mycanvas.create_window((0,40),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1340,height=1900,bg='#243e55')
mycanvas.create_window((0,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg='#243e55',width=100)
form_lable.place(x=0,y=0)


fun()
tit = Label(heading_frame, text="Reconcile An Account", font=('times new roman', 30, 'bold'),padx=475, pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()
head_label = Label(heading_frame,text="Open your statement and let's get started.", font=('times new roman', 9, 'bold'),padx=0, pady=2,width=189, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
head_label.pack()

F2 = LabelFrame(form_frame, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F2.place(x=5, y=100, width=500, height=700)
size=(500,700)


ax=Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size)
wer = ImageTk.PhotoImage(ax,master=root)
lab1=tk.Label(F2,image=wer)
lab1.place(relx=0.00,rely=-0,relheight=1,relwidth=1)

# ax1=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
# tk.Label(F2,image=ax1,bg='#243e54').place(relx=0.00,rely=-0,relheight=1,relwidth=1)

# image3 = tk.PhotoImage(file="bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg")
# Label(F2, text="", image = image3).grid(row=0, column=0)


# f2=tk.Frame(form_frame,bg='#243e54')
# size=(500,700)
# ax=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
# tk.Label(f2,image=ax,bg='#243e54').place(relx=0.00,rely=-0,relheight=1,relwidth=1)


wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

global accounttype,beginningbalance,endingbalance,endingdate,edat,serchar,expacc,idat1,intear,incacc
accounttype=StringVar()
beginningbalance=StringVar()
endingbalance=StringVar()
endingdate=StringVar()
edat=StringVar()
serchar=StringVar()
expacc=StringVar()
idat1=StringVar()
intear=StringVar()
incacc=StringVar()

F2 = LabelFrame(form_frame, text="Which account do you want to reconcile..??", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F2.place(x=510, y=100, width=830, height=700)

CheckVar1 = IntVar()

sanitizer1_lbl=tk.Label(F2,text="Account",bg='#243e55',fg='#fff',font=('times new roman', 16, 'bold'))

drop1=ttk.Combobox(F2,textvariable=accounttype)

drop1['values']=("Checking","Savings","Inventory Asset","Prepaid Expenses","Uncategorized Asset","Truck")

sanitizer1_lbl.place(x=10,y=50,height=15,width=100)
drop1.place(x=280,y=50,height=30,width=450)
wrappen.pack(fill='both',expand='yes',)


sanitize_lbl = Label(F2, text="Enter the following from your statement.", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitize_lbl.place(x=10,y=110)

mask_lbl = Label(F2, text="Beginning balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
mask_lbl.place(x=10,y=160)
mask_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE,textvariable=beginningbalance)
mask_txt.place(x=10,y=200)

hand_gloves_lbl = Label(F2, text="Ending balance", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
hand_gloves_lbl.place(x=280,y=160)
hand_gloves_txt = Entry(F2, width=22,  font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief =GROOVE,textvariable=endingbalance)
hand_gloves_txt.place(x=280,y=200)

syrup_lbl = Label(F2, text="Ending date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
syrup_lbl.place(x=550,y=160)
#Create a Calendar using DateEntry
cal = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable=endingdate)
cal.place(x=550,y=200)

sanitize_lbl = Label(F2, text="Enter the service charge or interest earned, if necessary.", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
sanitize_lbl.place(x=10,y=280)

cream_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
cream_lbl.place(x=10,y=340)
#Create a Calendar using DateEntry
cal1 = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable=edat)
cal1.place(x=10,y=380)

thermal_gun_lbl = Label(F2, text="Service charge", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_gun_lbl.place(x=280,y=340)
thermal_gun_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff",bd=5,relief=GROOVE,textvariable=serchar)
thermal_gun_txt.place(x=280,y=380)

select_customer_lab=tk.Label(F2,text="Expense Account",font=('times new roman', 16, 'bold'),bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop2=ttk.Combobox(F2,width=22,textvariable=expacc)

drop2['values']=('Advertising/Promotional',
            'Bank charges',
            'Business Licenses and Permits',
            'Charitable Contributions',
            'Computer and Internet Expense',
            'Continuing Education',
            'Depreciation Expense',
            'Dues and Subscriptions',
            'Housekeeping Charges',
            'Insurance Expense',
            'Insurance Expense-General Liability Insurance',
            'Insurance Expense-Health Insurance',
            'Insurance Expense-Life and Disability Insurance',
            'Insurance Expense-Professional Liability',
            'Interest Expense',
            'Meals and entertainment',
            'Office Supplies',
            'Postage and Delivery',
            'Printing and Reproduction',
            'Professional Fees',
            'Purchases',
            'Rent Expense',
            'Repair and maintenance',
            'Small Tools and Equipment',
            'Swachh Bharat Cess Expense',
            'Taxes - Property',
            'Telephone Expense',
            'Travel Expense',
            'Uncategorised Expense',
            'Utilities',
            'Cash and cash equivalents',
            'Accounts Receivable (Debtors)',
            'Deferred CGST',
            'Deferred GST Input Credit',
            'Deferred IGST',
            'Deferred Krishi Kalyan Cess Input Credit',
            'Deferred Service Tax Input Credit',
            'Deferred SGST',
            'Deferred VAT Input Credit',
            'GST Refund',
            'Inventory Asset',
            'Krishi Kalyan Cess Refund',
            'Prepaid Insurance',
            'Service Tax Refund',
            'TDS Receivable',
            'Uncategorised Asset',
            'Undeposited Funds',
            'Accumulated Depreciation',
            'Buildings and Improvements',
            'Furniture and Equipment',
            'Land',
            'Leasehold Improvements',
            'Vehicles',
            'CGST Payable',
            'CST Payable',
            'CST Suspense',
            'GST Payable',
            'GST Suspense',
            'IGST Payable',
            'Input CGST',
            'Input CGST Tax RCM',
            'Input IGST',
            'Input IGST Tax RCM',
            'Input Krishi Kalyan Cess',
            'Input Krishi Kalyan Cess RCM',
            'Input Service Tax',
            'Input Service Tax RCM',
            'Input SGST',
            'Input SGST Tax RCM',
            'Input VAT 14%',
            'Input VAT 4%',
            'Input VAT 5%',
            'Krishi Kalyan Cess Payable',
            'Krishi Kalyan Cess Suspense',
            'Output CGST',
            'Output CGST Tax RCM',
            'Output CST 2%',
            'Output IGST',
            'Output IGST Tax RCM',
            'Output Krishi Kalyan Cess',
            'Output Krishi Kalyan Cess RCM',
            'Output Service Tax',
            'Output Service Tax RCM',
            'Output SGST',
            'Output SGST Tax RCM',
            'Output VAT 14%',
            'Output VAT 4%',
            'Output VAT 5%',
            'Service Tax Payable',
            'Service Tax Suspense',
            'SGST Payable',
            'Swachh Bharat Cess Payable',
            'Swachh Bharat Cess Suspense',
            'TDS Payable',
            'VAT Suspense',
            'Opening Balance Equity',
            'Retained Earnings',
            'Billable Expense Income',
            'Consulting Income',
            'Product Sales',
            'Sales',
            'Sales - Hardware',
            'Sales - Software',
            'Sales - Support and Maintenance',
            'Sales Discounts',
            'Sales of Product Income',
            'Uncategorised Income',
            'Cost of sales',
            'Equipment Rental for Jobs',
            'Freight and Shipping Costs',
            'Merchant Account Fees',
            'Purchases - Hardware for Resale',
            'Purchases - Software for Resale'
            'Subcontracted Services',
            'Tools and Craft Supplies',
            'Finance Charge Income',
            'Insurance Proceeds Received',
            'Interest Income',
            'Proceeds from Sale of Assets',
            'Shipping and Delivery Income',
            'Ask My Accountant',
            'CGST write-off',
            'GST write-off',
            'IGST write-off',
            'Miscellaneous Expense',
            'Political Contributions',
            'SGST write-off',
            'Tax write-of',
            'Vehicle Expenses')

select_customer_lab.place(x=550,y=340)
drop2.place(x=550,y=380,width=250,height=33)
wrappen.pack(fill='both',expand='yes')

thermal_zone_lbl = Label(F2, text="Date", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zone_lbl.place(x=10,y=440)
#Create a Calendar using DateEntry
cal2 = DateEntry(F2, width= 22, font=('times new roman', 15, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable=idat1)
cal2.place(x=10,y=480)

thermal_zoo_lbl = Label(F2, text="Interest earned", font=('times new roman', 16, 'bold'), bg="#243e55", fg="#fff")
thermal_zoo_lbl.place(x=280,y=440)
thermal_zoo_txt = Entry(F2, width=22, font=('times new roman', 16, 'bold'),fg="#243e55",bg="#fff", bd=5, relief=GROOVE,textvariable=intear)
thermal_zoo_txt.place(x=280,y=480)

select_customer_lab1=tk.Label(F2,text="Income Account",font=('times new roman', 16, 'bold'),bg='#243e55',fg='#fff')
select_customer_input=StringVar()
drop3=ttk.Combobox(F2,width=22, textvariable = incacc)

drop3['values']=('Advertising/Promotional',
            'Bank charges',
            'Business Licenses and Permits',
            'Charitable Contributions',
            'Computer and Internet Expense',
            'Continuing Education',
            'Depreciation Expense',
            'Dues and Subscriptions',
            'Housekeeping Charges',
            'Insurance Expense',
            'Insurance Expense-General Liability Insurance',
            'Insurance Expense-Health Insurance',
            'Insurance Expense-Life and Disability Insurance',
            'Insurance Expense-Professional Liability',
            'Interest Expense',
            'Meals and entertainment',
            'Office Supplies',
            'Postage and Delivery',
            'Printing and Reproduction',
            'Professional Fees',
            'Purchases',
            'Rent Expense',
            'Repair and maintenance',
            'Small Tools and Equipment',
            'Swachh Bharat Cess Expense',
            'Taxes - Property',
            'Telephone Expense',
            'Travel Expense',
            'Uncategorised Expense',
            'Utilities',
            'Cash and cash equivalents',
            'Accounts Receivable (Debtors)',
            'Deferred CGST',
            'Deferred GST Input Credit',
            'Deferred IGST',
            'Deferred Krishi Kalyan Cess Input Credit',
            'Deferred Service Tax Input Credit',
            'Deferred SGST',
            'Deferred VAT Input Credit',
            'GST Refund',
            'Inventory Asset',
            'Krishi Kalyan Cess Refund',
            'Prepaid Insurance',
            'Service Tax Refund',
            'TDS Receivable',
            'Uncategorised Asset',
            'Undeposited Funds',
            'Accumulated Depreciation',
            'Buildings and Improvements',
            'Furniture and Equipment',
            'Land',
            'Leasehold Improvements',
            'Vehicles',
            'CGST Payable',
            'CST Payable',
            'CST Suspense',
            'GST Payable',
            'GST Suspense',
            'IGST Payable',
            'Input CGST',
            'Input CGST Tax RCM',
            'Input IGST',
            'Input IGST Tax RCM',
            'Input Krishi Kalyan Cess',
            'Input Krishi Kalyan Cess RCM',
            'Input Service Tax',
            'Input Service Tax RCM',
            'Input SGST',
            'Input SGST Tax RCM',
            'Input VAT 14%',
            'Input VAT 4%',
            'Input VAT 5%',
            'Krishi Kalyan Cess Payable',
            'Krishi Kalyan Cess Suspense',
            'Output CGST',
            'Output CGST Tax RCM',
            'Output CST 2%',
            'Output IGST',
            'Output IGST Tax RCM',
            'Output Krishi Kalyan Cess',
            'Output Krishi Kalyan Cess RCM',
            'Output Service Tax',
            'Output Service Tax RCM',
            'Output SGST',
            'Output SGST Tax RCM',
            'Output VAT 14%',
            'Output VAT 4%',
            'Output VAT 5%',
            'Service Tax Payable',
            'Service Tax Suspense',
            'SGST Payable',
            'Swachh Bharat Cess Payable',
            'Swachh Bharat Cess Suspense',
            'TDS Payable',
            'VAT Suspense',
            'Opening Balance Equity',
            'Retained Earnings',
            'Billable Expense Income',
            'Consulting Income',
            'Product Sales',
            'Sales',
            'Sales - Hardware',
            'Sales - Software',
            'Sales - Support and Maintenance',
            'Sales Discounts',
            'Sales of Product Income',
            'Uncategorised Income',
            'Cost of sales',
            'Equipment Rental for Jobs',
            'Freight and Shipping Costs',
            'Merchant Account Fees',
            'Purchases - Hardware for Resale',
            'Purchases - Software for Resale'
            'Subcontracted Services',
            'Tools and Craft Supplies',
            'Finance Charge Income',
            'Insurance Proceeds Received',
            'Interest Income',
            'Proceeds from Sale of Assets',
            'Shipping and Delivery Income',
            'Ask My Accountant',
            'CGST write-off',
            'GST write-off',
            'IGST write-off',
            'Miscellaneous Expense',
            'Political Contributions',
            'SGST write-off',
            'Tax write-of',
            'Vehicle Expenses')

select_customer_lab1.place(x=550,y=440)
drop3.place(x=550,y=480,width=250,height=33)
wrappen.pack(fill='both',expand='yes')

b1 = Button(F2,text = "Start Reconciling",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command=add_recon1)  
b1.place(x=280,y=560,width=250,height=40) 

# btn = Button(root, text="bank reconcilation",command=bank)
# btn.pack()
root.mainloop()


