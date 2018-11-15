import json, urllib

from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)  # create instance of class Flask
app.secret_key = "asdfadsfjskdfjqweruioqwerjlkasdjfl;asdjfadlksfkjlfdsjkldfsjkl"

CAT_FACTS = "https://catfact.ninja/fact"

RANDOM_CAT = "https://aws.random.cat/meow"

@app.route("/")
def root():
    cf = json.loads(urllib.request.urlopen(CAT_FACTS).read())
    rc = json.loads(urllib.request.urlopen(RANDOM_CAT).read())
    
    print(list(cf.keys()))
    print(cf)

    print(list(rc.keys()))
    print(rc)

    return render_template("base.html",
                           title = "Cats!",
                           img_src = rc['file'],
                           fact = cf['fact'])


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
