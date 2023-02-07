from flask import Flask, render_template, request

abc = Flask(__name__)

@abc.route("/")
@abc.route("/index")
@abc.route("/home")
def hello():
    return render_template("home.html")

@abc.route("/about")
def about():
    return "About Page"

@abc.route("/myform", methods=["GET", "POST"])
def myform():
    if request.method == "POST":
        user=request.form["username"]
        password=request.form["password"]
        return render_template("myform.html", user=user)
    else:
        return render_template("myform.html")

@abc.route('/name/<string:s>')
def name(s):
    return "Hello "+s

if __name__ == "__main__":
    abc.run(debug=True)