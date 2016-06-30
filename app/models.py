import requests


class Citar():
    url = "https://crossorigin.me/http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=40&callback="
    arrayCitations = []

    def __init__(self):
        self.arrayCitations = requests.get(self.url).json()

citations = Citar()
