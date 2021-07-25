'''
pagecontrols.py is used to store page control functions
'''

import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# Globals
web = ""
jobType = ""
jobLocation = ""

# Find search fields, input search parameters, and search
def search_home_page():
    what = web.find_element_by_xpath('//*[@id="text-input-what"]')
    what.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    what.send_keys(jobType)

    where = web.find_element_by_xpath('//*[@id="text-input-where"]')
    where.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    where.send_keys(jobLocation)

    time.sleep(2)

    # Check for popup
    try:
        emailPopup = web.find_element_by_xpath('//*[@id="popover-email"]')
        emailPopup.send_keys(Keys.ESCAPE)
        print("Popup detected.")
        time.sleep(1)
    except Exception:
        pass

    # Find correct search button
    try:
        searchButton = web.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
        searchButton.click()
    except:
        searchButton = web.find_element_by_xpath('//*[@id="jobsearch"]/button')
        searchButton.click()
    else:
        pass

# Retrieve current page content
def get_page_content():
    url = web.current_url
    page = requests.get(url)
    pageContent = BeautifulSoup(page.content, "html.parser")
    results = pageContent.find(id="resultsBody")
    return results