import os
from flask import Flask
if os.path.exists("env.py"):
    import  env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

from hello_world import routes