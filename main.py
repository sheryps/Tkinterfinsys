
from tkinter import *

def invoicehome():
    
    import invoice
    
def customershome():
    
    import customer

window = Tk()
window.geometry('500x500')
menubar = Menu(window)
Sale = Menu(menubar, tearoff=False)
Sale.add_command(label="Invoices", command=invoicehome)
Sale.add_command(label="Customers", command=customershome)
# Sale.add_command(label="Save", command=invoice)
menubar.add_cascade(label="Sale", menu=Sale)
window.config(menu=menubar)
window.mainloop() 
