# Team R (Rachel Ng, Raymond Wu)
# SoftDev1 pd7
# K10 -- Jinja Tuning
# 2018-09-25

from flask import Flask, render_template
app = Flask(__name__)  # create instance of class Flask

import util.auxiliary as aux #imports python functions

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
    # app doesn't need to be running to populate dictionary w. data
    aux.csvToDict()
    aux.dictWeights()
    
    app.debug = True
    app.run()
