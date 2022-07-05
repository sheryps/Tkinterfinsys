from enum import auto
import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
import tkinter.messagebox
from tkinter.tix import AUTO
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from requests import get
from tkcalendar import Calendar, DateEntry
import mysql.connector as mysql
import pymysql
from tkinter.tix import AUTO

def fun():#db connection
    global mydb1,mycursor
    mydb1=mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='finsYs_tkinter'
        )
    mycursor = mydb1.cursor()




def add_Employee():
    
    
    
    fun()
    mycursor = mydb1.cursor()
    user_id=[6]
    mycursor.execute("SELECT cid FROM app1_company WHERE id_id=%s",(user_id))
    cmp1=mycursor.fetchone()
    
    global Name,Joiningdate,Employeenumber,Designation,Department,Branch,Location,Gender,Age,Mobile,Gmail,Address,Providebankdetails,Bankaccountnumber,Ifsccode,Totalrentpaid,Hrareceived,Livein,Applicabletaxregime,Pannumber,Aadhaarnumber,Universalaccountnumber,Pfaccountnumber,Epsaccountnumber,Praccountnumber,Esinumber,Esidispensaryname,Basic,Da,Othincome1,Othamount1,Othincome2,Othamount2,Othincome3,Othamount3,Othincome4,Othamount4,Othincome5,Othamount5,Provifund,Proftax,Esi,Deduc1,Deduc2,Deduc3,Deduc4,Deducamt1,Deducamt2,Deducamt3,Deducamt4,cid_id
    Name=name.get()
    Joiningdate=joiningdate.get()
    Employeenumber=employeenumber.get()
    Designation=designation.get()
    Department=department.get()
    Branch=branch.get()
    Location=location.get()
    Gender=gender.get()
    Age=age.get()
    Mobile=mobile.get()
    Gmail=gmail.get()
    Address=address.get()
    # Providebankdetails=providebankdetails.get()
    Bankaccountnumber=bankaccountnumber.get()
    Ifsccode=ifsccode.get()
    Totalrentpaid=totalrentpaid.get()
    Hrareceived=hrareceived.get()
    Livein=livein.get()
    Applicabletaxregime=applicabletaxregime.get()
    Pannumber=pannumber.get()
    Aadhaarnumber=aadhaarnumber.get()
    Universalaccountnumber=universalaccountnumber.get()
    Pfaccountnumber=pfaccountnumber.get()
    Epsaccountnumber=epsaccountnumber.get()
    Praccountnumber=praccountnumber.get()
    Esinumber=esinumber.get()
    Esidispensaryname=esidispensaryname.get()
    Basic=basic.get()
    Da=da.get()
    Othincome1=othincome1.get()
    Othamount1=othamount1.get()
    Othincome2=othincome2.get()
    Othamount2=othamount2.get()
    Othincome3=othincome3.get()
    Othamount3=othamount3.get()
    Othincome4=othincome4.get()
    Othamount4=othamount4.get()
    Othincome5=othincome5.get()
    Othamount5=othamount5.get()
    Provifund=provifund.get()
    Proftax=proftax.get()
    Esi=esi.get()
    Deduc1=deduc1.get()
    Deduc2=deduc2.get()
    Deduc3=deduc3.get()
    Deduc4=deduc4.get()
    Deducamt1=deducamt1.get()
    Deducamt2=deducamt2.get()
    Deducamt3=deducamt3.get()
    Deducamt4=deducamt4.get()
    cid_id=cmp1[0]
    
    sql="INSERT INTO app1_employee (name,joiningdate,employeenumber,designation,department,branch,location,gender,age,mobile,gmail,address,providebankdetails,bankaccountnumber,ifsccode,totalrentpaid,hrareceived,livein,applicabletaxregime,pannumber,aadhaarnumber,universalaccountnumber,pfaccountnumber,epsaccountnumber,praccountnumber,esinumber,esidispensaryname,basic,da,othincome1,othamount1,othincome2,othamount2,othincome3,othamount3,othincome4,othamount4,othincome5,othamount5,provifund,proftax,esi,deduc1,deduc2,deduc3,deduc4,deducamt1,deducamt2,deducamt3,deducamt4,cid_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
    val=(Name,Joiningdate,Employeenumber,Designation,Department,Branch,Location,Gender,Age,Mobile,Gmail,Address,providebankdetails,Bankaccountnumber,Ifsccode,Totalrentpaid,Hrareceived,Livein,Applicabletaxregime,Pannumber,Aadhaarnumber,Universalaccountnumber,Pfaccountnumber,Epsaccountnumber,Praccountnumber,Esinumber,Esidispensaryname,Basic,Da,Othincome1,Othamount1,Othincome2,Othamount2,Othincome3,Othamount3,Othincome4,Othamount4,Othincome5,Othamount5,Provifund,Proftax,Esi,Deduc1,Deduc2,Deduc3,Deduc4,Deducamt1,Deducamt2,Deducamt3,Deducamt4,cid_id)
    mycursor.execute(sql, val)
    mydb1.commit()
    mydb1.close()
    tkinter.messagebox.showinfo("ADD", "Record entered successfully")


root = tk.Tk()
var = IntVar()
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

full_frame=Frame(mycanvas,width=1345,height=2550,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

heading_frame=Frame(mycanvas)
mycanvas.create_window((0,50),window=heading_frame,anchor="nw")

form_frame=Frame(mycanvas,width=1345,height=2550,bg='#2f516f')
mycanvas.create_window((3,150),window=form_frame,anchor="nw")
form_lable=tk.Label(form_frame,bg="#2f516f",width=100)
form_lable.place(x=0,y=0)

tit = Label(heading_frame, text="ADD EMPLOYEE", font=('times new roman', 25, 'bold'),padx=527, pady=2, bd=5, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack()

global name,joiningdate,employeenumber,designation,department,branch,location,gender,age,mobile,gmail,address,providebankdetails,bankaccountnumber,ifsccode,totalrentpaid,hrareceived,livein,applicabletaxregime,pannumber,aadhaarnumber,universalaccountnumber,pfaccountnumber,epsaccountnumber,praccountnumber,esinumber,esidispensaryname,basic,da,othincome1,othamount1,othincome2,othamount2,othincome3,othamount3,othincome4,othamount4,othincome5,othamount5,provifund,proftax,esi,deduc1,deduc2,deduc3,deduc4,deducamt1,deducamt2,deducamt3,deducamt4

name=StringVar()
joiningdate=StringVar()
employeenumber=StringVar()
designation=StringVar()
department=StringVar()
branch=StringVar()
location=StringVar()
gender=StringVar()
age=StringVar()
mobile=StringVar()
gmail=StringVar()
address=StringVar()
# providebankdetails=StringVar()
bankaccountnumber=StringVar()
ifsccode=StringVar()
totalrentpaid=StringVar()
hrareceived=StringVar()
livein=StringVar()
applicabletaxregime=StringVar()
pannumber=StringVar()
aadhaarnumber=StringVar()
universalaccountnumber=StringVar()
pfaccountnumber=StringVar()
epsaccountnumber=StringVar()
praccountnumber=StringVar()
esinumber=StringVar()
esidispensaryname=StringVar()
basic=StringVar()
da=StringVar()
othincome1=StringVar()
othamount1=StringVar()
othincome2=StringVar()
othamount2=StringVar()
othincome3=StringVar()
othamount3=StringVar()
othincome4=StringVar()
othamount4=StringVar()
othincome5=StringVar()
othamount5=StringVar()
provifund=StringVar()
proftax=StringVar()
esi=StringVar()
deduc1=StringVar()
deduc2=StringVar()
deduc3=StringVar()
deduc4=StringVar()
deducamt1=StringVar()
deducamt2=StringVar()
deducamt3=StringVar()
deducamt4=StringVar()

F = LabelFrame(form_frame, font=('times new roman', 15, 'bold'),padx=50, pady=20, bd=0, fg="Black", bg="#243e55")
F.place(x=30, y=30, width=1270, height=2400)

label1=Label(F, text="Employee Information", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=450,y=-0.0)

# # Create an object of tkinter ImageTk
# img = ImageTk.PhotoImage(Image.open("emp.png"))

# # Create a Label Widget to display the text or Image
# label = Label(F, image = img,width=500,)
# label.pack()


# canvas= Canvas(F, width= 500, height= 1000,bg="#243e55",)
# canvas.pack(padx=0,pady=80)

# #Load an image in the script
# img= (Image.open("emp.png"))

# #Resize the Image using resize method
# resized_image= img.resize((500,1000), Image.ANTIALIAS)
# new_image= ImageTk.PhotoImage(resized_image)

# #Add image to the Canvas Items
# canvas.create_image(10,10, anchor=NW, image=new_image)
F2 = LabelFrame(F, font=('times new roman', 15, 'bold'), bd=0, fg="Black", bg="#243e55")
F2.place(x=0.0, y=100, width=500, height=800)
size=(400,700)
ax=ImageTk.PhotoImage(Image.open("emp.png").resize(size))
tk.Label(F2,image=ax,bg='#243e54').place(relx=-0.18,rely=-0,relheight=1,relwidth=1)

label2=Label(F, text="Name", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=90)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=name)
label2.place(x=400,y=130,height=40,width=200)

label3=Label(F, text="Joining Date", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=675,y=90)
cal2 = DateEntry(F, width= 22, font=('times new roman', 12, 'bold'),bg="#243e55",fg="#243e55", bd=5, relief=GROOVE,textvariable=joiningdate)
cal2.place(x=675,y=130,height=40,width=200)

label4=Label(F, text="Employee No", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=950,y=90)
label4=Entry(F,bg='#2f516a',fg='#fff',textvariable=employeenumber)
label4.place(x=950,y=130,height=40,width=200)

label2=Label(F, text="Designation", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=180)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=designation)
label2.place(x=400,y=220,height=40,width=200)

label3=Label(F, text="Department", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=675,y=180)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable=department)
label3.place(x=675,y=220,height=40,width=200)

label4=Label(F, text="Branch", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label4.place(x=950,y=180)
label4=Entry(F,bg='#2f516a',fg='#fff',textvariable=branch)
label4.place(x=950,y=220,height=40,width=200)

label2=Label(F, text="Location", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=270)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=location)
label2.place(x=400,y=310,height=40,width=200)

place_of_supply=Label(F,text="Gender",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
place_input=StringVar()
drop2=ttk.Combobox(F,textvariable =gender)
drop2['values']=("Female","Male","Others")
place_of_supply.place(x=675,y=270)
drop2.place(x=675,y=310,height=40,width=200)

place_of_supply1=Label(F,text="Age",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
place_input=StringVar()
drop3=ttk.Combobox(F,textvariable =age)
drop3['values']=("18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45",
                "46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73",
                "74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100")
place_of_supply1.place(x=950,y=270)
drop3.place(x=950,y=310,height=40,width=200)


label2=Label(F, text="Mobile", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=360)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=mobile)
label2.place(x=400,y=400,height=40,width=360)

label3=Label(F, text="Gmail", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=790,y=360)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable=gmail)
label3.place(x=790,y=400,height=40,width=360)

label2=Label(F, text="Address", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=450)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=address)
label2.place(x=400,y=490,height=80,width=750)

label1=Label(F, text="Bank Details", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=600)

def red():
    global providebankdetails
    Choice = label1radio.get()
    if Choice == 1:
        output = "Yes"
        
        lab2=Label(F, text="Bank Account Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
        lab2.place(x=400,y=690)
        lab=Entry(F,bg='#2f516a',fg='#fff',textvariable=bankaccountnumber)
        lab.place(x=400,y=730,height=40,width=360)

        lab3=Label(F, text="IFSC Code", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
        lab3.place(x=790,y=690)
        lab1=Entry(F,bg='#2f516a',fg='#fff',textvariable=ifsccode)
        lab1.place(x=790,y=730,height=40,width=360)
        providebankdetails="Yes"
    elif Choice == 2:
        output = "No"
        providebankdetails ="No"
    else:
        output = "Invalid"
 
#radio button
label1radio=IntVar()
label20=Label(F, text="Provide Bank Details :", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label20.place(x=400,y=660)
yes_entry=Radiobutton(F,text="Yes",variable=label1radio,value=1,font=('times new roman', 12, 'bold'),bg="#243e55",command=red)
yes_entry.place(x=600,y=660,)
No_entry=Radiobutton(F,text="No",variable=label1radio,value=2,font=('times new roman', 12, 'bold'),bg="#243e55",command=red)
No_entry.place(x=660,y=660)
print(label1radio)



label1=Label(F, text="HRA Declaration", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=670,y=790)

label2=Label(F, text="Actual Rent Paid", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=860)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=totalrentpaid)
label2.place(x=400,y=900,height=40,width=200)

label3=Label(F, text="HRA Received", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=675,y=860)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable=hrareceived)
label3.place(x=675,y=900,height=40,width=200)

CheckVar1 = IntVar()
sanitizer1_lbl=tk.Label(F,text="Do you live in metro cities? ",font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
drop1=ttk.Combobox(F,textvariable=livein)
drop1['values']=("Yes","No")
sanitizer1_lbl.place(x=950,y=860)
drop1.place(x=950,y=900,height=40,width=200)


label1=Label(F, text="Statutory Details", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=670,y=970)

label2=Label(F, text="Applicable Tax Regime", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=1030)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=applicabletaxregime)
label2.place(x=400,y=1070,height=40,width=750)

label2=Label(F, text="PAN Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=1120)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=pannumber)
label2.place(x=400,y=1160,height=40,width=360)

label3=Label(F, text="Aadhaar Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=790,y=1120)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable=aadhaarnumber)
label3.place(x=790,y=1160,height=40,width=360)

label2=Label(F, text="Universal Account Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=1210)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=universalaccountnumber)
label2.place(x=400,y=1250,height=40,width=360)

label3=Label(F, text="PF Account Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=790,y=1210)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable=pfaccountnumber)
label3.place(x=790,y=1250,height=40,width=360)

label2=Label(F, text="EPS Account Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=1310)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=epsaccountnumber)
label2.place(x=400,y=1350,height=40,width=360)

label3=Label(F, text="PR Account Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=790,y=1310)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable=praccountnumber)
label3.place(x=790,y=1350,height=40,width=360)

label2=Label(F, text="ESI Number", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label2.place(x=400,y=1410)
label2=Entry(F,bg='#2f516a',fg='#fff',textvariable=esinumber)
label2.place(x=400,y=1450,height=40,width=360)

label3=Label(F, text="ESI dispensary name", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label3.place(x=790,y=1410)
label3=Entry(F,bg='#2f516a',fg='#fff',textvariable=esidispensaryname)
label3.place(x=790,y=1450,height=40,width=360)

label1=Label(F, text="Salary Details", font=('times new roman', 20, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=480,y=1520)


# income
label1=Label(F, text="Income", font=('times new roman', 17, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=230,y=1580)

label1=Label(F, text="Earnings For Employee", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=50,y=1640)

label1=Label(F, text="Amount", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=310,y=1640)

label1=Label(F, text="Basic Salary", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=40,y=1700)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=basic)
label1.place(x=280,y=1700,height=40,width=230)

label1=Label(F, text="Dearance Allowance", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=40,y=1760)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=da)
label1.place(x=280,y=1760,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othincome1)
label1.place(x=40,y=1820,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othamount1)
label1.place(x=280,y=1820,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othincome2)
label1.place(x=40,y=1880,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othamount2)
label1.place(x=280,y=1880,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othincome3)
label1.place(x=40,y=1940,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othamount3)
label1.place(x=280,y=1940,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othincome4)
label1.place(x=40,y=2000,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othamount4)
label1.place(x=280,y=2000,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othincome5)
label1.place(x=40,y=2060,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=othamount5)
label1.place(x=280,y=2060,height=40,width=230)


# Deductions
label1=Label(F, text="Deduction", font=('times new roman', 17, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=870,y=1580)

label1=Label(F, text="Deductions For Employee", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1640)

label1=Label(F, text="Amount", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=970,y=1640)

label1=Label(F, text="Provident Fund", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1700)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=provifund)
label1.place(x=940,y=1700,height=40,width=230)

label1=Label(F, text="Profession Tax", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1760)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=proftax)
label1.place(x=940,y=1760,height=40,width=230)

label1=Label(F, text="ESI", font=('times new roman', 12, 'bold'), bd=12, bg="#243e55", fg="#fff")
label1.place(x=700,y=1820)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=esi)
label1.place(x=940,y=1820,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deduc1)
label1.place(x=700,y=1880,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deducamt1)
label1.place(x=940,y=1880,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deduc2)
label1.place(x=700,y=1940,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deducamt2)
label1.place(x=940,y=1940,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deduc3)
label1.place(x=700,y=2000,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deducamt3)
label1.place(x=940,y=2000,height=40,width=230)

label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deduc4)
label1.place(x=700,y=2060,height=40,width=230)
label1=Entry(F,bg='#2f516a',fg='#fff',textvariable=deducamt4)
label1.place(x=940,y=2060,height=40,width=230)


b1 = Button(F,text = "Submit Form",bg="#243e55",fg="#fff",font=('times new roman', 16, 'bold'),command=add_Employee)  
b1.place(x=470,y=2180,width=300,height=40)


wrappen.pack(fill='both',expand='yes',)




root.mainloop()