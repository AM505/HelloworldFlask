import os
from flask import Flask
from hello_world import app
if os.path.exists("env.py"):
    import  env


@app.route("/")
@app.route("/index")
def hello():
    return "<h1>Hello World!</h1>"