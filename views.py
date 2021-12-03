from flask import * 
from database  import *
from datetime import date
from objective import ObjectiveTest
from evaluatetest import EvaluateTest  


app = Flask(__name__)
app.secret_key = 'aiexaminationsystemquestionanswergenrator'

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
@app.route("/logout")
def logout():
    if session["user"] ==1:
        session.clear("studentid",None)
        return redirect(url_for('login')) 
    if session["user"] ==0:
        session.clear("teacher",None)
        return redirect(url_for('login')) 

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
                student = row[0]
                session["user"] = "1"
                session["studentid"] = student["id"]
                return redirect(url_for('studentDashboard')) 
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
                session["teacherid"] = teacher["id"]
                return redirect(url_for('teacherDashboard')) 
    if request.method == "GET":
        return render_template('loginForm.html') 

# static routes -- End
# student pages --- Start
@app.route("/studentDashboard")
def studentDashboard():
    db = database()
    student= db.get_student(session["studentid"])
    tests= db.get_tests();
    return render_template('studentDashboard.html',student=student, tests=tests)



@app.route("/attempttest/<testtype>/<testid>")
def attempttest(testtype,testid):
    db = database()
    db1 = database()
    student= db.get_student(session["studentid"])
    test= db1.get_testsbytestid(testid);
    if(testtype =='Objective Test'):
        return render_template('attemptTestObjective.html',student=student, test=test)
    if(testtype =='Subjective Test'):
        return render_template('attemptTestSubjective.html',student=student, test=test)

@app.route("/submittest", methods = ["POST"])
def submittest():
    db = database()
    user_ans = list()
    user_ans.append(str(request.form["objectiveans1"]).strip().upper())
    user_ans.append(str(request.form["objectiveans2"]).strip().upper())
    user_ans.append(str(request.form["objectiveans3"]).strip().upper())
    user_ans.append(str(request.form["objectiveans4"]).strip().upper())
    user_ans.append(str(request.form["objectiveans5"]).strip().upper())
    testid = request.form["testid"]
    testtype = request.form["testtype"]
    teacherid = request.form["teacherid"]
    studentroll = request.form["studentroll"]
    studentname = request.form["studentname"]
    subject = request.form["subject"]
    et = EvaluateTest()
    result,total_score = et.evalute_objective_test(testid, user_ans)
    db.set_result(testid,testtype,teacherid,studentroll,studentname,subject,total_score,result)
    return redirect(url_for('studentDashboard'))

@app.route("/viewstudentresult/<testid>/<studentroll>")
def viewstudentresult(testid,studentroll):
    db = database()
    result = db.get_result_by_roll(testid,studentroll)
    return render_template("studentViewResult.html",result = result)

# student pages ----End

# teacher pages -------start

@app.route("/teacherDashboard")
def teacherDashboard():
    db = database()
    teacher = db.get_teacher(session["teacherid"])
    print("teacher got")
    tests = db.get_testsbyid(session["teacherid"])
    print("test got")
    return render_template('teacherDashboard.html',teacher=teacher, tests=tests)

@app.route("/result/<id>")
def result(id):
    db = database()
    result = db.get_resultbytestid(id)
    return render_template("teacherViewResult.html",result = result)

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
            db = database()
            db.set_test(teacherid,subject,"Objective Test",datesubmitted,question_list,answer_list)
            print("data send to db")
            return redirect(url_for('teacherDashboard'))
    return render_template('attemptTestObjective.html')


     