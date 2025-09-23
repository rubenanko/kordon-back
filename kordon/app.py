from flask import Flask,request
from flask_cors import CORS
from database import *
import ollama

import configparser
import time
import os


#flask
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

CONFIG["AVAILABLE_LLMS"] = CONFIG["AVAILABLE_LLMS"].split(" ")

#config
CONFIG_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0],"config.ini")
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

@app.route('/api/v1/auth/login',methods=['POST'])
def login():
    token = request.get_json()["token"]
    response = {"success": True } if token == "test" else {"success": False }
    return response

@app.route('/api/v1/request/llm',methods=['POST'])
def login():
    token = request.get_json()["token"]
    model = request.get_json()["model"]
    messages = request.get_json()["messages"]

    if check_token(token):
        if model in CONFIG["AVAILABLE_LLMS"]:
            response = ollama.chat(model=model, messages=messages, stream=True)
        response = {"response" : response['message']['content'], "status": "success" }
        else:   response = { "status": "unknown_model" }
    else:   response = { "status": "unknown_token" }
    return response