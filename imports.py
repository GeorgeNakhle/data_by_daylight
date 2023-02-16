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

class role(Enum):
    survivor = 'Survivor'
    killer = 'Killer'
    shared = 'General'

class rarity(Enum):
    common = 'Common'
    uncommon = 'Uncommon'
    rare = 'Rare'
    veryrare = 'Very Rare'
    ultrarare = 'Ultra Rare'
    specialevent = 'Special Event'
    artifact = 'Artifact'
    legendary = 'Legendary'

class eventType(Enum):
    bloodpoints = 'Bloodpoints'
    special = 'Special'

class itemType(Enum):
    medkit = 'Med-Kit'
    flashlight = 'Flashlight'
    toolbox = 'Toolbox'
    map = 'Map'
    key = 'Key'
    firecracker = 'Firecracker'
    limited = 'Limited'

#endregion

#region FUNCTIONS

def clearFolder(folder):
    if folder == None:
        return
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
    if url == None:
        return
    path = "images/"
    for folder in url.split('/')[2:]:
        path += "{}/".format(folder)
    return path[:-1]

def getSpeedMS(value):
    if value == None:
        return
    return value / 100;

def getSpeedPercentage(value):
    if value == None:
        return
    return 100 * value / 400;

def getTerrorRadius(value):
    if value == None:
        return
    return value / 100;

def successMessage(file):
    if file == None:
        return
    print(bcolors.OKGREEN + "{} created!".format(file) + bcolors.ENDC)

#endregion