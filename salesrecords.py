from math import prod
from multiprocessing.sharedctypes import Value
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
import tkinter.messagebox
import mysql.connector as mysql
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkcalendar import Calendar, DateEntry
import datetime as dt

def fun():#db connection
    global mydb1,mycursor
    mydb1=mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='finsys_tkinter1'
        )
    mycursor = mydb1.cursor()
#def add_custom():
    #import addcustomer_form



#edir customer 
def edit_sale():
    #update data
    def get_selected_e_product(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4,final_total
        createsubtotal =0
        finding_tax1=0
        finding_tax2=0
        finding_tax3=0
        finding_tax4=0
        final_total=0
        selected_product=[]
        product=product_drop1.get()
        quantity=qty_input1.get()
        selected_product.append(product)
        # for product in sal_data:
        #     product_details="SELECT * FROM salesrecpts WHERE name=%s"
        #     mycursor.execute(product_details,selected_product)
        #     data=mycursor.fetchall()
        #     for i in data:
        #         e_hsn.set(i[11])
        #         e_desc.set(i[12])
        #         e_price.set(i[14])
        #         e_sale_price=i[14]
        #         tota_price=int(e_sale_price)*int(quantity)
        #         e_total.set(tota_price)
        for product in inv_data:
            product_details="SELECT * FROM inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn.set(i[4])
                e_desc.set(i[11])
                e_price.set(i[12])
                e_sale_price=i[12]
                tota_price=int(e_sale_price)*int(quantity)
                e_total.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn.set(i[4])
                e_desc.set(i[7])
                e_price.set(i[8])
                e_sale_price=i[8]
                tota_price=int(e_sale_price)*int(quantity)
                e_total.set(tota_price) 
        
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn.set(i[4])
                e_desc.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                e_price.set(sale_price)
                
                tota_price=int(sale_price)*int(quantity)
                e_total.set(tota_price)   
        createsubtotal=int(e_total.get())+int(e_total2.get())+int(e_total3.get())+int(e_total4.get())
        e_subtotal.set(createsubtotal)
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
        e_taxamount.set(finding_tax)
        
        if e_taxamount==None:
            final_total=0
            e_grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            e_grand.set(final_total)
        # amount_recieved=amt_received_input.get()
        # balancedue=final_total-int(amount_recieved)
        # e_balance.set(balancedue)




    def get_selected_e_product2(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        print("subtotal",createsubtotal)
        selected_product=[]
        product=product_drop2.get()
        selected_product.append(product)
        quantity2=qty_input2.get()
        # for product in sal_data:
        #     product_details="SELECT * FROM salesrecpts WHERE name=%s"
        #     mycursor.execute(product_details,selected_product)
        #     data=mycursor.fetchall()
        #     for i in data:
        #         e_hsn.set(i[11])
        #         e_desc.set(i[12])
        #         e_price.set(i[14])
        #         e_sale_price=i[14]
        #         tota_price=int(e_sale_price)*int(quantity2)
        #         e_total.set(tota_price)
        for product in inv_data:
            product_details="SELECT * FROM inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn2.set(i[4])
                e_desc2.set(i[11])
                e_price2.set(i[12])
                e_sale_price=i[12]
                tota_price=int(e_sale_price)*int(quantity2)
                e_total2.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn2.set(i[4])
                e_desc2.set(i[7])
                e_price2.set(i[8]) 
                e_sale_price=i[8]
                tota_price=int(e_sale_price)*int(quantity2)
                e_total2.set(tota_price)
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn2.set(i[4])
                e_desc2.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                e_price2.set(sale_price)
                tota_price=int(sale_price)*int(quantity2)
                e_total2.set(tota_price)
        createsubtotal=int(e_total.get())+int(e_total2.get())+int(e_total3.get())+int(e_total4.get())
        e_subtotal.set(createsubtotal) 


        gst=tax_drop2.get()
        print("seslscted gst",gst)
        if gst=="18.0% GST(18%)":
            print("totla",tota_price)
            finding_tax2=int(tota_price)*(18/100)
        elif gst=="28.0% GST(28%)":
            finding_tax2=int(tota_price)*(28/100)
            
        elif gst=="12.0% GST(12%)":
            finding_tax2=int(tota_price)*(12/100)
            
        elif gst=="06.0% GST(06%)":
            finding_tax2=int(tota_price)*(6/100)
            
        elif gst=="05.0% GST(05%)":
            finding_tax2=int(tota_price)*(5/100)
            
        elif gst=="03.0% GST(03%)":
            finding_tax2=int(tota_price)*(3/100)
            
        elif gst=="0.25% GST(0.25%)":
            finding_tax2=int(tota_price)*(.25/100)
            
        else:
            finding_tax2=0
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        e_taxamount.set(finding_tax)
    
        if e_taxamount==None:
            final_total=0
            e_grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            print("final_total=",final_total)
            e_grand.set(final_total)
        # amount_recieved=amt_received_input.get()
        # balancedue=final_total-int(amount_recieved)
        # e_balance.set(balancedue)



    def get_selected_e_product3(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        selected_product=[]
        product=product_drop3.get()
        selected_product.append(product)
        quantity3=qty_input3.get()
        for product in inv_data:
            product_details="SELECT * FROM inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn3.set(i[4])
                e_desc3.set(i[11])
                e_price3.set(i[12])
                e_sale_price=i[12]
                tota_price=int(e_sale_price)*int(quantity3)
                e_total3.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn3.set(i[4])
                e_desc3.set(i[7])
                e_price3.set(i[8])
                e_sale_price=i[8]
                tota_price=int(e_sale_price)*int(quantity3)
                e_total3.set(tota_price)
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn3.set(i[4])
                e_desc3.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                e_price3.set(sale_price)
                tota_price=int(sale_price)*int(quantity3)
                e_total3.set(tota_price)
        createsubtotal=int(e_total.get())+int(e_total2.get())+int(e_total3.get())+int(e_total4.get())
        e_subtotal.set(createsubtotal) 


        gst=tax_drop3.get()
        print("seslscted gst",gst)
        if gst=="18.0% GST(18%)":
            print("totla",tota_price)
            finding_tax3=int(tota_price)*(18/100)
        elif gst=="28.0% GST(28%)":
            finding_tax3=int(tota_price)*(28/100)
            
        elif gst=="12.0% GST(12%)":
            finding_tax3=int(tota_price)*(12/100)
            
        elif gst=="06.0% GST(06%)":
            finding_tax3=int(tota_price)*(6/100)
            
        elif gst=="05.0% GST(05%)":
            finding_tax3=int(tota_price)*(5/100)
            
        elif gst=="03.0% GST(03%)":
            finding_tax3=int(tota_price)*(3/100)
            
        elif gst=="0.25% GST(0.25%)":
            finding_tax3=int(tota_price)*(.25/100)
            
        else:
            finding_tax3=0
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        e_taxamount.set(finding_tax)
    
        if e_taxamount==None:
            final_total=0
            e_grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            e_grand.set(final_total)
        # amount_recieved=amt_received_input.get()
        # balancedue=final_total-int(amount_recieved)
        # e_balance.set(balancedue)


    def get_selected_e_product4(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        selected_product=[]
        product=product_drop4.get()
        selected_product.append(product)
        quantity4=qty_input4.get()
        # for product in sal_data:
        #     product_details="SELECT * FROM salesrecpts WHERE name=%s"
        #     mycursor.execute(product_details,selected_product)
        #     data=mycursor.fetchall()
        #     for i in data:
        #         e_hsn4.set(i[11])
        #         e_desc4.set(i[12])
        #         e_price4.set(i[14])
        #         e_sale_price=i[14]
        #         tota_price=int(e_sale_price)*int(quantity4)
        #         e_total.set(tota_price)
        for product in inv_data:
            product_details="SELECT * FROM inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn4.set(i[4])
                e_desc4.set(i[11])
                e_price4.set(i[12])
                e_sale_price=i[12]
                tota_price=int(e_sale_price)*int(quantity4)
                e_total4.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn4.set(i[4])
                e_desc4.set(i[7])
                e_price4.set(i[8]) 
                e_sale_price=i[8]
                tota_price=int(e_sale_price)*int(quantity4)
                e_total4.set(tota_price)
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                e_hsn4.set(i[4])
                e_desc4.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                e_price4.set(sale_price)
                tota_price=int(sale_price)*int(quantity4)
                e_total4.set(tota_price)
        createsubtotal=int(e_total.get())+int(e_total2.get())+int(e_total3.get())+int(e_total4.get())
        e_subtotal.set(createsubtotal)


        gst=tax_drop4.get()
        print("seslscted gst",gst)
        if gst=="18.0% GST(18%)":
            print("totla",tota_price)
            finding_tax4=int(tota_price)*(18/100)
        elif gst=="28.0% GST(28%)":
            finding_tax4=int(tota_price)*(28/100)
            
        elif gst=="12.0% GST(12%)":
            finding_tax4=int(tota_price)*(12/100)
            
        elif gst=="06.0% GST(06%)":
            finding_tax4=int(tota_price)*(6/100)
            
        elif gst=="05.0% GST(05%)":
            finding_tax4=int(tota_price)*(5/100)
            
        elif gst=="03.0% GST(03%)":
            finding_tax4=int(tota_price)*(3/100)
            
        elif gst=="0.25% GST(0.25%)":
            finding_tax4=int(tota_price)*(.25/100)
            
        else:
            finding_tax4=0
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        e_taxamount.set(finding_tax)
    
        if e_taxamount==None:
            final_total=0
            e_grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            print("final_total=",final_total)
            e_grand.set(final_total)
        # amount_recieved=amt_received_input.get()
        # balancedue=final_total-int(amount_recieved)
        # e_balance.set(balancedue)
    
    
    def chan_data():
        
        global custom,emal,amount,billaddress,date,salerecno,place,paymethod,refno,deposit,product,hsn,desc,qty,price,total,tax,subtotal,tax2,grand,product,hsn,desc,qty,price,total,tax,subtotal,taxamount,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,cid_id
        custom=custom_name.get()
        emal=email_id.get()
        amount=gamount.get()
        billaddress=saleaddress.get()
        date=saledate.get()
        salerecno=saleno.get()
        place=salesplace.get()
        paymethod=salepay.get()
        refno=salerefno.get()
        deposit=saledeposit.get()
        product=e_product.get()
        hsn=e_hsn.get()
        desc=e_desc.get()
        qty=e_qty.get()
        price=e_price.get()
        total=e_total.get()
        tax=e_tax.get()
        subtotal=e_subtotal.get()
        grand=e_grand.get()
        product2=e_product2.get()
        hsn2=e_hsn2.get()
        desc2=e_desc2.get()
        qty2=e_qty2.get()
        price2=e_price2.get()
        total2=e_total2.get()
        tax2=e_tax2.get()
        
        product3=e_product3.get()
        hsn3=e_hsn3.get()
        desc3=e_desc3.get()
        qty3=e_qty3.get()
        price3=e_price3.get()
        total3=e_total3.get()
        tax3=e_tax3.get()
        
        product4=e_product4.get()
        hsn4=e_hsn4.get()
        desc4=e_desc4.get()
        qty4=e_qty4.get()
        price4=e_price4.get()
        total4=e_total4.get()
        tax4=e_tax4.get()

        # amt_received=e_amt_received.get()
        taxamount=e_taxamount.get()
        # balance=e_balance.get()
        cid_id=cmp1[0]
        mycursor.execute("UPDATE salesrecpts SET salename =%s, saleemail =%s, saleaddress =%s, saledate =%s, saleno =%s, salesplace =%s, salepay =%s, salerefno =%s,saledeposit =%s, salepro =%s, salehsn =%s, saledescription =%s, saleqty =%s,saleprice =%s, saaletotal =%s, tax =%s, salesubtotal=%s, salegrandtotal =%s, category2 =%s, categoryhsn2 =%s, descrptin2 =%s, catqty2 =%s, catprice2 =%s, cattotal2 =%s, tax1 =%s, category3 =%s, categoryhsn3 =%s, descrptin3 =%s, catqty3 =%s, catprice3 =%s, cattotal3 =%s, tax2 =%s, category4 =%s, categoryhsn4 =%s, descrptin4 =%s, catqty4 =%s, catprice4 =%s, cattotal4 =%s, tax3 =%s, saletaxamount =%s, cid_id =%s WHERE salesrecptsid=%s"
        ,(custom,emal,amount,date,salerecno,place,paymethod,refno,deposit,product,hsn,desc,qty,price,total,tax,subtotal,grand,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,taxamount,cid_id,data[0]))
        mydb1.commit()
        mydb1.close()
        messagebox.showinfo('invoice edited Added')
        
        

# selected_item = tree_data.selection()[0]
    global customer_name
    focus_data = tree_data.focus()
    values=tree_data.item(focus_data,'values')
    salesrecpts_id=[values[-1]]
    mycursor.execute("SELECT * FROM salesrecpts WHERE salesrecptsid=%s",(salesrecpts_id))
    data=mycursor.fetchone()
    
    

    
    
    
    
    
    
    
    
    

   

    root = tk.Toplevel()
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

    full_frame=Frame(mycanvas,width=1345,height=2500,bg='#2f516a')
    mycanvas.create_window((0,0),window=full_frame,anchor="nw")

   
    heading_frame=Frame(mycanvas)
    mycanvas.create_window((0,40),window=heading_frame,anchor="nw")
    invoice_heading= tk.Label(heading_frame, text="CASH MEMO",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=74)
    invoice_heading.pack()
    invoice_heading= tk.Label(heading_frame, textvariable="saleno",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=74)
    invoice_heading.pack()





    #form fields

    form_frame=Frame(mycanvas,width=1345,height=1900,bg='#243e55')
    mycanvas.create_window((0,150),window=form_frame,anchor="nw")
    form_lable=tk.Label(form_frame,bg='#243e55',width=100)
    form_lable.place(x=0,y=0)
    form_heading=tk.Label(form_lable, text="FinsYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=90)
    form_heading.pack()


    
    #get customer datas from customer table
    mycursor.execute('select * from app1_customer ')
    customers=mycursor.fetchall()
    customers_data=[]
    for cus in customers:
        customers_data.append(cus)


    #set today date 
    date = dt.datetime.now()
    format_date = f"{date:%Y - %d - %m }"
    today_date = Label(form_frame, text=format_date, fg="white", bg="black", font=("helvetica", 40))

    #company details
    user_id=[6]
    mycursor.execute("SELECT cid FROM app1_company WHERE id_id=%s",(user_id))
    cmp1=mycursor.fetchone()

    # cmp1=[1]

    mycursor.execute("SELECT cname,cemail,state FROM app1_company WHERE id_id=%s",(user_id))
    cmp_data=mycursor.fetchone()
    print(cmp1)
    
    #salesrecpts data
    mycursor.execute("SELECT * FROM app1_salesrecpts WHERE cid_id =%s",(cmp1))
    sales_data=mycursor.fetchall()
    
    #invetory data
    mycursor.execute("SELECT * FROM app1_inventory WHERE cid_id =%s",(cmp1))
    inventory_data=mycursor.fetchall()
    print(cmp1)
    #bundle data
    mycursor.execute("SELECT * FROM app1_bundle WHERE cid_id=%s",(cmp1))
    bundle_data=mycursor.fetchall()

    #noninventor data
    mycursor.execute("SELECT * FROM app1_noninventory WHERE cid_id=%s",(cmp1))
    noninventory_data=mycursor.fetchall()

    #service data
    mycursor.execute("SELECT * FROM app1_service WHERE cid_id=%s",(cmp1))
    services_data=mycursor.fetchall()


    global custom_name,email_id,gamount,saleaddress,saledate,saleno,salesplace,salepay,salerefno,saledeposit,e_product,e_hsn,e_desc,e_qty,e_price,e_total,e_tax,e_subtotal,e_taxamount,e_grand,e_amt_received,e_balance,e_product2,e_product3,e_product4,e_hsn2,e_hsn3,e_hsn4,e_desc2,e_desc3,e_desc4,e_qty2,e_qty3,e_qty4,e_price2,e_price3,e_price4, e_total2,e_total3,e_total4,e_tax2,e_tax3,e_tax4
    custom_name=StringVar(form_frame) 
    email_id=StringVar(form_frame)
    gamount=StringVar(form_frame)
    saleaddress=StringVar(form_frame)
    saledate=StringVar(form_frame)
    saleno=StringVar()
    saleno.set("0")
    salesplace=StringVar(form_frame)
    salepay=StringVar(form_frame)
    salerefno=StringVar(form_frame)
    saledeposit=StringVar(form_frame)
    e_product=StringVar()
    e_hsn=StringVar()
    e_desc=StringVar()
    e_qty=StringVar()
    e_price=StringVar()
    e_total=StringVar()
    e_total.set("0")
    e_tax=StringVar()
    e_subtotal=StringVar()
    e_taxamount=StringVar()
    e_taxamount.set("0")
    e_grand=StringVar()
    e_grand.set("0")
    e_amt_received=StringVar()
    e_balance=StringVar()
    e_product2=StringVar()
    e_product3=StringVar()
    e_product4=StringVar()
    e_hsn2=StringVar()
    e_hsn3=StringVar()
    e_hsn4=StringVar()
    e_desc2=StringVar()
    e_desc3=StringVar()
    e_desc4=StringVar()
    e_qty2=StringVar()
    e_qty3=StringVar()
    e_qty4=StringVar()
    e_price2=StringVar()
    e_price3=StringVar()
    e_price4=StringVar()
    e_total2=StringVar()
    e_total3=StringVar()
    e_total4=StringVar()
    e_tax2=StringVar()
    e_tax3=StringVar()
    e_tax4=StringVar()
    
    
    
    existing_custom=data[1]
    custom_name.set(existing_custom)

    existing_email=data[2]
    email_id.set(existing_email)

    # existing_amount=data[30]
    # gamount.set(existing_amount)
    
    existing_billaddress=data[3]
    saleaddress.set(existing_billaddress)
    
    existing_date=data[4]
    saledate.set(existing_date)
    
    existing_salerecno=data[5]
    saleno.set(existing_salerecno)
    
    existing_place=data[6]
    salesplace.set(existing_place)
    
    existing_salepay=data[7]
    salepay.set(existing_salepay)
    
    existing_refno=data[8]
    salerefno.set(existing_refno)
    
    existing_deposit=data[9]
    saledeposit.set(existing_deposit)

    existing_product=data[10]
    e_product.set(existing_product)

    existing_han=data[11]
    e_hsn.set(existing_han)

    existing_desc=data[12]
    e_desc.set(existing_desc)

    existing_qty=data[13]
    e_qty.set(existing_qty)

    existing_price=data[14]
    e_price.set(existing_price)

    existing_total=data[15]
    e_total.set(existing_total)

    existing_tax=data[18]
    e_tax.set(existing_tax)

    existing_product2=data[20]
    e_product2.set(existing_product2)

    existing_hsn2=data[21]
    e_hsn2.set(existing_hsn2)

    existing_desc2=data[22]
    e_desc2.set(existing_desc2)

    existing_qty2=data[23]
    e_qty2.set(existing_qty2)

    existing_price2=data[24]
    e_price2.set(existing_price2)

    existing_total2=data[25]
    e_total2.set(existing_total2)

    existing_tax2=data[26]
    e_tax2.set(existing_tax2)

    existing_product3=data[27]
    e_product3.set(existing_product3)

    existing_hsn3=data[28]
    e_hsn3.set(existing_hsn3)

    existing_desc3=data[29]
    e_desc3.set(existing_desc3)

    existing_qty3=data[30]
    e_qty3.set(existing_qty3)

    existing_price3=data[31]
    e_price3.set(existing_price3)

    existing_total3=data[32]
    e_total3.set(existing_total3)

    existing_tax3=data[33]
    e_tax3.set(existing_tax3)

    existing_product4=data[34]
    e_product4.set(existing_product4)

    existing_hsn4=data[35]
    e_hsn4.set(existing_hsn4)

    existing_desc4=data[36]
    e_desc4.set(existing_desc4)

    existing_qty4=data[37]
    e_qty4.set(existing_qty4)

    existing_price4=data[38]
    e_price4.set(existing_price4)

    existing_total4=data[39]
    e_total4.set(existing_total4)

    existing_tax4=data[40]
    e_tax4.set(existing_tax4)




    existing_subtotal=data[16]
    e_subtotal.set(existing_subtotal)

    existing_taxamount=data[40]
    e_taxamount.set(existing_taxamount)

    existing_grand=data[17]
    e_grand.set(existing_grand)

    existing_amt_received=data[39]
    e_amt_received.set(existing_amt_received)

    existing_balance=data[41]
    e_balance.set(existing_balance)
    

    select_customer_lab=tk.Label(form_frame,text="Select Customer",bg='#243e55',fg='#fff')
    select_customer_input=StringVar()
    drop2=ttk.Combobox(form_frame,textvariable = custom_name)

    drop2['values']=("Select-Options")

    select_customer_lab.place(x=30,y=150,height=15)
    drop2.place(x=30,y=180,height=40,width=300)
    wrappen.pack(fill='both',expand='yes',)

    email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
    email_lab.place(x=500,y=150,)
    email_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=email_id)
    email_input.place(x=500,y=180,height=40,width=300)

    Due_date_lab=Label(form_frame,text="AMOUNT",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=150,height=40)
    Due_date_lab=Label(form_frame,text="0.00",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=180,height=40)

    invoice_date_lab=Label(form_frame,text="Billing Address",bg='#243e55',fg='#fff')
    invoice_date_lab.place(x=30,y=250,)
    invoice_date_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=saleaddress)
    invoice_date_input.place(x=30,y=280,height=170,width=300)

    terms_lab=Label(form_frame,text="Sales receipt Date:",bg='#243e55',fg='#fff')
    terms_lab.place(x=500,y=250,)
    terms_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=saledate)
    terms_input.place(x=500,y=280,height=40,width=300)

    Due_date_lab=Label(form_frame,text="Sales receipt No:",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=250)
    Due_date_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=saleno )
    Due_date_input.place(x=970,y=280,height=40,width=300)

    place_of_supply=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')
    place_input=StringVar()
    drop2=ttk.Combobox(form_frame,textvariable =salesplace)
    drop2['values']=("Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh",
                     "Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir",
                     "Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram",
                     "Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamilnadu","Telangana","Tripura","Uttar Predesh",
                     "Uttarakhand","West Bengal","Other Territory")
    place_of_supply.place(x=30,y=490,)
    drop2.place(x=30,y=520,height=40,width=300)

    Due_date_labe=Label(form_frame,text="Payment Method:",bg='#243e55',fg='#fff')
    Due_date_labe.place(x=30,y=590)
    Due_datee_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=salepay )
    Due_datee_input.place(x=30,y=620,height=40,width=300)
    
    Due_date_labe=Label(form_frame,text="Reference No:",bg='#243e55',fg='#fff')
    Due_date_labe.place(x=500,y=590)
    Due_datee_input=Entry(form_frame,bg='#2f516a',fg='#fff', textvariable=salerefno )
    Due_datee_input.place(x=500,y=620,height=40,width=300)

    place_of_supply=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')
    place_input=StringVar()
    drop2=ttk.Combobox(form_frame,textvariable =saledeposit)
    drop2['values']=("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit",
                    "Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Service Tax Refund",
                    "TDS Receivable","Uncategorised Asset","Undeposited Funds")
    place_of_supply.place(x=970,y=590,)
    drop2.place(x=970,y=620,height=40,width=300)
    
   
    # table form
    # h_lab=Label(form_frame,text="#",bg='#243e55',fg='#fff')
    # h_lab.place(x=30,y=730)

    # h_input1=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    # h_input1.place(x=30,y=780,height=40,width=40)

    # h_input2=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    # h_input2.place(x=30,y=850,height=40,width=40)

    # h_input3=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    # h_input3.place(x=30,y=930,height=40,width=40)

    # h_input4=Entry(form_frame,width=10,bg='#2f516a',fg='#fff')
    # h_input4.place(x=30,y=1000,height=40,width=40)


   
    #col-1
    product_lab=Label(form_frame,text="PRODUCT / SERVICES",bg='#243e55',fg='#fff')
    product_lab.place(x=60,y=730,)

    product_drop1=ttk.Combobox(form_frame,textvariable = e_product)
    product1=[]
    # for proinv in sales_data: 
    #     if proinv[-1] == cmp1[0] :
    #         sal_data=proinv[2]
    #         product1.append(sal_data)
    
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
    product_drop1.bind("<<ComboboxSelected>>",get_selected_e_product)

    product_drop1.place(x=30,y=780,height=40,width=200)

    product_drop2=ttk.Combobox(form_frame,textvariable = e_product2)

   
    product_drop2['values']=product1
    product_drop2.bind("<<ComboboxSelected>>",get_selected_e_product2)

    product_drop2.place(x=30,y=850,height=40,width=200)

   
    product_drop3=ttk.Combobox(form_frame,textvariable = e_product3)
            
    product_drop3['values']=product1
    product_drop3.bind("<<ComboboxSelected>>",get_selected_e_product3)
    product_drop3.place(x=30,y=930,height=40,width=200)

   
    product_drop4=ttk.Combobox(form_frame,textvariable = e_product4)
    product_drop4['values']=product1
    product_drop4.bind("<<ComboboxSelected>>",get_selected_e_product4)
    product_drop4.place(x=30,y=1000,height=40,width=200)


    #col-2
    hsn_lab=Label(form_frame,text="HSN",bg='#243e55',fg='#fff')
    hsn_lab.place(x=300,y=730,)

    hsn_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn)
    hsn_input1.place(x=270,y=780,height=40)

    
    hsn_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn2)
    hsn_input2.place(x=270,y=850,height=40)

    hsn_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn3)
    hsn_input3.place(x=270,y=930,height=40)

    hsn_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn4)
    hsn_input4.place(x=270,y=1000,height=40)
    
    #col-3
    desc_lab=Label(form_frame,text="DESCRIPTION",bg='#243e55',fg='#fff')
    desc_lab.place(x=440,y=730,)


    desc_input1=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc)
    desc_input1.place(x=430,y=780,height=40)

    desc_input2=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc2)
    desc_input2.place(x=430,y=850,height=40)

    desc_input3=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc3)
    desc_input3.place(x=430,y=930,height=40)

    desc_input4=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc4)
    desc_input4.place(x=430,y=1000,height=40)

    #col-4
    qty_lab=Label(form_frame,text="QUANTITY",bg='#243e55',fg='#fff')
    qty_lab.place(x=660,y=730,)

    qty_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty)
    qty_input1.place(x=620,y=780,height=40)

    qty_input1.bind("<KeyRelease>",get_selected_e_product)


    qty_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty2)
    qty_input2.place(x=620,y=850,height=40)
    qty_input2.bind("<KeyRelease>",get_selected_e_product2)


    qty_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty3)
    qty_input3.place(x=620,y=930,height=40)
    qty_input3.bind("<KeyRelease>",get_selected_e_product3)


    qty_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty4)
    qty_input4.place(x=620,y=1000,height=40)
    qty_input4.bind("<KeyRelease>",get_selected_e_product4)

    #col-5
    price_lab=Label(form_frame,text="PRICE",bg='#243e55',fg='#fff')
    price_lab.place(x=800,y=730,)

    price_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price)
    price_input1.place(x=775,y=780,height=40)
    # price_input1.bind("<KeyRelease>",get_qty)

    
    price_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price2)
    price_input2.place(x=775,y=850,height=40)

    price_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price3)
    price_input3.place(x=775,y=930,height=40)

    price_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price4)
    price_input4.place(x=775,y=1000,height=40)

    #col-6
    total_lab=Label(form_frame,text="TOTAL",bg='#243e55',fg='#fff')
    total_lab.place(x=960,y=730,)

    total_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total)
    # total_input1.bind("<KeyRelease>",get_total)
    total_input1.place(x=930,y=780,height=40)

   
   
    total_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total2)
    total_input2.place(x=930,y=850,height=40)

    
    total_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total3)
    total_input3.place(x=930,y=930,height=40)

    
    total_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total4)
    total_input4.place(x=930,y=1000,height=40)

    #ocol-7
    tax_lab=Label(form_frame,text="TAX (%)",bg='#243e55',fg='#fff')
    tax_lab.place(x=1160,y=730,)

    # # tax1=StringVar()
    tax_drop1=ttk.Combobox(form_frame,textvariable = e_tax)
    tax_values=("Choose","28.0% GST(28%)","18.0% GST(18%)","12.0% GST(12%)","06.0% GST(06%)","05.0% GST(05%)","03.0% GST(03%)","0.25% GST(0.25%)","0.0% GST(0%)","Exempt GST(0%)","Out of Scope(0%)")
    tax_drop1['values']=tax_values
    tax_drop1.bind("<<ComboboxSelected>>",get_selected_e_product)
    tax_drop1.place(x=1110,y=780,height=40,width=200)
    
    tax_drop2=ttk.Combobox(form_frame,textvariable = e_tax2)
    tax_drop2['values']=tax_values
    tax_drop2.bind("<<ComboboxSelected>>",get_selected_e_product2)
    tax_drop2.place(x=1110,y=850,height=40,width=200)

   
    tax_drop3=ttk.Combobox(form_frame,textvariable = e_tax3)
    tax_drop3['values']=tax_values
    tax_drop3.bind("<<ComboboxSelected>>",get_selected_e_product3)
    tax_drop3.place(x=1110,y=930,height=40,width=200)

   
    tax_drop4=ttk.Combobox(form_frame,textvariable = e_tax4)
    tax_drop4['values']=tax_values
    tax_drop4.bind("<<ComboboxSelected>>",get_selected_e_product4)
    tax_drop4.place(x=1110,y=1000,height=40,width=200)





    subtotal_lab=Label(form_frame,text="Sub Total",bg='#243e55',fg='#fff')
    subtotal_lab.place(x=900,y=1200,height=40)
    subtotal_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable= e_subtotal)
    subtotal_input.place(x=1000,y=1200,height=40)

    tax2_lab=Label(form_frame,text="Tax Amount",bg='#243e55',fg='#fff')
    tax2_lab.place(x=900,y=1300,height=40)
    tax2_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable= e_taxamount)
    tax2_input.place(x=1000,y=1300,height=40)

    grand_lab=Label(form_frame,text="Grand Total",bg='#243e55',fg='#fff')
    grand_lab.place(x=900,y=1400,height=40)
    grand_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_grand)
    grand_input.place(x=1000,y=1400,height=40)


    submit_button=Button(form_frame,text="Save",background="#2f516a", foreground="white",width=20,height=2,command=chan_data)

    submit_button.place(x=1100,y=1500)
    font=('Times', 15)


#Delete salerecords
def delete_salerecords():
    focus_data = tree_data.focus()
    values=tree_data.item(focus_data,'values')
    salesrecpts_id=[values[-1]]
    mycursor.execute("DELETE FROM app1_salesrecpts WHERE salesrecptsid=%s",(salesrecpts_id))
    mydb1.commit()
    messagebox.showinfo('successfully Deleted')
    print('sucessfully deleted')
    tree_data.delete(focus_data)


def get_selected_producting(event):
    select_pro=[]
    pr1=product_drop5.get()
    select_pro.append(pr1)
    print(pr1)
    if pr1 == "Invoice":
        import invoice
    if pr1 == "Payment":
        import payments
    if pr1 == "Sales Receipt":
        import Salesreceipt
    if pr1 == "Credit note":
        import creditnote
    if pr1 == "Estimate":
        import estimate
    if pr1 == "Delayed Charge":
        import delayedcharge
    if pr1 == "Time Activity":
        import salestimactivity
    
root = tk.Tk()
fun()
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
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1340,height=1900,bg='#243e55')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#243e55",width=100)
form_lable.place(x=0,y=0)

tit = Label(heading_frame, text="SALES RECORDS", font=('times new roman', 28, 'bold'),padx=504, pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F.place(x=20, y=50, width=1300, height=400)

# menu= StringVar()
# menu.set("New Transaction")

# #Create a dropdown Menu
# drop= OptionMenu(form_frame, menu,"Invoice", "Payment","Sales Receipt","Credit note","Estimate","Delayed Charge","Time Activity")
# drop.place(x=1150,y=10,width=150)
pr1 = "Invoice", "Payment","Sales Receipt","Credit note","Estimate","Delayed Charge","Time Activity"
product_drop5=ttk.Combobox(form_frame,font=('times new roman', 10, 'bold'), )
product_drop5.set("New Transaction")
product_drop5['values']=pr1
product_drop5.bind("<<ComboboxSelected>>",get_selected_producting)
product_drop5.place(x=1120,y=10,height=40,width=200)


global tree_data
tree_data = ttk.Treeview(F,height=15)
tree_data['show'] = 'headings'

sb = ttk.Scrollbar(F, orient="vertical", command=tree_data.yview)
sb.grid(row=1,column=1,sticky="NS",pady=5)

tree_data.configure(yscrollcommand=sb.set)

tree_data["columns"]=("1","2","3","4","5","6","7","8","9")

tree_data.column("1", width=140)
tree_data.column("2", width=140)
tree_data.column("3", width=140)
tree_data.column("4", width=140)
tree_data.column("5", width=140)
tree_data.column("6", width=140)
tree_data.column("7", width=140)
tree_data.column("8", width=140)
tree_data.column("9", width=130)


tree_data.heading("1", text="DATE")
tree_data.heading("2", text="TYPE")
tree_data.heading("3", text="NO.")
tree_data.heading("4", text="CUSTOMER")
tree_data.heading("5", text="DUE DATE")
tree_data.heading("6", text="BALANCE")
tree_data.heading("7", text="TOTAL BEFORE")
tree_data.heading("8", text="TAX")
tree_data.heading("9", text="TOTAL")

sql = 'SELECT saledate,salepay,saleno,salename,saledate,saaletotal,salesubtotal,saletaxamount,salegrandtotal,salesrecptsid from salesrecpts'
mycursor.execute(sql)
trees_data=mycursor.fetchall()
total=mycursor.rowcount

for data in trees_data:
    tree_data.insert("", 'end',values=data)
    
tree_data.grid(row=1,column=0,padx=5,pady=5)


edit_btn = ttk.Button(F, text="Edit", command=edit_sale)
edit_btn.place(relx=0.35, rely=0.88, relheight=0.1, relwidth=0.1)
del_btn = ttk.Button(F, text="Delete",command=delete_salerecords)
del_btn.place(relx=0.5, rely=0.88, relheight=0.1, relwidth=0.1)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)

wrappen.pack(fill='both',expand='yes',)



root.mainloop()





