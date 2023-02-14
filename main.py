import os
import shutil
import json
import requests
import csv
from enum import Enum

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

#region general

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

def createMetadataCSV():
    file = open("./source_data/metadata.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["endpoint", "version", "lastupdate"])

    res = requests.get("https://dbd.tricky.lol/api/versions")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        writer.writerow([key, value["version"], value["lastupdate"]])

    file.close()
    successMessage("metadata.csv")

def createSurvivorCSV():
    file = open("./source_data/survivor.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "dlcID", "name", "gender", "bio", "lore", "image"])

    res = requests.get("https://dbd.tricky.lol/api/characters?role=survivor")
    response = json.loads(res.text)

    index = 0
    for i in response:
        writer.writerow([index, i["dlc"], i["name"], gender[i["gender"]].value, i["bio"], i["story"], getImagePath(i["image"])])
        index += 1

    file.close()
    successMessage("survivor.csv")

def createKillerCSV():
    file = open("./source_data/killer.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "dlcID", "powerID", "name", "difficulty", "gender", "bio", "lore", "speedMS", "speedPercentage", "terrorRadius", "image"])

    res = requests.get("https://dbd.tricky.lol/api/characters?role=killer")
    response = json.loads(res.text)

    for key, value in response.items():
        writer.writerow([key, value["dlc"], value["item"], value["name"], difficulty[value["difficulty"]].value, gender[value["gender"]].value, value["bio"], value["story"], getSpeedMS(value["tunables"]["maxwalkspeed"]), getSpeedPercentage(value["tunables"]["maxwalkspeed"]), getTerrorRadius(value["tunables"]["terrorradius"]), getImagePath(value["image"])])

    file.close()
    successMessage("killer.csv")

#endregion

#region MAIN

clearFolder("./source_data/")
createMetadataCSV()
createSurvivorCSV()
createKillerCSV()

#endregion

# Source: https://github.com/gatheringhallstudios/MHWorldData
# DB Model: https://lucid.app/lucidchart/9bb20e80-bc4d-4554-b7de-69b98f221707/edit?view_items=vfXvHWz-LJRf&invitationId=inv_6be87b84-7a83-4069-a5f2-9a2da022a2b1

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# Use https://dbd.tricky.lol/api for everything that you can
# Default images: https://packs.dbdicontoolbox.com/Dead-By-Daylight-Default-Icons.zip

# XAMPP -> MySQL Workbench