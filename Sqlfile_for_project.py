import sqlite3

conn = sqlite3.connect('database.sqlite')

#conn.execute("""CREATE TABLE DISEASE
#(ID INT,
#Disease TEXT, Pathogen TEXT, Symptoms TEXT, Management TEXT)
#""")

cursor = conn.cursor()
cursor.execute("SELECT * FROM disease")
rows = cursor.fetchall()
for i in rows:
    print(i)
    print(type(i))


print("Table created Successfully")

conn.close()