import sqlite3
import csv

# Connect to SQLite DB
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# ✅ Load all departments into a lookup map
cursor.execute("SELECT name, id FROM departments")
dept_map = {name: id for name, id in cursor.fetchall()}

# ✅ Read CSV and process
with open('data/products.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dept_name = row['department']

        # ✅ Insert department if not already added
        if dept_name not in dept_map:
            cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", (dept_name,))
            conn.commit()
            cursor.execute("SELECT id FROM departments WHERE name = ?", (dept_name,))
            dept_id = cursor.fetchone()[0]
            dept_map[dept_name] = dept_id
        else:
            dept_id = dept_map[dept_name]

        # ✅ Insert product with department_id
        cursor.execute('''
            INSERT OR REPLACE INTO products (
                id, cost, category, name, brand, retail_price, sku, distribution_center_id, department_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            int(row['id']),
            float(row['cost']),
            row['category'],
            row['name'],
            row['brand'],
            float(row['retail_price']),
            row['sku'],
            int(row['distribution_center_id']),
            dept_id
        ))

conn.commit()
conn.close()
print("✅ products.csv loaded with departments successfully!")
