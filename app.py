import trafilatura
from flask import Flask, render_template, request
from flask_cors import CORS
from trafilatura.settings import use_config

app = Flask(__name__)
CORS(app)

cfg = use_config("trafilatura.cfg")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/extract")
def extractUrl():
    try:
        url = request.args.get('url', default="https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/")
        downloaded = trafilatura.fetch_url(url)
        result = trafilatura.extract(downloaded, config=cfg)
        return result
    except:
        return "An error occured.."

@app.route("/extract/json")
def extractUrl():
    try:
        url = request.args.get('url', default="https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/")
        downloaded = trafilatura.fetch_url(url)
        result = trafilatura.extract(downloaded, output_format="json", include_comments=False, config=cfg)
        return result
    except:
        return "An error occured.."
