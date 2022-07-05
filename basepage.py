from ast import Lambda
from cProfile import label
from json import tool
from tkinter import *
import tkinter
from PIL import ImageTk
from tkinter import messagebox
import pymysql
from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter.font import Font
from  tkinter import ttk
from PIL import Image


#create the class
class base:
    def __init__(self,root):
        self.root=root  
        self.root.title('FinsYs')
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        self.root.geometry("%dx%d" %(width,height))
        self.root.configure(bg="#2f516f")
        self.main()
        
    def main(self):
        
        Frame_login=Frame(self.root,bg="#2f516f")
        Frame_login.place(x=0,y=0,height=700,width=1365)
        
        lab = Label(Frame_login,bg="#213b52")
        lab.place(x=0,y=0,width=1365,height=170)
        
        btn2=Button(lab,command=self.Regbase,text=" >>> ",cursor="hand2",font=("haveltica",15,'bold'),fg="white",bg="#213b52",bd=1,width=10,height=1)
        btn2.place(x=1210,y=120)
        
        
        size=(60,60)
        self.img1 = ImageTk.PhotoImage(Image.open("default11.png").resize(size))
        self.img2 = ImageTk.PhotoImage(Image.open("not.png").resize(size))
        self.img3 = ImageTk.PhotoImage(Image.open("cogwheel.png").resize(size))

        toolbar = tk.Frame(Frame_login, bd=5, relief=RAISED,bg='#213e57',height=200) 
        toolbar.pack(side=TOP, fill=X)
        
        size=(50,50)
        self.ax=ImageTk.PhotoImage(Image.open("logo-icon.png").resize(size))
        tk.Label(toolbar,image=self.ax,bg='#213e57').place(x=10,y=5)

        F2 = LabelFrame(toolbar,text="Fin sYs", font=('times new roman', 22, 'bold'), bd=0, fg="#fff", bg="#213b52")
        F2.place(x=65, y=10, width=100, height=50)
        
        
        menubtn1 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
        text="",image=self.img1,bg='#213e57')
        menubtn1.pack(side=RIGHT, padx=45, pady=0)

        menubtn2 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
        text="", image=self.img2,bg='#213e57')
        menubtn2.place(x=1040,y=0)

        menubtn3 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
        text="", image=self.img3,bg='#213e57')
        menubtn3.place(x=950,y=0)
        
        
        labl = Label(toolbar,bg="#213b52",fg="#fff",text="MAP Creations",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1110,y=5)
        
        labl = Label(toolbar,bg="#213b52",fg="#fff",text="Online",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1110,y=35)

        # drop down menubtn3
        menu = tk.Menu(menubtn3, tearoff=0)
        menubtn3.config(menu=menu,bg='#213e57')
        
        menu.insert_command(0, label='Accounts and Settings', command=lambda: print('Submit clicked'))
        menu.insert_command(1, label='Customize Form Style', command=lambda: print('Submit clicked'))
        menu.insert_command(2, label='Chart of Accounts', command=lambda: print('Submit clicked'))
        
        
        # drop down menubtn2
        menu = tk.Menu(menubtn2, tearoff=0)
        menubtn2.config(menu=menu,bg='#213e57')
        
        menu.insert_command(0, label='New Customers', command=lambda: print('Submit clicked'))
        menu.insert_command(1, label='New Orders', command=lambda: print('Submit clicked'))
        menu.insert_command(2, label='24 PDF File', command=lambda: print('Submit clicked'))
        menu.insert_command(3, label='Time Response', command=lambda: print('Submit clicked'))
        

        # drop down menubtn1
        menu = tk.Menu(menubtn1, tearoff=0)
        menubtn1.config(menu=menu,bg='#213e57')

        menu.insert_command(0, label='Profile', command=lambda: print('Submit clicked'))
        menu.insert_command(0, label='Dashboard', command=lambda: print('Submit clicked'))
        menu.insert_command(0, label='Logout', command=lambda: print('Submit clicked'))
        
        
        
        
        
        
        #icon in tkinter title
        p1 = PhotoImage(file = 'logo-icon.png')

        # Setting icon of master window
        root.iconphoto(False, p1)
        
        
        
        
        
        def calldashboard():
            import dashboard
        btn = Button(lab,text='Dashboard',bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'),width=13,height=1,command=calldashboard)
        btn.place(x=10,y=120)
        
        #dropdown
        OptionList = [
        "Online Banking",
        "Offline Banking",
        "Bank Reconcilation"
        ]
        def bank(n):
            bk=bankvariable.get()
            if bk=='Online Banking':
                import onlinebanking
            elif bk=='Offline Banking': 
                import offlinebanking  
            elif bk=='Bank Reconcilation':
                import bankrecon

        bankvariable = tk.StringVar(lab)
        bankvariable.set('Banking')

        opt = tk.OptionMenu(lab, bankvariable, *OptionList,command=bank)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=160,y=120)

        2
        OptionList = [
        "Sales Records",
        "Invoices",
        "Customers",
        "Product and Services"
        ]
        def salesrec(x):
            sal=salesvariable.get()
            if sal=='Sales Records':
                import salesrecords
            elif sal=='Invoices':
                import invoice
            elif sal== 'Customers':
                import customer
        salesvariable = tk.StringVar(lab)
        salesvariable.set('Sales')
        opt = tk.OptionMenu(lab, salesvariable, *OptionList,command=salesrec)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=310,y=120)
        
        # 3
        OptionList = [
        "Expenses",
        "Suppliers",
        ]
        def exp_supp(n):
            v=expvariable.get()
            print(v)
            if v=='Expenses':
                import expensemain
            if v=='Suppliers':
                import finsyssuppliers
        expvariable = tk.StringVar(lab)
        expvariable.set('Expenses')
        opt = tk.OptionMenu(lab, expvariable, *OptionList,command=exp_supp)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=460,y=120)

        # 4
        OptionList = [
        "Employee",
        "Payslip"
        ]
        def payment_method(p):
            pay = paymentvariable.get()
            if pay == 'Employee':
                import employee
            elif pay == 'Payslip':
                import showpayslip
        paymentvariable = tk.StringVar(lab)
        paymentvariable.set('Payroll')
        opt = tk.OptionMenu(lab, paymentvariable, *OptionList,command=payment_method)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=610,y=120)
        
        # 5
        OptionList = [
        "Profit and loss",
        "Balance sheet",
        "Accounts receivables",
        "Accounts payables"
        ]
        def reportsec(n):
            rep=reportvariable.get()
            if rep=='Profit and loss':
                import profit_loss
            elif rep=="Balance sheet":
                import balancesheet    
            elif rep=="Accounts receivables":
                import accreceivables
            elif rep=="Accounts payables":
                import accpayables     
        reportvariable = tk.StringVar(lab)
        reportvariable.set('Report')
        opt = tk.OptionMenu(lab, reportvariable, *OptionList, command=reportsec)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=760,y=120)

        # 6
        OptionList = [
        "GST",
        "New..."
        ]
        variable = tk.StringVar(lab)
        variable.set('Taxes')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=910,y=120)

        # 7
        OptionList = [
        "Chart of Accounts",
        "Reconcile"
        ]
        variable = tk.StringVar(lab)
        variable.set('Accounting')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=1060,y=120)

        
        
        
        
        
        
    def Regbase(self):
        
        
        frame_input3=Frame(self.root,bg="#2f516f")
        frame_input3.place(x=0,y=0,height=700,width=1365)
        
        lab = Label(frame_input3,bg="#213b52")
        lab.place(x=0,y=0,width=1365,height=170)
        
        
        
        btn2=Button(lab,command=self.main,text="<<",cursor="hand2",font=("Helvetica",15,'bold'),fg="white",bg="#213b52",bd=1,width=5,height=1)
        btn2.place(x=10,y=120)
        
        size=(60,60)
        self.img1 = ImageTk.PhotoImage(Image.open("default11.png").resize(size))
        self.img2 = ImageTk.PhotoImage(Image.open("not.png").resize(size))
        self.img3 = ImageTk.PhotoImage(Image.open("cogwheel.png").resize(size))

        toolbar = tk.Frame(frame_input3, bd=5, relief=RAISED,bg='#213e57',height=200) 
        toolbar.pack(side=TOP, fill=X)
        
        size=(50,50)
        self.ax=ImageTk.PhotoImage(Image.open("logo-icon.png").resize(size))
        tk.Label(toolbar,image=self.ax,bg='#213e57').place(x=10,y=5)

        F2 = LabelFrame(toolbar,text="Fin sYs", font=('times new roman', 22, 'bold'), bd=0, fg="#fff", bg="#213b52")
        F2.place(x=65, y=10, width=100, height=50)
        
        
        menubtn1 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
        text="",image=self.img1,bg='#213e57')
        menubtn1.pack(side=RIGHT, padx=45, pady=0)

        menubtn2 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
        text="", image=self.img2,bg='#213e57')
        menubtn2.place(x=1040,y=0)

        menubtn3 = tk.Menubutton(toolbar, relief=FLAT, compound= LEFT, 
        text="", image=self.img3,bg='#213e57')
        menubtn3.place(x=950,y=0)
        
        
        labl = Label(toolbar,bg="#213b52",fg="#fff",text="MAP Creations",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1110,y=5)
        
        labl = Label(toolbar,bg="#213b52",fg="#fff",text="Online",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1110,y=35)

        # drop down menubtn3
        menu = tk.Menu(menubtn3, tearoff=0)
        menubtn3.config(menu=menu,bg='#213e57')
        
        menu.insert_command(0, label='Accounts and Settings', command=lambda: print('Submit clicked'))
        menu.insert_command(1, label='Customize Form Style', command=lambda: print('Submit clicked'))
        menu.insert_command(2, label='Chart of Accounts', command=lambda: print('Submit clicked'))
        
        
        # drop down menubtn2
        menu = tk.Menu(menubtn2, tearoff=0)
        menubtn2.config(menu=menu,bg='#213e57')
        
        menu.insert_command(0, label='New Customers', command=lambda: print('Submit clicked'))
        menu.insert_command(1, label='New Orders', command=lambda: print('Submit clicked'))
        menu.insert_command(2, label='24 PDF File', command=lambda: print('Submit clicked'))
        menu.insert_command(3, label='Time Response', command=lambda: print('Submit clicked'))
        

        # drop down menubtn1
        menu = tk.Menu(menubtn1, tearoff=0)
        menubtn1.config(menu=menu,bg='#213e57')

        menu.insert_command(0, label='Profile', command=lambda: print('Submit clicked'))
        menu.insert_command(0, label='Dashboard', command=lambda: print('Submit clicked'))
        menu.insert_command(0, label='Logout', command=lambda: print('Submit clicked'))
        
        
        
        
        
        
        
        
        
        # 8
        OptionList = [
        "Chart of Accounts",
        "Reconcile"
        ]
        variable = tk.StringVar(lab)
        variable.set('My Accountant')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=90,y=120)

        # 9
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Cash Management')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=270,y=120)
        
        # 10
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Production')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=450,y=120)
        
        # 11
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Quality Management')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=630,y=120)
        
        # 12
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Project Management')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=810,y=120)
        
        # 13
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Usage Decisions')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=990,y=120)
        
        # 14
        OptionList = [
        "Cash Position",
        "Cash Flow Analyzer"
        "Check Cash Flow"
        ]
        variable = tk.StringVar(lab)
        variable.set('Accounts and Payable')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=13, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=1170,y=120)
        

        
        

root=Tk()
ob = base(root)
root.mainloop()