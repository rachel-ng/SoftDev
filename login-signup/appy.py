from flask import Flask, render_template, session, request, url_for, redirect
from config import sec_key

app = Flask(__name__)
app.secret_key = sec_key

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.form['username'] != 'bob':
        session["msg"] = "wrong username"
        return redirect(url_for("error"))
    else:
        session["username"] = request.cookies.get("username")
    return render_template("home.html")

@app.route("/error")
def error():
    # msg = "wrong username"
    return render_template("error.html", error_message = session["msg"])
    

if __name__ == "__main__":
	app.debug = True
	app.run()
