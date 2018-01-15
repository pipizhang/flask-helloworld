#!/bin/env python
from flask import Flask
from flask import request
from flask import render_template
from lib import os
from lib import helper

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", msg="It works")

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name="Flask"):
    return render_template("hello.html", name=name.strip().title())

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
def top():
    return helper.mtop()

if __name__ == "__main__":
    app.run(port=3000)

