import sqlite3

# Connect to your database
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Show total products
cursor.execute("SELECT COUNT(*) FROM products")
count = cursor.fetchone()[0]
print(f"✅ Total products in DB: {count}")

# Show 5 sample entries
cursor.execute("SELECT id, name, brand, cost, retail_price, category, department FROM products LIMIT 5")
rows = cursor.fetchall()

print("\n🔍 Sample Products:")
for row in rows:
    print(row)

conn.close()
