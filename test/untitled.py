
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy product data (replace with your actual product data)
products = {
    "123456789": {"name": "Product 1", "price": 10.99, "category": "Category A", "quantity": 100},
    "987654321": {"name": "Product 2", "price": 5.99, "category": "Category B", "quantity": 50}
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/get_product_info')
def get_product_info():
    barcode = request.args.get('barcode')
    print('fdfdf')
    product_info = products.get(barcode, {})
    return jsonify(product_info)

if __name__ == '__main__':
    app.run(debug=True)