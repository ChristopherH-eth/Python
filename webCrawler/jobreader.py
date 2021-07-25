'''
jobreader.py is used to receive input from the C++ GUI
'''

import pagecontrols

# Globals
pc = pagecontrols

# Function to get data from file, store in list, and set pagecontrol variables
def get_data():
    # Change "f" to local path
    f = open("C:\\Users\\chris\\source\\repos\\C-Plus-Plus\\VA_GUI\VA_GUI\\jobtemp.txt", "r")
    lines = f.readlines()
    f.close()

    pc.jobType = lines[0]
    pc.jobLocation = lines[1]