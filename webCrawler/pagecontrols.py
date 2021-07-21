'''
pagecontrols.py is used to store page control functions
'''

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# Globals
web = ""

# Find search fields, input search parameters, and search
def search_home_page():
    jobType = "Software Developer"
    jobLocation = "Remote"

    what = web.find_element_by_xpath('//*[@id="text-input-what"]')
    what.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    what.send_keys(jobType)

    where = web.find_element_by_xpath('//*[@id="text-input-where"]')
    where.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    where.send_keys(jobLocation)

    searchButton = web.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
    searchButton.click()

# Retrieve current page content
def get_page_content():
    url = web.current_url
    page = requests.get(url)
    pageContent = BeautifulSoup(page.content, "html.parser")
    results = pageContent.find(id="resultsBody")
    return results