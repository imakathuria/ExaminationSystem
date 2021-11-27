from flask import * 
value = Markup('<strong>The HTML String</strong>')
import sqlite3
import json
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello_world():
    list1 = ['gautam','shaurya']   
    return render_template('index.html',b=list1)


@app.route("/contact")
def contact_us():
    return render_template('TeacherDashboard.html')


@app.route("/about")
def about_us():
    return render_template('AboutUs.html')

@app.route("/userlogin")
def user_login():
    return render_template('UserLoggedIn.html')

# @app.route("/student_info")
# def student_info():
#     connection = sqlite3.connect("student_detials.db")
#     connection.row_factory = sqlite3.Row
#     cursor = connection.cursor()
#     cursor.execute("select * from Student_Info")
#     rows = cursor.fetchall()
#     jsonStr = json.dumps([dict(ix) for ix in rows],ensure_ascii=False)
#     print(jsonStr)
#     return render_template("studentInfo.html",rows = jsonStr)    

if __name__ == '__main__':
    app.run(debug=True)    