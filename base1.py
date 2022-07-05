from tkinter import *
from tkinter import PhotoImage
import tkinter as tk
from tkinter.font import Font
from PIL import Image,ImageTk
from  tkinter import ttk


root = Tk()
root.title('FinsYs')
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")
# root.geometry('1700x1700')

h=Scrollbar(root, orient='horizontal')
h.pack(side=BOTTOM, fill='x')

label1 = Label(root,bg="#213b52",)
label1.place(x=0,y=0,width="1500", height="250")


h.config()
h.pack(side=BOTTOM,expand='yes',)


# Load the image
image=Image.open('logo-icon.png')

# Resize the image in the given (width, height)
img=image.resize((50, 50))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(label1, image=my_img,bg="#213b52")
label.place(x=10,y=10)

F2 = LabelFrame(label1,text="Fin sYs", font=('times new roman', 18, 'bold'), bd=0, fg="#fff", bg="#213b52")
F2.place(x=65, y=20, width=100, height=50)

# Load the image
image=Image.open('imgtog.png')
img1=image.resize((40, 40))
my_img1=ImageTk.PhotoImage(img1)
label=Label(label1, image=my_img1,bg="#213b52")
label.place(x=200,y=10)

btn = Button(label1,text='Dashboard',bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'),width=10,height=1)
btn.place(x=10,y=120)

#dropdown
OptionList = [
"Online Banking",
"Offline Banking",
"Bank Reconcilation"
]

variable = tk.StringVar(label1)
variable.set('Banking')
image=Image.open('imgtog.png')
img1=image.resize((40, 40))
my_img1=ImageTk.PhotoImage(img1)
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=120,y=120)

# 2
OptionList = [
"Sales Records",
"Invoices",
"Customers"
"Product and Services"
]
variable = tk.StringVar(label1)
variable.set('Sales')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=240,y=120)

# 3
OptionList = [
"Expenses",
"Suppliers",
]
variable = tk.StringVar(label1)
variable.set('Expenses')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=360,y=120)

# 4
OptionList = [
"Employee",
"Payslip"
]
variable = tk.StringVar(label1)
variable.set('Payroll')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=480,y=120)

# 5
OptionList = [
"Profit and loss",
"Balance sheet",
"Accounts receivables",
"Accounts payables"
]
variable = tk.StringVar(label1)
variable.set('Report')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=600,y=120)

# 6
OptionList = [
"GST",
"New..."
]
variable = tk.StringVar(label1)
variable.set('Taxes')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=720,y=120)

# 7
OptionList = [
"Chart of Accounts",
"Reconcile"
]
variable = tk.StringVar(label1)
variable.set('Accounting')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=8, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=840,y=120)

# 8
OptionList = [
"Chart of Accounts",
"Reconcile"
]
variable = tk.StringVar(label1)
variable.set('Accounting')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=25, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=960,y=120)

# 9
OptionList = [
"Chart of Accounts",
"Reconcile"
]
variable = tk.StringVar(label1)
variable.set('Accounting')
opt = tk.OptionMenu(label1, variable, *OptionList)
opt.config(width=25, bg="#213b52",fg="#fff",font=('Helvetica', 12, 'bold'))
opt.place(x=1200,y=120)


root.mainloop()