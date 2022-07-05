
# from tkinter import *
# import tkinter as tk
# from tkinter import *
# from  tkinter import ttk
# import tkinter.font as font
# from tkinter import messagebox as MessageBox
# import tkinter.messagebox
# from PIL import Image,ImageTk
# from tkinter.ttk import Combobox
# from requests import get
# from tkcalendar import Calendar, DateEntry
# import mysql.connector as mysql
# import pymysql

# def bankrecon():
    
#     import bankrecon
    

# window = Tk()
# window.geometry('320x150')
# menubar = Menu(window)
# Sale = Menu(menubar, tearoff=False)
# Sale.add_command(label="Online Banking")
# Sale.add_command(label="Offline Banking")
# Sale.add_command(label="Bank Reconcilation", command=bankrecon)
# menubar.add_cascade(label="Banking", menu=Sale)

# def salesrecords():
    
#     import salesrecords
    

# Sale = Menu(menubar, tearoff=False)
# Sale.add_command(label="Sales Records",command=salesrecords)
# Sale.add_command(label="Invoices")
# Sale.add_command(label="Customers")
# Sale.add_command(label="Product and Services")
# menubar.add_cascade(label="Sales", menu=Sale)
# window.config(menu=menubar)
# window.mainloop() 








from tkinter import *
import tkinter
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#create the class
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login and registration system for Apps")
        self.root.geometry("1365x700+0+0")
        self.root.resizable(False,False)
        self.loginform()
        
    def loginform(self):
        
        Frame_login=Frame(self.root,bg="#213e57")
        Frame_login.place(x=0,y=0,height=700,width=675)
        
        label10=Label(Frame_login,text="New here ?",font=('times new roman',25,'bold'),fg="white",bg="#213e57")
        label10.place(x=330,y=40)
        
        label11=Label(Frame_login,text="Join here to start a business with FinsYs!",font=('times new roman',10,'bold'),fg="white",bg="#213e57")
        label11.place(x=290,y=90)
        
        btn2=Button(Frame_login,command=self.Register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=330,y=120)
        # self.img=ImageTk.PhotoImage(Image.open("log.svg").resize(size))
        # self.img=Label(Frame_login,Image=self.img).place(relx=0.00,rely=-0,relheight=1,relwidth=1)
        # size=(500,700)
        # ax=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
        # Tk.Label(Frame_login,image=ax,bg='#243e54').place(relx=0.00,rely=-0,relheight=1,relwidth=1)
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=675,y=0,height=700,width=800)
        
        # self.img=ImageTk.PhotoImage(file="background2.jpg")
        # img=Label(Frame_login,image=self.img).place(x=0,y=0,width950,height=700)
        
        frame_input=Frame(self.root,bg="white")
        frame_input.place(x=860,y=100,height=400,width=300)
        
        label1=Label(frame_input,text="Sign in",font=('impact',32,'bold'),fg="orangered",bg="white")
        label1.place(x=75,y=20)
        
        label2=Label(frame_input,text="Username",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
        label2.place(x=30,y=95)
        
        self.email_txt=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
        self.email_txt.place(x=30,y=145,width=270,height=35)
        
        label3=Label(frame_input,text="Password",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
        label3.place(x=30,y=190)
        
        self.password=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
        self.password.place(x=30,y=240,width=270,height=35)
        
        btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
        btn1.place(x=125,y=300)
        
        btn2=Button(frame_input,text="Login",command=self.login,cursor='hand2',font=('times new roman',15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=80,y=330)
        
        btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
        btn3.place(x=110,y=380)
        
    def login(self):
        if self.email_text.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',database="finsys_tkinter")
                cur=con.cursor()
                cur.execute('select * from register where emailid =%s and password =%s',(self.email_txt.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username and password',parent=self.root)
                else:
                    self.appscreen()
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f'Error Due to : {str(es)}',parent=self.root)
                
                
    def Register(self):
        
        Frame_login1=Frame(self.root,bg="white")
        Frame_login1.place(x=0,y=0,height=700,width=1365)
        
        frame_input2=Frame(self.root,bg="white")
        frame_input2.place(x=100,y=0,height=700,width=680)
        
        label1=Label(frame_input2,text="Sign up",font=('impact',32,'bold'),fg="orangered",bg="white")
        label1.place(x=45,y=50)
        
        label2=Label(frame_input2,text="Firstname",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label2.place(x=0,y=150)
        
        self.entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry.place(x=0,y=190,width=200,height=35)
        
        label6=Label(frame_input2,text="Lastname",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label6.place(x=300,y=150)
        
        self.entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry.place(x=300,y=190,width=200,height=35)
        
        label3=Label(frame_input2,text="Password",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label3.place(x=0,y=350)
        
        self.entry3=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry3.place(x=0,y=390,width=200,height=35)
        
        label4=Label(frame_input2,text="Email",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label4.place(x=0,y=250)
        
        self.entry2=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry2.place(x=0,y=290,width=200,height=35)
        
        label7=Label(frame_input2,text="Username",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label7.place(x=300,y=250)
        
        self.entry5=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry5.place(x=300,y=290,width=200,height=35)
        
        
        label5=Label(frame_input2,text="Confirm Password",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label5.place(x=300,y=350)
        
        self.entry4=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry4.place(x=300,y=390,width=200,height=35)

        btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=30,height=1)
        btn2.place(x=80,y=460)
        
        btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg="white",fg="black",bd=0)
        btn3.place(x=170,y=500)
        
        
        frame_input3=Frame(self.root,bg="#213e57")
        frame_input3.place(x=680,y=0,height=700,width=680)
        
        label15=Label(frame_input3,text="One of us ?",font=('times new roman',20,'bold'),fg="#fff",bg="#213e57")
        label15.place(x=400,y=120)
        
        label16=Label(frame_input3,text="click here for work with FinsYs.",font=('Goudy old style',14,'bold'),fg="#fff",bg="#213e57")
        label16.place(x=350,y=160)
        
        btn2=Button(frame_input3,command=self.loginform,text="SIGN IN",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=400,y=200)
        
    def register(self):
        if self.entry.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" or self.entry4.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.entry2.get()!=self.entry4.get():
            messagebox.showerror("Error","password and Confirm Password Should Be Same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="finsys_tkinter")
                cur=con.cursor()
                cur.execute("select * from register where emailid=%s",self.entry3.get()) 
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
                else:
                    cur.execute("insert into register values(%s,%s,%s,%s"),(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get())
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successfull",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
                
    def appscreen(self):
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1000)
        label1=Label(Frame_login,text="Hi! Welcome To Seek coding", font=("times new roman",32,'bold'),fg="black",bg="white")
        label1.place(x=375,y=100)
        
        btn2=Button(Frame_login,command=self.loginform,text="Logout",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=700,y=20)                                 
        
        

root=Tk()
ob = Login(root)
root.mainloop()










from tkinter import *
import tkinter
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#create the class
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login and registration system for Apps")
        self.root.geometry("1365x700+0+0")
        self.root.resizable(False,False)
        self.loginform()
        
    def loginform(self):
        
        Frame_login=Frame(self.root,bg="#213e57")
        Frame_login.place(x=0,y=0,height=700,width=675)
        
        label10=Label(Frame_login,text="New here ?",font=('times new roman',25,'bold'),fg="white",bg="#213e57")
        label10.place(x=330,y=40)
        
        label11=Label(Frame_login,text="Join here to start a business with FinsYs!",font=('times new roman',10,'bold'),fg="white",bg="#213e57")
        label11.place(x=290,y=90)
        
        btn2=Button(Frame_login,command=self.Register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=330,y=120)
        # self.img=ImageTk.PhotoImage(Image.open("log.svg").resize(size))
        # self.img=Label(Frame_login,Image=self.img).place(relx=0.00,rely=-0,relheight=1,relwidth=1)
        # size=(500,700)
        # ax=ImageTk.PhotoImage(Image.open('bank-building-on-the-background-of-the-city-white-car-near-the-bank-free-vector.jpg').resize(size))
        # Tk.Label(Frame_login,image=ax,bg='#243e54').place(relx=0.00,rely=-0,relheight=1,relwidth=1)
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=675,y=0,height=700,width=800)
        
        # self.img=ImageTk.PhotoImage(file="background2.jpg")
        # img=Label(Frame_login,image=self.img).place(x=0,y=0,width950,height=700)
        
        frame_input=Frame(self.root,bg="white")
        frame_input.place(x=860,y=100,height=400,width=300)
        
        label1=Label(frame_input,text="Sign in",font=('impact',32,'bold'),fg="orangered",bg="white")
        label1.place(x=75,y=20)
        
        label2=Label(frame_input,text="Username",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
        label2.place(x=30,y=95)
        
        self.email_txt=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
        self.email_txt.place(x=30,y=145,width=270,height=35)
        
        label3=Label(frame_input,text="Password",font=('Goudy old style',20,'bold'),fg="orangered",bg="white")
        label3.place(x=30,y=190)
        
        self.password=Entry(frame_input,font=('times new roman',15,'bold'),bg="lightgray")
        self.password.place(x=30,y=240,width=270,height=35)
        
        btn1=Button(frame_input,text="forgot password?",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
        btn1.place(x=125,y=300)
        
        btn2=Button(frame_input,text="Login",command=self.login,cursor='hand2',font=('times new roman',15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=80,y=330)
        
        btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor='hand2',font=('calibri',10),bg="white",fg="black",bd=0)
        btn3.place(x=110,y=380)
        
    def login(self):
        if self.email_text.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',database="finsys_tkinter")
                cur=con.cursor()
                cur.execute('select * from register where emailid =%s and password =%s',(self.email_txt.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username and password',parent=self.root)
                else:
                    self.appscreen()
                    con.close()
            except Exception as es:
                messagebox.showerror("Error",f'Error Due to : {str(es)}',parent=self.root)
                
                
    def Register(self):
        
        Frame_login1=Frame(self.root,bg="white")
        Frame_login1.place(x=0,y=0,height=700,width=1365)
        
        frame_input2=Frame(self.root,bg="white")
        frame_input2.place(x=100,y=0,height=700,width=680)
        
        label1=Label(frame_input2,text="Sign up",font=('impact',32,'bold'),fg="orangered",bg="white")
        label1.place(x=45,y=50)
        
        label2=Label(frame_input2,text="Firstname",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label2.place(x=0,y=150)
        
        self.entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry.place(x=0,y=190,width=200,height=35)
        
        label6=Label(frame_input2,text="Lastname",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label6.place(x=300,y=150)
        
        self.entry=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry.place(x=300,y=190,width=200,height=35)
        
        label3=Label(frame_input2,text="Password",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label3.place(x=0,y=350)
        
        self.entry3=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry3.place(x=0,y=390,width=200,height=35)
        
        label4=Label(frame_input2,text="Email",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label4.place(x=0,y=250)
        
        self.entry2=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry2.place(x=0,y=290,width=200,height=35)
        
        label7=Label(frame_input2,text="Username",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label7.place(x=300,y=250)
        
        self.entry5=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry5.place(x=300,y=290,width=200,height=35)
        
        
        label5=Label(frame_input2,text="Confirm Password",font=('Goudy old style',15,'bold'),fg="orangered",bg="white")
        label5.place(x=300,y=350)
        
        self.entry4=Entry(frame_input2,font=('times new roman',12,'bold'),bg="lightgray")
        self.entry4.place(x=300,y=390,width=200,height=35)

        btn2=Button(frame_input2,command=self.register,text="Register",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=30,height=1)
        btn2.place(x=80,y=460)
        
        btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg="white",fg="black",bd=0)
        btn3.place(x=170,y=500)
        
        
        frame_input3=Frame(self.root,bg="#213e57")
        frame_input3.place(x=680,y=0,height=700,width=680)
        
        label15=Label(frame_input3,text="One of us ?",font=('times new roman',20,'bold'),fg="#fff",bg="#213e57")
        label15.place(x=400,y=120)
        
        label16=Label(frame_input3,text="click here for work with FinsYs.",font=('Goudy old style',14,'bold'),fg="#fff",bg="#213e57")
        label16.place(x=350,y=160)
        
        btn2=Button(frame_input3,command=self.loginform,text="SIGN IN",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=400,y=200)
        
    def register(self):
        if self.entry.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" or self.entry4.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.entry2.get()!=self.entry4.get():
            messagebox.showerror("Error","password and Confirm Password Should Be Same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="finsys_tkinter")
                cur=con.cursor()
                cur.execute("select * from register where emailid=%s",self.entry3.get()) 
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
                else:
                    cur.execute("insert into register values(%s,%s,%s,%s"),(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get())
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successfull",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
                
    def appscreen(self):
        
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1000)
        label1=Label(Frame_login,text="Hi! Welcome To Seek coding", font=("times new roman",32,'bold'),fg="black",bg="white")
        label1.place(x=375,y=100)
        
        btn2=Button(Frame_login,command=self.loginform,text="Logout",cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=700,y=20)                                 
        
        

root=Tk()
ob = Login(root)
root.mainloop()