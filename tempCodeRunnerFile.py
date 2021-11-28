import sqlite3
connection = sqlite3.connect("aisystem.db")
print("Database opened successfully")
cursor = connection.cursor()
# delete
# cursor.execute('''DROP TABLE Student_Info;''')
cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()
for row in rows:
    print(row)
print("Table created successfully")
connection.close()   