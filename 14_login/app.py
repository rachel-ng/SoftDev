from flask import Flask, render_template, session, request, url_for, redirect
from config import sec_key

app = Flask(__name__)
app.secret_key = sec_key

usr = "bob"
pw = "pass"

pri = False

def p(nt): # turn printing messages on and off
    if pri == True: 
        print (nt)
        
@app.route("/")
@app.route("/home")
def home():
    p("")
    p("home")
    p(session)
    if len(session.keys()) > 0:
        return render_template("logout.html",
                               username = session["username"])
    return render_template("login.html")
            
@app.route("/login", methods=["POST"])
def login():
    p("")
    p("logging in...\tuser: " + request.form["username"])
    if request.form["username"] != usr and request.form["passwd"] != pw: # both wrong
        session["msg"] = "wrong username and password"
        return redirect(url_for("error"))
    if request.form["username"] != usr:  # wrong username
        session["msg"] = "wrong username"
        return redirect(url_for("error"))
    if request.form["passwd"] != pw:  # wrong password
        session["msg"] = "wrong password"
        return redirect(url_for("error"))
    else:
        session["username"] = request.form["username"]
        #request.cookies.get("username") - returns None
        session["passwd"] = request.form["passwd"]
        #request.cookies.get("passwd") - returns None
        p(session)
    return redirect(url_for("home"))

@app.route("/error")
def error():
    p("")
    p("oof - an error has occured: " + session["msg"])
    problem = session["msg"] # stores error message
    session.clear() # clears session so we can try logging in again
    return render_template("error.html", error_message = problem) 

@app.route("/logout", methods=["POST"])
def logout():
    p("")
    p("logging out...")
    if request.form["sub1"] == "Logout":
        # session.pop("username")
        # session.pop("passwd")
        # session.pop("msg")
        session.clear() # clears session
        return render_template("home.html") 


if __name__ == "__main__":
	app.debug = True
	app.run()
