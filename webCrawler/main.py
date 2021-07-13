import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com"
page = requests.get(URL)

pageContent = BeautifulSoup(page.content, "html.parser")