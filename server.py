#!/bin/env python
from flask import Flask
from flask import request
from lib import os
from lib import helper

app = Flask(__name__)

@app.route("/")
def home():
    return "It works"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/uname")
def uname():
    return os.uname(request.args.get("all")=="1")

@app.route("/whoami")
def whoami():
    return os.whoami()

@app.route("/df")
def df():
    return os.df()

@app.route("/top", methods=["GET", "POST"])
def hello():
    return helper.mtop()

@app.route("/park")
def pk():
    return helper.park()

app.run(port=3000)

