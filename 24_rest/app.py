from flask import Flask, render_template, request
app = Flask(__name__)  # create instance of class Flask

import urllib, json

apikey = "https://api.nasa.gov/planetary/apod?api_key=yZkZkfYZ6LFutD3Gau2DZY4mksEJKx8dSEELb4QM"

@app.route("/")
def root():
    response = urllib.request.urlopen(apikey)
    d = json.loads(response.read())
    
    print(list(d.keys()))
    print(d)

    return render_template("base.html",
                           title = d['title'],
                           media_type = d['media_type'],
                           url = d['url'],
                           explanation = d['explanation'])


@app.route("/<date>")
def root_date(date):
    response = urllib.request.urlopen(apikey + "&date=" + date)
    d = json.loads(response.read())

    print(list(d.keys()))
    print(d)

    return render_template("base.html",
                           title = d['title'],
                           media_type = d['media_type'],
                           url = d['url'],
                           explanation = d['explanation'])

    
if __name__ == "__main__":
    app.debug = True
    app.run()
