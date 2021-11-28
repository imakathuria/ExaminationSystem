from flask import * 
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
@app.route("/login")
def login():
     
    return render_template('')   
@app.route("/logout")
def login():
     
    return render_template('') 

@app.route("/signup")
def login():
     
    return render_template('') 

# static routes -- End
# student pages --- Start
@app.route("/studentDashboard")
def studentDashboard():
     
    return render_template('studentDashboard.html')



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
     