import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='finsys_tkinter',
    )
mycursor = mydb.cursor()
# mycursor.execute('CREATE TABLE invoice(invoiceid int PRIMARY KEY AUTO_INCREMENT,customername VARCHAR(255),email VARCHAR(255),invoiceno int,terms VARCHAR(255),invoicedate VARCHAR(255),duedate VARCHAR(255),bname VARCHAR(255),placosupply VARCHAR(255) ,product VARCHAR(255),hsn VARCHAR(255),description VARCHAR(255),qty int ,price VARCHAR(255),total int,tax VARCHAR(255),subtotal int,grandtotal int,product2 VARCHAR(255) ,hsn2 VARCHAR(255),description2 VARCHAR(255) ,qty2 int,price2 VARCHAR(255),total2 int,tax2 VARCHAR(255),product3 VARCHAR(255) ,hsn3 VARCHAR(255) ,description3 VARCHAR(255) ,qty3 int ,price3 VARCHAR(255),total3 int,tax3 VARCHAR(255) ,product4 VARCHAR(255),hsn4 VARCHAR(255),description4 VARCHAR(255),qty4 int,price4 VARCHAR(255) ,total4 int,tax4 VARCHAR(255),amtrecvd int,taxamount  int ,baldue VARCHAR(255) )')

mycursor.execute('CREATE TABLE customer(customerid int PRIMARY KEY AUTO_INCREMENT,title VARCHAR(255),firstname VARCHAR(255),lastname VARCHAR(255),company VARCHAR(255),location VARCHAR(255),gsttype VARCHAR(255),gstin VARCHAR(255),panno VARCHAR(255),email VARCHAR(255),website VARCHAR(255),mobile VARCHAR(255),street VARCHAR(255),city VARCHAR(255),state VARCHAR(255),pincode VARCHAR(255),country VARCHAR(255),shipstreet VARCHAR(255),shipcity VARCHAR(255),shipstate VARCHAR(255),shippincode VARCHAR(255),shipcountry VARCHAR(255))')

    
