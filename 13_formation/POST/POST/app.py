from flask import Flask, render_template, request
app = Flask(__name__)  # create instance of class Flask

import cgi

@app.route("/", methods=["GET", "POST"])
def home():
    print(app)
    return render_template("forms.html", title = "hi")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    return render_template("template.html",
                           title = "hi",
                           username = request.args['username'],
                           rmethod = request.method)#,
                          # fullpath = request.full_path)
    # return "hi " + request.args['username'] + "<br>your request method was " + request.method + "<br> your full path is " + request.full_path


if __name__ == "__main__":
    app.debug = True
    app.run()
