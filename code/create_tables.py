import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)") # By putting id as INTEGER PRIMARY KEY, we are setting the id value into Auto Increment starting from 1
cursor.execute("INSERT INTO users VALUES ('1', 'admin', '1234')")

cursor.execute("CREATE TABLE IF NOT EXISTS items (name TEXT, price REAL)")
# cursor.execute("INSERT INTO items VALUES ('chair', 10.99)") # Use this line for testing if INSERT into TABLE is working or not

connection.commit()
connection.close()