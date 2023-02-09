from flask import Flask, render_template, request, session, redirect
from mysql.connector import connect

con=connect(host='localhost'
            ,port=3306
            ,database='cse'
            ,user='root')
# cur=con.cursor()
# cur.execute("SELECT * FROM data where roll=%s",(roll))
# res=cur.fetchall()

abc = Flask(__name__)
abc.secret_key="hfuegik"

@abc.route("/")
@abc.route("/index")
@abc.route("/home")
def hello():
    session['user']='karthik'
    return redirect('myform')

@abc.route("/about")
def about():
    session.clear()
    return "About Page"

@abc.route("/myform", methods=["GET", "POST"])
def myform():
    if session.get('name'):
        return render_template("myform.html", user=session["name"])
    else:
        if request.method == "POST":
            name=request.form["name"]
            roll=request.form["roll"]
            cur=con.cursor()
            cur.execute("insert into data values(%s,%s)",(name,roll))
            con.commit()
            session["name"]=name
            return render_template("myform.html", user=name)
        else:
            return render_template("myform.html")

@abc.route('/name/<string:s>')
def name(s):
    return "Hello "+s

if __name__ == "__main__":
    abc.run(debug=True)