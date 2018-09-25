# Team R (Rachel Ng, Raymond Wu)
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-25

from flask import Flask, render_template
from util import halp

app = Flask(__name__)  # create instance of class Flask

@app.route("/")
def rootroute():
    return "<h2>Go to <a href='occupations'>/occupations</a>!</h2>"

# this function is assigned to a route...!
@app.route("/occupations")
def showOccupations():

    return render_template("occupationsTable.html",
                           occupations = halp.getOccupationsDict(),  # `occupation` here refers to Jinja var
                           randomOccupation = halp.getRandomOccupation()
                           # puts the keys to occupation dict in a list, choose randomly (weighted) from that list
                           # random.choices() returns a k-sized list (default=1) ... only concerned with first output
    )


if __name__ == "__main__":
    # must populate dictionary & list with data
    # these methods are not linked to a Flask route,
    # so not necessary that app is running...
    halp.csvToDict()
    halp.dictWeights()
    
    app.debug = True
    app.run()
