import json, urllib

from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)  # create instance of class Flask
app.secret_key = "asdfadsfjskdfjqweruioqwerjlkasdjfl;asdjfadlksfkjlfdsjkldfsjkl"

CAT_FACTS = "https://catfact.ninja/fact"

RANDOM_CAT = "https://aws.random.cat/meow"

ADVICE_SLIP = "https://api.adviceslip.com/advice"

@app.route("/")
def root():
    cf = json.loads(urllib.request.urlopen(CAT_FACTS).read())
    rc = json.loads(urllib.request.urlopen(RANDOM_CAT).read())
    ad = json.loads(urllib.request.urlopen(ADVICE_SLIP).read())

    
    print(list(cf.keys()))
    print(cf)

    print(list(rc.keys()))
    print(rc)
    
    print(list(ad.keys()))
    print(ad)


    return render_template("base.html",
                           title = "Cats!",
                           img_src = rc['file'],
                           fact = cf['fact'],
                           advice = ad['slip']['advice'])


if __name__ == "__main__":
    app.debug = True
    app.run()
