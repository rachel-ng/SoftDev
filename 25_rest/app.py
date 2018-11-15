import json, urllib

from flask import Flask, render_template, request
app = Flask(__name__)  # create instance of class Flask


URL_STUB = "https://archive.org/wayback/available?"
URL_QUERY = "url="
site = "https://archive.org/help/wayback_api.php"

URL = URL_STUB + URL_QUERY + site
print(URL)

@app.route("/")
def root():
    response = urllib.request.urlopen(URL)
    archived = json.loads(response.read())['archived_snapshots']
    if archived:
        d = archived['closest']
    else:
        d = {"available": "", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "timestamp": "YYYYMMDDhhmmss", "status": "400"}

    print(list(d.keys()))
    print(d)

    return render_template("base.html",
                           title = "Wayback Machine",
                           url = d['url'],
                           timestamp = d['timestamp'])




@app.route("/<time>")
def root_url(time):
    print(time)
    response = urllib.request.urlopen(URL + "&timestamp=" + time)
    archived = json.loads(response.read())['archived_snapshots']
    if archived:
        d = archived['closest']
    else:
        d = {"available": "", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "timestamp": "YYYYMMDDhhmmss", "status": "400"}

    print(list(d.keys()))
    print(d)

    return render_template("base.html",
                           title = "Wayback Machine",
                           url = d['url'],
                           timestamp = d['timestamp'])

if __name__ == "__main__":
    app.debug = True
    app.run()
