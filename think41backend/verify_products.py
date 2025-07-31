import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# ✅ Create departments table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
''')

# ✅ Add department_id column to products if not already exists
try:
    cursor.execute("ALTER TABLE products ADD COLUMN department_id INTEGER")
except sqlite3.OperationalError:
    pass  # column exists

# ✅ Check total products
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
print(f"✅ Total Products Loaded: {count}")

# ✅ Show 5 sample entries
cursor.execute("SELECT * FROM products LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
