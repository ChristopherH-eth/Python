'''
Indeed Web Scraper Application v1.0
Author: Christopher Hardy
Description: Utilizes selenium webdriver in conjunction with chromedriver and beautiful soup to scrape
relevant web data.
'''

import requests
import time
import jobsFileCreator
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Globals
jfc = jobsFileCreator

# Initialize webdriver
web = webdriver.Chrome("D:\\Chris\\source\\chromedriver.exe")
startUrl = "https://www.indeed.com"
web.get(startUrl)

# Find search fields, input search parameters, and search
def search_home_page():
    whatJob = "Software Developer"
    whatLocation = "Remote"

    what = web.find_element_by_xpath('//*[@id="text-input-what"]')
    what.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    what.send_keys(whatJob)

    where = web.find_element_by_xpath('//*[@id="text-input-where"]')
    where.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    where.send_keys(whatLocation)

    searchButton = web.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
    searchButton.click()

# Retrieve current page content
def get_page_content():
    url = web.current_url
    page = requests.get(url)
    pageContent = BeautifulSoup(page.content, "html.parser")
    results = pageContent.find(id="resultsBody")
    return results

# Main Function
def main():
    search_home_page()
    time.sleep(5)
    results = get_page_content()

    # Check to see if job listings were found
    try:
        checkForJobs = web.find_element_by_xpath('//*[@id="resultsCol"]/div[2]/div/h1')
        print("No jobs found.\n")
        jobExists = False
    except Exception:
        jobExists = True

    # If job listings were found, crawl job postings
    if (jobExists):
        jobBoxes = web.find_elements_by_css_selector('*[class="job_seen_beacon"]')
        jobsPage = results.find("div", id="searchCountPages")
        print(len(jobBoxes), "Jobs Found on " + jobsPage.text.strip()[0:6] + ".\n")

        for jobBox in jobBoxes:
            jobBox.click()
            time.sleep(2)

            # Switch to iframe for additional job info
            iframe = web.find_element_by_xpath('//*[@id="vjs-container-iframe"]')
            web.switch_to.frame(iframe)
            time.sleep(2)

            # Exception handling in case of extra images in job posting
            try:
                jobTitleElement = web.find_element_by_xpath('//div[1]/div[1]/h1')
            except Exception:
                jobTitleElement = web.find_element_by_xpath('//div[2]/div[1]/h1')
            else:
                pass
            # Exception handling in case of hyperlink
            try:
                companyElement = web.find_element_by_xpath('//div[1]/div[2]/div/div/div[1]/div')
            except Exception:
                companyElement = web.find_element_by_xpath('//div[2]/div[2]/div/div/div[1]/div[1]/a')
            else:
                pass
            # Exception handling for multiple xpaths
            try:
                locationElement = web.find_element_by_xpath('//div[1]/div[2]/div/div/div[2]')
            except Exception:
                locationElement = web.find_element_by_xpath('//div[2]/div[2]/div/div/div[2]')
            else:
                pass

            # Send job text to be written to csv file
            jfc.jobTitle = jobTitleElement.text.strip()
            jfc.companyName = companyElement.text.strip()
            jfc.jobLocation = locationElement.text.strip()
            print(jobTitleElement.text.strip())
            print(companyElement.text.strip())
            print(locationElement.text.strip())
            print()

            jfc.file_io()

            web.switch_to.default_content()
    else:
        pass

    web.quit()

main()