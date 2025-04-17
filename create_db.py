import sqlite3

conn = sqlite3.connect("sales_data.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS sales (
               product TEXT,
               quantity INTEGER,
               price REAL
               )
               ''')

cursor.execute("INSERT INTO sales VALUES ('Laptop', 5, 800)")
cursor.execute("INSERT INTO sales VALUES ('Mouse', 20, 15)")
cursor.execute("INSERT INTO sales VALUES ('Keyboard', 10, 50)")
cursor.execute("INSERT INTO sales VALUES ('Monitor', 3, 200)")

conn.commit()
conn.close()

print("Database 'sales_data.db' created successfully!")