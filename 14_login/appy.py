from flask import Flask, render_template, session, request, url_for, redirect
from config import sec_key

app = Flask(__name__)
app.secret_key = sec_key

@app.route("/")
@app.route("/home")
def home():
	if len(session.keys()) > 0:
		if session['bob'] == request.cookies.get("username"):
			return render_template("logout.html")
		else:
			return redirect(url_for("error", msg = "corrupted cookie"))

	return render_template("login.html")

@app.route("/logout")
def logout():
	if len(session.keys()) > 0:
		session.pop('bob')
	return render_template("login.html")



@app.route("/login", methods=["POST"])
def login():
    if request.form.get('username') != 'bob':
        return redirect(url_for("error", msg = "wrong username"))
    elif request.form.get('passwd') != 'pass':
    	return redirect(url_for("error", msg = "wrong password"))
    else:
    	session[request.form.get('username')] = request.cookies.get("username")
    return redirect(url_for("home"))

@app.route("/error/<msg>")
def error(msg = "flask error"):
    # msg = "wrong username"
    return render_template("error.html", error_message = msg)
    

if __name__ == "__main__":
	app.debug = True
	app.run()
