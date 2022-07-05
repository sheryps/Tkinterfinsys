import tkinter as tk
import webbrowser
from tkinter import *
from tkinter import ttk, filedialog, scrolledtext, messagebox
from datetime import date
from tkcalendar import DateEntry
import datetime
import center_tk_window
import os
from tkinter.filedialog import askopenfile
from tkinter import filedialog as fd

# try:
#     from Tkinter import *
#     from ttk import *
# except ImportError:  # Python 3
#     from tkinter import *
#     from tkinter.ttk import *
    
# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="f-billing"
# )

# mycursor = mydb.cursor()

root = tk.Tk()
root.title('FinsYs Tkinter')
# icon1=PhotoImage(file='invoice.png')
# icon=icon1.subsample(1,1)

# root.iconphoto(False,icon)

width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))

def refresh_invoice():
    root.destroy()
    os.system('real.py')

def our_command():
    pass

def check(*args):
    print(f"the variable has changed to '{variable.get()}'")



tabControl = ttk.Notebook(root)
variable = StringVar(tabControl, value='United States')
variable.trace('w', check)
countries = ['Bahamas','Canada', 'Cuba', 'Dominica', 'Jamaica', 'Mexico', 'United States']
variable.set(countries[6])

tabControl.pack(expand = 1, fill ="both")

dropdown = OptionMenu(
    root,
    variable,
    *countries
)
dropdown.pack(expand=True)

root.mainloop()