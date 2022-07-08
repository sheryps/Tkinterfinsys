
from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk
from xml.etree.ElementInclude import include
import mysql.connector
from tkinter import messagebox
import datetime as dt
import re
 


def fun():#db connection
    global mydb,mycursor
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='finsys_tkinter1'
        )
    mycursor = mydb.cursor()



def add_invoice():
    
    def get_email(event):
        name=[]
        option=drop1.get()
        name.append(option)
        for custm in customers_data:
            full_name=custm[2]+custm[3]
            if full_name==name[0]:
                first_name=custm[2]
                last_name=custm[3]
        mycursor.execute("SELECT * FROM customer where firstname=%s and lastname=%s",(first_name,last_name))
        table2=mycursor.fetchall()
        for i in table2:
            email.set(i[9])
            billto.set(i[12:17])



    def add_custom():
        
        def save_customdata():
            if CheckVar1.get()==1:
                fun()
                global title,first_name,last_name,company,location,gst,gstin,pan_no,email,website,mobile,street,city,state,pin,country,shipstreet,shipcity,shipstate,shippin,shipcountry
                title=title.get()
                first_name=first_name.get()
                last_name=last_name.get()
                company=company.get()
                location=location.get()
                gst=gst.get()


                gstin=gstin.get()
                pan_no=pan_no.get()
                email=email.get()
                website=website.get()
                mobile=mobile.get()
                street=street.get()
                city=city.get()
                state=state.get()
                pin=pin.get()
                country=country.get()
                shipstreet=shipstreet.get()
                shipcity=shipcity.get()
                shipstate=shipstate.get()
                shippin=shippin.get()
                shipcountry=shipcountry.get()
                cid_id=cmp1[0]
                sql='SELECT * FROM customer WHERE firstname=%s AND lastname=%s'# selecting entire table from db,taking username , nd check the existance
                val=(first_name,last_name)
                mycursor.execute(sql,val)
                if mycursor.fetchone()is not None:
                    messagebox.showerror('error', 'First Name and Last Name already exist!!')
                else:
                    
                    sql="INSERT INTO customer (title,firstname,lastname ,company,location,gsttype,gstin ,panno ,email ,website,mobile,street ,city ,state,pincode ,country ,shipstreet ,shipcity ,shipstate,shippincode ,shipcountry,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
                    val=(title,first_name,last_name,company,location,gst,gstin,pan_no,email,website,mobile,street,city,state,pin,country,shipstreet,shipcity,shipstate,shippin,shipcountry,cid_id)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    messagebox.showinfo(title='Success',message='New Customer Added')
                    mydb.close()
                    
            else:
                messagebox.showerror('error', 'Accept terms and conditions')




        #assign Shipping address 
        def sameaddress():
            global selstreet,selcity,selstate,selpin,selcountry
            if CheckVar2.get()==1:
                selstreet=street.get()
                shipstreet.set(selstreet)
                selcity=city.get()
                shipcity.set(selcity)
                selstate=state.get()
                shipstate.set(selstate)
                selpin=pin.get()
                shippin.set(selpin)
                selcountry=country.get()
                shipcountry.set(selcountry)

            

        fun()
        addcustomer_form = Toplevel(invoice)
        addcustomer_form.title("finsYs")
        addcustomer_form.geometry("2000x2000")
        addcustomer_form['bg']='#2f516a'
        wrappen=ttk.LabelFrame(addcustomer_form)
        mycanvas=Canvas(wrappen)
        mycanvas.pack(side=LEFT,fill="both",expand="yes")
        yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT,fill='y')

        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

        full_frame=Frame(mycanvas,width=2000,height=2000,bg='#2f516a')
        mycanvas.create_window((0,0),window=full_frame,anchor="nw")

        # global cid
        # cid=mycursor.execute('select cid from app1_company where id_id=os.getuid()')
        # print(cid)
        heading_frame=Frame(mycanvas)
        mycanvas.create_window((150,40),window=heading_frame,anchor="nw")
        # headingfont=font.Font(family='Times New Roman', size=25,)
        addcustomer_heading= tk.Label(heading_frame, text="ADD CUSTOMER",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
        addcustomer_heading.pack()

        #form fields

        form_frame=Frame(mycanvas,width=1600,height=1000,bg='#243e55')
        mycanvas.create_window((150,150),window=form_frame,anchor="nw")
        form_lable=tk.Label(form_frame,bg='#243e55',width=100)
        form_lable.place(x=0,y=0)
        form_heading=tk.Label(form_lable, text="Customer Information",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
        form_heading.pack(fill=X)

        global title,first_name,last_name,company,location,gst,gstin,pan_no,email,website,mobile,street,city,state,pin,country,shipstreet,shipcity,shipstate,shippin,shipcountry
        title=StringVar()
        first_name=StringVar(form_frame)
        last_name=StringVar()
        company=StringVar()
        location=StringVar()
        gst=StringVar()
        gstin=StringVar()
        pan_no=StringVar()
        email=StringVar()
        website=StringVar()
        mobile=StringVar()
        street=StringVar()
        city=StringVar()
        state=StringVar()
        pin=StringVar()
        country=StringVar()
        shipstreet=StringVar()
        shipcity=StringVar()
        shipstate=StringVar()
        shippin=StringVar()
        shipcountry=StringVar()




        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        gstregexp = "[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[Z]{1}[0-9a-zA-Z]{1}"
        panregexp = "[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}"
        webregexp = "www."
        mobregexp = "[0-9]{10}"
        title_lab=tk.Label(form_frame,text="Title",bg='#243e55',fg='#fff')

        drop2=ttk.Combobox(form_frame,textvariable = title)

        drop2['values']=("Mr","Mrs","Miss","Ms")

        title_lab.place(x=10,y=100,height=15,width=100)
        drop2.place(x=30,y=130,height=40,width=450)
        wrappen.pack(fill='both',expand='yes',)


        fname=Label(form_frame,text="First Name",bg='#243e55',fg='#fff')
        fname.place(x=530,y=100,)
        fname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = first_name)
        fname_input.place(x=530,y=130,height=40)


        lname=Label(form_frame,text="Last Name",bg='#243e55',fg='#fff')
        lname.place(x=1060,y=100,)
        lname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = last_name)
        lname_input.place(x=1060,y=130,height=40)

        company_lab=Label(form_frame,text="Company",bg='#243e55',fg='#fff')
        company_lab.place(x=30,y=200,)
        company_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = company)
        company_input.place(x=30,y=230,height=40)

        location_lab=Label(form_frame,text="Location",bg='#243e55',fg='#fff')
        location_lab.place(x=530,y=200,)
        location_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = location)
        location_input.place(x=530,y=230,height=40)

        GST_lab=tk.Label(form_frame,text="GST Type",bg='#243e55',fg='#fff')
        GST_drop=ttk.Combobox(form_frame,textvariable = gst)
        GST_drop['values']=("Consumer","GST Registered-Regular","GST unregistered","GST Registered-Composition","Overseas", "Deemed exports - EOU's STP's EHTP's")
        GST_lab.place(x=20,y=300,height=15,width=100)
        GST_drop.place(x=30,y=330,height=40,width=450)

        def gst_validation(event):
                gstin=gstin_input.get()
                if gst!="Consumer"or gst!="Overseas":
                    if gst!="GST unregistered":
                        if gst!="Overseas":
                            if re.search(gstregexp, gstin):
                                wdgLst_gst.configure(text='GST',fg='#4BB543')
                                
                            else:
                                wdgLst_gst.configure(text='Please provide a valid GST Number',fg='#FF0000')
                                return False
                else:
                    pass



        reggst = invoice.register(gst_validation)
        gstin_lab=Label(form_frame,text="GSTIN",bg='#243e55',fg='#fff')
        gstin_lab.place(x=530,y=300,)
        gstin_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = gstin)
        gstin_input.bind("<KeyRelease>",gst_validation)
        gstin_input.config(validate="focusout", validatecommand=(reggst, '%P'))
        wdgLst_gst = gstin_lab
        gstin_input.place(x=530,y=330,height=40)

        def pan_validation(event):
            pan_no=pan_no_input.get()
            if re.search(panregexp, pan_no):
                    wdgLst_pan.configure(text='pan number',fg='#4BB543')
                    
            else:
                wdgLst_pan.configure(text='Please provide a valid PAN Number',fg='#FF0000')
                return False
                




        regpan = invoice.register(pan_validation)
        pan_no_lab=Label(form_frame,text="PAN NO",bg='#243e55',fg='#fff')
        pan_no_lab.place(x=1060,y=300,)
        pan_no_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = pan_no)
        pan_no_input.bind("<KeyRelease>",pan_validation)
        pan_no_input.config(validate="focusout", validatecommand=(regpan, '%P'))
        wdgLst_pan = pan_no_lab
        pan_no_input.place(x=1060,y=330,height=40)
        
        def email_validation(event):
            email=email_input.get()

            if re.search(regex, email):
                wdgLst_email.configure(text='Email',fg='#4BB543')
                
            else:
                wdgLst_email.configure(text='Please provide a valid email',fg='#FF0000')
                return False




        regEmail = invoice.register(email_validation)
        email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
        email_lab.place(x=30,y=400,)
        email_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = email)
        email_input.bind("<KeyRelease>",email_validation)
        email_input.config(validate="focusout", validatecommand=(regEmail, '%P'))
        wdgLst_email = email_lab
        email_input.place(x=30,y=430,height=40)

        def web_validation(event):
            website=web_input.get()
            if re.search(webregexp, website):
                wdgLst_web.configure(text='website',fg='#4BB543')
                
            else:
                wdgLst_web.configure(text='Please provide a valid website',fg='#FF0000')
                return False

        regweb = invoice.register(web_validation)
        web_lab=Label(form_frame,text="Website",bg='#243e55',fg='#fff')
        web_lab.place(x=530,y=400,)
        web_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = website)
        web_input.bind("<KeyRelease>",web_validation)
        web_input.config(validate="focusout", validatecommand=(regweb, '%P'))
        wdgLst_web = web_lab
        web_input.place(x=530,y=430,height=40)

        def mob_validation(event):
            mobile=mobile_input.get()
            if re.search(mobregexp, mobile):
                wdgLst_mob.configure(text='mobile',fg='#4BB543')
                
            else:
                wdgLst_mob.configure(text='Please provide a valid phone Number',fg='#FF0000')
                return False

        regmob = invoice.register(mob_validation)
        mobile_lab=Label(form_frame,text="Mobile",bg='#243e55',fg='#fff')
        mobile_lab.place(x=1060,y=400,)
        mobile_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = mobile)
        mobile_input.bind("<KeyRelease>",mob_validation)
        mobile_input.config(validate="focusout", validatecommand=(regmob, '%P'))
        wdgLst_mob = mobile_lab
        mobile_input.place(x=1060,y=430,height=40)

        #Billing session
        # sub_headingfont=font(family='Times_New_Roman', size=18,)
        form2_frame=Frame(mycanvas,width=1600,height=650,bg='#243e55',bd=1,relief="groove")
        mycanvas.create_window((150,650),window=form2_frame,anchor="nw")

        bill_heading=tk.Label(form2_frame, text="Billing Address",fg='#fff',bg='#243e55',height=2,width=15)
        bill_heading.place(x=30,y=10,)

        street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
        street_lab.place(x=30,y=100,)
        street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff',textvariable = street)
        street_input.place(x=30,y=130,height=80)


        city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
        city_lab.place(x=30,y=250,)
        city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = city)
        city_input.place(x=30,y=280,height=40)


        state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
        state_lab.place(x=370,y=250,)
        state_drop=ttk.Combobox(form2_frame,textvariable = state)
        state_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
                                                    
        state_drop.place(x=370,y=280,height=40,width=330)

        pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
        pin_lab.place(x=30,y=350,)
        pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = pin)
        pin_input.place(x=30,y=380,height=40)

        country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
        country_lab.place(x=370,y=350,)
        country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = country)
        country_input.place(x=370,y=380,height=40)

        CheckVar1 = IntVar(form2_frame)
        terms_condition=Checkbutton(form2_frame, variable = CheckVar1,onvalue = 1, offvalue = 0,bg='#243e55')
        terms_condition.place(x=30,y=450,)   
        terms_condition_lab= Label(form2_frame,text = " Agree to Terms and Conditions",bg='#243e55',fg='#fff') 
        terms_condition_lab.place(x=70,y=450,)

        #Shipping Address 

        shipping_heading=tk.Label(form2_frame, text="Shipping Address",fg='#fff',bg='#243e55',height=2,width=15)
        shipping_heading.place(x=850,y=10,)

        CheckVar2 = IntVar(form2_frame)
        same_address=Checkbutton(form2_frame, variable = CheckVar2,onvalue = 1, offvalue = 0,bg='#243e55',command=sameaddress)
        same_address.place(x=1100,y=30,)   
        same_address_lab= Label(form2_frame,text = "Same as Billing Address",bg='#243e55',fg='#fff') 
        same_address_lab.place(x=1150,y=30,)

        street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
        street_lab.place(x=850,y=100,)
        street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff',textvariable = shipstreet)
        street_input.place(x=850,y=130,height=80)


        city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
        city_lab.place(x=850,y=250,)
        city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = shipcity)
        city_input.place(x=850,y=280,height=40)


        state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
        state_lab.place(x=1200,y=250,)
        state_drop=ttk.Combobox(form2_frame,textvariable = shipstate)
        state_drop['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
        state_drop.place(x=1200,y=280,height=40,width=330)

        pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
        pin_lab.place(x=850,y=350,)
        pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = shippin)
        pin_input.place(x=850,y=380,height=40)

        country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
        country_lab.place(x=1200,y=350,)
        country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff',textvariable = shipcountry)
        country_input.place(x=1200,y=380,height=40)


        submit_button=Button(form2_frame,text="Submit Form",background="#2f516a", foreground="white",width=40,height=2,command=save_customdata)

        submit_button.place(x=600,y=500)
        
        


        # import customer
    #getting terms from dropdown
    def get_terms(event):
        global invno
        options=terms_input.get()
        if options=="Add New Term":
            invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
            invno_lab.place(x=500,y=400,)
            invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=invno)
            invno_input.place(x=500,y=430,height=40)
        else:
            invno.set(0)
    #getting selected product1 and quantity and set some entry feild value
    
    def get_selected_product(event):
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
        print("qtyyyy=",quantity)
        selected_product.append(product)
        for product in inv_data:
            product_details="SELECT * FROM inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn.set(i[4])
                desc.set(i[11])
                price.set(i[12])
                sale_price=i[12]
                print("sale_price=",sale_price)
                tota_price=int(sale_price)*int(quantity)
                total.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn.set(i[4])
                desc.set(i[7])
                price.set(i[8])
                sale_price=i[8]
                tota_price=int(sale_price)*int(quantity)
                total.set(tota_price) 
        
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn.set(i[4])
                desc.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                price.set(sale_price)
                
                tota_price=int(sale_price)*int(quantity)
                total.set(tota_price)   
        createsubtotal=int(total.get())+int(total2.get())+int(total3.get())+int(total4.get())
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
        amount_recieved=amt_received_input.get()
        if amount_recieved=='':
            amount_recieved='0'
        balancedue=final_total-int(amount_recieved)
        balance.set(balancedue)

    #getting selected product2 and set some entry feild value
    def get_selected_product2(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        print("subtotal",createsubtotal)
        selected_product=[]
        product=product_drop2.get()
        selected_product.append(product)
        quantity2=qty_input2.get()
        for product in inv_data:
            product_details="SELECT * FROM inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn2.set(i[4])
                desc2.set(i[11])
                price2.set(i[12])
                sale_price=i[12]
                tota_price=int(sale_price)*int(quantity2)
                total2.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn2.set(i[4])
                desc2.set(i[7])
                price2.set(i[8]) 
                sale_price=i[8]
                tota_price=int(sale_price)*int(quantity2)
                total2.set(tota_price)
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn2.set(i[4])
                desc2.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                price2.set(sale_price)
                tota_price=int(sale_price)*int(quantity2)
                total2.set(tota_price)
        createsubtotal=int(total.get())+int(total2.get())+int(total3.get())+int(total4.get())
        subtotal.set(createsubtotal) 


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
        taxamount.set(finding_tax)
    
        if taxamount==None:
            final_total=0
            grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            print("final_total=",final_total)
            grand.set(final_total)
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        balance.set(balancedue)


    def get_selected_product3(event):
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
                hsn3.set(i[4])
                desc3.set(i[11])
                price3.set(i[12])
                sale_price=i[12]
                tota_price=int(sale_price)*int(quantity3)
                total3.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn3.set(i[4])
                desc3.set(i[7])
                price3.set(i[8])
                sale_price=i[8]
                tota_price=int(sale_price)*int(quantity3)
                total3.set(tota_price)
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn3.set(i[4])
                desc3.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                price3.set(sale_price)
                tota_price=int(sale_price)*int(quantity3)
                total3.set(tota_price)
        createsubtotal=int(total.get())+int(total2.get())+int(total3.get())+int(total4.get())
        subtotal.set(createsubtotal) 


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
        taxamount.set(finding_tax)
    
        if taxamount==None:
            final_total=0
            grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            print("final_total=",final_total)
            grand.set(final_total)
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        balance.set(balancedue)



    def get_selected_product4(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        selected_product=[]
        product=product_drop4.get()
        selected_product.append(product)
        quantity4=qty_input4.get()
        for product in inv_data:
            product_details="SELECT * FROM inventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn4.set(i[4])
                desc4.set(i[11])
                price4.set(i[12])
                sale_price=i[12]
                tota_price=int(sale_price)*int(quantity4)
                total4.set(tota_price)
        for product in noninv_data:
            product_details="SELECT * FROM noninventory WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn4.set(i[4])
                desc4.set(i[7])
                price4.set(i[8]) 
                sale_price=i[8]
                tota_price=int(sale_price)*int(quantity4)
                total4.set(tota_price)
        for product in bundleinv_data:
            product_details="SELECT * FROM bundle WHERE name=%s"
            mycursor.execute(product_details,selected_product)
            data=mycursor.fetchall()
            for i in data:
                hsn4.set(i[4])
                desc4.set(i[7])
                sale_price=(i[21]+i[22]+i[23]+i[24])
                price4.set(sale_price)
                tota_price=int(sale_price)*int(quantity4)
                total4.set(tota_price)
        createsubtotal=int(total.get())+int(total2.get())+int(total3.get())+int(total4.get())
        subtotal.set(createsubtotal)


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
        taxamount.set(finding_tax1+finding_tax2+finding_tax3+finding_tax4)
        finding_tax=finding_tax1+finding_tax2+finding_tax3+finding_tax4
        taxamount.set(finding_tax)
    
        if taxamount==None:
            final_total=0
            grand.set(final_total)
        else:
            final_total=0
            total_amount=createsubtotal+finding_tax
            final_total=final_total+total_amount
            print("final_total=",final_total)
            grand.set(final_total)
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        balance.set(balancedue)

    def save_invoice():
        global select_customer,email,invoice_date,terms,Due_date,billto,invno,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,taxamount,grand,amt_received,balance,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,cid_id


        Select_customer=select_customer.get()
        email=email.get()
        invoice_date=invoice_date.get()
        terms=terms.get()
        Due_date=Due_date.get()
        billto=billto.get()
        Invno=invno.get()
        if invno==None:
            Invno=0
        place_of_supply=place_of_supply.get()
        product=product.get()
        hsn=hsn.get()
        desc=desc.get()
        qty=qty.get()
        price=price.get()
        total=total.get()
        tax=tax.get()
        subtotal=subtotal.get()
        grand=grand.get()
        product2=product2.get()
        hsn2=hsn2.get()
        desc2=desc2.get()
        qty2=qty2.get()
        price2=price2.get()
        total2=total2.get()
        tax2=tax2.get()
        
        product3=product3.get()
        hsn3=hsn3.get()
        desc3=desc3.get()
        qty3=qty3.get()
        price3=price3.get()
        total3=total3.get()
        tax3=tax3.get()
        
        product4=product4.get()
        hsn4=hsn4.get()
        desc4=desc4.get()
        qty4=qty4.get()
        price4=price4.get()
        total4=total4.get()
        tax4=tax4.get()

        amt_received=amt_received.get()
        taxamount=taxamount.get()
        balance=balance.get()
        cid_id=cmp1[0]

        sql="INSERT INTO invoice (customername,email,invoiceno ,terms,invoicedate,duedate,bname ,placosupply ,product ,hsn,description,qty ,price ,total,tax ,subtotal ,grandtotal ,product2 ,hsn2,description2 ,qty2,price2,total2,tax2,product3,hsn3,description3,qty3,price3,total3,tax3,product4,hsn4,description4,qty4,price4,total4,tax4,amtrecvd,taxamount,baldue,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(Select_customer,email,Invno,terms,invoice_date,Due_date,billto,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,grand,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,amt_received,taxamount,balance,cid_id)
        mycursor.execute(sql,val)
        mydb.commit()
        mydb.close()
        messagebox.showinfo('New Customer Added')
        


    fun()
    invoice_form = Toplevel(invoice)
    invoice_form.title("finsYs")
    invoice_form.geometry("5000x2000")
    invoice_form['bg']='#2f516a'
    wrappen=ttk.LabelFrame(invoice_form)
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
    invoice_heading= tk.Label(heading_frame, text="INVOICE",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
    invoice_heading.pack()

    #form fields

    form_frame=Frame(mycanvas,width=1600,height=1900,bg='#243e55')
    mycanvas.create_window((150,150),window=form_frame,anchor="nw")
    form_lable=tk.Label(form_frame,bg='#243e55',width=50)
    form_lable.place(x=0,y=0)
    form_heading=tk.Label(form_lable, text="FinsYs",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
    form_heading.pack()

    #get customer datas from customer table
    mycursor.execute('select * from customer ')
    customers=mycursor.fetchall()
    customers_data=[]
    for cus in customers:
        customers_data.append(cus)


    #set today date 
    date = dt.datetime.now()
    format_date = f"{date:%Y - %d - %m }"
    today_date = Label(form_frame, text=format_date, fg="white", bg="black", font=("helvetica", 40))

    #company details
    user_id=[4]
    mycursor.execute("SELECT cid FROM company WHERE id_id=%s",(user_id))
    cmp1=mycursor.fetchone()

    # cmp1=[1]

    mycursor.execute("SELECT cname,cemail,state FROM company WHERE id_id=%s",(user_id))
    cmp_data=mycursor.fetchone()


    #invetory data
    mycursor.execute("SELECT * FROM inventory WHERE cid_id=%s",(cmp1))
    inventory_data=mycursor.fetchall()

    #bundle data
    mycursor.execute("SELECT * FROM bundle WHERE cid_id=%s",(cmp1))
    bundle_data=mycursor.fetchall()

    #noninventor data
    mycursor.execute("SELECT * FROM noninventory WHERE cid_id=%s",(cmp1))
    noninventory_data=mycursor.fetchall()

    #service data
    mycursor.execute("SELECT * FROM service WHERE cid_id=%s",(cmp1))
    services_data=mycursor.fetchall()



    global select_customer,email,invoice_date,terms,Due_date,billto,invno,cmpname,cpmemail,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,taxamount,grand,amt_received,balance

    select_customer=StringVar(form_frame)
    email=StringVar(form_frame)
    invoice_date=StringVar(form_frame)
    terms=StringVar(form_frame)
    Due_date=StringVar(form_frame)
    billto=StringVar(form_frame)
    invno=StringVar(form_frame)
    place_of_supply=StringVar(form_frame)
    product=StringVar(form_frame)
    hsn=StringVar(form_frame)
    desc=StringVar(form_frame)
    qty=StringVar(form_frame)
    price=StringVar(form_frame)
    total=StringVar(form_frame)
    total.set("0")
    tax=StringVar(form_frame)
    subtotal=StringVar(form_frame)
    taxamount=StringVar(form_frame)
    taxamount.set("0")
    grand=StringVar(form_frame)
    grand.set("0")
    amt_received=StringVar(form_frame)
    balance=StringVar(form_frame)






    company_name_lab=Label(form_frame,text=cmp_data[0],bg='#243e55',fg='#fff',font="Helvetica 22 bold")
    company_name_lab.place(x=50,y=70,)

    company_email_lab=Label(form_frame,text=cmp_data[1],bg='#243e55',fg='#fff',font="Helvetica 10 bold")
    company_email_lab.place(x=50,y=120,)

    select_customer_lab=tk.Label(form_frame,text="Select Customer",bg='#243e55',fg='#fff')

    drop1=ttk.Combobox(form_frame,textvariable = select_customer)

    value=[]
    for cust in  customers_data:
        customer_values=cust[-1]
        
        if customer_values==cmp1[0]:
            value.append((cust[2]+cust[3]))
            drop1['values']=value
            
        else:
            messagebox.showerror('error', 'invalid data')

    drop1.bind("<<ComboboxSelected>>",get_email)
    select_customer_lab.place(x=30,y=200,height=15)
    drop1.place(x=30,y=230,height=40,width=335)
    wrappen.pack(fill='both',expand='yes',)

    add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=2,command=add_custom)
    add_custom.place(x=370,y=230)

    email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
    email_lab.place(x=500,y=200,)
    email_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=email)
    email_input.place(x=500,y=230,height=40)

    invoice_date_lab=Label(form_frame,text="Invoice Date",bg='#243e55',fg='#fff')
    invoice_date_lab.place(x=30,y=300,)
    invoice_date.set(format_date)
    invoice_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=invoice_date)
    invoice_date_input.place(x=30,y=330,height=40)

    terms_lab=Label(form_frame,text="Terms",bg='#243e55',fg='#fff')
    terms_lab.place(x=500,y=300,)
    terms_input=ttk.Combobox(form_frame,textvariable = terms)
    terms_input['values']=("Due on Receipt","NET15","NET30","NET60","Add New Term")
    # terms_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=terms)
    terms_input.bind("<<ComboboxSelected>>",get_terms)
    terms_input.place(x=500,y=330,height=40,width=335)

    Due_date_lab=Label(form_frame,text="Due Date",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=300,height=40)
    Due_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=Due_date)
    Due_date_input.place(x=970,y=330,height=40)

    billto_lab=Label(form_frame,text="Bill To",bg='#243e55',fg='#fff')
    billto_lab.place(x=30,y=400,)
    billto_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=billto)
    billto_input.place(x=30,y=430,height=150)


    # invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
    # invno_lab.place(x=500,y=400,)
    # invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=invno)
    # invno_input.place(x=500,y=430,height=40)

    place_of_supply_lab=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')

    drop2=ttk.Combobox(form_frame,textvariable=place_of_supply)
    drop2['values']=(cmp_data[2],"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Prede1sh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
    
    place_of_supply_lab.place(x=30,y=600,)
    drop2.place(x=30,y=630,height=40,width=335)

    # table form

    #col-1
    product_lab=Label(form_frame,text="PRODUCT / SERVICES",bg='#243e55',fg='#fff')
    product_lab.place(x=100,y=730,)

    product_drop1=ttk.Combobox(form_frame,textvariable = product)
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
    product_drop1.bind("<<ComboboxSelected>>",get_selected_product)

    product_drop1.place(x=70,y=780,height=40,width=200)

    global product2,product3,product4,hsn2,hsn3,hsn4,desc2,desc3,desc4,qty2,qty3,qty4
    product2=StringVar(form_frame)
    product_drop2=ttk.Combobox(form_frame,textvariable = product2)

   
    product_drop2['values']=product1
    product_drop2.bind("<<ComboboxSelected>>",get_selected_product2)

    product_drop2.place(x=70,y=850,height=40,width=200)

    product3=StringVar(form_frame)
    product_drop3=ttk.Combobox(form_frame,textvariable = product3)
            
    product_drop3['values']=product1
    product_drop3.bind("<<ComboboxSelected>>",get_selected_product3)
    product_drop3.place(x=70,y=930,height=40,width=200)

    product4=StringVar(form_frame)
    product_drop4=ttk.Combobox(form_frame,textvariable = product4)
    product_drop4['values']=product1
    product_drop4.bind("<<ComboboxSelected>>",get_selected_product4)
    product_drop4.place(x=70,y=1000,height=40,width=200)

    #col-2

    hsn_lab=Label(form_frame,text="HSN",bg='#243e55',fg='#fff')
    hsn_lab.place(x=350,y=730,)

    hsn_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn)
    hsn_input1.place(x=300,y=780,height=40)

    hsn2=StringVar(form_frame)
    hsn_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn2)
    hsn_input2.place(x=300,y=850,height=40)

    hsn3=StringVar(form_frame)
    hsn_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn3)
    hsn_input3.place(x=300,y=930,height=40)

    hsn4=StringVar(form_frame)
    hsn_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = hsn4)
    hsn_input4.place(x=300,y=1000,height=40)

    #col-3

    desc_lab=Label(form_frame,text="DESCRIPTION",bg='#243e55',fg='#fff')
    desc_lab.place(x=550,y=730,)


    desc_input1=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc)
    desc_input1.place(x=500,y=780,height=40)

    desc2=StringVar(form_frame)
    desc_input2=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc2)
    desc_input2.place(x=500,y=850,height=40)

    desc3=StringVar(form_frame)
    desc_input3=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc3)
    desc_input3.place(x=500,y=930,height=40)

    desc4=StringVar(form_frame)
    desc_input4=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = desc4)
    desc_input4.place(x=500,y=1000,height=40)

    #col-4
    qty_lab=Label(form_frame,text="QUANTITY",bg='#243e55',fg='#fff')
    qty_lab.place(x=800,y=730,)
    qty.set(0)
    qty_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty)
    qty_input1.place(x=750,y=780,height=40)

    qty_input1.bind("<KeyRelease>",get_selected_product)


    qty2=StringVar(form_frame)
    qty_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty2)
    qty_input2.place(x=750,y=850,height=40)
    qty_input2.bind("<KeyRelease>",get_selected_product2)


    qty3=StringVar(form_frame)
    qty_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty3)
    qty_input3.place(x=750,y=930,height=40)
    qty_input3.bind("<KeyRelease>",get_selected_product3)


    qty4=StringVar(form_frame)
    qty_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = qty4)
    qty_input4.place(x=750,y=1000,height=40)
    qty_input4.bind("<KeyRelease>",get_selected_product4)


    #col-5
    price_lab=Label(form_frame,text="PRICE",bg='#243e55',fg='#fff')
    price_lab.place(x=1000,y=730,)

    price_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price)
    price_input1.place(x=950,y=780,height=40)
    # price_input1.bind("<KeyRelease>",get_qty)

    global price2,price3,price4
    price2=StringVar(form_frame)
    price_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price2)
    price_input2.place(x=950,y=850,height=40)

    price3=StringVar(form_frame)
    price_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price3)
    price_input3.place(x=950,y=930,height=40)

    price4=StringVar(form_frame)
    price_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = price4)
    price_input4.place(x=950,y=1000,height=40)

    #col-6
    total_lab=Label(form_frame,text="TOTAL",bg='#243e55',fg='#fff')
    total_lab.place(x=1200,y=730,)



    total_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total)
    # total_input1.bind("<KeyRelease>",get_total)
    total_input1.place(x=1150,y=780,height=40)

    global total2,total3,total4
    total2=StringVar(form_frame)
    total2.set("0")
    total_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total2)
    total_input2.place(x=1150,y=850,height=40)

    total3=StringVar(form_frame)
    total3.set("0")
    total_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total3)
    total_input3.place(x=1150,y=930,height=40)

    total4=StringVar(form_frame)
    total4.set("0")
    total_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = total4)
    total_input4.place(x=1150,y=1000,height=40)

    #ocol-7
    tax_lab=Label(form_frame,text="TAX (%)",bg='#243e55',fg='#fff')
    tax_lab.place(x=1400,y=730,)

    # tax1=StringVar()
    tax_drop1=ttk.Combobox(form_frame,textvariable = tax)
    tax_values=("Choose","28.0% GST(28%)","18.0% GST(18%)","12.0% GST(12%)","06.0% GST(06%)","05.0% GST(05%)","03.0% GST(03%)","0.25% GST(0.25%)","0.0% GST(0%)","Exempt GST(0%)","Out of Scope(0%)")
    tax_drop1['values']=tax_values
    tax_drop1.bind("<<ComboboxSelected>>",get_selected_product)



    tax_drop1.place(x=1350,y=780,height=40,width=200)
    global tax2,tax3,tax4
    tax2=StringVar(form_frame)
    tax_drop2=ttk.Combobox(form_frame,textvariable = tax2)
    tax_drop2['values']=tax_values
    tax_drop2.bind("<<ComboboxSelected>>",get_selected_product2)
    tax_drop2.place(x=1350,y=850,height=40,width=200)

    tax3=StringVar(form_frame)
    tax_drop3=ttk.Combobox(form_frame,textvariable = tax3)
    tax_drop3['values']=tax_values
    tax_drop3.bind("<<ComboboxSelected>>",get_selected_product3)
    tax_drop3.place(x=1350,y=930,height=40,width=200)

    tax4=StringVar(form_frame)
    tax_drop4=ttk.Combobox(form_frame,textvariable = tax4)
    tax_drop4['values']=tax_values
    tax_drop4.bind("<<ComboboxSelected>>",get_selected_product4)
    tax_drop4.place(x=1350,y=1000,height=40,width=200)





    subtotal_lab=Label(form_frame,text="Sub Total",bg='#243e55',fg='#fff')
    subtotal_lab.place(x=970,y=1200,height=40)
    subtotal_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = subtotal)
    subtotal_input.place(x=1100,y=1200,height=40)

    taxamount_lab=Label(form_frame,text="Tax Amount",bg='#243e55',fg='#fff')
    taxamount_lab.place(x=970,y=1300,height=40)
    taxamount_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = taxamount)
    taxamount_input.place(x=1100,y=1300,height=40)

    grand_lab=Label(form_frame,text="Grand Total",bg='#243e55',fg='#fff')
    grand_lab.place(x=970,y=1400,height=40)
    grand_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = grand)

    grand_input.place(x=1100,y=1400,height=40)

    amt_received_lab=Label(form_frame,text="Amount Received",bg='#243e55',fg='#fff')
    amt_received_lab.place(x=970,y=1500,height=40)
    amt_received_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = amt_received)
    amt_received_input.bind("<KeyRelease>",get_selected_product)
    amt_received_input.place(x=1100,y=1500,height=40)

    balance_lab=Label(form_frame,text="Balance Due",bg='#243e55',fg='#fff')
    balance_lab.place(x=970,y=1600,height=40)
    balance_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = balance)

    balance_input.place(x=1100,y=1600,height=40)

    submit_button=Button(form_frame,text="Save",background="#2f516a",command=save_invoice, foreground="white",width=20,height=2)

    submit_button.place(x=1150,y=1700)
    font=('Times', 15)
    notice_lab=Label(form_frame,text="Notice :",bg='#243e55',fg='#808080',font=('Times', 15),)
    notice_lab.place(x=30,y=1800,)

    note_lab=Label(form_frame,text="Fin sYs Terms and Conditions Apply ",bg='#243e55',fg='#808080',)
    note_lab.place(x=30,y=1825,)
    note2_lab=Label(form_frame,text="Invoice was created on a computer and is valid without the signature and seal.  ",bg='#243e55',fg='#808080',)
    note2_lab.place(x=30,y=1850,)




    






















def edit_customer():

    def get_email(event):
        name=[]
        options=drop1.get()
        name.append(options)
        for custm in customers_data:
            full_name=custm[2]+custm[3]
            if full_name==name[0]:
                first_name=custm[2]
                last_name=custm[3]
        mycursor.execute("SELECT * FROM customer where firstname=%s and lastname=%s",(first_name,last_name))
        table2=mycursor.fetchall()
        for i in table2:
            e_email.set(i[9])
            e_billto.set(i[12:17])




    def get_e_terms(event):
        global e_invno
        options=terms_input.get()
        if options=="Add New Term":
            invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
            invno_lab.place(x=500,y=400,)
            invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=e_invno)
            invno_input.place(x=500,y=430,height=40)
        else:
            e_invno.set(0)

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
        for product in inv_data:
            product_details="SELECT * FROM app1_inventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_noninventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_bundle WHERE name=%s"
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
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        e_balance.set(balancedue)




    def get_selected_e_product2(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        # print("subtotal",createsubtotal)
        selected_product=[]
        product=product_drop2.get()
        selected_product.append(product)
        quantity2=qty_input2.get()
        for product in inv_data:
            product_details="SELECT * FROM app1_inventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_noninventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_bundle WHERE name=%s"
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
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        e_balance.set(balancedue)



    def get_selected_e_product3(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        selected_product=[]
        product=product_drop3.get()
        selected_product.append(product)
        quantity3=qty_input3.get()
        for product in inv_data:
            product_details="SELECT * FROM app1_inventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_noninventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_bundle WHERE name=%s"
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
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        e_balance.set(balancedue)


    def get_selected_e_product4(event):
        global createsubtotal,finding_tax1,finding_tax2,finding_tax3,finding_tax4
        selected_product=[]
        product=product_drop4.get()
        selected_product.append(product)
        quantity4=qty_input4.get()
        for product in inv_data:
            product_details="SELECT * FROM app1_inventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_noninventory WHERE name=%s"
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
            product_details="SELECT * FROM app1_bundle WHERE name=%s"
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
        amount_recieved=amt_received_input.get()
        balancedue=final_total-int(amount_recieved)
        e_balance.set(balancedue)


    def save_edited_data():
        global select_customer,email,invoice_date,terms,Due_date,billto,invno,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,taxamount,grand,amt_received,balance,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,cid_id


        Select_customer=e_select_customer.get()
        email=e_email.get()
        invoice_date=e_invoice_date.get()
        terms=e_terms.get()
        Due_date=e_Due_date.get()
        billto=e_billto.get()
        Invno=e_invno.get()
        if Invno==None:
            Invno=0
        place_of_supply=e_place_of_supply.get()
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

        amt_received=e_amt_received.get()
        taxamount=e_taxamount.get()
        balance=e_balance.get()
        cid_id=cmp1[0]


        mycursor.execute("UPDATE invoice SET customername =%s, email =%s, invoiceno =%s, terms =%s, invoicedate =%s, duedate =%s, bname =%s, placosupply =%s, product =%s, hsn =%s,description =%s, qty =%s,price =%s, total =%s, tax =%s, subtotal=%s, grandtotal =%s, product2 =%s, hsn2 =%s, description2 =%s, qty2 =%s, price2 =%s, total2 =%s, tax2 =%s, product3 =%s, hsn3 =%s, description3 =%s, qty3 =%s, price3 =%s, total3 =%s, tax3 =%s, product4 =%s, hsn4 =%s, description4 =%s, qty4 =%s, price4 =%s, total4 =%s, tax4 =%s, amtrecvd =%s, taxamount =%s, baldue =%s, cid_id =%s where invoiceid=%s"
        ,(Select_customer,email,Invno,terms,invoice_date,Due_date,billto,place_of_supply,product,hsn,desc,qty,price,total,tax,subtotal,grand,product2,hsn2,desc2,qty2,price2,total2,tax2,product3,hsn3,desc3,qty3,price3,total3,tax3,product4,hsn4,desc4,qty4,price4,total4,tax4,amt_received,taxamount,balance,cid_id,data[0]))
        mydb.commit()
        mydb.close()
        messagebox.showinfo('invoice edited Added')



    focus_data = set.focus()
    values=set.item(focus_data,'values')
    invoice_id=[values[-1]]
    mycursor.execute("SELECT * FROM invoice WHERE invoiceid=%s",(invoice_id))
    data=mycursor.fetchone()
    print("Selected data is ",data)
    editinvoice_form = Toplevel(invoice)
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


    #get customer datas from customer table
    
    mycursor.execute('select * from app1_customer ')
    customers=mycursor.fetchall()
    customers_data=[]
    for cus in customers:
        customers_data.append(cus)

    #set today date 
    date = dt.datetime.now()
    formated_date = f"{date:%Y - %d - %m }"
    today_date = Label(form_frame, text=formated_date, fg="white", bg="black", font=("helvetica", 40))




    user_id=[4]
    mycursor.execute("SELECT cid FROM app1_company WHERE id_id=%s",(user_id))
    cmp1=mycursor.fetchone()

    # cmp1=[1]

    mycursor.execute("SELECT cname,cemail,state FROM app1_company WHERE id_id=%s",(user_id))
    cmp_data=mycursor.fetchone()


    #invetory data
    mycursor.execute("SELECT * FROM app1_inventory WHERE cid_id=%s",(cmp1))
    inventory_data=mycursor.fetchall()

    #bundle data
    mycursor.execute("SELECT * FROM app1_bundle WHERE cid_id=%s",(cmp1))
    bundle_data=mycursor.fetchall()

    #noninventor data
    mycursor.execute("SELECT * FROM app1_noninventory WHERE cid_id=%s",(cmp1))
    noninventory_data=mycursor.fetchall()

    #service data
    mycursor.execute("SELECT * FROM app1_service WHERE cid_id=%s",(cmp1))
    services_data=mycursor.fetchall()



    global e_select_customer,e_email,e_invoice_date,e_terms,e_Due_date,e_billto,e_invno,cmpname,cpmemail,e_place_of_supply,e_product,e_hsn,e_desc,e_qty,e_price,e_total,e_tax,e_subtotal,e_taxamount,e_grand,e_amt_received,e_balance,e_product2,e_product3,e_product4,e_hsn2,e_hsn3,e_hsn4,e_desc2,e_desc3,e_desc4,e_qty2,e_qty3,e_qty4,e_price2,e_price3,e_price4, e_total2,e_total3,e_total4,e_tax2,e_tax3,e_tax4

    e_select_customer=StringVar(form_frame)
    e_email=StringVar(form_frame)
    e_invoice_date=StringVar(form_frame)
    e_terms=StringVar(form_frame)
    e_Due_date=StringVar(form_frame)
    e_billto=StringVar(form_frame)
    e_invno=StringVar(form_frame)
    e_place_of_supply=StringVar(form_frame)
    e_product=StringVar(form_frame)
    e_hsn=StringVar(form_frame)
    e_desc=StringVar(form_frame)
    e_qty=StringVar(form_frame)
    e_price=StringVar(form_frame)
    e_total=StringVar(form_frame)
    e_total.set("0")
    e_tax=StringVar(form_frame)
    e_subtotal=StringVar(form_frame)
    e_taxamount=StringVar(form_frame)
    e_taxamount.set("0")
    e_grand=StringVar(form_frame)
    e_grand.set("0")
    e_amt_received=StringVar(form_frame)
    e_balance=StringVar(form_frame)
    e_product2=StringVar(form_frame)
    e_product3=StringVar(form_frame)
    e_product4=StringVar(form_frame)
    e_hsn2=StringVar(form_frame)
    e_hsn3=StringVar(form_frame)
    e_hsn4=StringVar(form_frame)
    e_desc2=StringVar(form_frame)
    e_desc3=StringVar(form_frame)
    e_desc4=StringVar(form_frame)
    e_qty2=StringVar(form_frame)
    e_qty3=StringVar(form_frame)
    e_qty4=StringVar(form_frame)
    e_price2=StringVar(form_frame)
    e_price3=StringVar(form_frame)
    e_price4=StringVar(form_frame)
    e_total2=StringVar(form_frame)
    e_total3=StringVar(form_frame)
    e_total4=StringVar(form_frame)
    e_tax2=StringVar(form_frame)
    e_tax3=StringVar(form_frame)
    e_tax4=StringVar(form_frame)
    

    print("dataaaaaaaaaa",data)
    existing_customer=data[1]
    e_select_customer.set(existing_customer)

    existing_email=data[2]
    e_email.set(existing_email)

    existing_terms=data[4]
    e_terms.set(existing_terms)
    if existing_terms=="Add New Term":
        existing_invno=data[3]
        e_invno.set(existing_invno)

    existing_invoice_date=data[5]
    e_invoice_date.set(existing_invoice_date)

    existing_Due_date=data[6]
    e_Due_date.set(existing_Due_date)

    existing_billto=data[7]
    e_billto.set(existing_billto)

    existing_place_of_supply=data[8]
    e_place_of_supply.set(existing_place_of_supply)

    existing_product=data[9]
    e_product.set(existing_product)

    existing_han=data[10]
    e_hsn.set(existing_han)

    existing_desc=data[11]
    e_desc.set(existing_desc)

    existing_qty=data[12]
    e_qty.set(existing_qty)

    existing_price=data[13]
    e_price.set(existing_price)

    existing_total=data[14]
    e_total.set(existing_total)

    existing_tax=data[15]
    e_tax.set(existing_tax)

    existing_product2=data[18]
    e_product2.set(existing_product2)

    existing_hsn2=data[19]
    e_hsn2.set(existing_hsn2)

    existing_desc2=data[20]
    e_desc2.set(existing_desc2)

    existing_qty2=data[21]
    e_qty2.set(existing_qty2)

    existing_price2=data[22]
    e_price2.set(existing_price2)

    existing_total2=data[23]
    e_total2.set(existing_total2)

    existing_tax2=data[24]
    e_tax2.set(existing_tax2)

    existing_product3=data[25]
    e_product3.set(existing_product3)

    existing_hsn3=data[26]
    e_hsn3.set(existing_hsn3)

    existing_desc3=data[27]
    e_desc3.set(existing_desc3)

    existing_qty3=data[28]
    e_qty3.set(existing_qty3)

    existing_price3=data[29]
    e_price3.set(existing_price3)

    existing_total3=data[30]
    e_total3.set(existing_total3)

    existing_tax3=data[31]
    e_tax3.set(existing_tax3)

    existing_product4=data[32]
    e_product4.set(existing_product4)

    existing_hsn4=data[33]
    e_hsn4.set(existing_hsn4)

    existing_desc4=data[34]
    e_desc4.set(existing_desc4)

    existing_qty4=data[35]
    e_qty4.set(existing_qty4)

    existing_price4=data[36]
    e_price4.set(existing_price4)

    existing_total4=data[37]
    e_total4.set(existing_total4)

    existing_tax4=data[38]
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




    company_name_lab=Label(form_frame,text=cmp_data[0],bg='#243e55',fg='#fff',font="Helvetica 22 bold")
    company_name_lab.place(x=50,y=70,)

    company_email_lab=Label(form_frame,text=cmp_data[1],bg='#243e55',fg='#fff',font="Helvetica 10 bold")
    company_email_lab.place(x=50,y=120,)

    select_customer_lab=tk.Label(form_frame,text="Select Customer",bg='#243e55',fg='#fff')

    drop1=ttk.Combobox(form_frame,textvariable = e_select_customer)
    value=[]
    for cust in  customers_data:
        customer_values=cust[-1]
        
        if customer_values==cmp1[0]:
            value.append((cust[2]+cust[3]))
            drop1['values']=value
        else:
            messagebox.showerror('error', 'invalid data')
    drop1.bind("<<ComboboxSelected>>",get_email)
    select_customer_lab.place(x=30,y=200,height=15)
    drop1.place(x=30,y=230,height=40,width=335)
    wrappen.pack(fill='both',expand='yes',)

    # add_custom=Button(form_frame,text="+",bg='#2f516a',fg='#fff',bd=3,relief="solid",width=2,command=add_custom)
    # add_custom.place(x=370,y=230)

    email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
    email_lab.place(x=500,y=200,)
    email_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=e_email)
    email_input.place(x=500,y=230,height=40)

    invoice_date_lab=Label(form_frame,text="Invoice Date",bg='#243e55',fg='#fff')
    invoice_date_lab.place(x=30,y=300,)
    invoice_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=e_invoice_date)
    e_invoice_date.set(formated_date)
    invoice_date_input.place(x=30,y=330,height=40)

    terms_lab=Label(form_frame,text="Terms",bg='#243e55',fg='#fff')
    terms_lab.place(x=500,y=300,)
    terms_input=ttk.Combobox(form_frame,textvariable = e_terms)
    terms_input['values']=("Due on Receipt","NET15","NET30","NET60","Add New Term")
    # # terms_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=terms)
    terms_input.bind("<<ComboboxSelected>>",get_e_terms)
    terms_input.place(x=500,y=330,height=40,width=335)

    Due_date_lab=Label(form_frame,text="Due Date",bg='#243e55',fg='#fff')
    Due_date_lab.place(x=970,y=300,height=40)
    Due_date_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=e_Due_date)
    Due_date_input.place(x=970,y=330,height=40)

    billto_lab=Label(form_frame,text="Bill To",bg='#243e55',fg='#fff')
    billto_lab.place(x=30,y=400,)
    billto_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=e_billto)
    billto_input.place(x=30,y=430,height=150)


    # # invno_lab=Label(form_frame,text="Invoice No",bg='#243e55',fg='#fff')
    # # invno_lab.place(x=500,y=400,)
    # # invno_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable=invno)
    # # invno_input.place(x=500,y=430,height=40)

    place_of_supply_lab=Label(form_frame,text="Place Of Supply",bg='#243e55',fg='#fff')

    drop2=ttk.Combobox(form_frame,textvariable=e_place_of_supply)
    drop2['values']=(cmp_data[2],"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Prede1sh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")
    
    place_of_supply_lab.place(x=30,y=600,)
    drop2.place(x=30,y=630,height=40,width=335)

    # # table form

    # #col-1
    product_lab=Label(form_frame,text="PRODUCT / SERVICES",bg='#243e55',fg='#fff')
    product_lab.place(x=100,y=730,)

    product_drop1=ttk.Combobox(form_frame,textvariable = e_product)
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
    product_drop1.bind("<<ComboboxSelected>>",get_selected_e_product)

    product_drop1.place(x=70,y=780,height=40,width=200)

    product_drop2=ttk.Combobox(form_frame,textvariable = e_product2)

   
    product_drop2['values']=product1
    product_drop2.bind("<<ComboboxSelected>>",get_selected_e_product2)

    product_drop2.place(x=70,y=850,height=40,width=200)

   
    product_drop3=ttk.Combobox(form_frame,textvariable = e_product3)
            
    product_drop3['values']=product1
    product_drop3.bind("<<ComboboxSelected>>",get_selected_e_product3)
    product_drop3.place(x=70,y=930,height=40,width=200)

   
    product_drop4=ttk.Combobox(form_frame,textvariable = e_product4)
    product_drop4['values']=product1
    product_drop4.bind("<<ComboboxSelected>>",get_selected_e_product4)
    product_drop4.place(x=70,y=1000,height=40,width=200)

    # #col-2

    hsn_lab=Label(form_frame,text="HSN",bg='#243e55',fg='#fff')
    hsn_lab.place(x=350,y=730,)

    hsn_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn)
    hsn_input1.place(x=300,y=780,height=40)

    
    hsn_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn2)
    hsn_input2.place(x=300,y=850,height=40)

    hsn_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn3)
    hsn_input3.place(x=300,y=930,height=40)

    hsn_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_hsn4)
    hsn_input4.place(x=300,y=1000,height=40)

    # #col-3

    desc_lab=Label(form_frame,text="DESCRIPTION",bg='#243e55',fg='#fff')
    desc_lab.place(x=550,y=730,)


    desc_input1=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc)
    desc_input1.place(x=500,y=780,height=40)

    desc_input2=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc2)
    desc_input2.place(x=500,y=850,height=40)

    desc_input3=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc3)
    desc_input3.place(x=500,y=930,height=40)

    desc_input4=Entry(form_frame,width=25,bg='#2f516a',fg='#fff',textvariable = e_desc4)
    desc_input4.place(x=500,y=1000,height=40)

    # #col-4
    qty_lab=Label(form_frame,text="QUANTITY",bg='#243e55',fg='#fff')
    qty_lab.place(x=800,y=730,)

    qty_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty)
    qty_input1.place(x=750,y=780,height=40)

    qty_input1.bind("<KeyRelease>",get_selected_e_product)


    qty_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty2)
    qty_input2.place(x=750,y=850,height=40)
    qty_input2.bind("<KeyRelease>",get_selected_e_product2)


    qty_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty3)
    qty_input3.place(x=750,y=930,height=40)
    qty_input3.bind("<KeyRelease>",get_selected_e_product3)


    qty_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_qty4)
    qty_input4.place(x=750,y=1000,height=40)
    qty_input4.bind("<KeyRelease>",get_selected_e_product4)


    # #col-5
    price_lab=Label(form_frame,text="PRICE",bg='#243e55',fg='#fff')
    price_lab.place(x=1000,y=730,)

    price_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price)
    price_input1.place(x=950,y=780,height=40)
    # price_input1.bind("<KeyRelease>",get_qty)

    
    price_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price2)
    price_input2.place(x=950,y=850,height=40)

    price_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price3)
    price_input3.place(x=950,y=930,height=40)

    price_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_price4)
    price_input4.place(x=950,y=1000,height=40)

    # #col-6
    total_lab=Label(form_frame,text="TOTAL",bg='#243e55',fg='#fff')
    total_lab.place(x=1200,y=730,)

    total_input1=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total)
    # total_input1.bind("<KeyRelease>",get_total)
    total_input1.place(x=1150,y=780,height=40)

   
   
    total_input2=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total2)
    total_input2.place(x=1150,y=850,height=40)

    
    total_input3=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total3)
    total_input3.place(x=1150,y=930,height=40)

    
    total_input4=Entry(form_frame,width=20,bg='#2f516a',fg='#fff',textvariable = e_total4)
    total_input4.place(x=1150,y=1000,height=40)

    # #ocol-7
    tax_lab=Label(form_frame,text="TAX (%)",bg='#243e55',fg='#fff')
    tax_lab.place(x=1400,y=730,)

    # # tax1=StringVar()
    tax_drop1=ttk.Combobox(form_frame,textvariable = e_tax)
    tax_values=("Choose","28.0% GST(28%)","18.0% GST(18%)","12.0% GST(12%)","06.0% GST(06%)","05.0% GST(05%)","03.0% GST(03%)","0.25% GST(0.25%)","0.0% GST(0%)","Exempt GST(0%)","Out of Scope(0%)")
    tax_drop1['values']=tax_values
    tax_drop1.bind("<<ComboboxSelected>>",get_selected_e_product)
    tax_drop1.place(x=1350,y=780,height=40,width=200)
    
    tax_drop2=ttk.Combobox(form_frame,textvariable = e_tax2)
    tax_drop2['values']=tax_values
    tax_drop2.bind("<<ComboboxSelected>>",get_selected_e_product2)
    tax_drop2.place(x=1350,y=850,height=40,width=200)

   
    tax_drop3=ttk.Combobox(form_frame,textvariable = e_tax3)
    tax_drop3['values']=tax_values
    tax_drop3.bind("<<ComboboxSelected>>",get_selected_e_product3)
    tax_drop3.place(x=1350,y=930,height=40,width=200)

   
    tax_drop4=ttk.Combobox(form_frame,textvariable = e_tax4)
    tax_drop4['values']=tax_values
    tax_drop4.bind("<<ComboboxSelected>>",get_selected_e_product4)
    tax_drop4.place(x=1350,y=1000,height=40,width=200)





    subtotal_lab=Label(form_frame,text="Sub Total",bg='#243e55',fg='#fff')
    subtotal_lab.place(x=970,y=1200,height=40)
    subtotal_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_subtotal)
    subtotal_input.place(x=1100,y=1200,height=40)

    taxamount_lab=Label(form_frame,text="Tax Amount",bg='#243e55',fg='#fff')
    taxamount_lab.place(x=970,y=1300,height=40)
    taxamount_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_taxamount)
    taxamount_input.place(x=1100,y=1300,height=40)

    grand_lab=Label(form_frame,text="Grand Total",bg='#243e55',fg='#fff')
    grand_lab.place(x=970,y=1400,height=40)
    grand_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_grand)

    grand_input.place(x=1100,y=1400,height=40)

    amt_received_lab=Label(form_frame,text="Amount Received",bg='#243e55',fg='#fff')
    amt_received_lab.place(x=970,y=1500,height=40)
    amt_received_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_amt_received)
    amt_received_input.bind("<KeyRelease>",get_selected_e_product)
    amt_received_input.place(x=1100,y=1500,height=40)

    balance_lab=Label(form_frame,text="Balance Due",bg='#243e55',fg='#fff')
    balance_lab.place(x=970,y=1600,height=40)
    balance_input=Entry(form_frame,width=40,bg='#2f516a',fg='#fff',textvariable = e_balance)

    balance_input.place(x=1100,y=1600,height=40)

    submit_button=Button(form_frame,text="Save",background="#2f516a",foreground="white",width=20,height=2,command=save_edited_data)

    submit_button.place(x=1150,y=1700)
    font=('Times', 15)
    notice_lab=Label(form_frame,text="Notice :",bg='#243e55',fg='#808080',font=('Times', 15),)
    notice_lab.place(x=30,y=1800,)

    note_lab=Label(form_frame,text="Fin sYs Terms and Conditions Apply ",bg='#243e55',fg='#808080',)
    note_lab.place(x=30,y=1825,)
    note2_lab=Label(form_frame,text="Invoice was created on a computer and is valid without the signature and seal.  ",bg='#243e55',fg='#808080',)
    note2_lab.place(x=30,y=1850,)




#Delete constomer
def delete_invoice():
    focus_data = set.focus()
    values=set.item(focus_data,'values')
    invoic_id=[values[-1]]
    mycursor.execute("DELETE FROM invoice WHERE invoiceid=%s",(invoic_id))
    mydb.commit()
    messagebox.showinfo('successfully Delated')
    print('sucessfully deleted')
    set.delete(focus_data)



fun ()
invoice =tk.Tk()
invoice.title('fynsYs')
invoice.geometry("5000x5000")
invoice['bg']='#2f516a'
headingfont=font.Font(family='Helvitica', size=25,)
inv_heading= Label(invoice, text="INVOICES",bd=10,relief="groove",font=headingfont,bg='#243e55', fg='#fff',height=2,pady=2)
inv_heading.pack(fill=X)

content_label=Label(invoice,relief="groove",bg='#243e55', fg='#fff',width=500,height=30)

add_invoices=Button(content_label,text="Add Invoices",background='#243e55', foreground="white",command=add_invoice)
add_invoices.place(x=1450,y=100)

style = ttk.Style()
style.theme_use('classic')


set = ttk.Treeview(content_label)


set['columns']= ('invoice_no', 'invoice_date','customer','email_id','due_date','grade_total','balance_due')
set.column("#0", width=0,  stretch=NO)
set.column("invoice_no",anchor=CENTER )
set.column("invoice_date",anchor=CENTER, )
set.column("customer",anchor=CENTER,)
set.column("email_id",anchor=CENTER,)
set.column("due_date",anchor=CENTER,)
set.column("grade_total",anchor=CENTER)
set.column("balance_due",anchor=CENTER)

set.heading("#0",text="",anchor=CENTER)
set.heading("invoice_no",text="INVOICE NO",anchor=CENTER)
set.heading("invoice_date",text="INVOICE DATE",anchor=CENTER)
set.heading("customer",text="CUSTOMER",anchor=CENTER)
set.heading("email_id",text="EMAIL ID",anchor=CENTER)
set.heading("due_date",text="DUE DATE",anchor=CENTER)
set.heading("grade_total",text="GRADE TOTAL",anchor=CENTER)
set.heading("balance_due",text="BALANCE DUE",anchor=CENTER)
set.place(x=200,y=200)

sql='SELECT invoiceno,invoicedate,customername,email,duedate,grandtotal,baldue,invoiceid from invoice'
mycursor.execute(sql)
invoice_data=mycursor.fetchall()
total=mycursor.rowcount


for data in invoice_data: 
    set.insert("", 'end',values=data)

edit=Button(content_label,text="Edit",background='#243e55', foreground="white",command=edit_customer)
edit.place(x=850,y=450)

delete=Button(content_label,text="Delete",background='#243e55', foreground="white",command=delete_invoice)

delete.place(x=950,y=450)


content_label.place(x=0,y=150)
invoice.mainloop()
