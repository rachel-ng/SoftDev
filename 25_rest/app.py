import json, urllib

from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)  # create instance of class Flask
app.secret_key = "asdfadsfjskdfjqweruioqwerjlkasdjfl;asdjfadlksfkjlfdsjkldfsjkl"

URL_STUB = "https://archive.org/wayback/available?"
URL_QUERY = "url="


@app.route("/", methods=['GET', 'POST'])
def root():
    site = "https://www.google.com"
    trigger = False
    
    if (request.form.get('site') != None):
        site = request.form.get('site')
        trigger = True

    URL = URL_STUB + URL_QUERY + site
        
    response = urllib.request.urlopen(URL)
    archived = json.loads(response.read())['archived_snapshots']

    if archived:
        d = archived['closest']
    else:
        d = {"available": False, "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "timestamp": "YYYYMMDDhhmmss", "status": "400"}
        
    print(list(d.keys()))
    print(d)

    flash("<a href=d['url']>The Site at d['timestamp']</a>")
    return render_template("base.html",
                           title = "The Wayback Machine",
                           available = trigger,
                           url = d['url'],
                           timestamp = d['timestamp'])

@app.route("/rr/<url>", methods=['GET', 'POST'])
def rr(url):
    site = "/"
    trigger = False
    
    if (request.form.get('site') != None):
        site = request.form.get('site')
        trigger = True

    URL = URL_STUB + URL_QUERY + site
        
    response = urllib.request.urlopen(URL)
    archived = json.loads(response.read())['archived_snapshots']

    if archived:
        d = archived['closest']
    else:
        d = {"available": False, "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "timestamp": "YYYYMMDDhhmmss", "status": "400"}
        
    print(list(d.keys()))
    print(d['url'])

    if (not(trigger)):
        return redirect('{url}'.format(url=d['url']))
    else:
        return render_template("base.html",
                           title = "The Wayback Machine",
                           available = trigger,
                           url = d['url'],
                           timestamp = d['timestamp'])




#@app.route("/<time>")
#def root_time(time):
#    print(time)
#
#    URL = URL_STUB + URL_QUERY + site

#    response = urllib.request.urlopen(URL + "&timestamp=" + time)
#    archived = json.loads(response.read())['archived_snapshots']
#    if archived:
#        d = archived['closest']
#    else:
#        d = {"available": "", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "timestamp": "YYYYMMDDhhmmss", "status": "400"}

#    print(list(d.keys()))
#    print(d)
#
#    return render_template("base.html",
#                           title = "Wayback Machine",
#                           url = d['url'],
#                           timestamp = d['timestamp'])

if __name__ == "__main__":
    app.debug = True
    app.run()
