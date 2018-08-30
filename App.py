# App.py is designed to read raw data from a file, select a particular data set, and write it to a separate file in ascending order.
# The output seems to be correct, although there is doubt regarding the second half of the phrase.
# My goal here was to essentailly gather/read/convert necessary data, isolate the given range, sort said range, and write the desired data to a new file.

import csv
import datetime

with open('sample_data.csv', encoding = "utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')

    header = next(reader) # The first line contains column names

    date_format = "%m/%d/%Y %H:%M:%S"
    dates = []
    words = []
    i = 0

    for row in reader: # Read the csv data, convert dates to readable values
        date = row[1]
        word = row[8]
        date_converted = datetime.datetime.fromtimestamp(float(date)).strftime(date_format)

        if datetime.datetime.strptime("6/22/2014 0:00:00", date_format) <= datetime.datetime.strptime(date_converted, date_format) <= datetime.datetime.strptime("7/22/2014 23:59:59", date_format): # Only list dates that fall between the range of June 22, 2014 through July 22, 2014
            dates.append(date_converted)
            words.append(word)

    sort = sorted(zip(dates, words)) # Sort both lists based on the date
    dates, words = map(list, zip(*sort))

with open('D:/Data/new_data.csv', 'w') as csvfile: # Write both lists to a predetermined file
    writer = csv.writer(csvfile, delimiter = ',')
    writer.writerow(["Date", "Word"])

    for i in range(len(dates)): # Loop through and write lists to file maintaining one entry per line
        writer.writerow([dates[i], words[i]])
        i + 1



