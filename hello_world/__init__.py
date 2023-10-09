import os
from flask import Flask
if os.path.exists("env.py"):
    import  env

app = Flask(__name__)

from hello_world import routes