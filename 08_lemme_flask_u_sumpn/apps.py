from flask import Flask
app = Flask(__name__)

@app.route("/")
def func1():
      return '<a href="/mom"> Hi Mom! </a><br><a href="/dad"> Hi Dad! </a>'

@app.route("/mom")
def func2():
      return '<a href="/dad"> Hi Dad! </a><br><a href="/"> .-.</a>'
  
@app.route("/dad")
def func3():
      return '<a href="/mom"> Hi Mom! </a><br><a href="/"> .-.</a>'


if __name__ == "__main__":
    app.debug = True
    app.run()
