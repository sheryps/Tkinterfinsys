from logging import PlaceHolder
from tkinter import *
import tkinter.font as font
from  tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from turtle import bgcolor


def cmp_advce_details():
    
    advce_details_frame = Frame(registeration, padx=10, pady=10,bg="#fff")
    advce_details_frame.place(y=50,x=600,width=800,height=800)
    Label(advce_details_frame, text="Let's Start Building Your FinsYs", font=('Times', 30),bg="#fff").place(x=150,y=30)

    combany_name = Entry(advce_details_frame, font=('Times', 14))
    combany_name.insert(0, 'Legal Business Name')
    combany_name.place(x=30,y=100,height=50,width=700)

    your_industry=Label(advce_details_frame,text="Your Industry",background="white", foreground="black",font=14)
    your_industry.place(x=30,y=170)

    your_industry_input =ttk.Combobox(advce_details_frame)
    your_industry_input['values']=("Accounting Services" ,"Consultants, doctors, Lawyers and similar","Information Tecnology","Manufacturing","Professional Scientific and Technical Services","Restaurant/Bar and similar","Retail and Smilar","Other Finanacial Services")
    your_industry_input.place(x=30,y=200,height=50,width=700)
    your_industry_input.current(0)

    cmp_type=Label(advce_details_frame,text="Company type",background="white", foreground="black",font=14)
    cmp_type.place(x=30,y=270)

    cmp_type_input =ttk.Combobox(advce_details_frame)
    cmp_type_input['values']=("Private Limited Company" ,"Public Limited Company","Joint-Venture Company","Partnership Firm Company","One Person Company","Branch Office Company","Non Government Organization")
    cmp_type_input.place(x=30,y=300,height=50,width=700)
    cmp_type_input.current(0)

    radio=IntVar()            
    workers= Label(advce_details_frame,text = "Do you have an Accountant, Bookkeeper or Tax Pro ?",font=14,background='#fff') 
    workers.place(x=30,y=370)
    yes_input = Radiobutton(advce_details_frame, text="yes", variable=radio, value=1,font=14,background='#fff')  
    yes_input.place(x=30, y=400)
    no_input = Radiobutton(advce_details_frame, text="No", variable=radio, value=2,font=14,background='#fff')  

    no_input.place(x=130, y=400)

    paid_type=Label(advce_details_frame,text="How do you like to get paid?",background="white", foreground="black",font=14)
    paid_type.place(x=30,y=470)

    paid_type_input =ttk.Combobox(advce_details_frame)
    paid_type_input['values']=("Cash" ,"Cheque","Credit card/Debit card","Bank Transfer","Paypal/Other service")
    paid_type_input.place(x=30,y=500,height=50,width=700)
    paid_type_input.current(0)


    pre_btn = Button(advce_details_frame, width=15, text='Previous', font=('Times', 14), command=cmp_advce_details,bg='#2f516a',fg='#fff')
    pre_btn.place(x=250,y=580,height=50,width=100)
    sub_btn = Button(advce_details_frame, width=15, text='Submit', font=('Times', 14), command=cmp_advce_details,bg='#2f516a',fg='#fff')
    sub_btn.place(x=400,y=580,height=50,width=100)


def select_file():
    
    filename = askopenfilename(filetypes=(("jpg file", "*.jpg"), ("png file ",'*.png'), ("All files", "*.*"),))
    file_choose.select_clear()
    file_choose.insert(END, filename) # add this

registeration =tk.Tk()

registeration.title('fynsYs')
registeration.geometry("2000x2000")
registeration['bg']='#2f516a'
headingfont=font.Font(family='Helvitica', size=25,)
center_frame = Frame(registeration, padx=10, pady=10,bg="#fff")
center_frame.place(y=50,x=600,width=800,height=800)
Label(center_frame, text="We're Happy you're Here!", font=('Times', 30),bg="#fff").place(x=150,y=30)

combany_name = Entry(center_frame, font=('Times', 14))
combany_name.insert(0, 'Combany Name')
combany_name.place(x=30,y=100,height=50,width=700)
combany_address = Entry(center_frame, font=('Times', 14))
combany_address.place(x=30,y=170,height=50,width=700)
combany_address.insert(0, 'Combany Address')
city = Entry(center_frame, font=('Times', 14))
city.place(x=30,y=240,height=50,width=700)
city.insert(0, 'City')

state =ttk.Combobox(center_frame)
state['values']=("" ,"Andaman and Nicobar Islads","Andhra Predhesh","Arunachal Predesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Damn anad Diu","Delhi","Goa","Gujarat","Haryana","Himachal Predesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Predesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Predesh","Uttarakhand","West Bengal","Other Territory")



state.place(x=30,y=310,height=50,width=700)
state.insert(0, 'Choose')
pin = Entry(center_frame, font=('Times', 14))
pin.place(x=30,y=380,height=50,width=700)
pin.insert(0, 'Pincode')
email = Entry(center_frame, font=('Times', 14))
email.place(x=30,y=450,height=50,width=700)
email.insert(0, 'Email')

Phone = Entry(center_frame, font=('Times', 14))
Phone.place(x=30,y=520,height=50,width=700)
Phone.insert(0, 'Phone Numer')

file_choose=Entry(center_frame,font=40)
file_choose.place(x=130,y=590,height=50,width=600)
file_choose.insert(0, 'No file Selected')

reg_ch = Button(center_frame, width=15, text='Browse...', font=('Times', 14), command=select_file)
reg_ch.place(x=30,y=590,height=50,width=100)
reg_btn = Button(center_frame, width=15, text='next', font=('Times', 14), command=cmp_advce_details,bg='#2f516a',fg='#fff')
reg_btn.place(x=350,y=680,height=50,width=100)


# widgets placement






# reg_ge.grid(row=4, column=1, pady=10, padx=20)



registeration.mainloop()