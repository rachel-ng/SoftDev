# Team R (Rachel Ng, Raymond Wu)
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-25

import util.auxiliary as aux
from flask import Flask, render_template

app = Flask(__name__)  # create instance of class Flask

@app.route("/")
def rootroute():
    return "<h2><a href='/occupations'>Click here for /occupations</a></h2>" # link to /occupations


# this function is assigned to a route...!
@app.route("/occupations")
def showOccupations():
    return render_template("occupationsTable.html",
                           occupations = aux.getOccupationsDict(),
                           randomOccupation = aux.getRandomOccupation()
    )


if __name__ == "__main__":
    # must populate dictionary & list with data
    # these methods are not linked to a Flask route,
    # so not necessary that app is running...
    aux.csvToDict()
    aux.dictWeights()
    
    app.debug = True
    app.run()
