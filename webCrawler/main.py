# Web Scraper Application v1.0

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

web = webdriver.Chrome("D:\\Chris\\source\\chromedriver.exe")
url = "https://www.indeed.com"
web.get(url)
page = requests.get(url)
content = BeautifulSoup(page.content, "html.parser")

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

checkForJobs = web.find_element_by_xpath('//*[@id="resultsCol"]/div[2]/div/h1')

if "could not be found" in checkForJobs.text:
    print("No jobs found.")
else:
    results = content.find(class_="table-search-listings")
#job_elements = results.find_all("div", class_="card-content")
#python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
#python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]


#for job_element in job_elements:
#    title_element = job_element.find("h2", class_="title")
#    company_element = job_element.find("h3", class_="company")
#    location_element = job_element.find("p", class_="location")
#    print(title_element.text.strip())
#    print(company_element.text.strip())
#    print(location_element.text.strip())
#    print()

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