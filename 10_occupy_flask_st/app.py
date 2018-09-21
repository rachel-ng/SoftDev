# Rachel Ng
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-21

from flask import Flask, render_template
app = Flask(__name__)

import util.auxiliary as aux
# imported module

@app.route("/occupations")
def test_tmplt():
    return render_template("tmplt.html", title = "Occupations in The United States", dict = aux.d(), randomOccupation = aux.randocc())

if __name__ == "__main__":
    app.debug = True
    app.run()
