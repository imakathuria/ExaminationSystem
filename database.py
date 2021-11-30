import sqlite3

class database:
    def __init__(self):
        self.connection = sqlite3.connect("aisystem.db")
        self.connection.row_factory = sqlite3.Row 

    def get_student(self, id):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Students where id = ?",str(id))
        rows = db.fetchall()
        return rows[0];


    def check_students(self, username,password):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Students where username = ? AND password = ?",(username,password))
        rows = db.fetchall()
        return rows
    
    def check_teacher(self, username,password):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Teachers where username = ? AND password = ?",(username,password))
        rows = db.fetchall()
        if(len(rows)==0):
            return False
        if(len(rows)>0):
            return rows


    def insert_student(self,name,roll,username,password):
        db = self.connection.cursor()
        db.execute("INSERT INTO Students(name,roll,username,password) VALUES(?,?,?,?)",(name, roll,username,password))
        self.connection.commit()
        print("Student added successfully")

    def get_teacher(self, id):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Teachers where id = ?",str(id))
        rows = db.fetchall()
        return rows[0];

    def insert_teacher(self,name, subject,username,password):
        db = self.connection.cursor()
        db.execute("INSERT INTO Teachers(name,subject,username,password) VALUES(?,?,?,?)",(str(name), str(subject),str(username),str(password)))
        self.connection.commit()
        print("Teacher added successfully")

    