from flask import render_template
from app import meuapp
from app.models import citations
import re
counter = 0


@meuapp.route('/')
def index():
    return render_template("index_pt.html")


@meuapp.route('/pt-BR')
def index_portuguese():
    return render_template("index_pt.html")


@meuapp.route('/ramq')
def ranQuotes():
    content = "Default"
    author = "Default"
    global counter
    counter += 1
    print(citations.arrayCitations)

    content = citations.arrayCitations[counter]["content"][3:-5]
    content = re.sub(r"&#.{4};", " ", content)
    content = re.sub(r'<br />', " ", content)
    author = "- " + citations.arrayCitations[counter]["title"]
    twitter = "http://twitter.com/home/?status=" + content

    if (counter == 40):
        counter = 0

    return render_template('quotes.html', content=content, author=author, twitter=twitter)
