#region IMPORTS

import os
import shutil
import json
import requests
import csv
from enum import Enum

#endregion

#region ENUMS

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class difficulty(Enum):
    easy = 'Easy'
    intermediate = 'Intermediate'
    hard = 'Hard'
    veryhard = 'Very Hard'

class gender(Enum):
    male = 'Male'
    female = 'Female'
    multiple = 'Multiple'
    nothuman = 'N/A'

#endregion

#region FUNCTIONS

def clearFolder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def getImagePath(url):
    path = "images/"
    for folder in url.split('/')[2:]:
        path += "{}/".format(folder)
    return path[:-1]

def getSpeedMS(value):
    return value / 100;

def getSpeedPercentage(value):
    return 100 * value / 400;

def getTerrorRadius(value):
    return value / 100;

def successMessage(file):
    print(bcolors.OKGREEN + "{} created!".format(file) + bcolors.ENDC)

#endregion