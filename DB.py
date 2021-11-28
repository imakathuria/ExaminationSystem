import sqlite3
import json
connection = sqlite3.connect("aisystem.db")
connection.row_factory = sqlite3.Row
db = connection.cursor()
db.execute("SELECT * FROM Students where roll = 101")
rows = db.fetchall()
for row in rows:
    print("ID:"+str(row["id"])+"\n"+"Name:"+row["name"])
jsonstr = json.dumps( [dict(ix) for ix in rows] )

print(jsonstr)
connection.close()   
