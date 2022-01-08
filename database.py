import sqlite3
import json

class database:
    def __init__(self):
        self.connection = sqlite3.connect("aisystem.db")
        self.connection.row_factory = sqlite3.Row 

    def get_student(self, id):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Students where id = ?",(str(id),))
        rows = db.fetchall()
        jsonstr = json.dumps([dict(ix) for ix in rows])
        return jsonstr;


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
        jsonstr = json.dumps([dict(ix) for ix in rows])
        return jsonstr;

    def insert_teacher(self,name, subject,username,password):
        db = self.connection.cursor()
        db.execute("INSERT INTO Teachers(name,subject,username,password) VALUES(?,?,?,?)",(str(name), str(subject),str(username),str(password)))
        self.connection.commit()
        print("Teacher added successfully")

    def get_teacher_username(self):
        db = self.connection.cursor()
        db.execute("SELECT username FROM Teachers")
        rows = db.fetchall()
        return rows
    def get_student_username(self):
        db = self.connection.cursor()
        db.execute("SELECT username FROM Students")
        rows = db.fetchall()
        return rows

    def set_test(self,teacherid,subject,testtype,datesubmitted,questions,answers_set):
        answers = json.dumps(answers_set)
        db = self.connection.cursor()
        db.execute("INSERT INTO Test(teacherid,subject,type,datesubmitted,question1,question2,question3,question4,question5,answers) VALUES(?,?,?,?,?,?,?,?,?,?)",(teacherid,subject,testtype,datesubmitted,questions[0],questions[1],questions[2],questions[3],questions[4],answers))
        self.connection.commit()
        print("Test added successfully")

    def set_subjective_test(self,teacherid,subject,testtype,datesubmitted,questions,answers_set):
        answers = json.dumps(answers_set)
        db = self.connection.cursor()
        db.execute("INSERT INTO Test(teacherid,subject,type,datesubmitted,question1,question2,answers) VALUES(?,?,?,?,?,?,?)",(teacherid,subject,testtype,datesubmitted,questions[0],questions[1],answers))
        self.connection.commit()
        print("Test added successfully")

    def get_testsbyid(self, id):
        db = self.connection.cursor()
        db.execute("SELECT id,subject,type,datesubmitted FROM Test WHERE teacherid = ?",str(id))
        rows = db.fetchall()
        jsonstr = json.dumps([dict(ix) for ix in rows])
        print(jsonstr)
        return jsonstr

    def set_result(self,testid,testtype,teacherid,studentroll,student,subject,marks,result):
        db = self.connection.cursor()
        db.execute("INSERT INTO Result(testid,testtype,teacherid,studentroll,student,subject,marks,result) VALUES (?,?,?,?,?,?,?,?)",(testid,testtype,teacherid,studentroll,student,subject,marks,result))
        self.connection.commit()
        print("Result added successfully")
        

    def get_resultbytestid(self,id):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Result WHERE testid = ?",(id,))
        rows = db.fetchall()
        jsonstr = json.dumps([dict(ix) for ix in rows])
        print(jsonstr)
        return jsonstr

    def get_tests(self):
        db = self.connection.cursor()
        db.execute("SELECT id,teacherid,subject,type,datesubmitted,question1,question2,question3,question4,question5 FROM Test")
        rows = db.fetchall()
        jsonstr = json.dumps([dict(ix) for ix in rows])
        print(jsonstr)
        return jsonstr

    def get_testsbytestid(self,testid):
        print("--------------------------------------------------------------------------------------------------")
        print(testid)
        db = self.connection.cursor()
        db.execute("SELECT id, teacherid, subject, type, datesubmitted, question1, question2, question3, question4, question5 FROM Test WHERE id = ?",(str(testid),))
        rows = db.fetchall()
        jsonstr = json.dumps([dict(ix) for ix in rows])
        print(jsonstr)
        return jsonstr

    def get_answers(self, testid):
        answerlist = list()
        db = self.connection.cursor()
        db.execute("SELECT answers FROM Test WHERE id = ?",(str(testid),))
        rows = db.fetchall()
        row = rows[0]
        jsonlist = json.loads(row["answers"])
        for x in jsonlist:
            answerlist.append(str(x.strip().upper()))
        return answerlist
    
    def get_result_by_roll(self,testid,studentroll):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Result WHERE testid = ? AND studentroll = ?",(str(testid),str(studentroll)))
        rows = db.fetchall()
        jsonstr = json.dumps([dict(ix) for ix in rows])
        print(jsonstr)
        return jsonstr

    def get_resultforCSV(self,id):
        db = self.connection.cursor()
        db.execute("SELECT * FROM Result WHERE testid = ?",(id,))
        rows = db.fetchall()
        print(rows[0]["student"])
        return rows