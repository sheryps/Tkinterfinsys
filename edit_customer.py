# from calendar import c
# import tkinter as tk
# from tkinter import *
# from  tkinter import ttk
# import tkinter.font as font
# import mysql.connector

# def fun():#db connection
#     global mydb,mycursor
#     mydb=mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='finsys_tkinter'
#         )
#     mycursor = mydb.cursor()

# def update_data():
#     fun()
#     global title,first_name,last_name,company,location,gst,gstin,pan_no,email,website,mobile,street,city,state,pin,country,shipstreet,shipcity,shipstate,shippin,shipcountry
#     title=title.get()
#     first_name=first_name.get()
#     last_name=last_name.get()
#     company=company.get()
#     location=location.get()
#     gst=gst.get()
#     gstin=gstin.get()
#     pan_no=pan_no.get()
#     email=email.get()
#     website=website.get()
#     mobile=mobile.get()
#     street=street.get()
#     city=city.get()
#     state=state.get()
#     pin=pin.get()
#     country=country.get()
#     shipstreet=shipstreet.get()
#     shipcity=shipcity.get()
#     shipstate=shipstate.get()
#     shippin=shippin.get()
#     shipcountry=shipcountry.get()

#     # sql="UPDATE customer SET(title=title,)
#     mydb.commit()
#     mydb.close()





# editcustomer_form = tk.Tk()
# editcustomer_form.title("finsYs")
# editcustomer_form.geometry("2000x2000")
# editcustomer_form['bg']='#2f516a'
# wrappen=ttk.LabelFrame(editcustomer_form)
# mycanvas=Canvas(wrappen)
# mycanvas.pack(side=LEFT,fill="both",expand="yes")
# yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
# yscrollbar.pack(side=RIGHT,fill='y')

# mycanvas.configure(yscrollcommand=yscrollbar.set)
# mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

# full_frame=Frame(mycanvas,width=2000,height=2000,bg='#2f516a')
# mycanvas.create_window((0,0),window=full_frame,anchor="nw")


# heading_frame=Frame(mycanvas)
# mycanvas.create_window((150,40),window=heading_frame,anchor="nw")
# # headingfont=font.Font(family='Times New Roman', size=25,)
# addcustomer_heading= tk.Label(heading_frame, text="EDIT CUSTOMER",fg='#fff',bg='#243e55',height=2,bd=5,relief="groove",font=('Times', 25),width=93)
# addcustomer_heading.pack()

# # form fields
# # treevv=ttk.Treeview
# # str = treevv.focus()
# # values=treevv.item(str,'values')
# # b=[values[0]]
# # sql=('select * customer where id=2')
# # s=mycursor.fetchone()
# # print(sql)


# form_frame=Frame(mycanvas,width=1600,height=1000,bg='#243e55')
# mycanvas.create_window((150,150),window=form_frame,anchor="nw")
# form_lable=tk.Label(form_frame,bg='#243e55',width=100)
# form_lable.place(x=0,y=0)
# form_heading=tk.Label(form_lable, text="Customer Information",fg='#fff',bg='#243e55',height=2,bd=1,relief="groove",font=('Times', 20),width=125)
# form_heading.pack(fill=X)


# global title,first_name,last_name,company,location,gst,gstin,pan_no,email,website,mobile,street,city,state,pin,country,shipstreet,shipcity,shipstate,shippin,shipcountry
# title=StringVar()
# first_name=StringVar(form_frame)
# last_name=StringVar()
# company=StringVar()
# location=StringVar()
# gst=StringVar()
# gstin=StringVar()
# pan_no=StringVar()
# email=StringVar()
# website=StringVar()
# mobile=StringVar()
# street=StringVar()
# city=StringVar()
# state=StringVar()
# pin=StringVar()
# country=StringVar()
# shipstreet=StringVar()
# shipcity=StringVar()
# shipstate=StringVar()
# shippin=StringVar()
# shipcountry=StringVar()






# title_lab=tk.Label(form_frame,text="Title",bg='#243e55',fg='#fff')
# place_input=StringVar()
# drop2=ttk.Combobox(form_frame,textvariable = place_input)

# drop2['values']=("Mr","Mrs","Miss","Ms")

# title_lab.place(x=10,y=100,height=15,width=100)
# drop2.place(x=30,y=130,height=40,width=450)
# wrappen.pack(fill='both',expand='yes',)


# fname=Label(form_frame,text="First Name",bg='#243e55',fg='#fff')
# fname.place(x=530,y=100,)
# fname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
# fname_input.place(x=530,y=130,height=40)


# lname=Label(form_frame,text="Last Name",bg='#243e55',fg='#fff')
# lname.place(x=1060,y=100,)
# lname_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
# lname_input.place(x=1060,y=130,height=40)

# company_lab=Label(form_frame,text="Company",bg='#243e55',fg='#fff')
# company_lab.place(x=30,y=200,)
# company_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = company)
# company_input.place(x=30,y=230,height=40)

# location_lab=Label(form_frame,text="Location",bg='#243e55',fg='#fff')
# location_lab.place(x=530,y=200,)
# location_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = location)
# location_input.place(x=530,y=230,height=40)

# GST_lab=tk.Label(form_frame,text="GST Type",bg='#243e55',fg='#fff')
# GST_drop=ttk.Combobox(form_frame)
# GST_drop['values']=("Consumer","GST Registered-Regular","GST Registered-Composition","Overseas")
# GST_lab.place(x=20,y=300,height=15,width=100)
# GST_drop.place(x=30,y=330,height=40,width=450)

# gstin_lab=Label(form_frame,text="GSTIN",bg='#243e55',fg='#fff')
# gstin_lab.place(x=530,y=300,)
# gstin_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
# gstin_input.place(x=530,y=330,height=40)

# pan_no_lab=Label(form_frame,text="PAN NO",bg='#243e55',fg='#fff')
# pan_no_lab.place(x=1060,y=300,)
# pan_no_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
# pan_no_input.place(x=1060,y=330,height=40)

# email_lab=Label(form_frame,text="Email",bg='#243e55',fg='#fff')
# email_lab.place(x=30,y=400,)
# email_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
# email_input.place(x=30,y=430,height=40)

# web_lab=Label(form_frame,text="Website",bg='#243e55',fg='#fff')
# web_lab.place(x=530,y=400,)
# web_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff')
# web_input.place(x=530,y=430,height=40)


# mobile_lab=Label(form_frame,text="Mobile",bg='#243e55',fg='#fff')
# mobile_lab.place(x=1060,y=400,)
# mobile_input=Entry(form_frame,width=55,bg='#2f516a',fg='#fff',textvariable = mobile)
# mobile_input.place(x=1060,y=430,height=40)

# #Billing session
# sub_headingfont=font.Font(family='Times New Roman', size=18,)
# form2_frame=Frame(mycanvas,width=1600,height=650,bg='#243e55',bd=1,relief="groove")
# mycanvas.create_window((150,650),window=form2_frame,anchor="nw")

# bill_heading=tk.Label(form2_frame, text="Billing Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
# bill_heading.place(x=30,y=10,)

# street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
# street_lab.place(x=30,y=100,)
# street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff')
# street_input.place(x=30,y=130,height=80)


# city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
# city_lab.place(x=30,y=250,)
# city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
# city_input.place(x=30,y=280,height=40)


# state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
# state_lab.place(x=370,y=250,)
# state_drop=ttk.Combobox(form2_frame)
# state_drop['values']=("Kerala","Karnataka","Tamilnadu")
# state_drop.place(x=370,y=280,height=40,width=330)

# pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
# pin_lab.place(x=30,y=350,)
# pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
# pin_input.place(x=30,y=380,height=40)

# country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
# country_lab.place(x=370,y=350,)
# country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
# country_input.place(x=370,y=380,height=40)



# #Shipping Address 

# shipping_heading=tk.Label(form2_frame, text="Shipping Address",fg='#fff',bg='#243e55',height=2,font=sub_headingfont,width=15)
# shipping_heading.place(x=850,y=10,)



# street_lab=Label(form2_frame,text="Street",bg='#243e55',fg='#fff')
# street_lab.place(x=850,y=100,)
# street_input=Entry(form2_frame,width=85,bg='#2f516a',fg='#fff')
# street_input.place(x=850,y=130,height=80)


# city_lab=Label(form2_frame,text="City",bg='#243e55',fg='#fff')
# city_lab.place(x=850,y=250,)
# city_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
# city_input.place(x=850,y=280,height=40)


# state_lab=tk.Label(form2_frame,text="State",bg='#243e55',fg='#fff')
# state_lab.place(x=1200,y=250,)
# state_drop=ttk.Combobox(form2_frame)
# state_drop['values']=("Kerala","Karnataka","Tamilnadu")
# state_drop.place(x=1200,y=280,height=40,width=330)

# pin_lab=Label(form2_frame,text="Pin code",bg='#243e55',fg='#fff')
# pin_lab.place(x=850,y=350,)
# pin_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
# pin_input.place(x=850,y=380,height=40)

# country_lab=Label(form2_frame,text="Country",bg='#243e55',fg='#fff')
# country_lab.place(x=1200,y=350,)
# country_input=Entry(form2_frame,width=40,bg='#2f516a',fg='#fff')
# country_input.place(x=1200,y=380,height=40)

# submit_button=Button(form2_frame,text="Submit Form",background="#2f516a", foreground="white",width=40,height=2,command=update_data)

# submit_button.place(x=600,y=500)



# editcustomer_form.mainloop()
