'''
jobsfilecreator.py is used for file I/O controls
'''

import os
import csv
from datetime import date

# Globals
today = date.today()
today_ = today.strftime("%d-%m-%Y")
# Change "path" to local path
path = "C:\\Users\\Chris\\source\\repos\\Python\\webCrawler\\"
fileName = path + "jobs_from_" + today_ + ".csv"

jobTitle = ""
companyName = ""
jobLocation = ""
jobSalary = ""

# Check for file existence.  Create file if it doesn't exist.
def create_file():
    print("Checking for file.")
    if os.path.exists(fileName):
        print("File exists.")
    else:
        print("File does not exist.  Creating file.")
        f = open(fileName, "w", encoding="UTF8")
        writer = csv.writer(f)

        header = ["Job Title", "Company Name", "Job Location", "Salary"]
        writer.writerow(header)

        f.close()

# Append existing file.
def file_io():
    f = open(fileName, "a+", encoding="UTF8")
    writer = csv.writer(f, lineterminator="\n")

    data = [jobTitle, companyName, jobLocation, jobSalary]
    writer.writerow(data)

    f.close()
