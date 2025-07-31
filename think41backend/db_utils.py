# db_utils.py
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row  # to access columns by name
    return conn
