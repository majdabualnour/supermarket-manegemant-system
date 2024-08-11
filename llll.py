import sqlite3
from datetime import date

# Function to create/connect to the database
def connect_to_db():
    conn = sqlite3.connect('supermarket.db')
    return conn

# Function to create tables
def create_tables(conn):
    c = conn.cursor()

    # Table for products data
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                date TEXT,
                product_name TEXT,
                price REAL,
                category TEXT,
                barcode TEXT,
                img TEXT,
                quantity REAL ,
                selling REAL 

                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS productstemp (
                id INTEGER PRIMARY KEY,
                date TEXT,
                product_name TEXT,
                price REAL,
                category TEXT,
                barcode TEXT,
                img TEXT,
                quantity REAL ,
                selling REAL 

                )''')
    # Table for bills
    c.execute('''CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY,
                date TEXT,
                time TEXT,
                customer_name TEXT,
                total_price REAL,
                change REAL,
                discount REAL,
                payment_method TEXT,
                credit_card_number TEXT,
                seller_name TEXT
                )''')

    # Table for bill details
    c.execute('''CREATE TABLE IF NOT EXISTS bill_details (
                id INTEGER PRIMARY KEY,
                bill_id INTEGER,
                product_barcode TEXT,
                quantity TEXT,
                price TEXT
                )''')

    # Table for sellers
    c.execute('''CREATE TABLE IF NOT EXISTS sellers (
                id INTEGER PRIMARY KEY,
                username TEXT,
                name TEXT,
                password TEXT,
                img_location TEXT
                )''')

    conn.commit()

def add_product(conn, date, product_name, price, category, barcode, img, quantity):
    c = conn.cursor()
    c.execute('''INSERT INTO productstemp (date, product_name, price, category, barcode, img, quantity , selling)
                VALUES (?, ?, ?, ?, ?, ?, ?,?)''', (date, product_name, price, category, barcode, img, quantity, 0))
    c.execute('''INSERT INTO products (date, product_name, price, category, barcode, img, quantity, selling)
                VALUES (?, ?, ?, ?, ?, ?, ?,?)''', (date, product_name, price, category, barcode, img, quantity , 0))
    conn.commit()
def modify_product_selling(conn, barcode,  quantity):
    try :
        c = conn.cursor()
        c.execute('''SELECT quantity , selling FROM products  WHERE barcode=?''', ( barcode,))
        ppp =c.fetchone()
        print(ppp)
        selling = ppp[1]+ quantity
        new_quantity = ppp[0] - quantity 
        c.execute('''UPDATE products SET selling=? ,  quantity=? WHERE barcode=?''', (selling, new_quantity, barcode))
        conn.commit()
    except:
        return 'majd'
# Function to delete product from products table
def delete_product(conn, product_name):
    c = conn.cursor()
    c.execute('''DELETE FROM products WHERE product_name=?''', (product_name,))
    conn.commit()

# Function to modify product details
def modify_product(conn, product_name, new_price, new_quantity,date):
    c = conn.cursor()
    c.execute('''UPDATE products SET date= ?, price=?, quantity=? WHERE product_name=?''', (date, new_price, new_quantity, product_name))
    conn.commit()

# Function to insert data into bills table
def add_bill(conn, date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name, products):
    c = conn.cursor()
    c.execute('''INSERT INTO bills (date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name))
  
    c.execute('''SELECT id  FROM bills WHERE date =? AND time =?  ''', (date,time))
    
    dd = c.fetchone()
    print(dd)
    
    n = products
    jjjj = n[0]
    tempnumnum = 0
    for numnum in jjjj: 
      
    
        modify_product_selling(conn ,numnum,float(n[1][tempnumnum]))
        tempnumnum += 1
    i ='%'.join(n[0])
    i1 ='%'.join(n[1])
    i2 ='%'.join(n[2])
    add_bill_detail(conn,dd[0] , i,  i1,  i2)
    conn.commit()
def getusers(conn, username , passw): 
    d = conn.cursor()
    try:
        d.execute('''SELECT password  FROM sellers WHERE username = ?''', (username,))
    except:
        return False
    


    dd = d.fetchone()
    if passw == dd:
        return username
    return 'WRONG PASSWORD'
# Function to insert data into bill details table
def add_bill_detail(conn, bill_id, product_barcode, quantity, price):
    c = conn.cursor()
    c.execute('''INSERT INTO bill_details (bill_id, product_barcode, quantity, price)
                VALUES (?, ?, ?, ?)''', (bill_id, product_barcode, quantity, price))

    conn.commit()

def get_bill_detail(conn, bill_id):
    temp = []
    c = conn.cursor()

    c.execute('''SELECT  product_barcode, quantity, price FROM bill_details WHERE bill_id=?''',(bill_id,))
    ddd =c.fetchone()
    d = str(ddd[0]).split('%')
    d1 =  str(ddd[1]).split('%')
    d2 =str(ddd[2]).split('%')
    for t in d:
        o =t.index()
        temp.append([t,d1[o],d2[o]])
    return temp
# Function to retrieve total price of bills for today
def get_total_price_of_bills_today(conn):
    c = conn.cursor()
    today = date.today()
    c.execute('''SELECT SUM(total_price) FROM bills WHERE date=?''', (today,))
    total_price = c.fetchone()[0]
    return total_price
def get_productselling(conn , bar):
    try:
        c = conn.cursor()
        today = date.today()
        c.execute('''SELECT selling FROM products WHERE barcode=?''', (bar,))
        total_price = c.fetchone()[0]
        return total_price 
    except:
        return 'NO PRODUCT'
def get_seller(conn):
    try:

        temp = []
        tempp = []
        temppp = []
        c = conn.cursor()
        for rsdd in     c.execute('''SELECT selling , barcode FROM products '''):
            tempp.append(rsdd[0])
            temppp.append(rsdd[1])
        nmaj = tempp.index(max(tempp))
    
        dfdf = temppp[nmaj]
        c.execute('''SELECT * FROM products WHERE barcode =? ''', (dfdf,))
        temp.append(c.fetchone())
        return temp
    except:
        return 'NO PRODUCT'


        
 


# Function to retrieve number of bills and customers for today
def get_number_of_bills_and_customers_today(conn):
    c = conn.cursor()
    today = date.today()
    c.execute('''SELECT COUNT(DISTINCT id), COUNT(DISTINCT customer_name) FROM bills WHERE date=?''', (today,))
    result = c.fetchone()
    num_bills = result[0]
    num_customers = result[1]
    return num_bills, num_customers
def get_products(conn):
   temp = []
   c = conn.cursor()
   today = date.today()
   for rsd in     c.execute('''SELECT * FROM products '''):
      temp.append(rsd)
   return temp
# Example usage
conn = connect_to_db()

def get_bills_and_customers_today(conn):
    temp = []
    c = conn.cursor()
    today = date.today()
    for rsd in     c.execute('''SELECT  date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name FROM bills WHERE date=?''', (today,)):
        temp.append(rsd)
    
    return
# get_bills_and_customers_today(conn)
# Adding a product
# add_product(conn, '2024-06-03', 'Apple', 1.0, 1, '123456789', 'apple.jpg', 100 )
# add_product(conn, '2024-06-03', 'Apple', 1.0, 1, '123456789', 'apple.jpg', 100)
# add_product(conn, '2024-07-06', 'Apple', 1.0, 1, '123456789', 'apple.jpg', 100)
# # Deleting a product
# delete_product(conn, 'Apple')

# # Modifying a product
# modify_product(conn, 'Apple', 1.5, 150)
def add_seller(conn, username, name,  password, img):
   c = conn.cursor()
   c.execute('''INSERT INTO sellers (username, name, password, img_location)
               VALUES (?, ?, ?, ?)''', (username, name, password, img))
   # d = conn.cursor()
   # d.execute('''SELECT id  FROM bills WHERE date AND time =? AND ? ''', (date,))
   
   # dd = d.fetchone()
   # print(dd)
   # add_bill_detail(conn,dd , products[0],  products[1],  products[2])
   conn.commit()
# Adding a bill
p = connect_to_db()
create_tables(p)
# add_seller(conn, 'majd' , 'majd', '123' , 'od')
add_product(p,'9-3-2024','صلصة_بندورة', 12 , 'منظفات','12345677','img.png',19999.8)
add_product(p,'9-3-2024','test1', 12 , 'منظفات','12345666','img.png',19999.8)
add_product(p,'9-3-2024','test2', 12 , 'منظفات','12345555','img.png',19999.8)
add_product(p,'9-3-2024','test3', 12 , 'منظفات','12344444','img.png',19999.8)

# delete_product(conn , 'صلصة_بندورة')
# # add_bill(conn, '2024-03-09', '15:08', 'Johnoehfh', 50.0, 0.0, 0.0, 'cash', '', 'seller1' ,[2,3,4])
# add_bill(conn, '2024-03-10', '10:00', 'Johnosddehfh', 50.0, 0.0, 0.0, 'cash', '', 'majd' ,[['12345698'],['87777'],['9']])

# get_products(conn)

# add_product(p,'9-3-2024','صلصة_بندورة', 12 , 'منظفات','12345678','img.png',54.8)
# # add_product(p,'9-3-2024','صلصة_بندورة', 12 , 'العاب','12345678','img.png',54.8)
# add_product(p,'9-3-2024','صلصة_بندورة', 12 , 'مجمدات','12345678','img.png',54.8)
# add_product(p,'9-3-2024','صلصة_بندورة', 12 , 'مواد_تموينية','12345678','img.png',54.8)

# add_product(p,'9-3-2024','صلصة_بندورة', 12 , 'مسليات','12345678','img.png',54.8)



# print(get_products(conn))
def get_products_sh(conn, name):
   temp = []
   c = conn.cursor()
   # today = date.today()
   for rsd in     c.execute('''SELECT * FROM products WHERE product_name = ?''' , (name,)):
      temp.append(rsd)
   return temp
# add_seller(conn, 'majd', 'majd', '123' , 'k')
# print(get_products_sh(conn, 'd'))
# Adding bill details
# add_bill_detail(conn, 1, '123456789', 2, 3.0)
# print(get_productselling(conn, '12345678'))
# print((get_seller(conn)))
# Retrieving total price of bills for today
# total_price_today = get_total_price_of_bills_today(conn)
# print("Total price of bills for today:", total_price_today)

# Retrieving number of bills and customers for today
# num_bills_today, num_customers_today = get_number_of_bills_and_customers_today(conn)
# print("Number of bills today:", num_bills_today)
# print("Number of customers today:", num_customers_today)
# print (get_total_price_of_bills_today(conn))
# get_bill_detail(conn, '1')


conn.close()

