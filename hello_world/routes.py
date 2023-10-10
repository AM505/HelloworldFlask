import os
from flask import ( render_template, 
    redirect, request, session, url_for, flash)
from hello_world import app
if os.path.exists("env.py"):
    import  env


@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html")