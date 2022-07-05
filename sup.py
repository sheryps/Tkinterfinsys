import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as font
from tkcalendar import DateEntry,Calendar
def addsuppliers():
    global B
    B=tk.Toplevel(A)
    B.title('Add suppliers')
    B.geometry('1500x700')
    mycanvas=tk.Canvas(B,width=1800,height=1200)
    mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    yscrollbar =ttk.Scrollbar(B,orient='vertical',command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT,fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    frame=tk.Frame(mycanvas)
    frame['bg']='#2f516f'
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1000)
        #head frame

    head1 = tk.LabelFrame(frame,borderwidth=0,bg='#243e54')
    f1 = font.Font(family='Times New Roman',size=30)#font
    lb1=tk.Label(head1,text='ADD SUPPLIERS',bg='#243e54')
    
    lb1['font']=f1
    lb1.place(relx=0.4,rely=0.2)
    head1.place(relx=0.1,rely=0.02,relwidth=0.8,relheight=0.08)

    #contents frame
    hd1=tk.Frame(frame) 
    hd1['bg'] = '#243e54'
    f2 = font.Font(family='Times New Roman',size=20)#font
    label1=tk.Label(hd1,text='Supplier Information',bg='#243e54')
    label1['font']=f2
    label1.place(relx=0.01,rely=0)

    tk.Label(hd1,text='Title',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.05)
    #title.grid(row=3,column=2,padx=20,pady=20)
    cont=['Mr','Mrs','Miss','Ms']
    cmb=ttk.Combobox(hd1,values=cont)
    cmb.current(0)
    cmb.place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='First Name',bg='#243e54',font=('times new roman', 14)).place(relx=0.35,rely=0.05)
    efname=StringVar()
    tk.Entry(hd1,textvariable=efname).place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Last Name',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.05)
    elname=StringVar()
    tk.Entry(hd1,textvariable=elname).place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
    
    tk.Label(hd1,text='Company',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.13)
    ecomp=StringVar()
    tk.Entry(hd1,textvariable=ecomp).place(relx=0.02,rely=0.16,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Email',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.13)
    e_mail=StringVar()
    eemail=tk.Entry(hd1,textvariable=e_mail)
    eemail.insert(0,'example@gmail.com')
    eemail.place(relx=0.35,rely=0.16,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Mobile',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.13)
    emobile=StringVar()
    tk.Entry(hd1,textvariable=emobile).place(relx=0.68,rely=0.16,relwidth=0.3,relheight=0.035)
    
    tk.Label(hd1,text='Opening Balance',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.20)
    eopen=StringVar()
    tk.Entry(hd1,textvariable=eopen).place(relx=0.02,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Account No:',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.20)
    e_accno=StringVar()
    tk.Entry(hd1,textvariable=e_accno).place(relx=0.35,rely=0.24,relwidth=0.3,relheight=0.035)

    web=tk.Label(hd1,text='Website',font=('times new roman', 14),bg='#243e54')
    web.place(relx=0.68,rely=0.20)
    webb=StringVar()
    eweb=tk.Entry(hd1,textvariable=webb)
    eweb.insert(0,'www.example.com')
    eweb.place(relx=0.68,rely=0.24,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Billing Rate',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.28)
    ebill=StringVar()
    tk.Entry(hd1,textvariable=ebill).place(relx=0.02,rely=0.31,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Term',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.28)
    termvalues=['DUE ON RECEIPT','NET15','NET30','NET60','ADD NEW TERMS']
    eterms=ttk.Combobox(hd1,values=termvalues)
    eterms.current(0)
    eterms.place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='GST Type',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.35)
    gstvalues=['CHOOSE','GST registered-Regular','GST registered-Composition','GST-unregistered']
    egst=ttk.Combobox(hd1,values=gstvalues)
    egst.current(0)
    egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='GST IN',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.35)
    gstin=StringVar()
    egst_in=tk.Entry(hd1,textvariable=gstin)
    egst_in.insert(0,'22AAAAA0000A1Z5')
    egst_in.place(relx=0.35,rely=0.38,relwidth=0.3,relheight=0.035)

    taxreg=tk.Label(hd1,text='Tax Registeration N0',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.35)
    etaxreg=StringVar()
    tk.Entry(hd1,textvariable=etaxreg).place(relx=0.68,rely=0.38,relwidth=0.3,relheight=0.035)  

    tk.Label(hd1,text='Effective Date',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.42)
    ddate=StringVar()
    DateEntry(hd1,textvariable=ddate).place(relx=0.02,rely=0.45,relwidth=0.3,relheight=0.035)
    
    tk.Label(hd1,text='Default Expense Account',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.42)
    defvalues=['choose','Advertising/Promotional','Bank Charges','Business Licenses and Permitts','Charitable Contributions','Computer and Internet Expense','Continuing Education','Depreciation Expense','Dues and Subscriptions',
    'Housekeeping Charges','Insurance Expenses','Insurance Expenses-General Liability Insurance','Insurance Expenses-Health Insurance','Insurance Expenses-Life and Disability Insurance','Insurance Expenses-Professional Liability',
    'Internet Expenses','Meals and Entertainment','Office Supplies','Postage and Delivery','Printing and Reproduction','Professional Fees','Purchases','Rent Expense','Repair and Maintenance','Small Tools and Equipments',
    'wachh Barath Cess Expense','Taxes-Property','Telephone Expense','Travel Expense','Uncategorised Expense','Utilities','Ask My Accountant','CGST write-off','GST write-off','IGST write-off','Miscellaneous Expense','Political Contributions',
    'Reconciliation Discrepancies','SGST Write-off','Tax Write-off','Vehicle Expenses','Cost of Sales','Equipment Rental for Jobs','Freight and Shipping Cost','Merchant Account Fees','Purchases-Hardware For Resale','Purchases-Software For Resale','Subcontracted Services','Tools and Craft Suppliers']
    edefexp=ttk.Combobox(hd1,values=defvalues)
    edefexp.current(0)
    edefexp.place(relx=0.35,rely=0.45,relwidth=0.27,relheight=0.035)  

    tk.Button(hd1,text='+',font=(14),command=plus).place(relx=0.625,rely=0.45,relwidth=0.025,relheight=0.035)

    tk.Label(hd1,text='Apply TDS for Supplier',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.42)
    etds=StringVar()
    tk.Entry(hd1,textvariable=etds).place(relx=0.68,rely=0.45,relwidth=0.3,relheight=0.035)  
    
    label2=tk.Label(hd1,text='Address',bg='#243e54')
    label2['font']=f2
    label2.place(relx=0.01,rely=0.49)

    tk.Label(hd1,text='Street',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.53)
    estreet=StringVar()
    tk.Entry(hd1,textvariable=estreet).place(relx=0.02,rely=0.57,relwidth=0.63,relheight=0.035)  
    
    tk.Label(hd1,text='City',bg='#243e54',font=('times new roman', 14)).place(relx=0.68,rely=0.53)
    ecity=StringVar()
    tk.Entry(hd1,textvariable=ecity).place(relx=0.68,rely=0.57,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='State',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.61)
    stvalues=['choose','Andaman and Nicobar Islands','Andhra Pradhesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh',
    'Dadra and Nagar Haveli','Damn anad Diu','Delhi','Goa','Gujarat','Haryana','Himachal Predesh','Jammu and Kashmir'
    ,'Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Predesh','Maharashtra','Manipur',
    'Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
    'Uttar Predesh','Uttarakhand','West Bengal','Other Territory']
    estate=ttk.Combobox(hd1,values=stvalues)
    estate.current(0) 
    estate.place(relx=0.02,rely=0.64,relwidth=0.3,relheight=0.035) 

    tk.Label(hd1,text='Pin Code',bg='#243e54',font=('times new roman', 14)).place(relx=0.35,rely=0.61)
    epin=StringVar()
    tk.Entry(hd1,textvariable=epin).place(relx=0.35,rely=0.64,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Country',bg='#243e54',font=('times new roman', 14)).place(relx=0.68,rely=0.61)
    ctvalues=['choose','Afghanistan','Albania','Algeria','American Samoa','Andorra','Anguilla','Argentina','Aruba','Australia','Austria','Azerbaijan',
    'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia & Herzegovina','Botswana',
    'Bulgaria','Burundi','Cameroon','Canada','Canary Islands','Cape Verde','Chad','Channel Islands','Cape Verde','Cayman Islands','Channel Islands',
    'Chile','china','Christmas Island','Cocos Island','Colombia','Comoros','Congo','Cook Island','Costa Rica','Cote Divoire','Croatia','Cuba','Curacoa',
    'Cyprus','Czech Republic','Denmark','Dominica','Dominican Republic','East Timor','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia',
    'Ethiopia','Faroe Islands','Fiji','Finland','French Guiana','French Polynesia','French Southern Ter','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar',
    'Great Britain','Greece','Greenland','Guadeloupe','Guam','Guatemala','Guinea','Guyana','Haiti','Hawaii','Hong Kong','Hungary','Iceland','Indonesia','India','Iran',
    'Iraq','Ireland','Isle of Man','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kazakhstan','Kenya','Kiribati','Korea North','Korea South','Kuwait','Kyrgyzstan',
    'Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macau','Macedonia','Madagascar','Malaysia','Malawi','Malidives','Mali','Malta',
    'Marshall Island','Martinique','Mauritania','Mauritius','Mayotte']
    econt=ttk.Combobox(hd1,values=ctvalues)
    econt.current(0)
    econt.place(relx=0.68,rely=0.64,relwidth=0.3,relheight=0.035)

    tk.Label(hd1,text='Notes',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.68)
    enotes=StringVar()
    tk.Entry(hd1,textvariable=enotes).place(relx=0.02,rely=0.71,relwidth=0.8,relheight=0.045) 

    Checkbutton(hd1, text = "Agree to Terms and Conditions",bg='#243e54',font=('times new roman', 12)).place(relx=0.02,rely=0.76)  


    sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#243e54',command=enter).place(relx=0.5,rely=0.79)

    hd1.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.9)
    
    tk.Frame(frame,bg='#2f516f').place(relx=0,rely=0.92,relwidth=1,relheight=0.08)
    B.mainloop()