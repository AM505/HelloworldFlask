import os
from flask import Flask
from hello_world import app
if os.path.exists("env.py"):
    import hello_world.env as env


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"