from flask import Flask, redirect, url_for, request,render_template , session ,jsonify
# from firebase_admin import firestore
# from flask_jwt_extended import jwt_required
import sqlite3


# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# from firebase_admin import auth
import datetime

# from firebase_admin import storage
# Load the service account key from the JSON data
# service_account_key_data = '''
# {
#   "type": "service_account",
#   "project_id": "magictech-a68b3",
#   "private_key_id": "c8ad41ef83968dc5b01802fa04a41c56b7d894eb",
#   "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDGASAuK8nnftzx\\n66isqy11oGuv57FDWRQ7vzZrjw406SDJb2EvPec1wV3JviQJvW7piY4182IzQwpJ\\noY1r1U47d4slwhmQDyi42UCHzPQPJyj/+NmcUeUZ08LIL/gVTzOyfQhse2Lqk8EB\\nNEG6ktBcXZd1P4eJXqJKuH7nGY/wBnJSUMrISv7e4PeiB89H4A9pqEQVpKp9n0Lr\\nZEfaCtERxBHe9XKVsq3GaceyQDa8SJy+r/a8PUVqI+3XMxDGj3h/tXLFOZR6lKuM\\njRjOL8NB6eGsbb0KyRfIzpKyk5iJgvF85wDJOLdTQvcmXTbOr/vd105C8GvHAOdH\\nKB/UTimVAgMBAAECggEAXXVLkK93ee6N8BxI/dNAPkyNd7ZXG5BQthC/aY5Y6M1+\\n/cU2LHu+Bcfy8lXuobBJyS51su5hlAuZL/7yhwrkBbqbsaNHuJEHKhTVWiP5sKtN\\ntWBqqleXWRT0U9Qcd0Zugtl0X+vvWQSLrXtSaPOCKI6+fgeR/FtwI++oaoFMyMAV\\no9490jVUJyJdEx1VpYtXbEIhl9H3G2alZeVDHxOk2JQI0+Q2ZJyz7djIwTET+qp2\\n7p3SBWzIf0ZhrlWjR1n6vgX+7AuyaGZYZO/mNXXHRFC0TZzePcAvLBv3HijMayiq\\nw2wSAJlAbEo0ps98UIV0VJ6OQUtlMFUDenC7/V8CowKBgQDlVWPpexspNRrT+fu1\\nsGhoV+bLXnbBn3k6NXvSaEc72GMysGKCRbsnUKQG+FwKnv8X5F1FHz0LM03Py/tB\\nefjg43+MgDQj20E6jFOAgr2ptI//uPAvFZ06gfMefDRTVvM9ag2bFf47QD7BIXAW\\n1E0k1W6JrjK5+WT+1dgZwNwVUwKBgQDdBye7Y/GxUfrWhIlXAvuXETaWh5J8ewGe\\nMkJXn7Jcj9lp/AuvRz9eBRVB/Y9V44KRRz48HpXTa3ergkRjWGmJs+GtTG1X3D38\\n8U89NUVQN6BUXJeHhbNqJCSn48N9ZAI2YCnMJjGqpnYj+lLlT4zg0pFWRQ5YvsXf\\nQLHNl7bAdwKBgHdGCvmyujSbVwGqgTxErHigRvu8fJ1FOMKKcITFEU9Rwn3peMJy\\nS90ttrGdWBl6Cgg+EDhT/+akXzLUzy+FpWgpSfwj7Xo8nVc7Bm7PEJ+DtmT0pY6H\\nekeksHJJfNlfXpCxaLQhIyFjz3+YyXhGIH0ouB3JSL6qs9lKFOOIB67bAoGALZZF\\nNpwlhGohL0+EuCKQW5ccSC3MI8qHCebZ0hLJCdhNglOO4WbzhePMf6DZiGB1VJt6\\nFZJFWqbGtuQWUNsyYUltmX2y67UsP9hRfJFZK3NdqSizxCrqV1D/EnWio2EWJ7rr\\nxAR4p/bPVRpTMKKYruIfQcjabaljTGmegoXxFn8CgYBzDrC/keoC5wurNkzede5p\\nxa+7+k9sl9YWyib4yUwkf5/M4xNvIjtZCq+4XffBaEzAT+dzmlOizVk3ltuQzK/g\\neElUELYEfrl6yKrNKqW1JXg/C2fmxjh25Vks5xyEqMrtNyTDscljFRhspBLI3gNt\\n5ic8f/93iyV3Fv8EwQFnaw==\\n-----END PRIVATE KEY-----\\n",
#   "client_email": "firebase-adminsdk-9exhf@magictech-a68b3.iam.gserviceaccount.com",
#   "client_id": "101015886303015615111",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9exhf%40magictech-a68b3.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }
# '''

# Parse the JSON data
# service_account_key = json.loads(service_account_key_data)
# cred = credentials.Certificate(service_account_key)

# appd = firebase_admin.initialize_app(cred,
#                                      {
#     'storageBucket': 'magictech-a68b3.appspot.com'
# })
import sqlite3
from datetime import date , time
import datetime 

# Function to create/connect to the database
def connect_to_db():
    conn = sqlite3.connect('supermarket.db')
    return conn

# Function to create tables
# def create_tables(conn):
#     c = conn.cursor()

#     # Table for products data
#     c.execute('''CREATE TABLE IF NOT EXISTS products (
#                 id INTEGER PRIMARY KEY,
#                 date TEXT,
#                 product_name TEXT,
#                 price REAL,
#                 category INTEGER,
#                 barcode TEXT,
#                 img TEXT,
#                 quantity INTEGER
#                 )''')

#     # Table for bills
#     c.execute('''CREATE TABLE IF NOT EXISTS bills (
#                 id INTEGER PRIMARY KEY,
#                 date TEXT,
#                 time TEXT,
#                 customer_name TEXT,
#                 total_price REAL,
#                 change REAL,
#                 discount REAL,
#                 payment_method TEXT,
#                 credit_card_number TEXT,
#                 seller_name TEXT
#                 )''')

#     # Table for bill details
#     c.execute('''CREATE TABLE IF NOT EXISTS bill_details (
#                 bill_id  INTEGER PRIMARY KEY,
         
#                 product_barcode TEXT,
#                 quantity INTEGER,
#                 price REAL
#                 )''')

#     # Table for sellers
#     c.execute('''CREATE TABLE IF NOT EXISTS sellers (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT,
#                 name TEXT,
#                 password TEXT,
#                 img_location TEXT
#                 )''')

#     conn.commit()
def getusers(conn, username , passw): 
    d = conn.cursor()
    try:
        d.execute('''SELECT password FROM sellers WHERE username = ?''', (username,))
    except:
        return False
    


    dd = d.fetchone()
    try:
      if passw == dd[0]:
         return username 
      return 'WRONG PASSWORD'
    except:return False
# Function to insert data into products table
def add_product(conn, date, product_name, price, category, barcode, img, quantity):
    c = conn.cursor()
    c.execute('''INSERT INTO productstemp (date, product_name, price, category, barcode, img, quantity)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', (date, product_name, price, category, barcode, img, quantity))
    c.execute('''INSERT INTO products (date, product_name, price, category, barcode, img, quantity , selling)
                VALUES (?, ?, ?, ?, ?, ?, ? ,?)''', (date, product_name, price, category, barcode, img, quantity , 0))
    conn.commit()

# Function to delete product from products table
def delete_product(conn, product_name):
    c = conn.cursor()
    
    c.execute('''DELETE FROM products WHERE barcode=?''', (product_name,))
    conn.commit()

# Function to modify product details
def modify_product_selling(conn, barcode,  quantity):
   c = conn.cursor()
   c.execute('''SELECT quantity , selling FROM products WHERE barcode=?''', ( barcode,))
   ppp =c.fetchone()

   selling = ppp[1]+ quantity
   new_quantity = ppp[0] - quantity 
   c.execute('''UPDATE products SET selling=? ,  quantity=? WHERE barcode=?''', (selling, new_quantity, barcode))
   conn.commit()
def modify_product(conn, barcode, new_price, new_quantity):
    c = conn.cursor()
    c.execute('''UPDATE products SET price=?, quantity=? WHERE barcode=?''', (new_price, new_quantity, barcode))
    conn.commit()
# Function to insert data into bills table
# def add_bill(conn, date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name, products):
#     c = conn.cursor()
#     c.execute('''INSERT INTO bills (date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name))
  
#     c.execute('''SELECT id  FROM bills WHERE date =? AND time =?  ''', (date,time))

#     dd = c.fetchone()
#     print(dd)
#     n = products
#     modify_product(conn,'')
#     i ='%'.join(n[0])
#     i1 ='%'.join(n[1])
#     i2 ='%'.join(n[2])
#     add_bill_detail(conn,dd[0] , i,  i1,  i2)
#     conn.commit()
# Function to insert data into bill details table
def add_bill_detail(conn, bill_id, product_barcode, quantity, price):
    c = conn.cursor()
    c.execute('''INSERT INTO bill_details (bill_id, product_barcode, quantity, price)
                VALUES (?, ?, ?, ?)''', (bill_id, product_barcode, quantity, price))

    conn.commit()
def get_chart(conn):
   c= conn.cursor()
   c.execute('''SELECT COUNT(DISTINCT id) , SUM(quantity) FROM products WHERE category = ? ''', ('مجمدات',))
   a  =c.fetchone()[1]
   c.execute('''SELECT COUNT(DISTINCT id) , SUM(quantity) FROM products WHERE category = ? ''', ('منظفات',))
   b = c.fetchone()[1]
   c.execute('''SELECT COUNT(DISTINCT id) , SUM(quantity) FROM products WHERE category = ? ''', ('مواد_تموينية',))
   d  =c.fetchone()[1]

   if a == None:
      a = 0
   if d == None:
      d = 0
   if b == None:
      b = 0

   # t =c.fetchone()[1]
   return   a ,b ,d 

# Function to retrieve total price of bills for today
def get_total_price_of_bills_today(conn):
    c = conn.cursor()
    today = date.today()
    majd = session.get('username')

    c.execute('''SELECT SUM(total_price) FROM bills WHERE date=? AND seller_name=?''', (today,majd))
    total_price = c.fetchone()[0]
    return total_price

# Function to retrieve number of bills and customers for today
def get_number_of_bills_and_customers_today(conn):
   c = conn.cursor()
   today = date.today()
   majd = session.get('username')

   c.execute('''SELECT COUNT(DISTINCT id), COUNT(DISTINCT customer_name) FROM bills WHERE date=? AND seller_name=?''', (today,majd))
   result = c.fetchone()
   num_bills = result[0]
   num_customers = result[1]
   return num_bills, num_customers
def get_bills_and_customers_today(conn):
   
   temp = []
   c = conn.cursor()
   today = date.today()
   majd = session.get('username')

   for rsd in     c.execute('''SELECT id, date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name FROM bills WHERE date=? AND seller_name=?''', (today,majd)):
      temp.append(rsd)
   return temp
def get_billssss(conn,majd):
   temp = []
   c = conn.cursor()
   
   if majd== '' :
         
      today = date.today()
      # majd = session.get('username')

      for rsd in     c.execute('''SELECT id, date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name FROM bills WHERE date=? ''', (today,)):
         temp.append(rsd)
      return temp

   
   # majd = session.get('username')

   for rsd in     c.execute('''SELECT id, date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name FROM bills WHERE customer_name=?''', (majd,)):
      temp.append(rsd)
   return temp
def get_bills(conn,today):
   temp = []
   c = conn.cursor()
   if today== '' :
         
      today = date.today()
      # majd = session.get('username')

      for rsd in     c.execute('''SELECT id, date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name FROM bills WHERE date=? ''', (today,)):
         temp.append(rsd)
      return temp

   
   # majd = session.get('username')

   for rsd in     c.execute('''SELECT id, date, time, customer_name, total_price, change, discount, payment_method, credit_card_number, seller_name FROM bills WHERE date=? ''', (today,)):
      temp.append(rsd)
   return temp
def getprice(conn,today):

   c = conn.cursor()
   if today== '' :
      tempppp = []
      today = date.today()
      # majd = session.get('username')
      c.execute('''SELECT  username FROM sellers ''')
      temp = c.fetchall()
      c.execute('''SELECT SUM(total_price) FROM bills WHERE date=? ''', (today,))
      d = c.fetchone()[0]

      for a in temp:
         a = a[0]
         c.execute('''SELECT SUM(total_price), date , seller_name FROM bills WHERE date=? AND seller_name=?''', (today,a))
         ddf = c.fetchone()
         if ddf[1] != None:
            tempppp.append(ddf)
      return tempppp , d
   tempppp = []
   
   # majd = session.get('username')
   c.execute('''SELECT  username FROM sellers ''')
   temp = c.fetchall()
   c.execute('''SELECT SUM(total_price) FROM bills WHERE date=? ''', (today,))
   d = c.fetchone()[0]
   for a in temp:
      a = a[0]
      
      c.execute('''SELECT SUM(total_price), date , seller_name FROM bills WHERE date=? AND seller_name=?''', (today,a))
      ddf = c.fetchone()
      if ddf[1] != None:
         tempppp.append(ddf)
   return tempppp , d
   
def get_products(conn):
   temp = []
   c = conn.cursor()
   # today = date.today()
   for rsd in     c.execute('''SELECT * FROM products '''):
      temp.append(rsd)
   return temp
def get_products_sh(conn, name):
   temp = []
   c = conn.cursor()
   # today = date.today()
   for rsd in     c.execute('''SELECT * FROM products WHERE product_name = ?''' , (name,)):
      temp.append(rsd)
   return temp
def get_products_price(conn, name):
   
   c = conn.cursor()
   # today = date.today()
   c.execute('''SELECT price , quantity FROM products WHERE barcode = ?''' , (name,))

   return c.fetchone() 
def connect_to_db():
    conn = sqlite3.connect('supermarket.db')
    return conn
def get_num_of_pro(conn):
   c = conn.cursor()
   # today = date.today()
   c.execute('''SELECT COUNT(DISTINCT id) FROM products ''')
   result = c.fetchone()
   # num_bills = result[0]
   # num_customers = result[1]
   return result[0]
# Function to get product information from the database based on barcode
def get_product_info_from_db(barcode):
    conn = connect_to_db()
    c = conn.cursor()
    c.execute('''SELECT product_name, price, category, quantity FROM products WHERE barcode=?''', (barcode,))
    product_info = c.fetchone()
    conn.close()
    return product_info
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
def get_bill_detail(conn):
   temp =[]
   c = conn.cursor()

   for i in c.execute('''SELECT  name, username, img_location FROM sellers '''):
      temp.append(i)
  
   return temp

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
# # Example usage
# print('ddddddd')
# conn = connect_to_db()


# # Adding a product
# add_product(conn, '2024-06-03', 'Apple', 1.0, 1, '123456789', 'apple.jpg', 100 ,[2,3,4])
# add_product(conn, '2024-07-06', 'Apple', 1.0, 1, '123456789', 'apple.jpg', 100)
# # Deleting a product
# delete_product(conn, 'Apple')

# # Modifying a product
# modify_product(conn, 'Apple', 1.5, 150)

# # Adding a bill
# add_bill(conn, '2024-03-06', '10:00', 'John Dkoe', 50.0, 0.0, 0.0, 'cash', '', 'seller1')

# # Adding bill details
# add_bill_detail(conn, '123456789', 2, 3.0)

# # Retrieving total price of bills for today
# total_price_today = get_total_price_of_bills_today(conn)
# print("Total price of bills for today:", total_price_today)

# # Retrieving number of bills and customers for today
# num_bills_today, num_customers_today = get_number_of_bills_and_customers_today(conn)
# print("Number of bills today:", num_bills_today)
# print("Number of customers today:", num_customers_today)
# print (get_total_price_of_bills_today(conn))

# conn.close()


appf = Flask(__name__)

appf.secret_key = 'yoursecritkey'
# db = firestore.client()
#new 999999999999999999999999999999999999

# Function to connect to the SQLite database

@appf.route('/submit_bill', methods=['POST' , 'GET'])
def submit_bill():
   if 'username' in session:
      data = request.get_json()
      data =data['products']
   #  products = data.get('products', [])
      print(data)
      conn = connect_to_db()
      if len(data) == 6 :
         return jsonify({'message': 'Bill submitted successfully'})
      datea =date.today()
      datea = str(datea)
      username = session.get('username')
      quat =[]
      pr =[]
      na =[]
      if data[0]== []:
         return jsonify({'message': 'Bill submitted successfully'})
      for iiiiii in data[0]:
         # iiiiii =iiiiii
         tempi = iiiiii

         quat.append(str(tempi['quantity']))
         na.append(str(tempi['name']))
         pr.append(str(tempi['price']))
      
   
         time = str(datetime.datetime.today())
         time = time.split(' ')[1]
         # time = time.split('.')[0]
      add_bill(conn ,datea,time,data[1],data[2],data[3], data[4], data[5], data[6],username,[data[7],quat,pr])
      
      return jsonify({'message': 'Bill submitted successfully'})
   else :return render_template('login.html')

@appf.route('/bill')
def index():
   if 'username' in session:
      conn = connect_to_db()
      # data= get_bills_and_customers_today(conn)
      bills, cus =  get_number_of_bills_and_customers_today(conn)
      # visits = db.collection('visits').get()
      
      # visit_counts = get_chart(conn)
      # {doc.id: doc.get('count') for doc in visits}
      
      re = get_total_price_of_bills_today(conn)
      dd = get_num_of_pro(conn)
      if re == None :
         re =0
      return render_template('barcode.html', waited = bills ,  counta =cus,revinforto=re , ddd = dd)
   else:return render_template('login.html')
@appf.route('/add_to_bill', methods=['POST'])
def add_to_bill():
   if 'username' in session:
      data = request.get_json()
      barcode = data.get('barcode')
      #  producsuj.append[barcode]
      # product_info = get_product_info_from_db(barcode)
      #  product_info = [1,2,3,4]
      conn = connect_to_db()
      product_info =    get_product_info_from_db( barcode)
      #  print(product_infoo)
      #  product_infoo[0] == product_info[0]
      #  product_infoo[1] == product_info[1]
      #  product_infoo[2] == product_info[2]
      #  product_infoo[3] == product_info[3]
      
      if product_info:
         product = {
               "name": product_info[0],
               "price": product_info[1],
               "category": product_info[2],
               "quantity": product_info[3]
         }
         return jsonify(product)
      else:
         print('false')
         return jsonify({})
   else:return render_template('login.html')
#999999999999999999999999999999999999
@appf.route('/orderc',methods = ['POST', 'GET'])
def orderhss():
   if 'username' in session:
      if request.method == 'POST':
         search = request.form['search']
         conn = connect_to_db()
         print(search)
         data= get_bills(conn,search)
         print(data)
         img = session.get('avatar')

         return render_template("orderc.html" ,  data = data)
      img = session.get('avatar')
      conn = connect_to_db()
      data = get_bills(conn , '')


      return render_template("orderc.html" , image_url = img , data = data )
   else:return render_template('login.html')
@appf.route('/money',methods = ['POST', 'GET'])
def orderhssss():
   if 'username' in session:
      if request.method == 'POST':
         search = request.form['search']
         conn = connect_to_db()
         print(search)
         data , a= getprice(conn,search)

         img = session.get('avatar')
         if a == None:
            a =0

         return render_template("money.html" ,  data = data , all_mon=a )
      img = session.get('avatar')
      conn = connect_to_db()
      data ,a = getprice(conn , '')

      if a == None:
         a =0
               
      return render_template("money.html" , image_url = img , data = data , all_mon = a )
   else: return render_template('login.html')
@appf.route('/customers',methods = ['POST', 'GET'])
def ordesrhss():
   if 'username' in session:
      if request.method == 'POST':
         search = request.form['search']
         conn = connect_to_db()
         print(search)
         data= get_billssss(conn,search)
         print(data)
         img = session.get('avatar')

         return render_template("customers.html" ,  data = data)
      img = session.get('avatar')
      conn = connect_to_db()
      data = get_billssss(conn , '')


      return render_template("customers.html" , image_url = img , data = data )
   else:
      return render_template('login.html')

@appf.route('/orders',methods = ['POST', 'GET'])
def orderss():
   if 'username' in session:
      if request.method == 'POST':
         search = request.form['search']
         conn = connect_to_db()
         data= get_products_sh(conn,search)
         print(data)
         img = session.get('avatar')

         return render_template("orders.html" ,  data = data)
      img = session.get('avatar')
      conn = connect_to_db()
      data = get_products(conn)


      return render_template("orders.html" , image_url = img , data = data )
   else: return render_template('login.html')
# @appf.route('/doneprojects',methods = ['POST', 'GET'])
# def done():
#    if request.method == 'POST':
#       search = request.form['search']
#       data= getallorders(search)
#       img = session.get('avatar')

#       return render_template("donepro.html" ,  data = data)
#    img = session.get('avatar')
#    data, d= getallorders('get_done')


#    return render_template("donepro.html" , image_url = img , data = data )



@appf.route('/admins/<use>')
def admins(use):
   if 'username' in session:
      img = session.get('avatar')
      data = session.get('dataorders')
      majd = session.get('majd')
      countd = session.get('count')
      dd = session.get('ddd')
      conn = connect_to_db()
      # collection_ref = db.collection('users')
      print(dd)
      # Get the documents in the collection
      # documents = collection_ref.get()

      # Calculate the number of documents
      # count = session.get('cus')
      # len(documents)
      conn = connect_to_db()
      data= get_bills_and_customers_today(conn)
      bills, cus =  get_number_of_bills_and_customers_today(conn)
      # visits = db.collection('visits').get()
      
      visit_counts = get_chart(conn)
      print(visit_counts)
      # {doc.id: doc.get('count') for doc in visits}
      re = get_total_price_of_bills_today(conn)
      if re == None :
         re =0
      return render_template("admin.html" , name = use, image_url = img , data = data ,visit_counts = visit_counts , waited = bills , count= countd  , counta =cus,ddd =dd ,revinforto=re)
   else:
        return redirect(url_for('login'))
# @app.route('/addadmin')
# def addadmins():
   # if 'username' in session:
   #      return render_template("addadmin.html" )
   # else:
   #      return redirect(url_for('login'))
# @app.route('/log')
# def log():
#    return render_template("login.html")

# @app.route('/addadmin')
# def addadmin():
#    return render_template("addadmin.html")
# @appf.route('/code/<use>')
# def code(use):
#    date [[1,2],[3,5],[7,5]]
#    data = getallorderss(use)
  
#    if data != []:
#       return render_template("getcode.html" , data = data )
#    return render_template("home.html")
# @appf.route('/codedd')
# def codve():
#    data =[[1,2,6],[3,5,6],[7,5,6]]
#    # data = getallorderss(use)
#    print(data)
#    if data != []:
#       return render_template("test.html" , data = data )
#    return render_template("home.html")
def get_bill_detaill(conn, bill_id):
    temp = []
    c = conn.cursor()
    print(bill_id)
    c.execute('''SELECT  product_barcode, quantity, price FROM bill_details WHERE bill_id=?''',(bill_id,))
    ddd =c.fetchone()
    print(ddd)
    d = str(ddd[0]).split('%')
    d1 =  str(ddd[1]).split('%')
    d2 =str(ddd[2]).split('%')
    for t in d:
        o = d.index(t)
        print(o)
        uuuu = conn.cursor()
        uuuu.execute('''SELECT  product_name FROM productstemp WHERE barcode=?''',(t,))
        t =uuuu.fetchone()[0]  
       
        temp.append([t,d1[o],d2[o]])
    return temp
@appf.route('/codea/<use>')
def codea(use):
   
   conn = connect_to_db()
   data = get_bill_detaill(conn,use)
   
   # session['proname'] =data
   
   
   return render_template("ffas.html" , data = data )
@appf.route('/delete/<use>')
def delete(use):
   
   conn = connect_to_db()
   delete_product(conn,use)
   
   # session['proname'] =data
   
   
   return redirect(url_for('orderss'))
@appf.route('/edit/<use>' , methods = ['POST', 'GET'])
def edit(use):
   

   if 'username' in session:
      
      if request.method == 'POST':
         # file = request.files['picture']
         passw = request.form['pass']
         # name = request.form['name']
         email = request.form['email']
         conn = connect_to_db()
         # print(file)
   
         modify_product(conn,use ,passw, email)
         return redirect(url_for('orderss'))
         # file= ''
         # url = upload_picture(file)
         # dadtafire =addadmina( name , email ,occ,user, per , passw, url)
      conn = connect_to_db()

         # if dadtafire != None:
         #    return dadtafire
      t = get_products_price(conn ,use)
      tem = t[0]
      tem1 =t[1]
      return render_template("editproduct.html"  , a = use , tem = tem, tem1 = tem1)
   else:
      return redirect(url_for('login'))   

      
   # session['proname'] =data
   
   
   return render_template("ffas.html" , data = data )
   
@appf.route('/false')
def false():
   return f'failed to find your acount '
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
@appf.route('/add_product',methods = ['POST', 'GET'])
def add_pro():
   if 'username' in session:
      
      if request.method == 'POST':
         # file = request.files['picture']
         passw = request.form['pass']
         name = request.form['name']
         email = request.form['email']
         code = request.form['code']
         qua = request.form['qua']
         conn = connect_to_db()
         # print(file)
         file= ''
         datee = date.today()
         add_product(conn, datee,name ,passw,email, code, '', qua)
         # url = upload_picture(file)
         # dadtafire =addadmina( name , email ,occ,user, per , passw, url)
         return redirect(url_for('orderss'))
         # if dadtafire != None:
         #    return dadtafire
         
      return render_template("addpro.html" )
   else:
      return redirect(url_for('login'))   
@appf.route('/addadmin',methods = ['POST', 'GET'])
def addadmin():
   if 'username' in session:
      
      if request.method == 'POST':
         # file = request.files['picture']
         passw = request.form['pass']
         name = request.form['name']
         email = request.form['email']
         conn = connect_to_db()
         # print(file)
         file= ''
         add_seller(conn, email,name ,passw , file)
         # url = upload_picture(file)
         # dadtafire =addadmina( name , email ,occ,user, per , passw, url)
         majd = session.get('username')
         return redirect(url_for('admins', use = majd ))
         # if dadtafire != None:
         #    return dadtafire
         
      return render_template("addadmin.html" )
   else:
      return redirect(url_for('login'))   
      
      # # print(f'dd{user}')
      # if  user == False:
      #    return redirect(url_for('false' ))
      # else:
      #    session['username'] = user
      #    return redirect(url_for('admins', use = user ))
   # else:
   #    user = request.args.get('email')
   #    passw = request.args.get('pass')
   #    user = data.seacha(user,passw)
   #    # print(user')  
   #    if  user == False:
   #       return redirect(url_for('false' ))
   #    else:
   #       return redirect(url_for('admins', use = user ))
   return render_template("addadmin.html")
# @appf.route('/codeg',methods = ['POST', 'GET'])
# def codeg():
#    if request.method == 'POST':
      

#       name = request.form['code']
#       return  redirect(url_for('code', use = name ))
#    else:
#       return render_template('home.html')
# @appf.route('/save',methods = ['POST', 'GET'])
# def codes():
#    if request.method == 'POST':
#       countd = session.get('proname')

#       name = request.form['meet']
#       dead = request.form['dead']
#       update(name, dead,countd[0][3])
#       return  redirect(url_for('codea', use = countd[0][6] ))
# @appf.route('/done',methods = ['POST', 'GET'])
# def donde():
#    if request.method == 'POST':
#       countd = session.get('proname')
#       print(countd)
#       doneu('Done', countd[0][3])
#       return  redirect(url_for('codea', use = countd[0][6] ))
   
# @appf.route('/contact',methods = ['POST', 'GET'])
# def start():
#    if request.method == 'POST':
      

#       name = request.form['name']
#       email = request.form['email']
#       phone = request.form['phone']
#       cat = request.form['cat']
#       pname = request.form['pname']
#       idea = request.form['idea']
#       datetime = request.form['datetime']
#       date = request.form['date']


#     # Retrieve visit counts from Firestore

#       code = starta(pname,  name , email ,phone,cat, idea , datetime ,date)
#       return render_template('code.html' , code = code)
#    else:
#       m  = getmeetdates()
#       return render_template("contact.html" , dates =m )

# Function to retrieve number of bills and customers for today

@appf.route('/',methods = ['POST', 'GET'])
def login():

   if request.method == 'POST':
      session.pop('username', None)

      user = request.form['email']
      passw = request.form['pass']
      conn= connect_to_db()
      userafter = getusers(conn,user, passw)
      dddd = ''
      # print(f'dd{user}')
      if not userafter :
         return 'WRONG USERNAME'
      elif userafter == 'WRONG PASSWORD':
         return userafter
      else:
         # imgd , user = dateo.seachnamebyemail(user)
         imgd = dddd

         # dfdfdf = get_chart(conn)
         
      
         count  = 0
         countdo =0
         conn = connect_to_db()
         ddd =get_num_of_pro(conn)
         counta = 0
         # getallusers('get_all')
         session['username'] = user
         session['avatar'] = imgd
 
         session['count'] = countdo
         session['counta'] = counta
         session['ddd'] = ddd

         return redirect(url_for('admins', use = user ))
   # else:
   #    user = request.args.get('email')
   #    passw = request.args.get('pass')
   #    user = data.seacha(user,passw)
   #    # print(user')  
   #    if  user == False:
   #       return redirect(url_for('false' ))
   #    else:
   #       return redirect(url_for('admins', use = user ))
   majd = session.get('username')
   # print(majd)
   if majd != None:return redirect(url_for('admins', use = majd ))
   return render_template("login.html")

# @appf.route('/searchusers', methods=['GET', 'POST'])
# def searchusers():
#    if request.method == 'POST':
#       search = request.form['search']
#       data = getallusers(search)
#       return render_template("searchusers.html" ,  data = data)
#    conn = connect_to_db()
#    data =get_bill_detail(conn)
#    print(data)
#    return render_template("searchusers.html" ,  data = data)


@appf.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# @app.route('/deleteuser', methods=['GET', 'POST'])
# def deleteuser():
#    if request.method == 'POST':
#          search = request.form['search']
#          data = datafire.deleteuser(search)

import os
import webbrowser


def open_browser():
    # Open the default web browser with the local URL
    webbrowser.open('http://127.0.0.1:5000')

    

if __name__ == '__main__':
   
   from threading import Thread
   Thread(target=open_browser).start()
   appf.run(debug = True)
