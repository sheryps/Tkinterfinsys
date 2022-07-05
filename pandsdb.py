import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='finsys_tkinter')
mycursor=mydb.cursor()





mycursor.execute('''CREATE TABLE Company(cid int AUTO_INCREMENT PRIMARY KEY,
                 cname varchar(100),
                 caddress varchar(100),
                 city varchar(100),
                 state varchar(100),
                 pincode varchar(100),
                 cemail varchar(100),
                 phone varchar(100),
                 cimg varchar(100),
                bname varchar(100),
                industry varchar(100),
                ctype varchar(100),
                abt varchar(100),
                paid varchar(100))''')

mycursor.execute('''CREATE TABLE inventory
                 ( invproductid INT AUTO_INCREMENT PRIMARY KEY ,
                    cid INT ,
                    product_image varchar(100),
                    Product_name varchar(100),
                    sku varchar(100),
                    hsn varchar(100),
                    unit varchar(100),
                    category varchar(100),
                    Initial_quantity_in_hand varchar(100),
                    As_of_date varchar(100),
                    Low_Stock_alert varchar(100),
                    Inventory_asset_account varchar(100),
                    prodescription varchar(100),
                    Sales_price varchar(100),   
                    Tax  varchar(100),
                    Income_Account varchar(100),
                    Purchasing_information  varchar(100),
                    cost  varchar(100),
                    Purchasetax  varchar(100),
                    Expense_account  varchar(100),
                    Reverse_charge  varchar(100),
                    Preferred_Supplier  varchar(100),
                    FOREIGN KEY (cid) REFERENCES Company (cid) ON DELETE CASCADE)

                ''')


mycursor.execute('''CREATE TABLE  noninventory
                 ( noninvproductid INT AUTO_INCREMENT PRIMARY KEY ,
                    cid INT,
                    product_image varchar(100),
                    Product_name varchar(100),
                    sku varchar(100),
                    hsn varchar(100),
                    unit varchar(100),
                    category varchar(100),
                    Initial_quantity_in_hand varchar(100),
                    As_of_date varchar(100),
                    Low_Stock_alert varchar(100),
                    Inventory_asset_account varchar(100),
                    prodescription varchar(100),
                    Sales_price varchar(100),   
                    Tax  varchar(100),
                    Income_Account varchar(100),
                    Purchasing_information  varchar(100),
                    cost  varchar(100),
                    Purchasetax  varchar(100),
                    Expense_account  varchar(100),
                    Reverse_charge  varchar(100),
                    Preferred_Supplier  varchar(100),
                    FOREIGN KEY (cid) REFERENCES Company (cid) ON DELETE CASCADE)

                ''')


mycursor.execute('''CREATE TABLE service
                 ( serviceid INT AUTO_INCREMENT PRIMARY KEY ,
                    cid INT ,
                    product_image varchar(100),
                    Product_name varchar(100),
                    sku varchar(100),
                    sac varchar(100),
                    unit varchar(100),
                    category varchar(100),
                    prodescription varchar(100),
                    Sales_price varchar(100),   
                    Income_Account varchar(100),
                    Tax  varchar(100),
                    abatement varchar(100),
                    sertype varchar(100),
                    purchasedescr  varchar(100),
                    cost  varchar(100),
                    expenseaccount varchar(100),
                    Purchasetax  varchar(100),
                    Reverse_charge  varchar(100),
                    Preferred_Supplier  varchar(100),
                    FOREIGN KEY (cid) REFERENCES Company (cid) ON DELETE CASCADE)

                ''')


mycursor.execute('''CREATE TABLE  bundle
                 ( bundleid INT AUTO_INCREMENT PRIMARY KEY ,
                    cid INT,
                    product_image varchar(100),
                    Product_name varchar(100),
                    sku varchar(100),
                    prodescription varchar(100),
                    product1 varchar(100),
                    product2 varchar(100),
                    product3 varchar(100),
                    product4 varchar(100),
                    hsn1 varchar(100),
                    hsn2 varchar(100),
                    hsn3 varchar(100),
                    hsn4 varchar(100),
                    description1 varchar(100),
                    description2 varchar(100),
                    description3 varchar(100),
                    description4 varchar(100),
                    qty1 varchar(100),
                    qty2 varchar(100),
                    qty3 varchar(100),
                    qty4 varchar(100),
                    price1 varchar(100),
                    price2 varchar(100),
                    price3 varchar(100),
                    price4 varchar(100),
                    total1 varchar(100),
                    total2 varchar(100),
                    total3 varchar(100),
                    total4 varchar(100),
                    tax1 varchar(100),
                    tax2 varchar(100),
                    tax3 varchar(100),
                    tax4 varchar(100),
                    grandtotal varchar(100),
                    FOREIGN KEY (cid) REFERENCES Company (cid) ON DELETE CASCADE)

                ''')


mycursor.execute('''CREATE TABLE  ProductModel
                 ( Pid INT AUTO_INCREMENT PRIMARY KEY ,
                   Pname varchar(100))''')

mycursor.execute('''CREATE TABLE  ItemModel
                 ( Itemid INT AUTO_INCREMENT PRIMARY KEY ,
                   Itemname varchar(100),
                   Pid int,
                   FOREIGN KEY (Pid) REFERENCES ProductModel (Pid) ON DELETE CASCADE)''')

mycursor.execute('''CREATE TABLE accountype
                 (
                    accountypeid INT AUTO_INCREMENT PRIMARY KEY ,
                    cid int,
                    accountname varchar(100),
                    accountbal varchar(100),
                    FOREIGN KEY (cid) REFERENCES Company (cid) ON DELETE CASCADE)

                ''')

mycursor.execute('''CREATE TABLE accounts
    (accountsid INT AUTO_INCREMENT PRIMARY KEY ,
     cid int,
    proid int,
    pid int,
    acctype varchar(100)
    detype varchar(100)
    name varchar(100)
    description varchar(100)
    gst varchar(100)
    deftaxcode varchar(100)
    FOREIGN KEY (cid) REFERENCES Company (cid) ON DELETE CASCADE,
    FOREIGN KEY (proid) REFERENCES accountype (proid) ON DELETE CASCADE,
    FOREIGN KEY (Pid) REFERENCES ProductModel (Pid) ON DELETE CASCADE,)''')

mycursor.execute('''CREATE TABLE accounts1
    (accounts1id INT AUTO_INCREMENT PRIMARY KEY ,
     cid int,
     acctype varchar(100),
     detype varchar(100),
    name varchar(100),
    description varchar(100),
    gst varchar(100),
    deftaxcode varchar(100),
    FOREIGN KEY (cid) REFERENCES Company (cid) ON DELETE CASCADE,
    FOREIGN KEY (proid) REFERENCES accountype (proid) ON DELETE CASCADE,
    FOREIGN KEY (Pid) REFERENCES ProductModel (Pid) ON DELETE CASCADE,)''')

















