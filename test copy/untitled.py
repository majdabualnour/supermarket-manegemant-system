from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
products = {
    "15683497": {"name": "Product 1", "price": 10.99, "category": "Category A", "quantity": 100},
    "2": {"name": "Product 2", "price": 5.99, "category": "Category B", "quantity": 50}
}
# Function to connect to the SQLite database
def connect_to_db():
    conn = sqlite3.connect('supermarket.db')
    return conn

# Function to get product information from the database based on barcode
def get_product_info_from_db(barcode):
    conn = connect_to_db()
    c = conn.cursor()
    c.execute('''SELECT product_name, price, category, quantity FROM products WHERE barcode=?''', (barcode,))
    product_info = c.fetchone()
    conn.close()
    return product_info

@appf.route('/')
def index():
    return appf.send_static_file('index.html')

@appf.route('/add_to_bill', methods=['POST'])
def add_to_bill():
    data = request.get_json()
    barcode = data.get('barcode')
    # product_info = get_product_info_from_db(barcode)
    product_info = [1,2,3,4]
    product_infoo = products.get(barcode, {})
    print(product_infoo)
    product_infoo['name'] == product_info[0]
    product_infoo['price'] == product_info[1]
    product_infoo['category'] == product_info[2]
    product_infoo['quantity'] == product_info[3]
    print(product_infoo)
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

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
   