import requests
from bs4 import BeautifulSoup
from main import web

# Retrieve current page content
class getPageContent:
    def grabPage(self):
        url = web.current_url
        page = requests.get(url)
        pageContent = BeautifulSoup(page.content, "html.parser")
        results = pageContent.find(id="resultsBody")

        return results