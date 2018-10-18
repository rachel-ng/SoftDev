from flask import Flask, render_template, request
app = Flask(__name__)  # create instance of class Flask

import cgi

@app.route("/")
def home():
    print(app)
    return render_template("forms.html", title = "hi")

@app.route("/auth", methods=["GET", "POST"])
def authenticate():
    print(app)
    print(request)
    print(request.args)

    m = {}
    if request.method == "GET":
        m = request.args
    if request.method == "POST":
        m = request.form
    return render_template("template.html",
                           title = "hi",
                           username = m['username'],
                           rmethod = request.method)#,
                          # fullpath = request.full_path)
    # return "hi " + request.args['username'] + "<br>your request method was " + request.method + "<br> your full path is " + request.full_path


if __name__ == "__main__":
    app.debug = True
    app.run()
