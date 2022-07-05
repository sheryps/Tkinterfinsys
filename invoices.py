from json import load
from tkinter import *
from tkinter import ttk
import tkinter as tk
root = tk.Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))
root.configure(bg="#2f516f")

root.title("Finsys")
bg_color = "#badc57"

N = Label(root, bg="#243e55", fg="#fff",font=('times new roman', 10, 'bold'), relief=RAISED)
N.place(relx=0.1, rely=0.03, relheight=0.1, relwidth=0.8)
tit = Label(N, text="INVOICES", font=('times new roman', 28, 'bold'), pady=2, bd=12, bg="#243e55", fg="#fff", relief=GROOVE)
tit.pack(fill=X)

F = LabelFrame(root, font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#243e55")
F.place(x=5, y=140, width=1345, height=800)
b = Button(F,text = "Add Invoices",bg="#243e55",fg="#fff",font=('times new roman', 12, 'bold'))  
b.place(x=1100,y=10,width=200,height=40) 

tree = ttk.Treeview(F,height=10)
tree['show'] = 'headings'

sb = ttk.Scrollbar(F, orient="vertical", command=tree.yview)
sb.grid(row=1,column=1,sticky="NS",pady=5)

tree.configure(yscrollcommand=sb.set)

tree["columns"]=("1","2","3","4","5","6","7","8")

tree.column("1", width=165)
tree.column("2", width=165)
tree.column("3", width=165)
tree.column("4", width=165)
tree.column("5", width=165)
tree.column("6", width=165)
tree.column("7", width=165)
tree.column("8", width=145)


tree.heading("1", text="INVOICE NO")
tree.heading("2", text="INVOICE DATE")
tree.heading("3", text="CUSTOMER")
tree.heading("4", text="EMAIL ID")
tree.heading("5", text="DUE DATE")
tree.heading("6", text="GRAND TOTAL")
tree.heading("7", text="BALANCE DUE")
tree.heading("8", text="ACTION")

tree.grid(row=2,column=0,padx=5,pady=5)
data=['1','20-03-2022','John wick','johnwick@gmail.com','20-04-2022','5000000','500000','Action']
item1 = tree.insert("", "end", values=(data))
root.mainloop()