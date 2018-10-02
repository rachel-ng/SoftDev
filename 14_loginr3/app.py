from flask import Flask, render_template, session, request, url_for, redirect
from config import sec_key

app = Flask(__name__)
app.secret_key = sec_key

un = "bob"
pw = "pass"

@app.route("/")
def root():
    print ("root")
    print (session)
    if len(session.keys()) > 0:
        return render_template("logout.html",
                               username = session["username"])
    return render_template("login.html")
            
@app.route("/login", methods=["POST"])
def login():
    print ("login")
    print(request.form["username"])
    if request.form["username"] != un and request.form["passwd"] != pw:
        session["msg"] = "wrong username and password"
        return redirect(url_for("error"))
    if request.form["username"] != un:
        session["msg"] = "wrong username"
        return redirect(url_for("error"))
    if request.form["passwd"] != pw:
        session["msg"] = "wrong password"
        return redirect(url_for("error"))
    else:
        session["username"] = request.form["username"] #request.cookies.get("username")
        session["passwd"] = request.form["passwd"] #request.cookies.get("passwd")
        print (session["username"])
        print (session["passwd"])
        print (session)
    return redirect(url_for("welcome"))

@app.route("/error")
def error():
    print ("oof - an error")
    return render_template("error.html", error_message = session["msg"])

@app.route("/home")
def welcome():
    print ("help, i've fallen and i can't get up")
    return render_template("logout.html",
                           username = session["username"])

@app.route("/logout", methods=["POST"])
def logout():
    print ("byeeeeeee")
    if request.form["sub1"] == "Logout":
        # session.pop("username")
        # session.pop("passwd")
        # session.pop("msg")
        session.clear() # clears session
        return render_template("home.html") 


if __name__ == "__main__":
	app.debug = True
	app.run()
