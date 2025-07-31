import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Check total products
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
print(f"✅ Total Products Loaded: {count}")

# Show 5 sample entries
cursor.execute("SELECT * FROM products LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
