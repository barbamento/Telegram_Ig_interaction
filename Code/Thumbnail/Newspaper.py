from bs4 import BeautifulSoup
import requests


class Article:
    def __init__(self, url: str):
        self.req = requests.get(url)
