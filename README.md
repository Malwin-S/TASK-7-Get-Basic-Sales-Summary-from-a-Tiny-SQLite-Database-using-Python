# TASK-7-Get-Basic-Sales-Summary-from-a-Tiny-SQLite-Database-using-Python
Python script to analyze sales data from an SQLite database and generate a bar chart.

This repository contains a Python script that analyzes sales data from an SQLite database and generate a bar chart visualizing total revenue by product.

## SQL Query

The script uses the following SQL query to calculate total revenue by product:

'''sql
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales
GROUP BY product;
