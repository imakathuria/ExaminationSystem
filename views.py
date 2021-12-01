from flask import * 
from database  import *
from datetime import date
from objective import ObjectiveTest


app = Flask(__name__)
app.secret_key = 'aiexaminationsystemquestionanswergenrator'

global_answers = list()
# 3-static pages -- start
@app.route("/")
@app.route("/index")
def index():
     
    return render_template('index.html')

@app.route("/about")
def about():
     
    return render_template('about.html')   
    
@app.route("/contact")
def contact():
     
    return render_template('contact.html')    
# 3-static pages -- end

# static routes -- start 
@app.route("/signup", methods = ["POST","GET"])
def signup():
    if request.method == "POST":
        if request.form["options"] == "1" :
            print("Student Add request")
            name = request.form["name"]
            roll = request.form["roll"]
            username = request.form["username"]
            password = request.form["password"] 
            db = database()
            db.insert_student(name,roll,username,password)
            return render_template('signupSucess.html')
        if request.form["options"] == "0" :
            print("Teacher Add request")
            name = request.form["name"]
            subject = request.form["subject"]
            username = request.form["username"]
            password = request.form["password"] 
            db = database()
            db.insert_teacher(name,subject,username,password)
            return render_template('signupSucess.html')
    if request.method == "GET": 
        return render_template('signupForm.html')      
# @app.route("/logout")
# def logout():
     
#     return render_template('') 

@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        if request.form["options"] == "1" :
            print("Student Login request")
            username = request.form["username"]
            password = request.form["password"] 
            db = database()
            row = db.check_students(username,password)
            if len(row)==0:
                return redirect(url_for('login'))
            else:
                jsonstr = json.dumps([dict(ix) for ix in row])
                return redirect(url_for('studentDashboard',student = jsonstr)) 
        if request.form["options"] == "0" :
            print("Teacher Login request")
            username = request.form["username"]
            password = request.form["password"] 
            db = database()
            row = db.check_teacher(username,password)
            if len(row)==0:
                return redirect(url_for('login'))
            else:
                teacher = row[0]
                session["user"] = "0"
                session["id"] = teacher["id"]
               
                return redirect(url_for('teacherDashboard',id = teacher["id"])) 
    if request.method == "GET":
        return render_template('loginForm.html') 

# static routes -- End
# student pages --- Start
@app.route("/studentDashboard/<student>")
def studentDashboard(student):
    print(student)
    return render_template('studentDashboard.html',student=student)



@app.route("/generate_test",methods = ["POST"])
def generate_test():
    today = date.today()
    datesubmitted = today.strftime("%d/%m/%Y")
    if request.method == "POST":
        print("post called")
        rawdata = request.form["rawdata"]
        testType = request.form["testradio"] 
        teacherid = request.form["teacherId"]
        subject = request.form["subject"] 
        print("got data")
        if testType == "0":
            print("testtype aa gya")
            objective_generator = ObjectiveTest(rawdata)
            question_list, answer_list = objective_generator.generate_test()
            print("test generated")
            for ans in answer_list:
                global_answers.append(ans)
            db = database()
            db.set_test(teacherid,subject,"Objective Test",datesubmitted,question_list)
            print("data send to db")
            print(global_answers)
            return redirect(url_for('teacherDashboard'))
    return render_template('attemptTestObjective.html')

@app.route("/result/<id>")
def result(id):
    db = database()
    result = db.get_resultbytestid(id)
    return render_template("teacherViewResult.html",result = result)
 

@app.route("/studentViewResult")
def studentViewResult():
    
    return render_template('studentViewResult.html')

# student pages ----End

# teacher pages -------start
@app.route("/teacherDashboard")
def teacherDashboard():
    db = database()
    teacher = db.get_teacher(session["id"])
    print("teacher got")
    tests = db.get_testsbyid(session["id"])
    print("test got")
    return render_template('teacherDashboard.html',teacher=teacher, tests=tests)

@app.route("/teacherViewResult")
def teacherViewResult():
    
    return render_template('teacherViewResult.html')
# teacher pages -------End
     