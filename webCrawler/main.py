'''
Indeed Web Scraper Application v1.0
Author: Christopher Hardy
Description: Utilizes selenium webdriver in conjunction with chromedriver and beautiful soup to scrape
relevant web data.
'''

import requests
import time
import jobsfilecreator
import pagecontrols
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Globals
jfc = jobsfilecreator
pc = pagecontrols

# Initialize webdriver
web = webdriver.Chrome("C:\\Users\\Chris\\source\\chromedriver.exe")
pc.web = web
startUrl = "https://www.indeed.com"
web.get(startUrl)

# Main Function
def main():
    # Create job file if needed, search first page, and wait for search to complete
    jfc.create_file()
    pc.search_home_page()
    time.sleep(5)
    results = pc.get_page_content()

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

        # Iterate through each job in jobBoxes list
        for jobBox in jobBoxes:
            # Check for popup
            try:
                popupObj = web.switch_to.alert()
                popupMsg = web.find_element_by_xpath('//*[@id="popover-heading-what"]')
                print("Encountered a popup with the following message: " + popupMsg)
                popupObj.dismiss()
            except Exception:
                pass

            # Click job box and wait for iframe to update
            jobBox.click()
            time.sleep(2)

            # Switch to iframe for additional job info
            iframe = web.find_element_by_xpath('//*[@id="vjs-container-iframe"]')
            web.switch_to.frame(iframe)
            time.sleep(2)

            # Exception handling in case of extra images in job posting to get job title
            try:
                jobTitleElement = web.find_element_by_xpath('//div[1]/div[1]/h1')
            except Exception:
                jobTitleElement = web.find_element_by_xpath('//div[2]/div[1]/h1')
            else:
                pass
            # Exception handling in case of hyperlink to get company name
            try:
                companyElement = web.find_element_by_xpath('//div[1]/div[2]/div/div/div[1]/div')
            except Exception:
                companyElement = web.find_element_by_xpath('//div[2]/div[2]/div/div/div[1]/div[1]/a')
            else:
                pass
            # Exception handling for multiple xpaths to get job location
            try:
                locationElement = web.find_element_by_xpath('//div[1]/div[2]/div/div/div[2]')
            except Exception:
                locationElement = web.find_element_by_xpath('//div[2]/div[2]/div/div/div[2]')
            else:
                pass
            # Exception handling for salary
            try:
                salaryElement = web.find_element_by_xpath('//*[@id="jobDetailsSection"]/div[2]/span')
            except Exception:
                salaryElement = "No salary listed."
            else:
                pass

            # Send job text to be written to csv file
            jfc.jobTitle = jobTitleElement.text.strip()
            jfc.companyName = companyElement.text.strip()
            jfc.jobLocation = locationElement.text.strip()
            print(jobTitleElement.text.strip())
            print(companyElement.text.strip())
            print(locationElement.text.strip())

            # Check if salaryElement is passed as a string or text attribute
            if (type(salaryElement) == str):
                jfc.jobSalary = salaryElement
                print(salaryElement)
            else:
                jfc.jobSalary = salaryElement.text.strip()
                print(salaryElement.text.strip())
            print()

            # Execute file_io script
            jfc.file_io()

            # Switch out of iframe
            web.switch_to.default_content()
    else:
        pass

    web.quit()

main()