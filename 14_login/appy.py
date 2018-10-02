from flask import Flask, render_template, session, request, url_for, redirect
from config import sec_key

app = Flask(__name__)
app.secret_key = sec_key

@app.route("/")
@app.route("/home")
def home():
	if len(session.keys()) > 0:
		if session['bob'] == request.cookies.get("username"): # if username ('bob') is the same as the one entered
			return render_template("logout.html") # returns logout page
		else:
			return redirect(url_for("error", msg = "corrupted cookie")) # returns error page

	return render_template("login.html") # returns login page

@app.route("/logout")
def logout():
	if len(session.keys()) > 0:  # if session is not empty, remove bob
		session.pop('bob')
	return render_template("login.html") # returns login page

@app.route("/login", methods=["POST"])
def login():
    if request.form.get('username') != 'bob':
        return redirect(url_for("error", msg = "wrong username")) # returns error page if wrong username
    elif request.form.get('passwd') != 'pass':
    	return redirect(url_for("error", msg = "wrong password")) # returns error page if wrong password
    else:
    	session[request.form.get('username')] = request.cookies.get("username") # add username to session
    return redirect(url_for("home")) # returns welcome page

@app.route("/error/<msg>")
def error(msg = "flask error"):
    # msg = "wrong username"
    return render_template("error.html", error_message = msg) # returns error page with message 
    

if __name__ == "__main__":
	app.debug = True
	app.run()
