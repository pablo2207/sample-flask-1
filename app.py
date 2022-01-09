from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello my friend!",200
    #return render_template("index.html")
