'''
io.py is used to receive input from the C++ GUI
'''

import pagecontrols

# Globals
pc = pagecontrols
lines = []

# Function to get data from file and store in list
def get_data():
    f = open("", "r")

    for line in f:
        lines.append(line)

    f.close()

# Function to set data from list into search variables
def set_data():
    pc.jobType = lines[1]
    pc.jobLocation = lines[2]