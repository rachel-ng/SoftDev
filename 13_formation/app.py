from flask import Flask, render_template, request
app = Flask(__name__)  # create instance of class Flask

import cgi

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    print(request.args['username'])
    print(request.headers)
    return "hi " + request.args['username'] + "<br> your request method was" + request
#render_template("template.html", title = "hi", username = request.args['username'])

@app.route("/")
def home():
    #coll = [0,1,1,2,3,5,8]
    print(app)
    return render_template("forms.html", title = "hi") #, coll = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
