import sqlite3
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT * FROM disease")
rows = cursor.fetchall()
for i in rows:
    print(i)
    print(type(i))
conn.close()

