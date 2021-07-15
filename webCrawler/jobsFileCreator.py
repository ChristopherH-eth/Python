import os
import csv
from datetime import date

jobTitle = ""
companyName = ""
jobLocation = ""

def file_io():
    path = "D:\\Chris\\source\\repos\\Python\\webCrawler\\"
    today = date.today()
    today_ = today.strftime("%d-%m-%Y")
    fileName = path + "jobs_from_" + today_ + ".csv"

    f = open(fileName, "a+")
    f.write(jobTitle)

    f.close()