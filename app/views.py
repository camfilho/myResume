from flask import render_template
from app import meuapp
flag = False


@meuapp.route('/')
def index():
    global flag
    flag = False
    return render_template("index_pt.html")


@meuapp.route('/pt-BR')
def index_portuguese():
    return render_template("index_pt.html")


@meuapp.route('/en')
def index_english():
    global flag
    flag = True
    print(flag)
    return render_template("index.html")


@meuapp.route('/ramq')
def ranQuotes():
    return render_template('quotes.html')


@meuapp.errorhandler(404)
def page_not_found(e):
    print(flag)
    if (not(flag)):
        return render_template("underconstruction.html"), 404
    else:
        return render_template("underconstruction_en.html"), 404
