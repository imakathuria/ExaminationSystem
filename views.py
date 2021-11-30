from flask import * 
from database  import *



app = Flask(__name__)


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
            jsonstr = json.dumps([dict(ix) for ix in row])
            return redirect(url_for('studentDashboard',jsonstr)) 
        if request.form["options"] == "0" :
            print("Teacher Login request")
            username = request.form["username"]
            password = request.form["password"] 
            db = database()
            row = db.check_teacher(username,password)
            if row == False:
                return render_template('signupSucess.html')
            else:
                return render_template("teacherDashboard.html")
    if request.method == "GET":
        return render_template('loginForm.html') 

# static routes -- End
# student pages --- Start
@app.route("/studentDashboard/")
def studentDashboard(student):
    print(student)
    return render_template('studentDashboard.html',student=student)



@app.route("/test")
def getTest():
    
    return render_template('attemptTestObjective.html')

@app.route("/studentViewResult")
def studentViewResult():
    
    return render_template('studentViewResult.html')

# student pages ----End

# teacher pages -------start
@app.route("/teacherDashboard")
def teacherDashboard():
    
    return render_template('teacherDashboard.html')

@app.route("/teacherViewResult")
def teacherViewResult():
    
    return render_template('teacherViewResult.html')
# teacher pages -------End
     