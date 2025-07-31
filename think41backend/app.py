from flask import Flask, jsonify, abort
from flask_cors import CORS
from db_utils import get_db_connection

app = Flask(__name__)
CORS(app)  # Allow requests from frontend (localhost:3000)

@app.route('/api/products', methods=['GET'])
def get_all_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products LIMIT 100').fetchall()
    conn.close()

    product_list = [dict(row) for row in products]
    return jsonify(product_list), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()

    if product is None:
        abort(404, description="Product not found")

    return jsonify(dict(product)), 200

@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
