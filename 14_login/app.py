from flask import Flask, render_template, session, request, url_for, redirect
from config import sec_key

app = Flask(__name__)
app.secret_key = sec_key # secret key, make sure others can't see!

usr = "bob" 
pw = "pass"

pri = True
def p(nt): # turn printing messages on and off
    if pri == True: 
        print (nt)

@app.route("/") # for both root and /home
@app.route("/home")
def home():
    p("")
    p("home")
    p(session)
    
    if len(session.keys()) > 0: # if session isn't empty, return home page w/ greeting
        return render_template("logout.html", username = session["username"])
    return render_template("login.html") # return login page
            
@app.route("/login", methods=["POST"])
def login():
    p("")
    p("logging in...\tuser: " + request.form["username"])
    
    if request.form["username"] != usr and request.form["passwd"] != pw: # both wrong error page
        session["msg"] = "wrong username and password"
        return redirect(url_for("error"))
    elif request.form["username"] != usr: # wrong username error page
        session["msg"] = "wrong username"
        return redirect(url_for("error")) 
    elif request.form["passwd"] != pw: # wrong password error page
        session["msg"] = "wrong password"
        return redirect(url_for("error"))
    else: # adds username and password to session
        session["username"] = request.form["username"]
        session["passwd"] = request.form["passwd"]
        # request.cookies.get("username") - returns None # attempt w/ cookies
        # request.cookies.get("passwd") - returns None # attempt w/ cookies
    p(session)
    return redirect(url_for("home")) # return home page

@app.route("/error")
def error():
    p("")
    p("oof - an error has occured: " + session["msg"])
    
    problem = session["msg"] # stores error message
    session.clear() # clears session so we can try logging in again
    return render_template("error.html", error_message = problem) # return error page

@app.route("/logout", methods=["POST"])
def logout():
    p("")
    p("logging out...")
    
    if request.form["sub1"] == "Logout": # logout button
        session.clear() # clears session
        # session.pop("username") # session.pop("passwd") # session.pop("msg")
        return render_template("home.html") # return home page


if __name__ == "__main__":
	app.debug = True
	app.run()
