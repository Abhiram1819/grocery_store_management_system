import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='grocery_store')
cursor = cnx.cursor()

query = ("SELECT * FROM grocery_store.products")

cursor.execute(query)

for (product_id) in cursor:
    print(product_id)
cnx.close()