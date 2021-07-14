# Indeed Web Scraper Application v1.0
# Author: Christopher Hardy
# Description: Utilizes selenium webdriver in conjunction with chromedriver and beautiful soup to scrape 
# relevant web data.

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize webdriver
web = webdriver.Chrome("C:\\Users\\Chris\\source\\chromedriver.exe")
startUrl = "https://www.indeed.com"
web.get(startUrl)

# Initialize search variables
whatJob = "Software Developer"
whatLocation = "Remote"
jobExists = True

# Find search fields, input search parameters, and search
what = web.find_element_by_xpath('//*[@id="text-input-what"]')
what.send_keys(Keys.CONTROL, "a", Keys.DELETE)
what.send_keys(whatJob)

where = web.find_element_by_xpath('//*[@id="text-input-where"]')
where.send_keys(Keys.CONTROL, "a", Keys.DELETE)
where.send_keys(whatLocation)

searchButton = web.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
searchButton.click()

# Check to see if job listings were found
try:
    checkForJobs = web.find_element_by_xpath('//*[@id="resultsCol"]/div[2]/div/h1')
    print("No jobs found.")
    jobExists = False
except Exception:
    print("Jobs found.")
    jobExists = True

# If job listings were found, crawl job content
if (jobExists):
    url = web.current_url
    page = requests.get(url)
    pageContent = BeautifulSoup(page.content, "html.parser")
    results = pageContent.find(id="resultsCol")

    jobs = results.find_all("table", class_="jobCard-mainContent")
#python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
#python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

    for job_element in jobs:
        job_titles = [table_element.child.child.child.child.child.child for span_element in jobs]
        #title_element = job_element.find("h2", class_="jobTitle jobTitle-color-purple").child
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()
else:
    pass

#for python_job_element in python_job_elements:
#    title_element = python_job_element.find("h2", class_="title")
#    company_element = python_job_element.find("h3", class_="company")
#    location_element = python_job_element.find("p", class_="location")
#    link_url = python_job_element.find_all("a")[1]["href"]
#    print(f"Apply here: {link_url}\n")
#    print(title_element.text.strip())
#    print(company_element.text.strip())
#    print(location_element.text.strip())
#    print()