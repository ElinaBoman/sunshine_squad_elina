from flask import render_template, request, redirect, url_for
from appmanager import app

@app.route("/")
def home():
    return render_template("home.html")