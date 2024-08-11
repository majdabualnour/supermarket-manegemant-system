from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

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

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/add_to_bill', methods=['POST'])
def add_to_bill():
    data = request.get_json()
    barcode = data.get('barcode')
    product_info = get_product_info_from_db(barcode)
    if product_info:
        product = {
            "name": product_info[0],
            "price": product_info[1],
            "category": product_info[2],
            "quantity": product_info[3]
        }
        return jsonify(product)
    else:
        return jsonify({})

@app.route('/submit_bill', methods=['POST'])
def submit_bill():
    data = request.get_json()
    products = data.get('products', [])
    print(data)
    return jsonify({'message': 'Bill submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
    
  
  






    
    
    
