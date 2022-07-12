import tkinter as tk
from tkinter import *
from  tkinter import ttk
import tkinter.font as font
from turtle import bgcolor
from matplotlib.pyplot import xcorr
import mysql.connector
import  numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.cm as cm
import matplotlib.figure
import matplotlib.patches
from currency_converter import CurrencyConverter
import requests

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='finsystkinter1',
    )
mycursor = mydb.cursor()

class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount


def clear_frame():
   form_frame.destroy()
# $ USD","₹ INR","¥ YEN","€ EURO 
def crconvertor(event):
    if currencymenu.get()=="₹ INR":
        c=CurrencyConverter()
        valu=str(c.convert(1,'USD','INR'))
        cashposition=Label(heading_frame, text=f"Today: ₹ {valu} INR",font=('Helvitica',18),bg='#243e55',fg='white').place(x = 10, y =50,width=550)

    if currencymenu.get()=="€ EURO":
        c=CurrencyConverter()
        valu=str(c.convert(1,'USD','EUR'))    
        cashposition=Label(heading_frame,text=f"Today: € {valu} EUR",font=('Helvitica',18),bg='#243e55',fg='white').place(x = 10, y =50,width=550)

    if currencymenu.get()=="$ USD":
        c=CurrencyConverter()
        valu=str(c.convert(1,'INR','USD'))
        cashposition=Label(heading_frame,text=f"Today: $ {valu} USD",font=('Helvitica',18),bg='#243e55',fg='white').place(x =10 ,y =50,width=550)

    if currencymenu.get()=="¥ YEN": #YEN is Japanees(JPY) currency
        c=CurrencyConverter()
        valu=str(c.convert(1,'USD','JPY'))    
        cashposition=Label(heading_frame,text=f"Today: ¥ {valu} YEN",font=('Helvitica',18),bg='#243e55',fg='white').place(x = 10, y =50,width=550)

def selected(event):
    if menu.get() == 'Pie':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,260),window=form_frame,anchor="nw")
        fig = Figure(figsize=(11,6))
        ax = fig.add_subplot(111) 
        fig.set_facecolor("#243e55")
        colors = ( "#45BDEE", "#28A7EA", "#006CBB", "#034698") 
        patches, texts, autotexts =ax.pie(bala, radius=1, labels=name,autopct='%0.2f%%', shadow=True,colors = colors)
        for text in texts:
            text.set_color('white')
        for autotext in autotexts:
            autotext.set_color('black')
        chart1 = FigureCanvasTkAgg(fig,form_frame)
        chart1.get_tk_widget().pack()

    elif  menu.get() == 'Bubble':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,260),window=form_frame,anchor="nw")
        x = bala
        y = name
        fig = Figure(figsize=(11,6), dpi=100)
        ax = fig.add_subplot(111) 
        fig.set_facecolor("#243e55")
        ax.scatter(x, y,s=300,c="#6CB4EE")
        ax.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
        ax.tick_params(axis='y', colors='white')
        ax.set_facecolor("#2f516a")
        chart1 = FigureCanvasTkAgg(fig,master=form_frame)
        chart1.get_tk_widget().pack()
    elif  menu.get() == 'Doughnut':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,260),window=form_frame,anchor="nw")
        fig = matplotlib.figure.Figure(figsize=(11,6))
        colors = ( "#45BDEE", "#28A7EA", "#006CBB", "#034698") 
        ax = fig.add_subplot()
        patches, texts, autotexts=ax.pie(bala,autopct='%0.2f%%', labels=name,shadow=True,colors = colors) 
        for text in texts:
            text.set_color('white')
        for autotext in autotexts:
            autotext.set_color('white')
        ax.legend(name,loc="center left",bbox_to_anchor=(1, 0, 0, 1.9))
        fig.set_facecolor("#243e55")
        circle=matplotlib.patches.Circle( (0,0), 0.7, color='#243e55')
        ax.add_artist(circle)
        canvas = FigureCanvasTkAgg(fig, master=form_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()
    elif menu.get()=='Bar':
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,260),window=form_frame,anchor="nw")

        f = Figure(figsize=(11,6))
        ax = f.add_subplot(111)
        ax.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
        ax.tick_params(axis='y', colors='white')
        width = .3
        rects1 = ax.bar(name,bala, width)
        f.set_facecolor("#243e55")
        ax.set_facecolor("#2f516a")
        canvas = FigureCanvasTkAgg(f, master=form_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
    else :
        clear_frame()
        form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
        mycanvas.create_window((200,260),window=form_frame,anchor="nw")
        fig = Figure(figsize=(11, 6))
        fig.set_facecolor("#243e55")
        fig.add_subplot(111).plot(bala,name)
        canvas = FigureCanvasTkAgg(fig, master=form_frame)  
        canvas.draw()
        canvas.get_tk_widget().pack()
    

#query to fetch

name=[]
q1="SELECT name FROM app1_accounts"
mycursor.execute(q1)
result=mycursor.fetchall()
# print(result)
# bala=[]
for i in result:
    name=(i[0])
    # name.append(data)
    print(name)
bala=[]
q2="SELECT balance FROM app1_accounts"
mycursor.execute(q2)
r=mycursor.fetchall()
# print(result)
for i in r:
    bala=(i[0])
    # bala(d)
    print(bala)


# comment
window = tk.Tk()
window.title("finsYs")
width=window.winfo_screenwidth()
height=window.winfo_screenheight()
window.geometry("%dx%d" %(width,height))
window['bg']='#2f516a'
wrappen=ttk.LabelFrame(window)
mycanvas=Canvas(wrappen)
mycanvas.pack(side=LEFT,fill="both",expand="yes")
yscrollbar=ttk.Scrollbar(wrappen,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill='y')

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))

full_frame=Frame(mycanvas,width=2000,height=13500,bg='#2f516a')
mycanvas.create_window((0,0),window=full_frame,anchor="nw")

headingfont=font.Font(family='Arial', size=28,)
heading_frame=Frame(mycanvas,width=1200,bg='#243e55',height=200)
mycanvas.create_window((150,20),window=heading_frame,anchor="nw")
# inv_heading= Label(mycanvas, borderwidth=1, relief="raised",width=180,bg='#243e55', fg='#fff',height=13)
# inv_heading.pack(pady=20)
c=CurrencyConverter()
valu=str(c.convert(1,'INR','USD'))
cashposition=Label(heading_frame,text=f"Today: $ {valu} USD",font=('Helvitica',18),bg='#243e55',fg='white').place(x =10 ,y =50,width=550)
cash=Label(heading_frame,text="CASH POSITION",font=headingfont,bg='#243e55',fg='white').place(x = 60, y =110)                
global currencymenu
currencymenu= StringVar()
currencymenu.set("Change currency")
drop= OptionMenu(heading_frame, currencymenu,"$ USD","₹ INR","¥ YEN","€ EURO",command=crconvertor)
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))

drop.place(x=950,y=50,)
menu= StringVar()
menu.set("Bar Chart")
options=["Pie","Line","Bubble","Doughnut","Bar"]
drop= OptionMenu(heading_frame,menu,*options,command=selected )
drop.config(bg='#243e55', fg="white",font=('Arial',18))
drop['menu'].config(bg='#2f516a',fg="white",font=('Arial',18))
drop.place(x=950,y=110)
wrappen.pack(fill='both',expand='yes',)

form_frame=Frame(mycanvas,width=1450,height=13200,bg='#243e55')
mycanvas.create_window((200,260),window=form_frame,anchor="nw")

f = Figure(figsize=(11,6))
ax = f.add_subplot(111)

name=[]
q1="SELECT name FROM app1_accounts"
mycursor.execute(q1)
result=mycursor.fetchall()
print(result)
bala=[]
for i in result:
    name.append(i[0])
    # name.append(data)
    print(name)
bala=[]
q2="SELECT balance FROM app1_accounts"
mycursor.execute(q2)
r=mycursor.fetchall()
# print(result)
for i in r:
   
    bala.append(i[0])
   
width = .3
rects1 = ax.bar(name,bala, width)
ax.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
ax.tick_params(axis='y', colors='white')
f.set_facecolor("#243e55")
ax.set_facecolor("#2f516a")
canvas = FigureCanvasTkAgg(f, master=form_frame)
canvas.draw()
canvas.get_tk_widget().pack()

mycursor.close()
mydb.close()
window.mainloop()