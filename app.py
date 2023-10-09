import os
from flask import Flask
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"