from flask import Flask, jsonify, abort
from flask_cors import CORS
from db_utils import get_db_connection

app = Flask(__name__)
CORS(app)  # Allow requests from frontend (localhost:3000)

# Get all products with department name via JOIN
@app.route('/api/products', methods=['GET'])
def get_all_products():
    conn = get_db_connection()
    query = '''
        SELECT 
            p.id, p.name, p.brand, p.category, p.cost, p.retail_price, 
            p.sku, p.distribution_center_id, d.name AS department
        FROM products p
        LEFT JOIN departments d ON p.department_id = d.id
        LIMIT 100
    '''
    rows = conn.execute(query).fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({
            "id": row["id"],
            "name": row["name"],
            "brand": row["brand"],
            "category": row["category"],
            "cost": row["cost"],
            "retail_price": row["retail_price"],
            "sku": row["sku"],
            "distribution_center_id": row["distribution_center_id"],
            "department": row["department"]
        })

    return jsonify(products), 200

# Get single product by ID with department
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    conn = get_db_connection()
    query = '''
        SELECT 
            p.id, p.name, p.brand, p.category, p.cost, p.retail_price, 
            p.sku, p.distribution_center_id, d.name AS department
        FROM products p
        LEFT JOIN departments d ON p.department_id = d.id
        WHERE p.id = ?
    '''
    row = conn.execute(query, (product_id,)).fetchone()
    conn.close()

    if row is None:
        abort(404, description="Product not found")

    product = {
        "id": row["id"],
        "name": row["name"],
        "brand": row["brand"],
        "category": row["category"],
        "cost": row["cost"],
        "retail_price": row["retail_price"],
        "sku": row["sku"],
        "distribution_center_id": row["distribution_center_id"],
        "department": row["department"]
    }

    return jsonify(product), 200

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
