# Indeed Web Scraper Application v1.0
# Author: Christopher Hardy
# Description: Utilizes selenium webdriver in conjunction with chromedriver and beautiful soup to scrape 
# relevant web data.

import requests
import time
import pageContent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Initialize webdriver
web = webdriver.Chrome("C:\\Users\\Chris\\source\\chromedriver.exe")
startUrl = "https://www.indeed.com"
web.get(startUrl)

# Find search fields, input search parameters, and search
def searchHomePage():
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

# Main Function
def main():
    searchHomePage()
    time.sleep(5)
    currentPage = pageContent.getPageContent.grabPage()

    # Check to see if job listings were found
    try:
        checkForJobs = web.find_element_by_xpath('//*[@id="resultsCol"]/div[2]/div/h1')
        print("No jobs found.\n")
        jobExists = False
    except Exception:
        print("Jobs found.\n")
        jobExists = True

    # If job listings were found, crawl job postings
    if (jobExists):
        jobTiles = web.find_elements_by_css_selector('*[class="job_seen_beacon"]')
        jobsPage = currentPage.find(id, "searchCountPages")
        print(len(jobTiles), " jobs found on page " + jobsPage + ".\n")

        for jobTile in jobTiles:
            jobTile.click()
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

            print(jobTitleElement.text.strip())
            print(companyElement.text.strip())
            print(locationElement.text.strip())
            print()

            web.switch_to.default_content()
    else:
        pass

    web.quit()

main()