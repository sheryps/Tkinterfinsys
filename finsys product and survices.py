from audioop import reverse
from re import L
import tkinter as tk
from tkinter import *
from tkinter import VERTICAL, ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as font
from tokenize import Name
from unicodedata import category
from colorama import Cursor
from django.forms import ImageField
from regex import P
from tkcalendar import DateEntry
from PIL import Image, ImageTk
# database connection
import mysql.connector
shajeerdata= mysql.connector.connect(host='localhost', user='root', password='', database='finsys_tkinter')
shajeercursor = shajeerdata.cursor()


def uploadimage():
    def imageget():
        invimage = imagename.get()

    f_types = [('Png files', '.png'), ('Jpg Files', '.jpg')]
    imagename = filedialog.askopenfilename(filetypes=f_types)


def expenseaccount():
    def expvalueget():
        expacctype = expaccountype.get()
        expname = expname.get()
        expdtype = expdetailtype.get()
        expdesc = expdescription.get()
        expgtype = expgst.get()
        exptaxval = exptaxcode.get()
        e = '''INSERT INTO expaccount(acctype,name,detype,prodescription,gst,deftaxcode) 
            VALUES (%s,%s,%s,%s,%s,%s)'''
        shajeercursor.execute(e, [(expacctype), (expname), (expdtype), (expdesc), (expgtype), (exptaxval), ])
        shajeerdata.commit()
        print('sucessfully added')
        EXP.destroy()
    EXP = tk.Toplevel(B)
    EXP.title('account create')
    EXP.geometry('1400x700')
    EXP['bg'] = '#2f516f'

    expframe1 = tk.LabelFrame(EXP, borderwidth=0, bg='#243e54')
    explabel1 = tk.Label(expframe1, text='ACCOUNT CREATE',
                         bg='#243e54', foreground='white', font=('poppins', 30))
    explabel1.place(relx=0.35, rely=0.1)
    expframe1.place(relx=0.02, rely=0.05, relwidth=0.95, relheight=0.1)

    expframe2 = tk.Frame(EXP, bg='#243e54')
    explabel2 = tk.Label(expframe2, text='Account Type',
                         bg='#243e54', foreground='white', font=('poppins', 14))
    explabel2.place(relx=0.01, rely=0.05)
    expaccounttypevalues = ['Cost of goods sold']
    expaccountype = ttk.Combobox(expframe2, values=expaccounttypevalues)
    expaccountype.current(0)
    expaccountype.place(relx=0.01, rely=0.15, relwidth=0.47, relheight=0.08)

    explabel3 = tk.Label(expframe2, text='Name', bg='#243e54', foreground='white', font=(
        'poppins', 14)).place(relx=0.5, rely=0.05)
    expname= StringVar()
    tk.Entry(expframe2,textvariable=expname, bg='#2f516f').place(
        relx=0.5, rely=0.15, relwidth=0.47, relheight=0.08)

    explabel4 = tk.Label(expframe2, text='Detail Type', bg='#243e54',
                         foreground='white', font=('poppins', 14)).place(relx=0.01, rely=0.25)

    cont=[]

    expdetailtype = ttk.Combobox(expframe2, values=cont).place(
        relx=0.01, rely=0.35, relwidth=0.47, relheight=0.08)

    explabel5 = tk.Label(expframe2, text='Description', bg='#243e54',
                         foreground='white', font=('poppins', 14)).place(relx=0.5, rely=0.25)
    expdescription= StringVar()
    tk.Entry(expframe2,textvariable=expdescription, bg='#2f516f').place(
        relx=0.5, rely=0.35, relwidth=0.47, relheight=0.08)

    message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    textbox = Text(expframe2, bg='#2f516f')
    textbox.place(relx=0.01, rely=0.5, relwidth=0.47, relheight=0.3)
    textbox.insert('end', message)
    textbox.config(state='disabled')

    def activator():
        global expgst

        expgstvalues = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
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

        expgst=ttk.Combobox(expframe2, values=expgstvalues).place(
            relx=0.5, rely=0.55, relwidth=0.47, relheight=0.08)

    ch=IntVar()
    Checkbutton(expframe2, text="Is sub-account ", bg='#243e54', foreground='white',
                font=('poppins', 12), command=activator, variable=ch).place(relx=0.5, rely=0.45)
    ab = ch.get()
    print(ab)
    exptaxcode = tk.Label(expframe2, text='Default Tax Code', bg='#243e54',
                          foreground='white', font=('poppins', 14)).place(relx=0.5, rely=0.63)
    exptaxvalues = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                    '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
    exptaxcode = ttk.Combobox(expframe2, values=exptaxvalues).place(
        relx=0.5, rely=0.7, relwidth=0.47, relheight=0.08)
    expsub = tk.Button(expframe2, text='CREATE', font=15, bg='#5193e6',
                       foreground='white', command=expvalueget).place(relx=0.45, rely=0.9)
    expframe2.place(relx=0.02, rely=0.2, relwidth=0.95, relheight=0.6)
    EXP.mainloop()


def incomeaccount():
    def incvalueget():
        incacctype = incaccounttype.get()
        incname = incname.get()
        incdtype = incdetailtype.get()
        incdesc = incdescription.get()
        incgtype = incgst.get()
        inctaxval = inctaxcode.get()
        i = '''INSERT INTO expaccount(acctype,name,detype,prodescription,gst,deftaxcode) 
            VALUES (%s,%s,%s,%s,%s,%s)'''
        shajeercursor.execute(i, [(incacctype), (incname), (incdtype), (incdesc), (incgtype), (inctaxval), ])
        shajeerdata.commit()
        print('sucessfully added')
        INC.destroy()
    INC = tk.Toplevel(B)
    INC.title('account create')
    INC.geometry('1400x700')
    INC['bg'] = '#2f516f'

    incframe1 = tk.LabelFrame(INC, borderwidth=0, bg='#243e54')
    incl1 = tk.Label(incframe1, text='ACCOUNT CREATE',
                     bg='#243e54', foreground='white', font=('poppins', 30))
    incl1.place(relx=0.35, rely=0.1)
    incframe1.place(relx=0.02, rely=0.05, relwidth=0.95, relheight=0.1)

    incframe2 = tk.Frame(INC, bg='#243e54')
    incl2 = tk.Label(incframe2, text='Account Type', bg='#243e54',
                     foreground='white', font=('poppins', 14))
    incl2.place(relx=0.01, rely=0.05)
    incaccountypevalues = ['Income']
    incaccounttype= ttk.Combobox(incframe2, values=incaccountypevalues)
    incaccounttype.current(0)
    incaccounttype.place(relx=0.01, rely=0.15,
                              relwidth=0.47, relheight=0.08)

    incl3 = tk.Label(incframe2, text='Name', bg='#243e54', foreground='white', font=(
        'poppins', 14)).place(relx=0.5, rely=0.05)
    incname= StringVar()
    tk.Entry(incframe2 , textvariable=incname, bg='#2f516f').place(
        relx=0.5, rely=0.15, relwidth=0.47, relheight=0.08)

    incl4 = tk.Label(incframe2, text='Detail Type', bg='#243e54',
                     foreground='white', font=('poppins', 14)).place(relx=0.01, rely=0.25)
    def inccomboinput():
        shajeercursor.execute("SELECT itemname FROM itemmodel")
        valu = shajeercursor.fetchall()
        for row in valu:
            conti.append(row[0])
    conti=[]
    inccomboinput()
    incdetailtype= ttk.Combobox(incframe2, values=conti).place(
        relx=0.01, rely=0.35, relwidth=0.47, relheight=0.08)

    incl5 = tk.Label(incframe2, text='Description', bg='#243e54',
                     foreground='white', font=('poppins', 14)).place(relx=0.5, rely=0.25)
    incdescription= StringVar()
    incdescription = tk.Entry(incframe2 , textvariable=incdescription, bg='#2f516f').place(
        relx=0.5, rely=0.35, relwidth=0.47, relheight=0.08)

    message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    textbox = Text(incframe2)
    textbox.place(relx=0.01, rely=0.55, relwidth=0.47, relheight=0.3)
    textbox.insert('end', message)
    textbox.config(state='disabled')
    def incactivator():
        global incgst

        incgstvalues = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
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

        incgst=ttk.Combobox(incframe2, values=incgstvalues).place(
            relx=0.5, rely=0.55, relwidth=0.47, relheight=0.08)

    incch=IntVar()
    Checkbutton(incframe2, text="Is sub-account ", bg='#243e54', foreground='white',
                font=('poppins', 12), command=incactivator, variable=incch).place(relx=0.5, rely=0.45)
    ab = incch.get()
    print(ab)    
    
    incl6 = tk.Label(incframe2, text='Default Tax Code', bg='#243e54',
                     foreground='white', font=('poppins', 14)).place(relx=0.5, rely=0.63)

    inctaxvalues = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                    '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
    inctaxcode= ttk.Combobox(incframe2, values=inctaxvalues).place(
        relx=0.5, rely=0.7, relwidth=0.47, relheight=0.08)
    incsub= tk.Button(incframe2, text='CREATE', font=15, bg='#5193e6',
                     foreground='white',command=incvalueget).place(relx=0.45, rely=0.9)
    incframe2.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)
    INC.mainloop()


def inventoryasset():
    def invvalueget():
        invacctype = invaccounttype.get()
        invname = invname.get()
        invdtype = invdetailtype.get()
        invdesc = invdescription.get()
        invgtype = invgst.get()
        invtaxval = invtaxcode.get()
        inv = '''INSERT INTO expaccount(acctype,name,detype,prodescription,gst,deftaxcode) 
            VALUES (%s,%s,%s,%s,%s,%s)'''
        shajeercursor.execute(inv, [(invacctype), (invname), (invdtype), (invdesc), (invgtype), (invtaxval), ])
        shajeerdata.commit()
        print('sucessfully added')
        INV.destroy()    
    INV = tk.Toplevel(B)
    INV.title('account create')
    INV.geometry('1400x700')
    INV['bg'] = '#2f516f'

    expframe1 = tk.LabelFrame(INV, borderwidth=0, bg='#243e54')
    explabel1 = tk.Label(expframe1, text='ACCOUNT CREATE',
                         bg='#243e54', foreground='white', font=('poppins', 30))
    explabel1.place(relx=0.35, rely=0.1)
    expframe1.place(relx=0.02, rely=0.05, relwidth=0.95, relheight=0.1)

    invframe2 = tk.Frame(INV, bg='#243e54')
    invlabel2 = tk.Label(invframe2, text='Account Type', bg='#243e54',
                         foreground='white', font=('poppins', 14)).place(relx=0.01, rely=0.05)
    currentassetvalues = ['Current Assets']
    invaccounttype = ttk.Combobox(invframe2, values=currentassetvalues)
    invaccounttype.current(0)
    invaccounttype.place(relx=0.01, rely=0.15, relwidth=0.47, relheight=0.08)

    invlabel3 = tk.Label(invframe2, text='Name', bg='#243e54', foreground='white', font=(
        'poppins', 14)).place(relx=0.5, rely=0.05)
    invname=StringVar
    invname = tk.Entry(invframe2,textvariable=invname ,bg='#2f516f').place(
        relx=0.5, rely=0.15, relwidth=0.47, relheight=0.08)

    invlabel4 = tk.Label(invframe2, text='Detail Type', bg='#243e54',
                         foreground='white', font=('poppins', 14)).place(relx=0.01, rely=0.25)
    def invcomboinput():
        shajeercursor.execute("SELECT itemname FROM itemmodel")
        valu = shajeercursor.fetchall()
        for row in valu:
            conti.append(row[0])
    conti=[]
    invcomboinput()    
    invdetailtype = ttk.Combobox(invframe2, values=conti).place(
        relx=0.01, rely=0.35, relwidth=0.47, relheight=0.080)

    invlabel5 = tk.Label(invframe2, text='Description', bg='#243e54',
                         foreground='white', font=('poppins', 14)).place(relx=0.5, rely=0.25)
    invdescription=StringVar
    tk.Entry(invframe2,textvariable=invdescription, bg='#243e54').place(
        relx=0.5, rely=0.35, relwidth=0.47, relheight=0.08)

    message = '''Use Cash and Cash Equivalents to track cash or assets, that can be converted into cash immediately.For example marketable securities and Treasury bills.'''
    textbox = Text(invframe2)
    textbox.place(relx=0.01, rely=0.55, relwidth=0.47, relheight=0.3)
    textbox.insert('end', message)
    textbox.config(state='disabled')
    def invactivator():
        global invgst

        invgstvalues = ['Deferred CGST', 'Deferred GST Input Credit', 'Deferred Krishi Kalyan Cess',
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

        invgst=ttk.Combobox(invframe2, values=invgstvalues).place(
            relx=0.5, rely=0.55, relwidth=0.47, relheight=0.08)

    incch=IntVar()
    Checkbutton(invframe2, text="Is sub-account ", bg='#243e54', foreground='white',
                font=('poppins', 12), command=invactivator, variable=incch).place(relx=0.5, rely=0.45)
    ab = incch.get()
    print(ab)        
    
    invlabel6 = tk.Label(invframe2, text='Default Tax Code', bg='#243e54',
                         foreground='white', font=('poppins', 14)).place(relx=0.5, rely=0.63)

    invtaxcodevalue = ['18.0% IGST', ' 14.00% ST', '0% IGST', 'Out of Scope', '0% GST', '14.5% ST', '14.0% VAT', '6.0% IGST', '28.0% IGST', '15.0% ST', '28.0% GST', '12.0% GST', '18.0% GST',
                       '3.0% GST', '0.2% IGST', '5.0% GST', '6.0% GST', '0.2% GST', 'Exempt IGST', '3.0% IGST', '4.0% VAT', '5.0% IGST', '12.36% ST', '5.0% VAT', 'Exempt GST', '12.0% IGST', '2.0% CST']
    invtaxcode = ttk.Combobox(invframe2, values=invtaxcodevalue).place(
        relx=0.5, rely=0.7, relwidth=0.47, relheight=0.08)
    invsub = tk.Button(invframe2, text='CREATE', font=15, bg='#5193e6',
                     foreground='white',command=invvalueget).place(relx=0.45, rely=0.9)
    invframe2.place(relx=0.02, rely=0.2, relwidth=0.95, relheight=0.6)
    INV.mainloop()


def add_inventory_product():
    def invproduct():
        
        product_image = uploadproductimage.get()
        Product_name = invproductname.get()
        sku = invsku.get()
        hsn = invhsncode.get()
        Unit = invunit.get()
        Category = invcategory.get()
        Initial_quantity_in_hand = invicoh.get()
        As_of_date = invdate.get()
        Low_Stock_alert = invlsa.get()
        Inventory_asset_account = invinventoryassets.get()
        prodescription = invdescription.get()
        Sales_price = invsalesprice.get()
        Tax = invtax.get()
        Income_Account = invincomeaccount.get()
        Purchasing_information = invpurchasinginformation.get()
        Cost = invcost.get()
        Purchasetax = invpurchasetax.get()
        Expense_account = invexpaccount.get()
        Reverse_charge = invreversecharge.get()
        Preferred_Supplier = invprefferdsupplier.get()
        checkcostbn = Checkcosttax.get()
        checksalebn = Checksalesprice.get()
        if product_image == '':
            messagebox.showerror('Error', 'Please select the image', parent=B)
        elif Product_name == '':
            messagebox.showerror(
                'Error', 'Please enter the product name', parent=B)
        elif sku == '':
            messagebox.showerror(
                'Error', 'Please enter the sku code', parent=B)
        elif hsn == '':
            messagebox.showerror(
                'Error', 'Please enter the hsn code', parent=B)
        elif Unit == '':
                messagebox.showerror('Error', 'Please enter the unit', parent=B)
        elif Category== '':
                messagebox.showerror('Error', 'Please enter the category', parent=B)
        elif Initial_quantity_in_hand == '':
                messagebox.showerror('Error', 'Please enter the Initial_quantity_in_hand', parent=B)
        elif As_of_date == '':
                messagebox.showerror('Error', 'Please select the As_of_date', parent=B)
        elif Low_Stock_alert == '':
                messagebox.showerror('Error', 'Please enter the Low_Stock_alert', parent=B)
        elif Inventory_asset_account == '':
                messagebox.showerror('Error', 'Please enter the Inventory_asset_account', parent=B)
        elif prodescription == '':
            messagebox.showerror(
                'Error', 'Please enter the prodescription', parent=B)
       
        elif Sales_price == '':
            messagebox.showerror(
                'Error', 'Please enter the sales price', parent=B)
        elif Tax == '':
            messagebox.showerror(
                'Error', 'Please select the tax', parent=B)
        elif Income_Account == '':
            messagebox.showerror(
                'Error', 'Please select the income account', parent=B)
        elif Purchasing_information == '':
            messagebox.showerror(
                'Error', 'Please enter the Purchasing_information', parent=B)
        elif Cost == '':
            messagebox.showerror(
                'Error', 'Please enter the cost', parent=B)
        elif Purchasetax == '':
            messagebox.showerror(
                'Error', 'Please enter the purchase tax', parent=B)
        elif Expense_account == '':
            messagebox.showerror(
                'Error', 'Please enter the expense account', parent=B)
        elif reversecharge == '':
            messagebox.showerror(
                'Error', 'Please enter the reverse charge', parent=B)
        elif Preferred_Supplier == '':
            messagebox.showerror(
                'Error', 'Please enter the Preferred_Supplier', parent=B)
        elif checkcostbn == 0:
            checkcostbn.config(
                text='Please agree the Inclusive of tax', fg='red')
        elif checksalebn == 0:
            checksalebn.config(
                text='Please agree the Inclusive of purchase tax', fg='red')
        else:
            checkcostbn.config(text='checked', fg='green')
            tg='''INSERT INTO inventory (product_image,product_name,sku,hsn,unit,category,Initial_quantity_in_hand,As_of_date,Low_stock_alert,Inventory_asset_account,prodescription,Sales_price,Tax,
            Income_account,Purchasing_information,cost,Purchase_tax,Expense_account,Reverse_charge,Preferred_Supplier)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            # selecting entire table from db,taking username , nd check the existance
            shajeercursor.execute(tg,[(product_image),(Product_name),(sku),(hsn),(Unit),(Category),(Initial_quantity_in_hand),(As_of_date),(Low_Stock_alert),(Inventory_asset_account),(prodescription),(Sales_price),(Tax),
                            (Income_Account),(Purchasing_information),(Cost),(Purchasetax),(Expense_account),(reversecharge),(Preferred_Supplier),])
            shajeerdata.commit()
            messagebox.showinfo('Sucessfully','product added sucessfully')



    global B
    B = tk.Toplevel(A)
    B.title('Add products')
    B.geometry('1400x700')
    mycanvas = tk.Canvas(B, width=1500, height=1800)
    mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    yscrollbar = ttk.Scrollbar(B, orient='vertical', command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
        scrollregion=mycanvas.bbox('all')))
    frame = tk.Frame(mycanvas)
    frame['bg'] = '#2f516f'
    mycanvas.create_window((0, 0), window=frame,
                           anchor='nw', width=1500, height=1800)
    # head frame

    head1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    f1 = font.Font(family='poppins', size=30)  # font
    lb1 = tk.Label(head1, text='PRODUCT / SERVICE INFORMATION',
                   bg='#243e54', foreground='white')
    

    lb1['font'] = f1
    lb1.place(relx=0.2, rely=0.2)
    head1.place(relx=0, rely=0.035, relwidth=1, relheight=0.05)



    # contents frame
    hd1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    
    hd2 = tk.LabelFrame(frame, borderwidth=0, bg='#2f516f')

    f3 = font.Font(family='poppins', size=18)  # font
    hd2.place(relx=0.01, rely=0.115, relwidth=0.88, relheight=0.05)
    lb2 = tk.Label(hd2, text='INVENTORY', bg='#2f516f', foreground='white')
    producttype = Button(hd2, text="Choose Type", command=selectproducttype,
                bg="#5193e6", fg="#fff", font=('mali', 10, 'bold'))
    producttype.place(relx=0.55, rely=0.2, width=350, height=50)
    f4 = font.Font(family='poppins', size=24)  # font
    lb2['font'] = f4
    lb2.place(relx=0.35, rely=0.3)


    uploadproductimage = Button(hd1, text="UPLOAD IMAGE", command=uploadimage,
                  bg="#333333", fg="#fff", font=('mali', 10, 'bold'))
    uploadproductimage.place(relx=0.4, rely=0.08, width=250, height=50)

    tk.Label(hd1, text='Name', bg='#243e54', foreground='white',
             font=('poppins', 12)).place(relx=0.01, rely=0.12)
    # title.grid(row=3,column=2,padx=20,pady=20)
    invproductname = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.135, relwidth=0.98, relheight=0.018)

    tk.Label(hd1, text='SKU', bg='#243e54', foreground='white',
             font=('poppins', 12)).place(relx=0.01, rely=0.16)
    invsku = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.175, relwidth=0.49, relheight=0.018)

    l1=tk.Label(hd1, text='HSN Code', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.16)
    invhsncode = tk.Entry(hd1, bg='#2f516f').place(
      relx=0.51, rely=0.175, relwidth=0.48, relheight=0.018)
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")
    tk.Label(hd1, text='Unit', font=('poppins', 12), bg='#243e54',
            foreground='white').place(relx=0.01, rely=0.2)
    
    invunitvalu = ['CHOOSE', 'BAG Bags', 'BAL Bale BOU', 'BDL Bundles', 'BKL Buckles', 'BOX Box', 'BTL Bottles', 'CAN Cans', 'CTN Cartons', 'CCM Cubic centimeters', 'CBM Cubic meters', 'CMS Centimeters', 'DRM Drums', 'DOZ Dozens', 'GGK Great gross GYD', 'GRS GrossGMS', 'KME Kilometre', 'KGS Kilograms', 'KLR Kilo litre',
                 'MTS Metric ton', 'MLT Mili litre', 'MTR Meters', 'NOS Numbers', 'PAC Packs', 'PCS Pieces', 'PRS Pairs', 'QTL Quintal', 'ROL Rolls', 'SQY Square Yards', 'SET Sets', 'SQF Square feet', 'SQM Square meters', 'TBS Tablets', 'TUB Tubes', 'TGM Ten Gross', 'THD Thousands', 'TON Tonnes', 'UNT Units', 'lons', 'YDS Yards']
    invunit = ttk.Combobox(hd1, values=invunitvalu)
    invunit.pack()
    invunit.place(relx=0.01, rely=0.215, relwidth=0.49, relheight=0.018)

    tk.Label(hd1, text='Category', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.2)
    invcategory = tk.Entry(hd1, bg='#2f516f')
    invcategory.place(relx=0.51, rely=0.215, relwidth=0.48, relheight=0.018)

    tk.Label(hd1, text='Initial quantity on hand', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.24)
    invicoh = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.255, relwidth=0.32, relheight=0.018)
    date = tk.Label(hd1, text='As of date', font=('poppins', 12),
                    bg='#243e54', foreground='white').place(relx=0.34, rely=0.24)
    invdate = DateEntry(hd1, bg='#2f516f').place(
        relx=0.34, rely=0.255, relwidth=0.32, relheight=0.018)
    
    web = tk.Label(hd1, text='Low stock alert', font=(
        'poppins', 12), bg='#243e54', foreground='white')
    web.place(relx=0.67, rely=0.24)
    invlsa = tk.Entry(hd1, bg='#2f516f')
    invlsa.place(relx=0.67, rely=0.255, relwidth=0.32, relheight=0.018)
    
    defexp = tk.Label(hd1, text='Inventory asset account', font=(
        'poppins', 12), bg='#243e54', foreground='white').place(relx=0.01, rely=0.28)
    invassetsvalues = ['Inventory Assets']
    invinventoryassets = ttk.Combobox(hd1, values=invassetsvalues)
    invinventoryassets.current(0)
    invinventoryassets.place(relx=0.01, rely=0.295,
                             relwidth=0.44, relheight=0.018)

    tk.Button(hd1, text='+', font=(12), bg='#243e54', command=inventoryasset).place(relx=0.46,
                                                                      rely=0.295, relwidth=0.03, relheight=0.018)

    tk.Label(hd1, text='Description', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.32)
    invdescription = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.335, relwidth=0.98, relheight=0.04)

    tk.Label(hd1, text='Sales price/rate', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.38)
    Checksalesprice = IntVar()
    invsalesprice = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.395, relwidth=0.49, relheight=0.018)
    checkcostbn=Checkbutton(hd1, text="Inclusive of tax ", variable=Checksalesprice, onvalue=1,
                offvalue=0, bg='#243e54', font=('poppins', 12)).place(relx=0.01, rely=0.415)
    
    tk.Label(hd1, text='TAX', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.38)
    invtaxvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                    '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invtax = ttk.Combobox(hd1, values=invtaxvalues)
    invtax.current(0)
    invtax.place(relx=0.51, rely=0.395, relwidth=0.48, relheight=0.018)
    
    tk.Label(hd1, text='Income account', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.43)
    incometaxvalues = ['Billable Expense Income', 'Product Sales', 'Sales', 'Sales-Hardware',
                       'Sales-Software', 'Sales-Support and Maintanance', 'Sales of Product Income', 'Uncategorised Income']
    tk.Button(hd1, text='+', font=(12), bg='#243e54', command=incomeaccount).place(relx=0.46,
                                                                     rely=0.445, relwidth=0.03, relheight=0.018)
    invincomeaccount = ttk.Combobox(hd1, values=incometaxvalues)
    invincomeaccount.current(0)
    invincomeaccount
    invincomeaccount.place(relx=0.01, rely=0.445,
                           relwidth=0.44, relheight=0.018)

    

    tk.Label(hd1, text='Purchasing information', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.47)
    invpurchasinginformation = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.485, relwidth=0.98, relheight=0.05)

    tk.Label(hd1, text='Cost', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.01, rely=0.54)
    Checkcosttax = IntVar()
    checksalebn=Checkbutton(hd1, text="Inclusive of purchase tax ", variable=Checkcosttax, onvalue=1,
                offvalue=0, bg='#243e54', font=('poppins', 12)).place(relx=0.01, rely=0.575)
    invcost = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.555, relwidth=0.49, relheight=0.018)



    tk.Label(hd1, text='Purchase TAX', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.51, rely=0.54)
    purchasetaxvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                         '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invpurchasetax = ttk.Combobox(hd1, values=purchasetaxvalues)
    invpurchasetax.current(0)
    invpurchasetax.place(relx=0.51, rely=0.555, relwidth=0.48, relheight=0.018)


    tds = tk.Label(hd1, text='Expense account', font=(
        'poppins', 14), bg='#243e54', foreground='white').place(relx=0.01, rely=0.59)
    invexpaccountvalues = ['Cost of sales']
    invexpaccount = ttk.Combobox(hd1, values=invexpaccountvalues)
    invexpaccount.current(0)
    invexpaccount.place(relx=0.01, rely=0.605, relwidth=0.44, relheight=0.018)
    tk.Button(hd1, text='+', font=(14), bg='#243e54', command=expenseaccount).place(relx=0.45,
                                                                      rely=0.605, relwidth=0.03, relheight=0.018)

    reversecharge = tk.Label(hd1, text='Reverse Charge %', bg='#243e54',
                             foreground='white', font=('poppins', 12)).place(relx=0.01, rely=0.63)
    invreversecharge = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.645, relwidth=0.49, relheight=0.018)

    invprefferdsupplier = tk.Label(hd1, text='Preferred Supplier', bg='#243e54',
                                foreground='white', font=('poppins', 12)).place(relx=0.51, rely=0.63)
    invprefferdsupplier = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.51, rely=0.645, relwidth=0.48, relheight=0.018)

    invsubmit = tk.Button(hd1, text='SUBMIT', font=14, bg='#5193e6', foreground='white',
                          command=invproduct).place(relx=0.4, rely=0.69,width=250, height=40)

    hd1.place(relx=0, rely=0.1, relwidth=0.9, relheight=1.2)

    # tk.Frame(frame,bg='#2f516f').place(relx=0,rely=0.4,relwidth=1,relheight=0.01)
    B.mainloop()


def add_non_inventoryproduct():

    global B
    B = tk.Toplevel(A)
    B.title('Add products')
    B.geometry('1400x700')
    mycanvas = tk.Canvas(B, width=1500, height=1200)
    mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    yscrollbar = ttk.Scrollbar(B, orient='vertical', command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
        scrollregion=mycanvas.bbox('all')))
    frame = tk.Frame(mycanvas)
    frame['bg'] = '#2f516f'
    mycanvas.create_window((0, 0), window=frame,
                           anchor='nw', width=1500, height=1800)
    # head frame

    head1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    f1 = font.Font(family='poppins', size=30)  # font
    lb1 = tk.Label(head1, text='PRODUCT / SERVICE INFORMATION',
                   bg='#243e54', foreground='white')
    

    lb1['font'] = f1
    lb1.place(relx=0.2, rely=0.2)
    head1.place(relx=0, rely=0.035, relwidth=1, relheight=0.05)



    # contents frame
    hd1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    
    hd2 = tk.LabelFrame(frame, borderwidth=0, bg='#2f516f')

    f3 = font.Font(family='poppins', size=18)  # font
    hd2.place(relx=0.01, rely=0.115, relwidth=0.88, relheight=0.05)
    lb2 = tk.Label(hd2, text='NON INVENTORY', bg='#2f516f', foreground='white')
    producttype = Button(hd2, text="Choose Type", command=selectproducttype,
                bg="#5193e6", fg="#fff", font=('mali', 10, 'bold'))
    producttype.place(relx=0.58, rely=0.2, width=350, height=50)
    f4 = font.Font(family='poppins', size=24)  # font
    lb2['font'] = f4
    lb2.place(relx=0.35, rely=0.3)


    uploadproductimage = Button(hd1, text="UPLOAD IMAGE", command=uploadimage,
                  bg="#333333", fg="#fff", font=('mali', 10, 'bold'))
    uploadproductimage.place(relx=0.4, rely=0.08, width=250, height=50)

    tk.Label(hd1, text='Name', bg='#243e54', foreground='white',
             font=('poppins', 12)).place(relx=0.01, rely=0.12)
    # title.grid(row=3,column=2,padx=20,pady=20)
    noninvproductname = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.135, relwidth=0.98, relheight=0.018)

    tk.Label(hd1, text='SKU', bg='#243e54', foreground='white',
             font=('poppins', 12)).place(relx=0.01, rely=0.16)
    noninvsku = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.175, relwidth=0.49, relheight=0.018)

    l1=tk.Label(hd1, text='HSN Code', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.16)
    noninvhsncode = tk.Entry(hd1, bg='#2f516f').place(
      relx=0.51, rely=0.175, relwidth=0.48, relheight=0.018)
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")
    tk.Label(hd1, text='Unit', font=('poppins', 12), bg='#243e54',
            foreground='white').place(relx=0.01, rely=0.2)
    
    invunitvalu = ['CHOOSE', 'BAG Bags', 'BAL Bale BOU', 'BDL Bundles', 'BKL Buckles', 'BOX Box', 'BTL Bottles', 'CAN Cans', 'CTN Cartons', 'CCM Cubic centimeters', 'CBM Cubic meters', 'CMS Centimeters', 'DRM Drums', 'DOZ Dozens', 'GGK Great gross GYD', 'GRS GrossGMS', 'KME Kilometre', 'KGS Kilograms', 'KLR Kilo litre',
                 'MTS Metric ton', 'MLT Mili litre', 'MTR Meters', 'NOS Numbers', 'PAC Packs', 'PCS Pieces', 'PRS Pairs', 'QTL Quintal', 'ROL Rolls', 'SQY Square Yards', 'SET Sets', 'SQF Square feet', 'SQM Square meters', 'TBS Tablets', 'TUB Tubes', 'TGM Ten Gross', 'THD Thousands', 'TON Tonnes', 'UNT Units', 'lons', 'YDS Yards']
    noninvunit = ttk.Combobox(hd1, values=invunitvalu)
    noninvunit.pack()
    noninvunit.place(relx=0.01, rely=0.215, relwidth=0.49, relheight=0.018)

    tk.Label(hd1, text='Category', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.2)
    noninvcategory = tk.Entry(hd1, bg='#2f516f')
    noninvcategory.place(relx=0.51, rely=0.215, relwidth=0.48, relheight=0.018)

    tk.Label(hd1, text='Description', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.24)
    Checkbutton(hd1, text="I sell this product/service to my customers. ",
                bg='#243e54', foreground='white', font=('poppins', 12)).place(relx=0.01, rely=0.255)
    
    tk.Label(hd1, text='Description', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.28)
    invdescription = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.3, relwidth=0.98, relheight=0.07)

    tk.Label(hd1, text='Sales price/rate', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.38)
    Checksalesprice = IntVar()
    invsalesprice = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.395, relwidth=0.49, relheight=0.018)
    checkcostbn=Checkbutton(hd1, text="Inclusive of tax ", variable=Checksalesprice, onvalue=1,
                offvalue=0, bg='#243e54', font=('poppins', 12)).place(relx=0.01, rely=0.415)
    
    tk.Label(hd1, text='TAX', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.38)
    invtaxvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                    '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invtax = ttk.Combobox(hd1, values=invtaxvalues)
    invtax.current(0)
    invtax.place(relx=0.51, rely=0.395, relwidth=0.48, relheight=0.018)
    
    tk.Label(hd1, text='Income account', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.43)
    incometaxvalues = ['Billable Expense Income', 'Product Sales', 'Sales', 'Sales-Hardware',
                       'Sales-Software', 'Sales-Support and Maintanance', 'Sales of Product Income', 'Uncategorised Income']
    tk.Button(hd1, text='+', font=(12), bg='#243e54', command=incomeaccount).place(relx=0.46,
                                                                     rely=0.445, relwidth=0.03, relheight=0.018)
    invincomeaccount = ttk.Combobox(hd1, values=incometaxvalues)
    invincomeaccount.current(0)
    invincomeaccount
    invincomeaccount.place(relx=0.01, rely=0.445,
                           relwidth=0.44, relheight=0.018)

    

    tk.Label(hd1, text='Purchasing information', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.54)
    invpurchasinginformation = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.485, relwidth=0.98, relheight=0.07)
    tk.Label(hd1, text='Purchasing information', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.56)
    Checkbutton(hd1, text="I Purchase this product/service from Supplier. ",
                bg='#243e54', foreground='white', font=('poppins', 12)).place(relx=0.01, rely=0.58)

    invsubmit = tk.Button(hd1, text='SUBMIT', font=14, bg='#5193e6', foreground='white',
                          ).place(relx=0.4, rely=0.69,width=250, height=40)

    hd1.place(relx=0, rely=0.1, relwidth=0.9, relheight=1.2)

    
    B.mainloop()


def add_services():


    global B
    B = tk.Toplevel(A)
    B.title('PRODUCT / SERVICE INFORMATION')
    B.geometry('1400x700')
    mycanvas = tk.Canvas(B, width=1500, height=1200)
    mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    yscrollbar = ttk.Scrollbar(B, orient='vertical', command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
        scrollregion=mycanvas.bbox('all')))
    frame = tk.Frame(mycanvas)
    frame['bg'] = '#2f516f'
    mycanvas.create_window((0, 0), window=frame,
                           anchor='nw', width=1500, height=1800)
    # head frame

    head1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    f1 = font.Font(family='poppins', size=30)  # font
    lb1 = tk.Label(head1, text='PRODUCT / SERVICE INFORMATION',
                   bg='#243e54', foreground='white')
    

    lb1['font'] = f1
    lb1.place(relx=0.2, rely=0.2)
    head1.place(relx=0, rely=0.035, relwidth=1, relheight=0.05)



    # contents frame
    hd1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    
    hd2 = tk.LabelFrame(frame, borderwidth=0, bg='#2f516f')

    f3 = font.Font(family='poppins', size=18)  # font
    hd2.place(relx=0.01, rely=0.115, relwidth=0.88, relheight=0.05)
    lb2 = tk.Label(hd2, text='SERVICES', bg='#2f516f', foreground='white')
    producttype = Button(hd2, text="Choose Type", command=selectproducttype,
                bg="#5193e6", fg="#fff", font=('mali', 10, 'bold'))
    producttype.place(relx=0.58, rely=0.2, width=350, height=50)
    f4 = font.Font(family='poppins', size=24)  # font
    lb2['font'] = f4
    lb2.place(relx=0.35, rely=0.3)


    uploadproductimage = Button(hd1, text="UPLOAD IMAGE", command=uploadimage,
                  bg="#333333", fg="#fff", font=('mali', 10, 'bold'))
    uploadproductimage.place(relx=0.4, rely=0.08, width=250, height=50)

    tk.Label(hd1, text='Name', bg='#243e54', foreground='white',
             font=('poppins', 12)).place(relx=0.01, rely=0.12)
    # title.grid(row=3,column=2,padx=20,pady=20)
    noninvproductname = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.135, relwidth=0.98, relheight=0.018)

    tk.Label(hd1, text='SKU', bg='#243e54', foreground='white',
             font=('poppins', 12)).place(relx=0.01, rely=0.16)
    noninvsku = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.175, relwidth=0.49, relheight=0.018)

    l1=tk.Label(hd1, text='SAC Code', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.16)
    noninvhsncode = tk.Entry(hd1, bg='#2f516f').place(
      relx=0.51, rely=0.175, relwidth=0.48, relheight=0.018)
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")
    tk.Label(hd1, text='Unit', font=('poppins', 12), bg='#243e54',
            foreground='white').place(relx=0.01, rely=0.2)
    
    invunitvalu = ['CHOOSE', 'BAG Bags', 'BAL Bale BOU', 'BDL Bundles', 'BKL Buckles', 'BOX Box', 'BTL Bottles', 'CAN Cans', 'CTN Cartons', 'CCM Cubic centimeters', 'CBM Cubic meters', 'CMS Centimeters', 'DRM Drums', 'DOZ Dozens', 'GGK Great gross GYD', 'GRS GrossGMS', 'KME Kilometre', 'KGS Kilograms', 'KLR Kilo litre',
                 'MTS Metric ton', 'MLT Mili litre', 'MTR Meters', 'NOS Numbers', 'PAC Packs', 'PCS Pieces', 'PRS Pairs', 'QTL Quintal', 'ROL Rolls', 'SQY Square Yards', 'SET Sets', 'SQF Square feet', 'SQM Square meters', 'TBS Tablets', 'TUB Tubes', 'TGM Ten Gross', 'THD Thousands', 'TON Tonnes', 'UNT Units', 'lons', 'YDS Yards']
    noninvunit = ttk.Combobox(hd1, values=invunitvalu)
    noninvunit.pack()
    noninvunit.place(relx=0.01, rely=0.215, relwidth=0.49, relheight=0.018)

    tk.Label(hd1, text='Category', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.2)
    noninvcategory = tk.Entry(hd1, bg='#2f516f')
    noninvcategory.place(relx=0.51, rely=0.215, relwidth=0.48, relheight=0.018)

    tk.Label(hd1, text='Description', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.24)
    Checkbutton(hd1, text="I sell this product/service to my customers. ",
                bg='#243e54', foreground='white', font=('poppins', 12)).place(relx=0.01, rely=0.255)
    
    tk.Label(hd1, text='Description', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.28)
    invdescription = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.3, relwidth=0.98, relheight=0.07)

    tk.Label(hd1, text='Sales price/rate', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.38)
    Checksalesprice = IntVar()
    invsalesprice = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.395, relwidth=0.49, relheight=0.018)
    checkcostbn=Checkbutton(hd1, text="Inclusive of tax ", variable=Checksalesprice, onvalue=1,
                offvalue=0, bg='#243e54', font=('poppins', 12)).place(relx=0.01, rely=0.415)
    
    tk.Label(hd1, text='TAX', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.38)
    invtaxvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                    '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invtax = ttk.Combobox(hd1, values=invtaxvalues)
    invtax.current(0)
    invtax.place(relx=0.51, rely=0.395, relwidth=0.48, relheight=0.018)
    
    tk.Label(hd1, text='Income account', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.43)
    incometaxvalues = ['Billable Expense Income', 'Product Sales', 'Sales', 'Sales-Hardware',
                       'Sales-Software', 'Sales-Support and Maintanance', 'Sales of Product Income', 'Uncategorised Income']
    tk.Button(hd1, text='+', font=(12), bg='#243e54', command=incomeaccount).place(relx=0.46,
                                                                     rely=0.445, relwidth=0.03, relheight=0.018)
    invincomeaccount = ttk.Combobox(hd1, values=incometaxvalues)
    invincomeaccount.current(0)
    invincomeaccount
    invincomeaccount.place(relx=0.01, rely=0.445,
                           relwidth=0.44, relheight=0.018)



    tk.Label(hd1, text='Purchasing information', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.54)
    invpurchasinginformation = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.485, relwidth=0.98, relheight=0.07)
    tk.Label(hd1, text='Purchasing information', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.56)
    Checkbutton(hd1, text="I Purchase this product/service from Supplier. ",
                bg='#243e54', foreground='white', font=('poppins', 12)).place(relx=0.01, rely=0.58)
    tk.Label(hd1, text='Abatement %', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.6)
    invpurchasinginformation = tk.Entry(hd1, bg='#243e54').place(
        relx=0.01, rely=0.62, relwidth=0.49, relheight=0.018)


    defexp = tk.Label(hd1, text='Service Type', font=(
        'poppins', 12), bg='#243e54', foreground='white').place(relx=0.51, rely=0.6)
    invassetsvalues = ['Stock Broking', 'General Insurance', 'Courier', 'Advertising Agency', 'Consulting Engineer', 'Custom House Agent', 'Steamer Agent', 'Clearing and Forwarding', 'Man power Recruiting', 'Air Travel Agent', 'Tour operator', 'Rent a Cab', 'Architect', 'Interior Director', 'Management Consultment', 'Chartered Accountant', 'Cost Accountant', 'Company Secretary', 'Real Estate Agent', 'Security Agency', 'Credit Rating Agency', 'Market Research Agency', 'Underwriter', 'Beauty Parlor', 'Cargo Handling', 'Cable Operators', 'Dry Cleaning', 'Event Management', 'Fashion Designer', 'Life insurance', 'Scientific and Technical Consultancy', 'Photograghy', 'Convention Services', 'Video Tape Production', 'Sound Recording', 'Broadcasting', 'Insurance Auxilary Service', 'Banking and Other Financial', 'Port Serrvices', 'Authorised Service Station', 'Health Club and fitness centres', 'Rail Travel Agent', 'Storage and Warehousing', 'Business Auxillary', 'Commercial Coaching', 'Erection or Installation', 'Franchise Service', 'Internet Cafe', 'Maintenance or repair', 'Techincal testing', 'Technical Inspection', 'Foreign exchange broking', 'Port', 'Airport Services', 'Air Transport', 'Business Exhibition',
                       'Goods Transport', 'Construction of commerce complex', 'Intellectual property service', 'Opinion poll service', 'Outdoor Catering', 'Television and Radio Programme Production', 'Survey and exploration of minerals', 'Pandal and shamiana', 'Travel Agent', 'Forward Contract Brokerage', 'Transport through pipeline', 'Site Preparation', 'Dredging', 'Survey and map making', 'Cleaning Service', 'Clubs and Association Service', 'Packaging Service', 'Mailing list Compilation', 'Residential Complex Construction', 'Share transfer Agent', 'Atm Manintenance', 'Recovery Agent', 'Sale of space for advertisement', 'Sponsorship', 'International Air travel', 'Containerised rail transport', 'Business Support Service', 'Action Service', 'Public Relation Management', 'Ship Management', 'Internet Telephony', 'Cruise Ship tour', 'Credit Card', 'Telecommuniction Service', 'Mining of Mi,Oil or gas', 'Renting Immovable Property', 'Works Contract', 'Development of Consent', 'Asset Management', 'Design Services', 'Information Technology Services', 'ULIP Management', 'Stock Exchange Service', 'Services for transaction in Goods', 'Clearing House Services', 'Supply of Tangible goods', 'Online Information Retrieval', 'Mandap keeper']
    invinventoryassets = ttk.Combobox(hd1, values=invassetsvalues)
    invinventoryassets.current(0)
    invinventoryassets.place(relx=0.51, rely=0.62,
                             relwidth=0.48, relheight=0.018)

    invsubmit = tk.Button(hd1, text='SUBMIT', font=14, bg='#5193e6', foreground='white',
                          ).place(relx=0.4, rely=0.69,width=250, height=40)

    hd1.place(relx=0, rely=0.1, relwidth=0.9, relheight=1.2)
    B.mainloop()


def add_bundle_product():
    def add_product26():
        L = tk.Toplevel(B)
        L.title('PRODUCT / SERVICE INFORMATION')
        L.geometry('1400x700')

    global B
    B = tk.Toplevel(A)
    B.title('PRODUCT / SERVICE INFORMATION')
    B.geometry('1400x700')
    mycanvas = tk.Canvas(B, width=1500, height=1200)
    mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    yscrollbar = ttk.Scrollbar(B, orient='vertical', command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
        scrollregion=mycanvas.bbox('all')))
    frame = tk.Frame(mycanvas)
    frame['bg'] = '#2f516f'
    mycanvas.create_window((0, 0), window=frame,
                           anchor='nw', width=1500, height=1800)
    # head frame

    head1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    f1 = font.Font(family='poppins', size=30)  # font
    lb1 = tk.Label(head1, text='PRODUCT / SERVICE INFORMATION',
                   bg='#243e54', foreground='white')
    

    lb1['font'] = f1
    lb1.place(relx=0.2, rely=0.2)
    head1.place(relx=0, rely=0.035, relwidth=1, relheight=0.05)



    # contents frame
    hd1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
    
    hd2 = tk.LabelFrame(frame, borderwidth=0, bg='#2f516f')

    f3 = font.Font(family='poppins', size=18)  # font
    hd2.place(relx=0.01, rely=0.115, relwidth=0.88, relheight=0.05)
    lb2 = tk.Label(hd2, text='BUNDLE', bg='#2f516f', foreground='white')
    producttype = Button(hd2, text="Choose Type", command=selectproducttype,
                bg="#5193e6", fg="#fff", font=('mali', 10, 'bold'))
    producttype.place(relx=0.58, rely=0.2, width=350, height=50)
    f4 = font.Font(family='poppins', size=24)  # font
    lb2['font'] = f4
    lb2.place(relx=0.35, rely=0.3)


    uploadproductimage = Button(hd1, text="UPLOAD IMAGE", command=uploadimage,
                  bg="#333333", fg="#fff", font=('mali', 10, 'bold'))
    uploadproductimage.place(relx=0.4, rely=0.08, width=250, height=50)



    tk.Label(hd1, text='Name', bg='#243e54', foreground='white',
             font=('poppins', 12)).place(relx=0.01, rely=0.16)
    noninvsku = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.175, relwidth=0.49, relheight=0.018)

    l1=tk.Label(hd1, text='SAC Code', font=('poppins', 12), bg='#243e54',
             foreground='white').place(relx=0.51, rely=0.16)
    noninvhsncode = tk.Entry(hd1, bg='#2f516f').place(
      relx=0.51, rely=0.175, relwidth=0.48, relheight=0.018)
    tk.Label(hd1, text='Description', font=('poppins', 12),
             bg='#243e54', foreground='white').place(relx=0.01, rely=0.22)
    invdescription = tk.Entry(hd1, bg='#2f516f').place(
        relx=0.01, rely=0.25, relwidth=0.98, relheight=0.07)
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")
    tk.Label(hd1, text='Products/services included in the bundle', bg='#243e54',
             foreground='white', font=('poppins', 20)).place(relx=0.3, rely=0.37)
    tk.Label(hd1, text='PRODUCT/SERVICE', bg='#243e54', foreground='white',
             font=('poppins', 13)).place(relx=0.01, rely=0.42)

    expaccountvalues = ['choose', 'laptop', 'smartphone', 'smartwatch']
    invexpaccount = ttk.Combobox(hd1, values=expaccountvalues)
    invexpaccount.current(0)
    invexpaccount.place(relx=0.01, rely=0.46, relheight=0.02, relwidth=0.13)

    etds1 = ttk.Combobox(hd1, values=expaccountvalues)
    etds1.current(0)
    etds1.place(relx=0.01, rely=0.50, relheight=0.02, relwidth=0.13)

    etds2 = ttk.Combobox(hd1, values=expaccountvalues)
    etds2.current(0)
    etds2.place(relx=0.01, rely=0.54, relheight=0.020, relwidth=0.13)

    etds3 = ttk.Combobox(hd1, values=expaccountvalues)
    etds3.current(0)
    etds3.place(relx=0.01, rely=0.58, relheight=0.020, relwidth=0.13)


# col-2

    tk.Label(hd1, text='HSN', font=('poppins', 13), bg='#243e54',
             foreground='white').place(relx=0.185, rely=0.42)

    phsncode = tk.Entry(hd1, bg='#2f516f').place(relx=0.155, rely=0.46,
                                   relwidth=0.13, relheight=0.020)
    

    phsncode1 = tk.Entry(hd1, bg='#2f516f').place(relx=0.155, rely=0.50,
                                    relwidth=0.13, relheight=0.020)

    phsncode2 = tk.Entry(hd1, bg='#2f516f').place(relx=0.155, rely=0.54,
                                    relwidth=0.13, relheight=0.020)


    phsncode3 = tk.Entry(hd1, bg='#2f516f').place(relx=0.155, rely=0.58,
                                    relwidth=0.13, relheight=0.020)
   

    tk.Label(hd1, text='DESCRIPTION', font=('poppins', 13),
             bg='#243e54', foreground='white').place(relx=0.32, rely=0.42)
    phsncode = tk.Entry(hd1, bg='#2f516f').place(relx=0.295, rely=0.46,
                                   relwidth=0.13, relheight=0.020)


    phsncode1 = tk.Entry(hd1, bg='#2f516f').place(relx=0.295, rely=0.50,
                                    relwidth=0.13, relheight=0.020)


    phsncode2 = tk.Entry(hd1, bg='#2f516f').place(relx=0.295, rely=0.54,
                                    relwidth=0.13, relheight=0.020)
   

    phsncode3 = tk.Entry(hd1, bg='#2f516f').place(relx=0.295, rely=0.58,
                                    relwidth=0.13, relheight=0.020)
   

    tk.Label(hd1, text='QTY', font=('poppins', 13), bg='#243e54',
             foreground='white').place(relx=0.45, rely=0.42)
    phsncode = tk.Entry(hd1, bg='#2f516f').place(relx=0.44, rely=0.46,
                                   relwidth=0.10, relheight=0.020)
    

    phsncode1 = tk.Entry(hd1, bg='#2f516f').place(relx=0.44, rely=0.50,
                                    relwidth=0.10, relheight=0.020)
   
    phsncode2 = tk.Entry(hd1, bg='#2f516f').place(relx=0.44, rely=0.54,
                                    relwidth=0.10, relheight=0.020)

    phsncode3 = tk.Entry(hd1, bg='#2f516f').place(relx=0.44, rely=0.58,
                                    relwidth=0.10, relheight=0.020)


    tk.Label(hd1, text='PRICE', font=('poppins', 13), bg='#243e54',
             foreground='white').place(relx=0.55, rely=0.42)
    phsncode = tk.Entry(hd1, bg='#2f516f').place(relx=0.55, rely=0.46,
                                   relwidth=0.12, relheight=0.020)

    phsncode1 = tk.Entry(hd1, bg='#2f516f').place(relx=0.55, rely=0.50,
                                    relwidth=0.12, relheight=0.020)

    phsncode2 = tk.Entry(hd1, bg='#2f516f').place(relx=0.55, rely=0.54,
                                    relwidth=0.12, relheight=0.020)

    phsncode3 = tk.Entry(hd1, bg='#2f516f').place(relx=0.55, rely=0.58,
                                    relwidth=0.12, relheight=0.020)

# col-6
    tk.Label(hd1, text='TOTAL', font=('poppins', 14), bg='#243e54',
             foreground='white').place(relx=0.70, rely=0.42)
    phsncode = tk.Entry(hd1, bg='#2f516f').place(relx=0.69, rely=0.46,
                                   relwidth=0.14, relheight=0.020)


    phsncode1 = tk.Entry(hd1, bg='#2f516f').place(relx=0.69, rely=0.50,
                                    relwidth=0.14, relheight=0.020)


    phsncode2 = tk.Entry(hd1, bg='#2f516f').place(relx=0.69, rely=0.54,
                                    relwidth=0.14, relheight=0.020)


    phsncode3 = tk.Entry(hd1, bg='#2f516f').place(relx=0.69, rely=0.58,
                                    relwidth=0.14, relheight=0.020)


# ocol-7
    tk.Label(hd1, text='TAX', font=('poppins', 13), bg='#243e54',
             foreground='white').place(relx=0.85, rely=0.42)
    expaccountvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                        '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invexpaccount = ttk.Combobox(hd1, values=expaccountvalues)
    invexpaccount.current(0)
    invexpaccount.place(relx=0.84, rely=0.46, relheight=0.020, relwidth=0.15)

    expaccountvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                        '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invexpaccount = ttk.Combobox(hd1, values=expaccountvalues)
    invexpaccount.current(0)
    invexpaccount.place(relx=0.84, rely=0.50, relheight=0.020, relwidth=0.15)

    expaccountvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                        '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invexpaccount = ttk.Combobox(hd1, values=expaccountvalues)
    invexpaccount.current(0)
    invexpaccount.place(relx=0.84, rely=0.54, relheight=0.020, relwidth=0.15)

    expaccountvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                        '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
    invexpaccount = ttk.Combobox(hd1, values=expaccountvalues)
    invexpaccount.current(0)
    invexpaccount.place(relx=0.84, rely=0.58, relheight=0.020, relwidth=0.15)
    invsubmit = tk.Button(hd1, text='SUBMIT', font=14, bg='#5193e6', foreground='white',
                          ).place(relx=0.4, rely=0.69,width=250, height=40)
    hd1.place(relx=0, rely=0.1, relwidth=0.9, relheight=1.2)

    B.mainloop()


def selectproducttype():
    P = tk.Toplevel(A)
    P.title('PRODUCT AND SERVICES')
    P.geometry('1500x1000')
    P['bg'] = '#2f516f'
    mycanvas = tk.Canvas(P, width=1500, height=1200)
    mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    yscrollbar = ttk.Scrollbar(P, orient='vertical', command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=yscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
        scrollregion=mycanvas.bbox('all')))
    frame = tk.Frame(mycanvas)
    frame['bg'] = '#2f516f'
    mycanvas.create_window((0, 0), window=frame,
                           anchor='nw', width=1500, height=1200)

    head5 = tk.LabelFrame(P, borderwidth=0, bg='#243e54')
    f5 = font.Font(family='poppins', size=30)  # font
    lb5 = tk.Label(head5, text='PRODUCT / SERVICE INFORMATION',
                   bg='#243e54', foreground='white')
    lb5['font'] = f5
    lb5.place(relx=0.25, rely=0.2)
    head5.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.1)

    head6 = tk.LabelFrame(P, borderwidth=0, bg='#243e54')
    head7 = tk.LabelFrame(head6, borderwidth=0, bg='#2f516f')
    head7.place(relx=0.05, rely=0.07, relwidth=0.4, relheight=0.4)
    size = (100, 100)

    ax7 = ImageTk.PhotoImage(Image.open('1.png').resize(size))
    sub = tk.Button(head7, text='Add item', command=add_inventory_product,
                    font=15, bg='#5193e6', foreground='white').place(relx=0.42, rely=0.79)

    tk.Label(head7, image=ax7, bg='#2f516f').place(
        relx=0.25, rely=0.2, relheight=0.5, relwidth=0.5)
    lowstock = tk.Label(head7, text='Inventory', bg='#2f516f', font=(
        'poppins', 20), foreground='white').place(relx=0.35, rely=0.1)

    head8 = tk.LabelFrame(head6, borderwidth=0, bg='#2f516f')
    head8.place(relx=0.5, rely=0.07, relwidth=0.4, relheight=0.4)
    size = (100, 100)

    ax8 = ImageTk.PhotoImage(Image.open('2.png').resize(size))
    sub = tk.Button(head8, text='Add item', command=add_non_inventoryproduct,
                    font=15, bg='#5193e6', foreground='white').place(relx=0.42, rely=0.79)

    tk.Label(head8, image=ax8, bg='#2f516f').place(
        relx=0.25, rely=0.2, relheight=0.5, relwidth=0.5)
    lowstock = tk.Label(head8, text='Non-Inventory', bg='#2f516f',
                        font=('poppins', 20), foreground='white').place(relx=0.35, rely=0.1)

    head9 = tk.LabelFrame(head6, borderwidth=0, bg='#2f516f')
    head9.place(relx=0.05, rely=0.52, relwidth=0.4, relheight=0.4)
    size = (100, 100)

    ax9 = ImageTk.PhotoImage(Image.open('3.png').resize(size))
    sub = tk.Button(head9, text='Add item', command=add_services, font=15,
                    bg='#5193e6', foreground='white').place(relx=0.42, rely=0.79)

    tk.Label(head9, image=ax9, bg='#2f516f').place(
        relx=0.25, rely=0.2, relheight=0.5, relwidth=0.5)
    lowstock = tk.Label(head9, text='Services', bg='#2f516f', font=(
        'poppins', 20), foreground='white').place(relx=0.35, rely=0.1)

    head10 = tk.LabelFrame(head6, borderwidth=0, bg='#2f516f')
    head10.place(relx=0.5, rely=0.52, relwidth=0.4, relheight=0.4)
    size = (90, 90)

    ax10 = ImageTk.PhotoImage(Image.open('4.png').resize(size))
    sub = tk.Button(head10, text='Add item', command=add_bundle_product,
                    font=15, bg='#5193e6', foreground='white').place(relx=0.42, rely=0.79)

    tk.Label(head10, image=ax10, bg='#2f516f').place(
        relx=0.25, rely=0.2, relheight=0.5, relwidth=0.5)
    lowstock = tk.Label(head10, text='Bundle', bg='#2f516f', font=(
        'poppins', 20), foreground='white').place(relx=0.35, rely=0.1)

    head6.place(relx=0.01, rely=0.2, relwidth=0.95, relheight=0.8)

    P.mainloop()


def main():

    global A, data
    A = tk.Tk()
    A.title('PRODUCT AND SERVICES')
    style = ttk.Style(A)
    style.theme_use("clam",)
    style.configure("Treeview", background="#243e54",
                    fieldbackground="#243e54", foreground="white")
    A.geometry('1400x1000')
    A['bg'] = '#2f516f'

    # head frame
    head = tk.LabelFrame(A, borderwidth=0, bg='#243e54')
    f = font.Font(family='Poppins', size=30)  # font
    lb = tk.Label(head, text='PRODUCT AND SERVICES',
                  bg='#243e54', foreground='white')
    lb['font'] = f
    lb.place(relx=0.3, rely=0.2)
    head.place(relx=0.02, rely=0.20, relwidth=0.95, relheight=0.1)

    # contents frame

    hdk = tk.Frame(A, bg='#243e54')
    hdk.place(relx=0.02, rely=0.35, relwidth=0.95, relheight=0.5)
    ff = font.Font(family='Poppins', size=15)  # font
    size = (70, 70)

    ax = ImageTk.PhotoImage(Image.open('lowstock.png').resize(size))

    tk.Label(hdk, image=ax, bg='#243e54').place(
        relx=0.2, rely=0.01, relheight=0.3, relwidth=0.15)
    lowstock = tk.Label(hdk, text='LOW STOCK : 0', bg='#243e54', font=(
        'poppins', 18), foreground='white').place(relx=0.22, rely=0.28)
    axy = ImageTk.PhotoImage(Image.open('outofstock.png').resize(size))

    tk.Label(hdk, image=axy, bg='#243e54').place(
        relx=0.5, rely=0.01, relheight=0.3, relwidth=0.15)
    outofstock = tk.Label(hdk, text='OUT OF STOCK : 0', bg='#243e54', font=(
        'poppins', 18), foreground='white').place(relx=0.51, rely=0.28)

    bt = tk.Button(hdk, text='Add products', command=selectproducttype,
                   bg='#5193e6', foreground='white')
    bt['font'] = ff
    bt.place(relx=0.85, rely=0.3)

    def psfile_image(event):
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("pubg.jpg")
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img, image=image)
        psimage.photo = image
        psimage.pack()

    def prfile_image(event):
        edit_window_img = Toplevel()
        edit_window_img.title("View Image")
        edit_window_img.geometry("700x500")
        image = Image.open("pubg2.jpg")
        resize_image = image.resize((700, 500))
        image = ImageTk.PhotoImage(resize_image)
        psimage = Label(edit_window_img, image=image)
        psimage.photo = image
        psimage.pack()

    # table view

    treevv = ttk.Treeview(hdk, height=7, columns=(
        1, 2, 3, 4, 5, 6, 7), show='headings')
    ttk.Style().configure("treeview", bgcolor="black")
    treevv.bg = '#243e54'
    treevv.heading(1, text='IMAGE')  # headings
    treevv.heading(2, text='TYPE')
    treevv.heading(3, text='NAME')
    treevv.heading(4, text='SKU')
    treevv.heading(5, text='HSN/SAC')
    treevv.heading(6, text='QUANTITY')
    treevv.heading(7, text='ACTION')

    treevv.column(1, minwidth=30, width=140, anchor=CENTER)  # coloumns
    treevv.column(2, minwidth=30, width=140, anchor=CENTER)
    treevv.column(3, minwidth=30, width=140, anchor=CENTER)
    treevv.column(4, minwidth=30, width=140, anchor=CENTER)
    treevv.column(5, minwidth=30, width=140, anchor=CENTER)
    treevv.column(6, minwidth=30, width=140, anchor=CENTER)
    treevv.bind('<Double-Button-1>', psfile_image)
    treevv.bind('<Double-Button-2>', prfile_image)

    #treevv.column(7, minwidth=30, width=120,anchor=CENTER)
    
    image = Image.open("pubg.jpg")
    resize_image = image.resize((280, 160))
    image = ImageTk.PhotoImage(resize_image)
    treevv.insert('', 'end', values=(
        'double-tap to view', 'Inventory', 'Carlo', 'M24', 'M416', '2000'))
    treevv.insert('', 'end', values=(
        'double-tap to view', 'Non inventory', 'Sara', 'AWM', 'M762', '22000'))
    treevv.photo = image
    # data=['lowstock.png','Inventory','carlo','M24','m416','2000']
    # treevv.insert('', 'end', text=data, values=(data))
    treevv.place(relx=0, rely=0.5, relwidth=1, relheight=0.6)

    def edit_product():

        selected_item = treevv.selection()[0]
        global B
        B = tk.Toplevel(A)
        B.title('Add products')
        B.title('edit products')
        B.geometry('1400x700')
        mycanvas = tk.Canvas(B, width=1500, height=1200)
        mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        yscrollbar = ttk.Scrollbar(
            B, orient='vertical', command=mycanvas.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        mycanvas.configure(yscrollcommand=yscrollbar.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(
            scrollregion=mycanvas.bbox('all')))
        frame = tk.Frame(mycanvas)
        frame['bg'] = '#2f516f'
        mycanvas.create_window((0, 0), window=frame,
                               anchor='nw', width=1500, height=1000)
        # head frame

        head1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
        f1 = font.Font(family='poppins', size=30)  # font
        lb1 = tk.Label(head1, text='PRODUCT / SERVICE INFORMATION',
                       bg='#243e54', foreground='white')

        lb1['font'] = f1
        lb1.place(relx=0.2, rely=0.2)
        head1.place(relx=0, rely=0.05, relwidth=1, relheight=0.08)

        head3 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')
        f2 = font.Font(family='poppins', size=25)  # font
        lb2 = tk.Label(head3, text='INVENTORY',
                       bg='#243e54', foreground='white')
        bu = Button(head3, text="Choose Type", command=selectproducttype,
                    bg="#5193e6", fg="#fff", font=('mali', 10, 'bold'))
        bu.place(relx=0.5, rely=0.2, width=250, height=40)

        lb2['font'] = f2
        lb2.place(relx=0.3, rely=0.2)
        head3.place(relx=0, rely=0.15, relwidth=1, relheight=0.08)

    # contents frame
        hd1 = tk.LabelFrame(frame, borderwidth=0, bg='#243e54')

        f3 = font.Font(family='poppins', size=18)  # font
        hd1.place(relx=0, rely=0.06, relwidth=1, relheight=0.1)

        uploadproductimage = Button(hd1, text="UPLOAD IMAGE", command=uploadimage,
                      bg="black", fg="#fff", font=('mali', 10, 'bold'))
        uploadproductimage.place(relx=0.8, rely=0.02, width=250, height=30)

        tk.Label(hd1, text='Name', bg='#243e54', foreground='white',
                 font=('poppins', 14)).place(relx=0.02, rely=0.05)
    # title.grid(row=3,column=2,padx=20,pady=20)
        productname = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.02, rely=0.08, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='SKU', bg='#243e54', foreground='white',
                 font=('poppins', 14)).place(relx=0.35, rely=0.05)
        sku = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.35, rely=0.08, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='HSN Code', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.68, rely=0.05)
        phsncode = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.68, rely=0.08, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Unit', font=('poppins', 14), bg='#243e54',
                 foreground='white').place(relx=0.02, rely=0.13)
        valu = ['CHOOSE', 'BAG Bags', 'BAL Bale BOU', 'BDL Bundles', 'BKL Buckles', 'BOX Box', 'BTL Bottles', 'CAN Cans', 'CTN Cartons', 'CCM Cubic centimeters', 'CBM Cubic meters', 'CMS Centimeters', 'DRM Drums', 'DOZ Dozens', 'GGK Great gross GYD', 'GRS GrossGMS', 'KME Kilometre', 'KGS Kilograms', 'KLR Kilo litre',
                'MTS Metric ton', 'MLT Mili litre', 'MTR Meters', 'NOS Numbers', 'PAC Packs', 'PCS Pieces', 'PRS Pairs', 'QTL Quintal', 'ROL Rolls', 'SQY Square Yards', 'SET Sets', 'SQF Square feet', 'SQM Square meters', 'TBS Tablets', 'TUB Tubes', 'TGM Ten Gross', 'THD Thousands', 'TON Tonnes', 'UNT Units', 'lons', 'YDS Yards']
        punit = ttk.Combobox(hd1, values=valu)
        punit.current(0)
        punit.place(relx=0.02, rely=0.16, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Category', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.35, rely=0.13)
        invcategory = tk.Entry(hd1, bg='#2f516f')
        invcategory.place(relx=0.35, rely=0.16, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Low stock alert', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.68, rely=0.13)
        invlsa = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.68, rely=0.16, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Description', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.02, rely=0.20)
        invdescription = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.02, rely=0.24, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Sales price/rate', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.35, rely=0.20)
        invsalesprice = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.35, rely=0.24, relwidth=0.3, relheight=0.035)

        web = tk.Label(hd1, text='Initial quantity on hand', font=(
            'poppins', 14), bg='#243e54', foreground='white')
        web.place(relx=0.68, rely=0.20)
        invicoh = tk.Entry(hd1, bg='#2f516f')

        invicoh.place(relx=0.68, rely=0.24, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Purchasing information', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.02, rely=0.28)
        invpurchasinginformation = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.02, rely=0.31, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Cost', font=('poppins', 14), bg='#243e54',
                 foreground='white').place(relx=0.35, rely=0.28)
        Checkbutton(frame, text="Inclusive of purchase tax ", bg='#243e54',
                    foreground='white', font=('poppins', 12)).place(relx=0.4, rely=0.55)
        invcost = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.35, rely=0.31, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='TAX', font=('poppins', 14), bg='#243e54',
                 foreground='white').place(relx=0.02, rely=0.35)
        invtaxvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                        '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
        invtax = ttk.Combobox(hd1, values=invtaxvalues)
        invtax.current(0)
        invtax.place(relx=0.02, rely=0.38, relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Purchase TAX', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.35, rely=0.35)
        purchasetaxvalues = ['CHOOSE', '28.0% GST (28%)', '28.0% IGST (28%)', '18.0% GST (18%)', '18.0% IGST (18%)', '15.0% ST (100%)', '14.5% ST (100%)', '14.00% ST (100%)', '14.0% VAT (100%).36', '12.36% ST (100%)', '12.0% GST (12%)', '12.0% IGST (12%)', '6.0% GST (6%)', '6.0% IGST (6%)',
                             '5.0% GST (5%)', '5.0% IGST (5%)', '5.0% VAT (100%)', '4.0% VAT (100%)', '3.0% GST (3%)', '3.0% IGST (3%)', '2.0% CST (100%)', '25>0.25% GST (0.25%)25', '0.25% IGST (0.25%)', '0% GST (0%)', '0% IGST (0%)', 'Exempt GST (0%)', 'Exempt IGST (0%)', 'Out of Scope(0%)']
        invpurchasetax = ttk.Combobox(hd1, values=purchasetaxvalues)
        invpurchasetax.current(0)
        invpurchasetax.place(relx=0.35, rely=0.38,
                             relwidth=0.3, relheight=0.035)

        tk.Label(hd1, text='Income account', font=('poppins', 14),
                 bg='#243e54', foreground='white').place(relx=0.68, rely=0.35)
        incometaxvalues = ['Billable Expense Income', 'Product Sales', 'Sales', 'Sales-Hardware',
                           'Sales-Software', 'Sales-Support and Maintanance', 'Sales of Product Income', 'Uncategorised Income']
        invincomeaccount = ttk.Combobox(hd1, values=incometaxvalues)
        invincomeaccount.current(0)
        invincomeaccount
        invincomeaccount.place(relx=0.68, rely=0.38,
                               relwidth=0.27, relheight=0.035)

        date = tk.Label(hd1, text='As of date', font=(
            'poppins', 14), bg='#243e54', foreground='white').place(relx=0.02, rely=0.42)
        edate = DateEntry(hd1, bg='#2f516f').place(
            relx=0.02, rely=0.45, relwidth=0.3, relheight=0.035)
        tk.Button(hd1, text='+', font=(14), command=incomeaccount).place(relx=0.955,
                                                                         rely=0.38, relwidth=0.025, relheight=0.035)

        defexp = tk.Label(hd1, text='Inventory asset account', font=(
            'poppins', 14), bg='#243e54', foreground='white').place(relx=0.35, rely=0.42)
        invassetsvalues = ['Inventory Assets']
        invinventoryassets = ttk.Combobox(hd1, values=invassetsvalues)
        invinventoryassets.current(0)
        invinventoryassets.place(relx=0.35, rely=0.45,
                                 relwidth=0.27, relheight=0.035)

        tk.Button(hd1, text='+', font=(14), command=inventoryasset).place(
            relx=0.625, rely=0.45, relwidth=0.025, relheight=0.035)

        tds = tk.Label(hd1, text='Expense account', font=(
            'poppins', 14), bg='#243e54', foreground='white').place(relx=0.68, rely=0.42)
        expaccountvalues = ['Cost of sales']
        invexpaccount = ttk.Combobox(hd1, values=expaccountvalues)
        invexpaccount.current(0)
        invexpaccount.place(relx=0.68, rely=0.45,
                            relwidth=0.27, relheight=0.035)
        tk.Button(hd1, text='+', font=(14), command=expenseaccount).place(
            relx=0.955, rely=0.45, relwidth=0.025, relheight=0.035)

        street = tk.Label(hd1, text='Reverse Charge %', bg='#243e54', foreground='white', font=(
            'poppins', 14)).place(relx=0.02, rely=0.53)
        estreet = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.02, rely=0.57, relwidth=0.63, relheight=0.035)

        city = tk.Label(hd1, text='Preferred Supplier', bg='#243e54', foreground='white', font=(
            'poppins', 14)).place(relx=0.68, rely=0.53)
        ecity = tk.Entry(hd1, bg='#2f516f').place(
            relx=0.68, rely=0.57, relwidth=0.3, relheight=0.035)

        sub = tk.Button(hd1, text='SUBMIT', font=15, bg='#5193e6',
                        foreground='white').place(relx=0.02, rely=0.65)

        hd1.place(relx=0, rely=0.3, relwidth=0.9, relheight=0.9)

        tk.Frame(frame, bg='#243e54').place(
            relx=0.02, rely=0.95, relwidth=0.90, relheight=0.8)
        B.mainloop()

    def delete():
        # Get selected item to Delete
        selected_item = treevv.selection()[0]
        treevv.delete(selected_item)

    edit_btn = ttk.Button(hdk, text="Edit", command=edit_product)
    edit_btn.place(relx=0.35, rely=0.8, relheight=0.1, relwidth=0.1)
    del_btn = ttk.Button(hdk, text="Delete", command=delete)
    del_btn.place(relx=0.5, rely=0.8, relheight=0.1, relwidth=0.1)
    A.mainloop()


main()
