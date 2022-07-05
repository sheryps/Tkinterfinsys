from ast import Lambda
from cProfile import label
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
        
        # Load the image
        # image=Image.open('logo-icon.png')
        # img=image.resize((50, 50))
        # my_img1=ImageTk.PhotoImage(img)
       
        # my_img = tk.PhotoImage(file = "logo-icon.png") 
        # l2 = Label(lab,  image=my_img ,bg="#bbb")
        # l2.grid(row=0,column=0) 
        
        # my_img = ImageTk.PhotoImage(Image.open("logo-icon.png"))
        # b1=tk.Button(lab,image=my_img,bg="black",fg="white")
        # b1.grid(row=1,column=1)
        
        # my_img2 = ImageTk.PhotoImage(Image.open("logo-icon.png"))
        # bg = tk.Label(lab, image=my_img2)
        # bg.place(x=0, y=0, relwidth=0.40, relheight=0.60)
        
        # img=ImageTk.PhotoImage(Image.open("logo-icon.png"))
        # img=Label(lab,Image=img)
        # img.place(x=0,y=0)
        # size=(50,50)
        # ax=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
        # Tk.Label(lab,image=ax,bg='#243e54').place(x=0,y=0)
        
        # F3 = LabelFrame(root, font=('times new roman', 15, 'bold'), bd=0, fg="Black", bg="#243e55")
        # F3.place(x=100, y=200, width=50, height=50)
        # size=(200,200)
        # ax=ImageTk.PhotoImage(Image.open("emp.png").resize(size))
        # v=Label(root,image=ax,bg='#243e54')
        # v.place(x=10,y=10)
        # print(ax)
        
        size=(50,50)
        self.ax=ImageTk.PhotoImage(Image.open("logo-icon.png").resize(size))
       
        tk.Label(lab,image=self.ax,bg='#213e57').place(x=10,y=10)
        
        
        F2 = LabelFrame(lab,text="Fin sYs", font=('times new roman', 18, 'bold'), bd=0, fg="#fff", bg="#213b52")
        F2.place(x=65, y=20, width=100, height=50)
        
        #icon in tkinter title
        p1 = PhotoImage(file = 'logo-icon.png')

        # Setting icon of master window
        root.iconphoto(False, p1)
        
        
        # def submenu1():
        #     # gif icon for submenu1:
        #     imgvar1 = PhotoImage(file="cogwheel.png")
        
        # img12 = PhotoImage(file = "cogwheel.png")
        # size=(50,50)
        # img12=ImageTk.PhotoImage(Image.open("cogwheel.png").resize(size))
        # # Toolbar 
        # toolbar = Frame(lab, bd=1, relief=RAISED) 
        # toolbar.pack(side=BOTTOM, fill=X)
        # btn1 = Button(lab, relief=FLAT, compound= LEFT, text="",image=img12, command=submenu1)
        # btn1.pack(side=LEFT, padx=0, pady=0)
        
        OptionList = [
        "Accounts and Settings",
        "Customize Form Style",
        "Charts of Accounts"
        ]

        variable = tk.StringVar(lab)
        variable.set('Settings')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=2, bg="#213b52",bd=0,font=('Helvetica', 12, 'bold'))
        opt.place(x=750,y=20,height=50)
        
        
        size=(40,40)
        self.av=ImageTk.PhotoImage(Image.open("cogwheel.png").resize(size))
        tk.Label(lab,image=self.av,bg='#213e57').place(x=756,y=22)
        
        
        OptionList = [
        "Accounts and Settings",
        "Customize Form Style",
        "Charts of Accounts"
        ]

        variable = tk.StringVar(lab)
        variable.set('Notification')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=900,y=20)
        
        labl = Label(lab,bg="#213b52",fg="#fff",text="MAP Creations",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1050,y=20)
        
        labl = Label(lab,bg="#213b52",fg="#fff",text="Online",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1050,y=60)
        
        OptionList = [
        "Profile",
        "Dashboard",
        "Logout"
        ]

        variable = tk.StringVar(lab)
        variable.set('F')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=2, bg="#213b52",fg="#fff",font=('Helvetica', 15, 'bold'))
        opt.place(x=1245,y=20,height=65)
        
        size=(50,50)
        self.ap=ImageTk.PhotoImage(Image.open("default.png").resize(size))
        tk.Label(lab,image=self.ap,bg='#213e57').place(x=1250,y=21)
        
        
        btn = Button(lab,text='Dashboard',bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'),width=13,height=1)
        btn.place(x=10,y=120)
        
        #dropdown
        OptionList = [
        "Online Banking",
        "Offline Banking",
        "Bank Reconcilation"
        ]

        variable = tk.StringVar(lab)
        variable.set('Banking')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=160,y=120)

        2
        OptionList = [
        "Sales Records",
        "Invoices",
        "Customers"
        "Product and Services"
        ]
        variable = tk.StringVar(lab)
        variable.set('Sales')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=310,y=120)
        
        # 3
        OptionList = [
        "Expenses",
        "Suppliers",
        ]
        variable = tk.StringVar(lab)
        variable.set('Expenses')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=460,y=120)

        # 4
        OptionList = [
        "Employee",
        "Payslip"
        ]
        variable = tk.StringVar(lab)
        variable.set('Payroll')
        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=10, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=610,y=120)
        
        # 5
        OptionList = [
        "Profit and loss",
        "Balance sheet",
        "Accounts receivables",
        "Accounts payables"
        ]
        variable = tk.StringVar(lab)
        variable.set('Report')
        opt = tk.OptionMenu(lab, variable, *OptionList)
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
        
        size=(50,50)
        self.ax=ImageTk.PhotoImage(Image.open("logo-icon.png").resize(size))
       
        tk.Label(lab,image=self.ax,bg='#213e57').place(x=10,y=10)
        
        
        F2 = LabelFrame(lab,text="Fin sYs", font=('times new roman', 18, 'bold'), bd=0, fg="#fff", bg="#213b52")
        F2.place(x=65, y=20, width=100, height=50)
        
        OptionList = [
        "Accounts and Settings",
        "Customize Form Style",
        "Charts of Accounts"
        ]

        variable = tk.StringVar(lab)
        variable.set('Settings')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=750,y=20)
        
        OptionList = [
        "Accounts and Settings",
        "Customize Form Style",
        "Charts of Accounts"
        ]

        variable = tk.StringVar(lab)
        variable.set('Notification')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
        opt.place(x=900,y=20)
        
        labl = Label(lab,bg="#213b52",fg="#fff",text="MAP Creations",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1050,y=20)
        
        labl = Label(lab,bg="#213b52",fg="#fff",text="Online",font=('Helvetica', 12, 'bold'),width=13,height=1)
        labl.place(x=1050,y=60)
        
        OptionList = [
        "Profile",
        "Dashboard",
        "Logout"
        ]

        variable = tk.StringVar(lab)
        variable.set('F')

        opt = tk.OptionMenu(lab, variable, *OptionList)
        opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 15, 'bold'))
        opt.place(x=1200,y=20)
        
        
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