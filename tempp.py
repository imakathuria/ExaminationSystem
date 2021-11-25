import sqlite3

with sqlite3.connect("student_detials.db") as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT into Student_Info (name, email, gender, contact, dob, address) values (?,?,?,?,?,?)",("name12", "emai2l1", "g2ender1", "cadontact1", "ddasob1", "adaddress1"))
                connection.commit()