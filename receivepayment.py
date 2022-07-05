from msilib import Table
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import datetime as dt
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
        database='finsYs_tkinter',
        # buffer=True
        )
    mycursor = mydb2.cursor(buffered=True)
    

# def add_invoice():

def add_accountss():
    
    
    
    def sub_check():
        if sub_account.get()==1:
            subaccountinput = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
                        'Input Credit', 'Deferred Service Tax Input Credit', 'Deferred SGST', 'Deferred VAT Input Credit',
                        'GST Refund', 'Inventory Asset', 'Paid Insurance', 'Service Tax Refund', 'TDS Receivable', 'Uncategorised Asset',
                        'Accumulated Depreciation', 'Buildings and Improvements', 'Furniture and Equipment', 'Land', 'Leasehold Improvements',
                        'CGST Payable', 'CST Payable', 'CST Suspense', 'GST Payable', 'GST Suspense', 'IGST Payable', 'Input CGST', 'Input CGST Tax RCM',
                        'Input IGST', 'Input IGST Tax RCM', 'Input Krishi Kalyan Cess', 'Input Krishi Kalyan Cess RCM', 'Input Service Tax',
                        'Input Service Tax RCM', 'Input VAT 14%', 'Input VAT 4%', 'Input VAT 5%', 'Krishi Kalyan Cess Payable', 'Krishi Kalyan Cess Suspense',
                        'Output CGST', 'Output CGST Tax RCM', 'Output CST 2%', 'Output IGST', 'Output IGST Tax RCM', 'Output Krishi Kalyan Cess',
                        'Output Krishi Kalyan Cess DCM', 'Output Service Tax', 'Output Service Tax RCM', 'Output SGST', 'Output SGST Tax RCM',
                        'Output VAT 14%', 'Output VAT 4%', 'Output VAT 5%', 'Service Tax Payable', 'Service Tax Suspense', 'SGST Payable', 'Swachh Bharat Cess Payable',
                        'TDS Payable', 'VAT Payable', 'VAT Suspense', 'Opening Balance', 'Equity']

            cb = ttk.Combobox(hd1, values=subaccountinput)
            cb.current(0)
            cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)
        else:
            
            cb = Entry(hd1)

            cb.insert(0, " Deffered CGST")
            cb.config(state='disabled')

            cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)
    def cancel():
        add.destroy()
        
    fun()
    def save_data():
        fun()
        typelist=[]
        type = typeinput.get()
        typelist.append(type)
        
        #data fetched from app1_accountype
        sql="select * from app1_accountype where accountname=%s"
        mycursor.execute(sql,typelist)
        pro=mycursor.fetchone()

        sql2="select Pid from producttable where Pname=%s"
        mycursor.execute(sql2,typelist)
        product_id=mycursor.fetchone()

            


        # cur.execute("select cid from app1_company where id_id=%s",(uid))
        # cmp1=cur.fetchone()
        detlist=[]
        accname = fnameinput.get()
        detail_type = l.get()
        detlist.append(detail_type)
        description = co.get()
        sub_account = cb.get()
        deftaxcode = nb.get()
        
        cmp=cmp1
        

            #fetch data from app1_accountype
        prosql="select * from app1_accountype where accountname=%s"
        mycursor.execute(prosql,detlist)
        prodetdata=mycursor.fetchone()
        


        # fetch data from app1_accounts
        sql3="select *  from app1_accounts "
        mycursor.execute(sql3)
        accounts_data=mycursor.fetchall()
        fet_data=[]
        
        for data in accounts_data:
        
            if data[3]==accname and data[1]==type and data[10]==cmp:
                reda=data
                fet_data.append(reda)

        # fetch data from app1_accounts1
        sql3="select *  from app1_accounts1 "
        mycursor.execute(sql3)
        accounts_data=mycursor.fetchall()
        fet_data1=[]
        for data in accounts_data:

            if data[3]==accname and data[1]==type and data[10]==cmp:
                reda1=data
                fet_data1.append(reda1)
        




        if  prodetdata!=None :
            if fet_data!=None or fet_data1!=None:
                messagebox.showerror('error',f"Account with {accname} already exists. Please provide another name.")
        else:
            sql="INSERT INTO app1_accounts (acctype,detype,name,description,gst,deftaxcode,cid_id,productid_id,proid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
            val=(type,detail_type,accname,description,sub_account,deftaxcode,cmp[0],product_id[0],pro[0])
            mycursor.execute(sql,val)
            mydb2.commit()

            # sql1="INSERT INTO app1_accounts1 (detype,balance,cid_id) VALUES(%s,%s,%s)" #adding values into db
            # val1=(detail_type,finsys_amt,cmp[0])
            # cur.execute(sql1,val1)
            


            sql2="INSERT INTO app1_accountype (accountname,accountbal,cid_id) VALUES(%s,%s,%s)" #adding values into db
            val2=(detail_type,cmp[0])
            mycursor.execute(sql2,val2)
            mydb2.commit()

            mycursor.execute("select * from app1_accounts1 where name=%s and cid_id=%s ",("Opening Balance Equity",cmp[0]))
            balaceeq=mycursor.fetchone()
            balance=round(balaceeq[7]+float(),2)

            mycursor.execute("UPDATE app1_accounts1 SET balance =%s where accounts1id=%s and cid_id=%s",(balance,balaceeq[0],cmp[0]))
            mydb2.commit()
            
            messagebox.showinfo(title='Success',message='New Account Added')
            add.destroy()




    mycursor.execute('select Pname,Pid from producttable')
    product_data=mycursor.fetchall()
    mycursor.execute('select Itemname from itemstable')
    item_data=mycursor.fetchall()
    print("dataaaaaaaaaa",product_data)
    print("pta",item_data)

    global add, bm
    add = tk.Toplevel(root)
    add.title('Add Account')
    add.geometry('1000x800')

    # mycanvas = tk.Canvas(add, width=2000, height=1200)
    # mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    # yscrollbar = ttk.Scrollbar(
    #     add, orient='vertical', command=mycanvas.yview)
    # yscrollbar.pack(side=RIGHT, fill=Y)
    # mycanvas.configure(yscrollcommand=yscrollbar.set)
    # mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
    #     scrollregion=mycanvas.bbox('all')))
    # frame = tk.Frame(mycanvas)
    f2 = font.Font(family='Times New Roman', size=30)
    add['bg'] = '#2f516f'

    # mycanvas.create_window((0, 0), window=frame,
    #                         anchor='nw', width=2000, height=1000)

    # # contents frame
    uid=[4]
    mycursor.execute("select cid from app1_company where id_id=%s",(uid))
    cmp1=mycursor.fetchone()
    acc_heading= Label(add, text="ACCOUNT CREATE",bd=0,relief="groove",bg='#2f516f',font=f2, fg='#fff',height=2,pady=2,width=100)
    acc_heading.pack()
    hd1 = tk.Frame(add,width=900,height=650)
    hd1['bg'] = '#243e54'
    hd1.place(relx=0.05, rely=0.1)

        # font

    tk.Label(hd1, text='Account Type', bg='#243e54', fg="#fff",font=(
        'times new roman', 14)).place(relx=0.04, rely=0.05)
    typeinput = StringVar()
    cm1 =ttk.Combobox(hd1,textvariable = typeinput)
    value=[]
    for pro_data in product_data:
        value.append(pro_data[0])
        cm1['values']=value
    # cm1['values']=('Bank','Current Assets')
    cm1.place(relx=0.04, rely=0.10, relwidth=0.4, relheight=0.065)

    tk.Label(hd1, text='Name', bg='#243e54', fg="#fff",font=(
        'times new roman', 14)).place(relx=0.5, rely=0.05)
    nameinput = StringVar()
    fnameinput = tk.Entry(hd1, textvariable=nameinput,bg="#3E505C",fg="#fff")

    fnameinput.place(relx=0.5, rely=0.10, relwidth=0.4, relheight=0.065)


    def detype(g):
        def dtl():
            fnameinput.delete(0,END)
        ok=l.get()
        print("ctc",ok)
        dtl()
        fnameinput.insert(0,l.get())

    tk.Label(hd1, text='Detail Type',fg="#fff", font=('times new roman', 14),
                bg='#243e54').place(relx=0.04, rely=0.2)
    detailtypeinput = StringVar()
    l =ttk.Combobox(hd1,textvariable = detailtypeinput)
    itemvalue=[]
    for it_data in item_data:
        itemvalue.append(it_data)
        l['values']=itemvalue
        l.bind('<<ComboboxSelected>>',detype)
    l.place(relx=0.04, rely=0.25, relwidth=0.4, relheight=0.065)

    tk.Label(hd1, text='Description',fg="#fff", font=('times new roman', 14),
                bg='#243e54').place(relx=0.5, rely=0.2)
    descriptioninput = StringVar()
    co = tk.Entry(hd1, textvariable=descriptioninput,bg="#3E505C",fg="#fff")
    #co.insert(1, s[4])
    co.place(relx=0.5, rely=0.25, relwidth=0.4, relheight=0.065)

    message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    text_box = Text(hd1,bg="#3E505C",fg="#fff")
    text_box.place(relx=0.04, rely=0.35, relwidth=0.4, relheight=0.3)
    text_box.insert('end', message)
    text_box.config(state='disabled')
    sub_account= IntVar()
    sub_account_input=Checkbutton(hd1,onvalue=1, offvalue = 0 ,variable = sub_account, bg='#243e54',height=4,command='sub_check').place(relx=0.5, rely=0.32)


    tk.Label(hd1, text='Is sub-account', fg="#fff",font=('times new roman', 14),
                bg='#243e54').place(relx=0.55, rely=0.35)
    # subaccountinput="Deffered_CGST"
    typeinput = StringVar()
    cb =ttk.Combobox(hd1,textvariable = typeinput)
    cb['values']=("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Buildings and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Service Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","Service Tax Suspense","SGST Payable","SGST Suspense","Swachh Bharat Cess Payable","Swachh Bharat Cess Suspense","TDS Payable","VAT Payable","VAT Suspense","Opening Balance","Equity")
   
    cb.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.065)
    
    

    tk.Label(hd1, text='Default Tax Code', font=('times new roman', 14),fg="#fff",
                bg='#243e54').place(relx=0.5, rely=0.5)
    defaulttaxcodeinput = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                            '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
    nb = ttk.Combobox(hd1, values=defaulttaxcodeinput)

    nb.place(relx=0.5, rely=0.55, relwidth=0.4, relheight=0.065)

   
    sub = tk.Button(hd1, text='Create', font=15, bg='#243e54',fg="#fff",width=40,
                    command=save_data).place(relx=0.28, rely=0.8)

        



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

full_frame=Frame(mycanvas,width=1345,height=2550,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas,bg="white")
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1345,height=2550,bg='#2f516f')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#2f516f",width=100)
form_lable.place(x=0,y=0)

wrappen.pack(fill='both',expand='yes',)

tit = Label(heading_frame, text="RECIEVE PAYMENT", font=('times new roman', 25, 'bold'),padx=500, pady=2, bd=5, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()


fun()
mycursor.execute('select * from app1_customer ')
customers=mycursor.fetchall()
customers_data=[]
for cus in customers:
    customers_data.append(cus)


mycursor.execute('select * from app1_accounts ')
account=mycursor.fetchall()
account_data=[]
for acc in account:
    account_data.append(acc)
    
    
mycursor.execute('select * from app1_payment ')
payments=mycursor.fetchall()
payments_data=[]
for pay in payments:
    payments_data.append(pay)


#set today date 
date = dt.datetime.now()
format_date = f"{date:%Y - %d - %m }"
today_date = Label(form_frame, text=format_date, fg="white", bg="black", font=("helvetica", 40))

#company details
user_id=[4]
mycursor.execute("SELECT cid FROM app1_company WHERE id_id=%s",(user_id))
cmp1=mycursor.fetchone()

# cmp1=[1]

mycursor.execute("SELECT cname,cemail,state FROM app1_company WHERE id_id=%s",(user_id))
cmp_data=mycursor.fetchone()


global select_customer,email,invno,paydate,paymethod,deposit,amountrec,amountrecon,tabdescription,tabduedate,taboriginalamount,tabopenbalance,tabpayment,amountapply
select_customer = StringVar(form_frame)
email = StringVar(form_frame)
invno = StringVar(form_frame)
paydate = StringVar(form_frame)
paymethod = StringVar(form_frame)
add = StringVar(form_frame)
deposit = StringVar(form_frame)
amountrec = StringVar(form_frame)
amountrecon = StringVar(form_frame)
tabdescription = StringVar(form_frame)
tabduedate = StringVar(form_frame)
taboriginalamount = StringVar(form_frame)
tabopenbalance = StringVar(form_frame)
tabpayment = StringVar(form_frame)
amountapply = StringVar(form_frame)


F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=30, pady=30, bd=0, fg="Black", bg="#243e55")
F.place(x=35, y=30, width=1270, height=1950)

label4=Label(F, text="Fin sYs", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=530,y=5)


def get_mail(event):
    def des():
        label44tabdescription.delete(0,END)
        label33email.delete(0,END)
        label44tabduedate.delete(0,END)
        label44taboriginalamount.delete(0,END)
        label44tabopenbalance.delete(0,END)
    des()
    option=drop12.get()
    x = option.split(" ", 1)
    print("boy",option)
    # mycursor.execute("SELECT * FROM app1_customer where firstname=%s and lastname=%s",(x[0],x[1]))
    # table1=mycursor.fetchone()
    # email.set(table1[9])
        # billto.set(i[12:17])
    
    mycursor.execute("SELECT descrip,email,duedate,orgamt,openbal FROM app1_payment where customer=%s ",([option]))
    table2=mycursor.fetchone() 
    label33email.insert(0,table2[1])
    label44tabduedate.insert(0,table2[2])
    label44tabdescription.insert(0,table2[0])
    label44taboriginalamount.insert(0,table2[3])
    label44tabopenbalance.insert(0,table2[4])
        


select_customer_lab=tk.Label(F,text="Customer",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop12=ttk.Combobox(F,textvariable=select_customer,font=('times new roman', 11, 'bold'))
value=[]
for cust in  customers_data:
    customer_values=cust[-1]
    
    if customer_values==cmp1[0]:
        value.append((cust[2]+' '+cust[3]))
        drop12['values']=value
    else:
        pass

drop12.bind("<<ComboboxSelected>>",get_mail)
select_customer_lab.place(x=100,y=90)
drop12.place(x=100,y=130,height=40,width=270)



add_custom=Button(F,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command='add_custom')
add_custom.place(x=375,y=130)


label3=Label(F, text="Email", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=450,y=90)
label33email=Entry(F,bg='#2f516a',fg='#fff',textvariable=email, font=('times new roman', 11, 'bold'))
label33email.place(x=450,y=130,height=40,width=300)

label4=Label(F, text="Find by invoice number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=90)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=800,y=130,height=40,width=300)


label3=Label(F, text="Payment Date", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=100,y=170)
paydate.set(format_date)
label33=Entry(F,bg='#2f516a',fg='#fff',textvariable=paydate, font=('times new roman', 11, 'bold'))
label33.place(x=100,y=210,height=40,width=300)



def pmethod(event):
    global add,pro1
    p = drop1paymethod.get()
    print("wel",p)
      
    if p == 'Add New':
        def wer(n):
            cc=label44add.get()
            pro1.insert(0,cc)
            print("ff",pro1)
            drop1paymethod.insert(0,label44add.get())
        drop1paymethod.set("")
        label44add=Entry(F,bg='#2f516a',fg='#fff',textvariable=add, font=('times new roman', 11, 'bold'))
        label44add.place(x=100,y=340,height=40,width=300)
        label44add.bind("<FocusIn>",wer)
    else:
        add.set("")
    
pro1=["Cash","Check","Credit Card","Add New"]
sanitizer1_lbl=tk.Label(F,text="Payment Method",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop1paymethod=ttk.Combobox(F,values=pro1)

sanitizer1_lbl.place(x=100,y=250)
drop1paymethod.bind("<<ComboboxSelected>>",pmethod)
drop1paymethod.place(x=100,y=290,height=40,width=300)



sanitizer_lbl=tk.Label(F,text="Deposit To",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop1accounttype=ttk.Combobox(F,textvariable='accounttype')
drop1accounttype['values']=("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund")
sanitizer_lbl.place(x=800,y=250)
drop1accounttype.place(x=800,y=290,height=40,width=270)

add_custom=Button(F,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=3,height=2,command=add_accountss)
add_custom.place(x=1075,y=290)


def key_press(event):
    def dec():
        label4amount.delete(0,END)
        label44tabpayment.delete(0,END)
        label44amountapply.delete(0,END)
    # dec()   
    act=label44amountrec.get()
    print("wowo",act)
    dec()
    label4amount.insert(0,label44amountrec.get())
    label44tabpayment.insert(0,label44amountrec.get())
    label44amountapply.insert(0,label44amountrec.get())
    
label4=Label(F, text="Amount Recieved", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=340)
label44amountrec=Entry(F,bg='#2f516a',fg='#fff',textvariable=amountrec, font=('times new roman', 11, 'bold'))
label44amountrec.place(x=800,y=380,height=40,width=300)
label44amountrec.bind('<KeyRelease>', key_press)

label4=Label(F, text="AMOUNT RECIEVED", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=800,y=430)
label4amount=Entry(F,bg='#2f516a',fg='black',textvariable=amountrecon, font=('times new roman', 11, 'bold'),)
label4amount.place(x=800,y=470,height=40,width=300)





# Table

#
label4=Label(F, text="#", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=10,y=540)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=10,y=580,height=40,width=50)

label4=Label(F, text="DESCRIPTION", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=75,y=540)
label44tabdescription=Entry(F,bg='#2f516a',fg='#fff',textvariable=tabdescription, font=('times new roman', 11, 'bold'))
label44tabdescription.place(x=75,y=580,height=40,width=210)


label4=Label(F, text="DUE DATE", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=295,y=540)
label44tabduedate=Entry(F,bg='#2f516a',fg='#fff',textvariable=tabduedate, font=('times new roman', 11, 'bold'))
label44tabduedate.place(x=295,y=580,height=40,width=210)

label4=Label(F, text="ORIGINAL AMOUNT", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=515,y=540)
label44taboriginalamount=Entry(F,bg='#2f516a',fg='#fff',textvariable=taboriginalamount, font=('times new roman', 11, 'bold'))
label44taboriginalamount.place(x=515,y=580,height=40,width=210)

label4=Label(F, text="OPEN BALANCE", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=735,y=540)
label44tabopenbalance=Entry(F,bg='#2f516a',fg='#fff',textvariable=tabopenbalance, font=('times new roman', 11, 'bold'))
label44tabopenbalance.place(x=735,y=580,height=40,width=210)


def key_press1(event):
    def decc():
        label4amount.delete(0,END)
        label44amountrec.delete(0,END)
        label44amountapply.delete(0,END)
    # # dec()   
    acc=label44tabpayment.get()
    print("wowoc",acc)
    decc()
    label4amount.insert(0,label44tabpayment.get())
    label44amountrec.insert(0,label44tabpayment.get())
    label44amountapply.insert(0,label44tabpayment.get())
label4=Label(F, text="PAYMENT", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=955,y=540)
label44tabpayment=Entry(F,bg='#2f516a',fg='#fff',textvariable=tabpayment, font=('times new roman', 11, 'bold'))
label44tabpayment.place(x=955,y=580,height=40,width=210)
label44tabpayment.bind('<KeyRelease>', key_press1)







label4=Label(F, text="Amount to Apply", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=750,y=670)
label44amountapply=Entry(F,bg='#2f516a',fg='#fff',textvariable=amountapply, font=('times new roman', 11, 'bold'))
label44amountapply.place(x=955,y=670,height=40,width=210)


label4=Label(F, text="Amount to Credit", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=750,y=730)
label44=Entry(F,bg='#2f516a',fg='#fff',textvariable='desig', font=('times new roman', 11, 'bold'))
label44.place(x=955,y=730,height=40,width=210)


root.mainloop()