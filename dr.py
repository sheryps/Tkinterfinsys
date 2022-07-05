import mysql.connector

mydb1=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='finsys_tkinter',
    )
mycursor = mydb1.cursor()

mycursor.execute('CREATE TABLE salesrecpts(salesrecptsid int PRIMARY KEY AUTO_INCREMENT,salename VARCHAR(255),saleemail VARCHAR(255),saleaddress VARCHAR(255),saledate VARCHAR(255),saleno VARCHAR(255),salesplace VARCHAR(255),salepay VARCHAR(255),salerefno VARCHAR(255),saledeposit VARCHAR(255),salepro VARCHAR(255),salehsn VARCHAR(255),saledescription VARCHAR(255),saleqty VARCHAR(255),saleprice VARCHAR(255),saaletotal VARCHAR(255),salesubtotal VARCHAR(255),tax VARCHAR(255),saletaxamount VARCHAR(255),salegrandtotal VARCHAR(255),category2 VARCHAR(255),categoryhsn2 VARCHAR(255),descrptin2 VARCHAR(255),catqty2 VARCHAR(255),catprice2 VARCHAR(255),cattotal2 VARCHAR(255),tax1 VARCHAR(255),category3 VARCHAR(255),categoryhsn3 VARCHAR(255),descrptin3 VARCHAR(255),catqty3 VARCHAR(255),catprice3 VARCHAR(255),cattotal3 VARCHAR(255),tax2 VARCHAR(255),category4 VARCHAR(255),categoryhsn4 VARCHAR(255),descrptin4 VARCHAR(255),catqty4 VARCHAR(255),catprice4 VARCHAR(255),cattotal4 VARCHAR(255),tax3 VARCHAR(255),offline VARCHAR(255))')