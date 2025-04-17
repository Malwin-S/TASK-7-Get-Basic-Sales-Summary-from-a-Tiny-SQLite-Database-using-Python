import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")

query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"

df = pd.read_sql_query(query, conn)

conn.close()

print(df)

df.plot(kind='bar', x='product', y='revenue')

plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Total Revenue by Product")

plt.savefig("sales_chart.png")

plt.show()