import sqlite3
import csv

# Connect to SQLite DB (or create it)
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Step 1: Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        cost REAL,
        category TEXT,
        name TEXT,
        brand TEXT,
        retail_price REAL,
        department TEXT,
        sku TEXT,
        distribution_center_id INTEGER
    )
''')

# Step 2: Load CSV
with open('data/products.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [
        (
            int(row['id']),
            float(row['cost']),
            row['category'],
            row['name'],
            row['brand'],
            float(row['retail_price']),
            row['department'],
            row['sku'],
            int(row['distribution_center_id'])
        )
        for row in reader
    ]

# Step 3: Insert into table
cursor.executemany('''
    INSERT INTO products (
        id, cost, category, name, brand, retail_price, department, sku, distribution_center_id
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', rows)

conn.commit()
conn.close()

print("✅ products.csv loaded successfully!")
