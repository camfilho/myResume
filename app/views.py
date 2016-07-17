from flask import render_template
from app import meuapp


@meuapp.route('/')
def index():
    return render_template("index_pt.html")


@meuapp.route('/pt-BR')
def index_portuguese():
    return render_template("index_pt.html")


@meuapp.route('/en')
def index_english():
    return render_template("index.html")


@meuapp.route('/ramq')
def ranQuotes():
    return render_template('quotes.html')


@meuapp.errorhandler(404)
def page_not_found(e):
    return render_template("underconstruction.html"), 404
