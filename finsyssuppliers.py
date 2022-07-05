import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
from tkinter import messagebox
import tkinter.font as font
from tkcalendar import DateEntry,Calendar
import datetime as dt
import re
#database connection
import mysql.connector
mydata=mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter1')
cur=mydata.cursor()
def sherryplus():
    def valueget():
        ac=cm1.get()
        n=e3.get()
        dtype=cmb.get()
        desc=e5.get()
        gtype=cb.get()
        gstval=e6.get()
        cid=2
        bal=0
        balance=float(bal)
        d='''INSERT INTO accounts (acctype,detype,name,description,gst,deftaxcode,cid,balance) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
        cur.execute(d,[(ac),(dtype),(n),(desc),(gtype),(gstval),(cid),(balance)])
        dd='''INSERT INTO accounttype (cid,accountbal,accountname) 
        VALUES (%s,%s,%s)'''
        cur.execute(dd,[(cid),(balance),(dtype)])
        mydata.commit()
        jj='''SELECT name,balance FROM accounts1 WHERE cid= %s'''
        cur.execute(jj,[cid])
        cc=cur.fetchall()
        for i in cc:
            if i[0]=='Opening Balance Equity':
                a=i[0]
                b=i[1]
                b=b+balance
                cur.execute("""UPDATE accounts1 SET balance=%s WHERE name= %s""",(b,a))
            mydata.commit()

        print(cc)
        C.destroy()

    C=tk.Toplevel(B)
    C.title('account create')
    C.geometry('1400x700')
    C['bg'] = '#2f516f'

    frame1 = tk.LabelFrame(C,borderwidth=0,bg='#243e54')
    l1=tk.Label(frame1,text='ACCOUNT CREATE',bg='#243e54',font=('Times New Roman',30))
    l1.place(relx=0.35,rely=0.1)
    frame1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    frame2=tk.Frame(C,bg='#243e54')
    l2=tk.Label(frame2,text='Account Type',bg='#243e54',font=('times new roman', 14))
    l2.place(relx=0.04,rely=0.05)
    acc=['Cost of Goods Sold','Expenses','Other Expense']
    cm1=ttk.Combobox(frame2,values=acc)
    cm1.current(0)
    cm1.place(relx=0.04,rely=0.15,relwidth=0.4,relheight=0.065)
    
    l3=tk.Label(frame2,text='Name',bg='#243e54',font=('times new roman', 14)).place(relx=0.5,rely=0.05)
    e3=StringVar()
    tk.Entry(frame2,textvariable=e3).place(relx=0.5,rely=0.15,relwidth=0.4,relheight=0.065)

    l4=tk.Label(frame2,text='Detail Type',bg='#243e54',font=('times new roman', 14)).place(relx=0.04,rely=0.25)
    def comboinput():
        cur.execute("SELECT itemname FROM itemmodel")
        val=cur.fetchall()         
        for row in val:
            cont.append(row[0])
    cont=[]
    comboinput()
    cmb=ttk.Combobox(frame2,values=cont)
    cmb.place(relx=0.04,rely=0.35,relwidth=0.4,relheight=0.065)
    
    l5=tk.Label(frame2,text='Description',bg='#243e54',font=('times new roman', 14)).place(relx=0.5,rely=0.25)
    e5=StringVar()
    tk.Entry(frame2,textvariable=e5).place(relx=0.5,rely=0.35,relwidth=0.4,relheight=0.065)

    message='''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    text_box=Text(frame2)
    text_box.place(relx=0.04,rely=0.55,relwidth=0.4,relheight=0.2)
    text_box.insert('end',message)
    text_box.config(state='disabled')

    def activator():
        global cb
        bal=['Deferred CGST','Deferred GST Input Credit','Deferred Krishi Kalyan Cess',
         'Input Credit','Deferred Service Tax Input Credit','Deferred SGST','Deferred VAT Input Credit',
        'GST Refund','Inventory Asset','Paid Insurance','Service Tax Refund','TDS Receivable','Uncategorised Asset',
        'Accumulated Depreciation','Buildings and Improvements','Furniture and Equipment','Land','Leasehold Improvements',
        'CGST Payable','CST Payable','CST Suspense','GST Payable','GST Suspense','IGST Payable','Input CGST','Input CGST Tax RCM',
        'Input IGST','Input IGST Tax RCM','Input Krishi Kalyan Cess','Input Krishi Kalyan Cess RCM','Input Service Tax',
        'Input Service Tax RCM','Input VAT 14%','Input VAT 4%','Input VAT 5%','Krishi Kalyan Cess Payable','Krishi Kalyan Cess Suspense',
        'Output CGST','Output CGST Tax RCM','Output CST 2%','Output IGST','Output IGST Tax RCM','Output Krishi Kalyan Cess',
         'Output Krishi Kalyan Cess DCM','Output Service Tax','Output Service Tax RCM','Output SGST','Output SGST Tax RCM',
        'Output VAT 14%','Output VAT 4%','Output VAT 5%','Service Tax Payable','Service Tax Suspense','SGST Payable','Swachh Bharat Cess Payable',
        'TDS Payable','VAT Payable','VAT Suspense','Opening Balance','Equity']

        cb=ttk.Combobox(frame2,values=bal)
        cb.place(relx=0.5,rely=0.55,relwidth=0.4,relheight=0.065)
    ch=IntVar()
    Checkbutton(frame2, text = "Is sub-account ",bg='#243e54',font=('times new roman', 12),command=activator,variable=ch).place(relx=0.5,rely=0.45)
    ab=ch.get()
    print(ab)

    l6=tk.Label(frame2,text='Default Tax Code',bg='#243e54',font=('times new roman', 14)).place(relx=0.5,rely=0.63)
    val=['18.0% IGST',' 14.00% ST','0% IGST','Out of Scope','0% GST','14.5% ST','14.0% VAT','6.0% IGST','28.0% IGST','15.0% ST','28.0% GST','12.0% GST','18.0% GST',
    '3.0% GST','0.2% IGST','5.0% GST','6.0% GST','0.2% GST','Exempt IGST','3.0% IGST','4.0% VAT','5.0% IGST','12.36% ST','5.0% VAT','Exempt GST','12.0% IGST','2.0% CST']
    e6=ttk.Combobox(frame2,values=val)
    e6.place(relx=0.5,rely=0.7,relwidth=0.4,relheight=0.065)
    sub1=tk.Button(frame2,text='CREATE',font=15,bg='#2f516f',command=valueget).place(relx=0.45,rely=0.9)
    frame2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
    C.mainloop()
def addsuppliers():
    def enter():
 
        title=cmb.get()
        fname=efname.get()
        lname=elname.get()
        comp=ecomp.get()
        mail=eemail.get()
        mob=mb.get()
        open=eopen.get()
        acc=e_accno.get()
        webs=web.get()
        bill=ebill.get()
        terms=eterms.get()
        gst=egst.get()
        gst_in=gstin.get()
        tax=etaxreg.get()
        date=ddate.get()
        defexp=edefexp.get()
        tds=etds.get()
        street=estreet.get()
        city=ecity.get()
        state=estate.get()
        pin=epin.get()
        contry=econt.get()
        note=enotes.get()
        bn=bm.get()
        ckh=chh.get()
        if fname=='':
            messagebox.showerror('Error','Please enter your Firstname',parent=B)
        elif lname=='':
            messagebox.showerror('Error','Please enter your lastname',parent=B)
        elif comp=='':
            messagebox.showerror('Error','Please enter your company',parent=B)   
        elif mail=='':
            messagebox.showerror('Error','Please enter your mail',parent=B)  
        elif mob=='' or len(mob)<10:
            messagebox.showerror('Error','Please enter valid mobile number',parent=B)    
        elif open=='':
            messagebox.showerror('Error','Please enter your opening balance',parent=B)
        elif acc=='':
            messagebox.showerror('Error','Please enter your account number',parent=B)  
        elif street=='':
                  chk_bl.config(text='Please enter a valid street',fg='red')  
        elif city=='':
                  chk_b2.config(text='Please enter a valid City',fg='red') 
        elif pin=='':
                  chk_b3.config(text='Please enter  pincode',fg='red')
        elif ckh==0:
                  chk_b4.config(text='Please agree to terms and conditions',fg='red') 
        else:
                ds="SELECT firstname FROM supplier WHERE firstname= %s"
                cur.execute(ds,[fname])
                r=cur.fetchall()
                print(r)
                ss="SELECT lastname FROM supplier WHERE lastname= %s"
                cur.execute(ss,[lname])
                rr=cur.fetchall()
                print(rr)
                if r==[] and rr==[]:
                    chk_b4.config(text='checked',fg='green')           
                    #inserting to supplier table                                       
                    tg='''INSERT INTO supplier (title,firstname,lastname,company,mobile,email,website,billingrate,terms,addterms,openingbalance,accountno,gsttype,
                    gstin,taxregisterationno,effectivedate,defaultexpenceaccount,tds,street,city,state ,pincode,country,notes) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''
                    cur.execute(tg,[(title),(fname),(lname),(comp),(mob),(mail),(webs),(bill),(terms),(bn),(open),(acc),(gst),(gst_in),(tax),(date),(defexp),
                    (tds),(street),(city),(state),(pin),(contry),(note)]) 
                    toda = dt.datetime.now()
                    tod = toda.strftime("%Y-%m-%d") 
                    cid=2
                    bx=fname+lname
                    #inserting to bills table
                    billg='''INSERT INTO bills (cid,grandtotal,paymdate,payee) VALUES (%s,%s,%s,%s)'''
                    cur.execute(billg,[(cid),(open),(tod),(bx)])
                    mydata.commit()
                    #inserting balance into accounts
                    billg='''SELECT balance,name FROM accounts WHERE cid= %s'''
                    cur.execute(billg,[cid])
                    cc=cur.fetchall()
                    xx=float(open)
                    for i in cc:
                        if i[1]=='Accounts Payable(Creditors)':
                            a=i[1]
                            b=i[0]
                            print(a)
                            if xx!=0:
                                b=b+xx
                                cur.execute("""UPDATE accounts SET balance=%s WHERE name= %s""",(b,a))
                            mydata.commit()
                        if i[1]=='Ask Your Accountant':
                            a=i[1]
                            b=i[0]
                            print(a)
                            if xx!=0:
                                b=b+xx
                                cur.execute("""UPDATE accounts SET balance=%s WHERE name= %s""",(b,a))
                            mydata.commit()   
                    messagebox.showinfo('Sucessfull','Supplier added sucessfully')  
                elif r is not None and rr is not None:
                    messagebox.showerror('Already Exist','User exists,Try another Name',parent=B)     
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
    mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1200)
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

    tk.Label(hd1,text='Title',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.045)
    #title.grid(row=3,column=2,padx=20,pady=20)
    cont=['Mr','Mrs','Miss','Ms']
    cmb=ttk.Combobox(hd1,values=cont)
    cmb.current(0)
    cmb.place(relx=0.02,rely=0.075,relwidth=0.3,relheight=0.025)

    tk.Label(hd1,text='First Name',bg='#243e54',font=('times new roman', 14)).place(relx=0.35,rely=0.045)
    efname=tk.Entry(hd1)
    efname.place(relx=0.35,rely=0.075,relwidth=0.3,relheight=0.025)

    f_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    f_bl.place(relx=0.35,rely=0.11)

    tk.Label(hd1,text='Last Name',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.045)
    elname=tk.Entry(hd1)
    elname.place(relx=0.68,rely=0.075,relwidth=0.3,relheight=0.025)


    
    tk.Label(hd1,text='Company',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.13)
    ecomp=tk.Entry(hd1)
    ecomp.place(relx=0.02,rely=0.165,relwidth=0.3,relheight=0.025)

    def checkmail(event):
        mail=eemail.get()
        if len(mail)>=10:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",mail):
                em_bl.config(text='Looks Good',fg='green') 
                return True
            else:
                em_bl.config(text='Enter Valid Email',fg='RED')
                return False
        else:

            em_bl.config(text='Email too Short ',fg='red')
            return False           


    tk.Label(hd1,text='Email',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.13)
    eemail=tk.Entry(hd1)
    eemail.insert(0,'example@gmail.com')
    eemail.bind('<FocusOut>',checkmail)
    eemail.place(relx=0.35,rely=0.165,relwidth=0.3,relheight=0.025)

    em_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    em_bl.place(relx=0.35,rely=0.19)
    #second commit
    def valid_int(inp):
        if inp.isdigit():
                mb_bl.config(text='Looks Good',fg='green') 
                return True          
        else:
            return False

    tk.Label(hd1,text='Mobile',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.13)
    mb=tk.Entry(hd1)
    mb.place(relx=0.68,rely=0.165,relwidth=0.3,relheight=0.025)
    val=B.register(valid_int)
    mb.config(validate='key',validatecommand=(val,"%P"))

    mb_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    mb_bl.place(relx=0.68,rely=0.19)  

    def valid_open(inp):
        if inp.isdigit():
                op_bl.config(text='Looks Good',fg='green') 
                return True          
        else:
            return False

       
   
    tk.Label(hd1,text='Opening Balance',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.21)
    eopen=tk.Entry(hd1)
    eopen.place(relx=0.02,rely=0.235,relwidth=0.3,relheight=0.025)
    opn=B.register(valid_open)
    eopen.config(validate='key',validatecommand=(opn,"%P"))
 
    op_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    op_bl.place(relx=0.02,rely=0.26)

    def valid_account(inp):
        if inp.isdigit():
                ap_bl.config(text='Looks Good',fg='green') 
                return True          
        else:
            return False


    tk.Label(hd1,text='Account No:',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.21)
    e_accno=tk.Entry(hd1)
    e_accno.place(relx=0.35,rely=0.235,relwidth=0.3,relheight=0.025)
    acn=B.register(valid_account)
    e_accno.config(validate='key',validatecommand=(acn,"%P"))

   

    ap_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    ap_bl.place(relx=0.35,rely=0.26)

    def checkweb(event):
        wbbb=web.get()  
        if re.match("^www.",wbbb):
            w_bl.config(text='Looks Good',fg='green') 
            return True
        else:
                w_bl.config(text='Enter Valid Website',fg='RED')
                return False    

    tk.Label(hd1,text='Website',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.21)
    web=tk.Entry(hd1)
    web.insert(0,'www.example.com')
    web.bind('<FocusOut>',checkweb)
    web.place(relx=0.68,rely=0.235,relwidth=0.3,relheight=0.025)

    w_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    w_bl.place(relx=0.68,rely=0.26)

    tk.Label(hd1,text='Billing Rate',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.28)
    ebill=tk.Entry(hd1)
    ebill.place(relx=0.02,rely=0.31,relwidth=0.3,relheight=0.025)

    def addnewterms(event):
        
        et=eterms.get() 
        t=termvalues[4]  
        if et==t:
            bm.place(relx=0.68,rely=0.31,relwidth=0.3,relheight=0.025)
            return True
        else:
            return False  

   
    bm=tk.Entry(hd1,)
    tk.Label(hd1,text='Term',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.28)
    termvalues=['DUE ON RECEIPT','NET15','NET30','NET60','ADD NEW TERMS']
    eterms=ttk.Combobox(hd1,values=termvalues)
    eterms.bind('<FocusOut>',addnewterms)
    eterms.place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.025)

    def gstfn(ent):
        cc=egst.get()
        if cc=='GST-unregistered':
            egst_in['state']='disabled'
            etaxreg['state']='disabled'
        else:
            egst_in['state']='normal'
            etaxreg['state']='normal'    

    tk.Label(hd1,text='GST Type',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.35)
    gstvalues=['GST registered-Regular','GST registered-Composition','GST-unregistered']
    egst=ttk.Combobox(hd1,values=gstvalues)
    egst.current(0)
    egst.bind('<<ComboboxSelected>>',gstfn)
    egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.025)

    def checkgst(event):
        gstno=egst_in.get()
        if re.match('^([0][1-9]|[1-2][0-9]|[3][0-7])([a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9a-zA-Z]{1}[zZ]{1}[0-9a-zA-Z]{1})+$',gstno):
            return True
        else:
            messagebox.showwarning('Invalid','Enter Valid GST NO:',parent=B)               


    tk.Label(hd1,text='GST IN',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.35)
    gstin=StringVar()
    egst_in=tk.Entry(hd1,textvariable=gstin)
    egst_in.insert(0,'22AAAAA0000A1Z5')
    egst_in.bind('<FocusOut>',checkgst)
    egst_in.place(relx=0.35,rely=0.38,relwidth=0.3,relheight=0.025)

    w_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    w_bl.place(relx=0.68,rely=0.26)

    taxreg=tk.Label(hd1,text='Tax Registeration N0',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.35)
    etaxreg=tk.Entry(hd1)
    etaxreg.place(relx=0.68,rely=0.38,relwidth=0.3,relheight=0.025)  

    tk.Label(hd1,text='Effective Date',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.41)
    ddate=StringVar()
    DateEntry(hd1,textvariable=ddate).place(relx=0.02,rely=0.44,relwidth=0.3,relheight=0.025)
    
    tk.Label(hd1,text='Default Expense Account',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.41)
    defvalues=['choose','Advertising/Promotional','Bank Charges','Business Licenses and Permitts','Charitable Contributions','Computer and Internet Expense','Continuing Education','Depreciation Expense','Dues and Subscriptions',
    'Housekeeping Charges','Insurance Expenses','Insurance Expenses-General Liability Insurance','Insurance Expenses-Health Insurance','Insurance Expenses-Life and Disability Insurance','Insurance Expenses-Professional Liability',
    'Internet Expenses','Meals and Entertainment','Office Supplies','Postage and Delivery','Printing and Reproduction','Professional Fees','Purchases','Rent Expense','Repair and Maintenance','Small Tools and Equipments',
    'wachh Barath Cess Expense','Taxes-Property','Telephone Expense','Travel Expense','Uncategorised Expense','Utilities','Ask My Accountant','CGST write-off','GST write-off','IGST write-off','Miscellaneous Expense','Political Contributions',
    'Reconciliation Discrepancies','SGST Write-off','Tax Write-off','Vehicle Expenses','Cost of Sales','Equipment Rental for Jobs','Freight and Shipping Cost','Merchant Account Fees','Purchases-Hardware For Resale','Purchases-Software For Resale','Subcontracted Services','Tools and Craft Suppliers']
    edefexp=ttk.Combobox(hd1,values=defvalues)
    edefexp.current(0)
    edefexp.place(relx=0.35,rely=0.44,relwidth=0.27,relheight=0.025)  

    tk.Button(hd1,text='+',font=(14),command=sherryplus).place(relx=0.625,rely=0.44,relwidth=0.025,relheight=0.025)

    tk.Label(hd1,text='Apply TDS for Supplier',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.41)
    fg=['Yes','No']
    etds=ttk.Combobox(hd1,values=fg)
    etds.place(relx=0.68,rely=0.44,relwidth=0.3,relheight=0.025)  
    
    label2=tk.Label(hd1,text='Address',bg='#243e54')
    label2['font']=f2
    label2.place(relx=0.01,rely=0.47)

    tk.Label(hd1,text='Street',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.52)
    estreet=tk.Entry(hd1)
    estreet.place(relx=0.02,rely=0.55,relwidth=0.63,relheight=0.025)  

    chk_bl=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    chk_bl.place(relx=0.02,rely=0.575)
    
    tk.Label(hd1,text='City',bg='#243e54',font=('times new roman', 14)).place(relx=0.68,rely=0.52)
    ecity=tk.Entry(hd1)
    ecity.place(relx=0.68,rely=0.55,relwidth=0.3,relheight=0.025)

    chk_b2=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    chk_b2.place(relx=0.68,rely=0.575)

    tk.Label(hd1,text='State',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.60)
    stvalues=['choose','Andaman and Nicobar Islands','Andhra Pradhesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh',
    'Dadra and Nagar Haveli','Damn anad Diu','Delhi','Goa','Gujarat','Haryana','Himachal Predesh','Jammu and Kashmir'
    ,'Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Predesh','Maharashtra','Manipur',
    'Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
    'Uttar Predesh','Uttarakhand','West Bengal','Other Territory']
    estate=ttk.Combobox(hd1,values=stvalues)
    estate.current(0) 
    estate.place(relx=0.02,rely=0.63,relwidth=0.3,relheight=0.025) 

    tk.Label(hd1,text='Pin Code',bg='#243e54',font=('times new roman', 14)).place(relx=0.35,rely=0.60)
    epin=tk.Entry(hd1)
    epin.place(relx=0.35,rely=0.63,relwidth=0.3,relheight=0.025)

    chk_b3=tk.Label(hd1,text='',font=('arial',11),fg='red',bg='#243e54')
    chk_b3.place(relx=0.35,rely=0.66)

    tk.Label(hd1,text='Country',bg='#243e54',font=('times new roman', 14)).place(relx=0.68,rely=0.60)
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
    econt.place(relx=0.68,rely=0.63,relwidth=0.3,relheight=0.025)

    tk.Label(hd1,text='Notes',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.67)
    enotes=tk.Entry(hd1)
    enotes.place(relx=0.02,rely=0.70,relwidth=0.71,relheight=0.035) 
    chh=IntVar()
    ch=Checkbutton(hd1,variable=chh, text = "Agree to Terms and Conditions",bg='#243e54',font=('times new roman', 14),onvalue=1,offvalue=0)
    ch.place(relx=0.02,rely=0.75)  
    
    chk_b4=tk.Label(hd1,text='',font=('arial',12),fg='red',bg='#243e54')
    chk_b4.place(relx=0.02,rely=0.80)

    sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#243e54',command=enter).place(relx=0.5,rely=0.8)

    hd1.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.9)
    
    tk.Frame(frame,bg='#2f516f').place(relx=0,rely=0.92,relwidth=1,relheight=0.09)


    B.mainloop()
def sherrymain():

    global A,data
    A=tk.Tk()
    A.title('suppliers')
    A.geometry('1500x1000')
    A['bg'] = '#2f516f'

    #head frame
    head = tk.LabelFrame(A,borderwidth=0,bg='#243e54')
    f = font.Font(family='Times New Roman',size=30)#font
    lb=tk.Label(head,text='SUPPLIERS',bg='#243e54')
    lb['font']=f
    lb.place(relx=0.4,rely=0.2)
    head.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

    #contents frame
    hd=tk.Frame(A,bg='#243e54')
    hd.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.5)
    ff = font.Font(family='Times New Roman',size=15)#font
    bt=tk.Button(hd,text='Add Suppliers',command=addsuppliers,bg='#243e54')
    bt['font']=ff
    bt.place(relx=0.85,rely=0.05)

    #table view
    style=ttk.Style()
    style.theme_use('default')
    style.configure('Treeview',background='silver',foreground='black',fieldbackground='#243e54')
    style.map('Treeview',background=[('selected','green')])
    treevv = ttk.Treeview(hd, height=7, columns=(1,2,3,4,5,6,7), show='headings') 
    treevv.heading(1, text='ID')
    treevv.heading(2, text='SUPPLIER')#headings
    treevv.heading(3, text='GST TYPE')
    treevv.heading(4, text='GSTIN')
    treevv.heading(5, text='MOBILE')
    treevv.heading(6, text='EMAIL ID')
    treevv.heading(7, text='OPENING BALANCE')
    #treevv.heading(7, text='Actions')

    treevv.column(1, minwidth=10, width=40,anchor=CENTER)#coloumns
    treevv.column(2, minwidth=30, width=140,anchor=CENTER)
    treevv.column(3, minwidth=30, width=140,anchor=CENTER)
    treevv.column(4, minwidth=30, width=140,anchor=CENTER)
    treevv.column(5, minwidth=30, width=140,anchor=CENTER)
    treevv.column(6, minwidth=30, width=140,anchor=CENTER)
    treevv.column(7, minwidth=30, width=120,anchor=CENTER)
    cur.execute("SELECT supplier_id,firstname,lastname,gsttype,gstin,mobile,email,openingbalance FROM supplier")
    val=cur.fetchall()
    if val:
        for x in val:
            treevv.insert('', 'end',values=(x[0],x[1]+x[2],x[3],x[4],x[5],x[6],x[7]))
    treevv.place(relx=0,rely=0.2,relwidth=1,relheight=0.6)
    def editsupplier():
        def changeedit():
            title=cmb.get()
            fname=efname.get()
            lname=elname.get()
            comp=ecomp.get()
            mail=e_mail.get()
            mob=emobile.get()
            open1=eopen.get()
            acc=e_accno.get()
            webs=webb.get()
            bill=ebill.get()
            terms=eterms.get()
            gst=egst.get()
            gst_in=gstin.get()
            tax=etaxreg.get()
            date=ddate.get()
            defexp=edefexp.get()
            tdss=tds.get()
            street=estreet.get()
            city=ecity.get()
            state=estat.get()
            pin=epin.get()
            contry=cont.get()
            note=enotes.get()
           # bn=bm.get()
            print(title,fname,lname,comp,mail,mob,open1,acc,webs,bill,terms,gst,gst_in,tax,date,defexp,tds,street,city,state,pin,contry,note,b)
            cur.execute("""UPDATE supplier SET title =%s, firstname =%s, lastname =%s, company =%s, mobile =%s, email =%s, website =%s, billingrate =%s, terms =%s, openingbalance =%s,accountno =%s, gsttype =%s,gstin =%s, taxregisterationno =%s, effectivedate =%s, defaultexpenceaccount =%s, tds =%s, street =%s, city =%s, state =%s, pincode =%s, country =%s, notes =%s WHERE supplier_id =%s""",
            (title, fname, lname, comp, mob, mail, webs, bill, terms, open1, acc, gst, gst_in, tax, date, defexp, tdss, street, city, state, pin, contry, note, b[0],))
            mydata.commit()
            D.destroy()

        # Get selected item to Edit
        global D,bm
        str = treevv.focus()
        values=treevv.item(str,'values')
        print(values)
        b=[values[0]]
        print(b)
        cur.execute("SELECT * FROM supplier WHERE supplier_id=%s",(b))
        s=cur.fetchone()
        D=tk.Toplevel(A)
        D.title('Add suppliers')
        D.geometry('1500x700')
        mycanvas=tk.Canvas(D,width=1800,height=1200)
        mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
        yscrollbar =ttk.Scrollbar(D,orient='vertical',command=mycanvas.yview)
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
        try:
            cmb.insert(0,s[1])
        except:
            pass    
        cmb.place(relx=0.02,rely=0.08,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='First Name',bg='#243e54',font=('times new roman', 14)).place(relx=0.35,rely=0.05)
        efname=StringVar()
        f=tk.Entry(hd1,textvariable=efname)
        try:
            f.insert(0,s[2])
        except:
            pass       
        f.place(relx=0.35,rely=0.08,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Last Name',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.05)
        elname=StringVar()
        l=tk.Entry(hd1,textvariable=elname)
        try:
            l.insert(0,s[3])
        except:
            pass        
        l.place(relx=0.68,rely=0.08,relwidth=0.3,relheight=0.035)
        
        tk.Label(hd1,text='Company',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.13)
        ecomp=StringVar()
        co=tk.Entry(hd1,textvariable=ecomp)
        try:
            co.insert(0,s[4])
        except:
            pass        
        co.place(relx=0.02,rely=0.16,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Email',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.13)
        e_mail=StringVar()
        eemail=tk.Entry(hd1,textvariable=e_mail)
        try:
            eemail.insert(0,s[6])
        except:
            pass    
        eemail.place(relx=0.35,rely=0.16,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Mobile',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.13)
        emobile=StringVar()
        x=tk.Entry(hd1,textvariable=emobile)
        try:
            x.insert(0,s[5])
        except:
            pass        
        x.place(relx=0.68,rely=0.16,relwidth=0.3,relheight=0.035)
        
        tk.Label(hd1,text='Opening Balance',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.20)
        eopen=StringVar()
        o=tk.Entry(hd1,textvariable=eopen)
        try:
            o.insert(0,s[11])
        except:
            pass
        o.place(relx=0.02,rely=0.24,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Account No:',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.20)
        e_accno=StringVar()
        ac=tk.Entry(hd1,textvariable=e_accno)
        try:
            ac.insert(0,s[12])
        except:
            pass    
        ac.place(relx=0.35,rely=0.24,relwidth=0.3,relheight=0.035)

        web=tk.Label(hd1,text='Website',font=('times new roman', 14),bg='#243e54')
        web.place(relx=0.68,rely=0.20)
        webb=StringVar()
        eweb=tk.Entry(hd1,textvariable=webb)
        try:
            eweb.insert(0,s[7])
        except:
            pass    
        eweb.place(relx=0.68,rely=0.24,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Billing Rate',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.28)
        ebill=StringVar()
        bl=tk.Entry(hd1,textvariable=ebill)
        try:
            bl.insert(0,s[8])
        except:
            pass
        bl.place(relx=0.02,rely=0.31,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Term',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.28)
        termvalues=['DUE ON RECEIPT','NET15','NET30','NET60','ADD NEW TERMS']
        eterms=ttk.Combobox(hd1,values=termvalues)
        try:
            eterms.insert(0,s[9])
        except:
            pass    
        eterms.place(relx=0.35,rely=0.31,relwidth=0.3,relheight=0.035)

        #bm=StringVar()
        #tk.Entry(hd1).place(relx=0.68,rely=0.31,relwidth=0.3,relheight=0.035)

        def gsttfn(ent):
            cc=egst.get()
            if cc=='GST-unregistered':
                egst_in['state']='disabled'
                tx['state']='disabled'
            else:
                egst_in['state']='normal'
                tx['state']='normal' 

        tk.Label(hd1,text='GST Type',font=('times new roman', 14),bg='#243e54').place(relx=0.02,rely=0.35)
        gstvalues=['GST registered-Regular','GST registered-Composition','GST-unregistered']
        egst=ttk.Combobox(hd1,values=gstvalues)
        egst.bind('<<ComboboxSelected>>',gsttfn)
        try:
            egst.insert(0,s[13])
        except:
            pass    
        egst.place(relx=0.02,rely=0.38,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='GST IN',font=('times new roman', 14),bg='#243e54').place(relx=0.35,rely=0.35)
        gstin=StringVar()
        egst_in=tk.Entry(hd1,textvariable=gstin)
        try:
            egst_in.insert(0,s[14])
        except:
            pass    
        egst_in.place(relx=0.35,rely=0.38,relwidth=0.3,relheight=0.035)

        taxreg=tk.Label(hd1,text='Tax Registeration N0',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.35)
        etaxreg=StringVar()
        tx=tk.Entry(hd1,textvariable=etaxreg)
        try:
            tx.insert(0,s[15])
        except:
            pass    
        tx.place(relx=0.68,rely=0.38,relwidth=0.3,relheight=0.035)  

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
        try:
            edefexp.insert(0,s[17])
        except:
            pass    
        edefexp.place(relx=0.35,rely=0.45,relwidth=0.27,relheight=0.035)  

        tk.Button(hd1,text='+',font=(14),command=sherryplus).place(relx=0.625,rely=0.45,relwidth=0.025,relheight=0.035)

        tk.Label(hd1,text='Apply TDS for Supplier',font=('times new roman', 14),bg='#243e54').place(relx=0.68,rely=0.42)
        fg=['Yes','No']
        tds=ttk.Combobox(hd1,values=fg)
        try:
            tds.insert(0,s[18])
        except:
            pass    
        tds.place(relx=0.68,rely=0.45,relwidth=0.3,relheight=0.035)  
        
        label2=tk.Label(hd1,text='Address',bg='#243e54')
        label2['font']=f2
        label2.place(relx=0.01,rely=0.49)

        tk.Label(hd1,text='Street',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.53)
        estreet=StringVar()
        st=tk.Entry(hd1,textvariable=estreet)
        try:
            st.insert(0,s[19])
        except:
            pass
        st.place(relx=0.02,rely=0.57,relwidth=0.63,relheight=0.035)  
        
        tk.Label(hd1,text='City',bg='#243e54',font=('times new roman', 14)).place(relx=0.68,rely=0.53)
        ecity=StringVar()
        cy=tk.Entry(hd1,textvariable=ecity)
        try:
            cy.insert(0,s[20])
        except:
            pass    
        cy.place(relx=0.68,rely=0.57,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='State',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.61)
        stvalues=['choose','Andaman and Nicobar Islands','Andhra Pradhesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh',
        'Dadra and Nagar Haveli','Damn anad Diu','Delhi','Goa','Gujarat','Haryana','Himachal Predesh','Jammu and Kashmir'
        ,'Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Predesh','Maharashtra','Manipur',
        'Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura',
        'Uttar Predesh','Uttarakhand','West Bengal','Other Territory']
        estat=ttk.Combobox(hd1,values=stvalues)
        try:
            estat.insert(0,s[21])
        except:
            pass    
        estat.place(relx=0.02,rely=0.64,relwidth=0.3,relheight=0.035) 

        tk.Label(hd1,text='Pin Code',bg='#243e54',font=('times new roman', 14)).place(relx=0.35,rely=0.61)
        epin=StringVar()
        pin=tk.Entry(hd1,textvariable=epin)
        try:
            pin.insert(0,s[22])
        except:
            pass
        pin.place(relx=0.35,rely=0.64,relwidth=0.3,relheight=0.035)

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
        cont=ttk.Combobox(hd1,values=ctvalues)
        try:
            cont.insert(0,s[23])
        except:
            pass    
        cont.place(relx=0.68,rely=0.64,relwidth=0.3,relheight=0.035)

        tk.Label(hd1,text='Notes',bg='#243e54',font=('times new roman', 14)).place(relx=0.02,rely=0.68)
        enotes=StringVar()
        no=tk.Entry(hd1,textvariable=enotes)
        try:
            no.insert(0,s[24])
        except:
            pass    
        no.place(relx=0.02,rely=0.71,relwidth=0.8,relheight=0.045) 

        Checkbutton(hd1, text = "Agree to Terms and Conditions",bg='#243e54',font=('times new roman', 12)).place(relx=0.02,rely=0.76)  


        sub=tk.Button(hd1,text='SUBMIT',font=15,bg='#243e54',command=changeedit).place(relx=0.5,rely=0.79)

        hd1.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.9)
        
        tk.Frame(frame,bg='#2f516f').place(relx=0,rely=0.92,relwidth=1,relheight=0.08)
        D.mainloop()

    def supplierdelete():
        # Get selected item to Delete
        str=treevv.focus() 
        values=treevv.item(str,'values')
        b=[values[0]]
        cur.execute("DELETE FROM supplier WHERE supplier_id=%s",(b))
        mydata.commit()
        print('sucessfully deleted')
        treevv.delete(str)
    edit_btn = Button(hd, text="Edit",command=editsupplier)
    edit_btn.place(relx=0.35,rely=0.8,relheight=0.1,relwidth=0.1)
    del_btn = Button(hd, text="Delete", command=supplierdelete)
    del_btn.place(relx=0.5,rely=0.8,relheight=0.1,relwidth=0.1)   
    treevv.bind("<<TreeviewSelect>>")
    A.mainloop()   
sherrymain()    
