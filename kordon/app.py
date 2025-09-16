from flask import Flask,request
from flask_cors import CORS

import configparser
import time
import os

#flask
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#config
CONFIG_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0],"config.ini")
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

@app.route('/api/v1/auth/login',methods=['POST'])
def login():
    token = request.get_json()["token"]
    response = {"success": True } if token == "test" else {"success": False }
    return response