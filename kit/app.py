from flask import Flask, render_template
app = Flask(__name__)  # create instance of class Flask

@app.route("/")
def home():
    return "que"

if __name__ == "__main__":
    app.debug = True
    app.run()

