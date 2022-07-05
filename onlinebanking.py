import tkinter as tk
from tkinter import *
import webbrowser
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import StringVar, ttk

win=tk.Tk()
win.title('ONLINE BANKING')
win.geometry('1500x1000')
win['bg'] = '#2f516f'
mycanvas=tk.Canvas(win,width=1800,height=1200)
mycanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
yscrollbar =ttk.Scrollbar(win,orient='vertical',command=mycanvas.yview)
yscrollbar.pack(side=RIGHT,fill=Y)
mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion=mycanvas.bbox('all')))
frame=tk.Frame(mycanvas)
frame['bg']='#2f516f'
mycanvas.create_window((0,0),window=frame,anchor='nw',width=1500,height=1200)
hf1=tk.Frame(frame,bg='#243e54')
tk.Label(hf1,text='Connect Your Bank',font=('Times New Roman',30),bg='#243e54').place(relx=0.4,rely=0.1)
hf1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.1)

hf2=tk.Frame(frame,bg='#243e54')
tk.Label(hf2,text='Select Your Bank',font=('Times New Roman',20),bg='#243e54').place(relx=0.05,rely=0.05)

def bank(event):
    z=combobank.get()
    if z=='ICICI Bank':
        webbrowser.open('www.icicibank.com')
    elif z=='Bank of Baroda':
        webbrowser.open('http://www.bankofbaroda.in/')   
    elif z=='Bank of India':
        webbrowser.open('http://www.bankofindia.co.in/')      
    elif z=='Federal Bank':
        webbrowser.open('www.fednetbank.com') 
    elif z=='Allahabad Bank':
            webbrowser.open('https://indianbank.in/departments/e-allahabad-bank/#!')
    elif z=='Andhra Bank':
            webbrowser.open('https://www.unionbankofindia.co.in/english/andhrabank-financialservice.aspx')
    elif z=='Axis Bank':
        webbrowser.open('www.axisbank.com')    
    elif z=='Bank of Baharin and Kuwait':
        webbrowser.open('https://www.bbkonline.com/Pages/default.aspx')
    elif z=='Canara Bank':
        webbrowser.open('http://www.canarabank.com/')  
    elif z=='Central Bank of India':
        webbrowser.open('http://www.centralbankofindia.co.in/')
    elif z=='City Union Bank':
        webbrowser.open('http://www.cityunionbank.com/')  
    elif z=='Corporation Bank':
        webbrowser.open('https://corpnetbanking.com/')  
    elif z=='Development Credit Bank':
        webbrowser.open('http://www.dcbbank.com/')
    elif z=='Dhanlaxmi Bank':
        webbrowser.open('http://www.dhanbank.com/')
    elif z=='IDBI Bank':
        webbrowser.open('https://www.idbibank.in/index.asp')
    elif z=='Indian Overseas Bank':
        webbrowser.open('http://www.iob.in/')  
    elif z=='IndusInd Bank':
        webbrowser.open('http://www.indusind.com/')  
    elif z=='Jammu and Kashmir Bank':
        webbrowser.open('http://www.jkbank.com/')  
    elif z=='Karnataka Bank Ltd':
        webbrowser.open('http://karnatakabank.com/')  
    elif z=='Karur Vysya Bank':
        webbrowser.open('http://www.kvb.co.in/')   
    elif z=='Kotak Bank':
        webbrowser.open('https://www.kotak.com/en.html')
    elif z=='Laxmi Vilas Bank':
        webbrowser.open('http://www.lvbank.com/')
    elif z=='Oriental Bank of Commerce':
        webbrowser.open('https://www.obcindia.co.in/')
    elif z=='Punjab National Bank':
        webbrowser.open('http://www.pnbindia.in/')
    elif z=='South Indian Bank':
        webbrowser.open('www.southindianbank.com/') 
    elif z=='State Bank of India':
        webbrowser.open('https://www.onlinesbi.com/')
    elif z=='Syndicate Bank':
        webbrowser.open('http://www.syndicatebank.in/')
    elif z=='UCO Bank':
        webbrowser.open('http://www.ucobank.com/')
    elif z=='United Bank of India':
        webbrowser.open('https://www.unitedbank.co.in/')
    elif z=='Vijaya Bank':
        webbrowser.open('https://evijaya.bankofbaroda.in/')
    elif z=='Yes Bank Ltd':
        webbrowser.open('http://www.yesbank.in/')                                                                     
           

values=['select bank','Allahabad Bank','Andhra Bank','Axis Bank','Bank of Baharin and Kuwait','Bank of Baroda','Bank of India','Canara Bank',
'Central Bank of India','City Union Bank','Corporation Bank','Development Credit Bank','Dhanlaxmi Bank','Federal Bank','ICICI Bank','IDBI Bank','Indian Overseas Bank','IndusInd Bank',
'Jammu and Kashmir Bank','Karnataka Bank Ltd','Karur Vysya Bank','Kotak Bank','Laxmi Vilas Bank','Oriental Bank of Commerce','Punjab National Bank','South Indian Bank','State Bank of India',
'Syndicate Bank','UCO Bank','United Bank of India','Vijaya Bank','Yes Bank Ltd']
combobank=ttk.Combobox(hf2,values=values,font=14)
combobank.bind('<<ComboboxSelected>>',bank)
combobank.current(0) 
combobank.place(relx=0.05,rely=0.1,relwidth=0.5,relheight=0.05)

size=(270,180)
sv=Image.open('sbi1.png').resize(size)
sax=ImageTk.PhotoImage(sv,master=win)
say=tk.Label(hf2,image=sax)
say.place(relx=0.05,rely=0.18,relheight=0.25,relwidth=0.15)

asize=(180,180)
av=Image.open('axis.png').resize(asize)
aax=ImageTk.PhotoImage(av,master=win)
aay=tk.Label(hf2,image=aax)
aay.place(relx=0.23,rely=0.18,relheight=0.25,relwidth=0.15)

fasize=(200,200)
fav=Image.open('fed.png').resize(fasize)
faax=ImageTk.PhotoImage(fav,master=win)
faay=tk.Label(hf2,image=faax)
faay.place(relx=0.41,rely=0.18,relheight=0.25,relwidth=0.15)

csize=(180,180)
cav=Image.open('canara.png').resize(csize)
cax=ImageTk.PhotoImage(cav,master=win)
cay=tk.Label(hf2,image=cax)
cay.place(relx=0.05,rely=0.45,relheight=0.25,relwidth=0.15)

hsize=(170,170)
hav=Image.open('hdfc.png').resize(hsize)
hax=ImageTk.PhotoImage(hav,master=win)
hay=tk.Label(hf2,image=hax)
hay.place(relx=0.23,rely=0.45,relheight=0.25,relwidth=0.15)

ysize=(170,170)
yav=Image.open('yes.png').resize(ysize)
yax=ImageTk.PhotoImage(yav,master=win)
yay=tk.Label(hf2,image=yax)
yay.place(relx=0.41,rely=0.45,relheight=0.25,relwidth=0.15)

sosize=(170,170)
soav=Image.open('south.png').resize(sosize)
soax=ImageTk.PhotoImage(soav,master=win)
soay=tk.Label(hf2,image=soax)
soay.place(relx=0.05,rely=0.72,relheight=0.25,relwidth=0.15)

isize=(210,190)
iav=Image.open('indian.png').resize(isize)
iax=ImageTk.PhotoImage(iav,master=win)
iay=tk.Label(hf2,image=iax)
iay.place(relx=0.23,rely=0.72,relheight=0.25,relwidth=0.15)

ksize=(210,190)
kav=Image.open('kotak.png').resize(ksize)
kax=ImageTk.PhotoImage(kav,master=win)
kay=tk.Label(hf2,image=kax)
kay.place(relx=0.41,rely=0.72,relheight=0.25,relwidth=0.15)

hf2.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
win.mainloop()

