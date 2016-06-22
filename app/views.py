from flask import render_template, url_for
from app import meuapp

@meuapp.route('/')
def index():
    return render_template("index.html")

