from flask import Flask
app = Flask(__name__)


@app.route("/")
def user():
    return "Welcome to GoGretzky API!"
