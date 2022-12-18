import trafilatura
from flask import Flask, request
from flask import render_template
from trafilatura.settings import use_config

app = Flask(__name__)

newconfig = use_config("trafilatura.cfg")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/extract")
def extractUrl():
    try:
        url = request.args.get('url', default="https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/")
        downloaded = trafilatura.fetch_url(url)
        result = trafilatura.extract(downloaded, config=newconfig)
        return result
    except:
        return "An error occured.."
