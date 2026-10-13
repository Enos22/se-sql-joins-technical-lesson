# connect to the DB
import sqlite3
import pandas as pd
conn = sqlite3.connect('data.sqlite')

# Dis/p Product Details Along with Order Details
q = """
SELECT *
 FROM orderdetails
      JOIN products
      ON orderdetails.productCode = products.productCode
      LIMIT 10;
"""
print(pd.read_sql(q, conn))

#compare the individual tables

#a: Orderdetails Table
q = """
SELECT *
 FROM orderdetails
 LIMIT 10;
"""
print(pd.read_sql(q, conn))

#b: products Table:
q = """
SELECT *
 FROM products
 LIMIT 10;
"""
print(pd.read_sql(q, conn))

#the USING Clause:

q = """
SELECT *
 FROM orderdetails
   JOIN products
     USING(productCode)
 LIMIT 10;
"""
print(pd.read_sql(q, conn))

#More Liasing
q = """
SELECT *
 FROM orderdetails AS od
   JOIN products AS p
     ON od.productCode = p.productCode
 LIMIT 10;
"""
print(pd.read_sql(q, conn))

#LEFT JOINs
q = """
SELECT *
 FROM products
   LEFT JOIN orderdetails
     USING(productCode);
"""
df = pd.read_sql(q, conn)

print("Number of records returned:", len(df))
print("Number of records where order details are null:", len(df[df.orderNumber.isnull()]))

#Primary Vs Foreign Keys
q = """
SELECT *
 FROM customers AS c
      JOIN employees AS e
      ON c.salesRepEmployeeNumber = e.employeeNumber
      ORDER By employeeNumber;
"""
print(pd.read_sql(q, conn))

conn.close()
