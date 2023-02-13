import os
import shutil
import json
import requests
import csv

#region CLASSES

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

def successMessage(file):
    print(bcolors.OKGREEN + "{} created!".format(file) + bcolors.ENDC)

#endregion

def createMetadataCSV():
    file = open("./source_data/metadata.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["endpoint", "version", "lastupdate"])

    res = requests.get("https://dbd.tricky.lol/api/versions")
    response = json.loads(res.text)

    for key, value in response.items():
        writer.writerow([key, value["version"], value["lastupdate"]])

    file.close()
    successMessage("metadata.csv")

def createSurvivorCSV():
    print("WIP")

def createKillerCSV():
    print("WIP")

def createSurvivorPerkCSV():
    print("WIP")


def createKillerPerkCSV():
    print("WIP")

#endregion

#region MAIN

clearFolder("./source_data/")
createMetadataCSV()
#createSurvivorCSV()
#createKillerCSV()
#createSurvivorPerkCSV()
#createKillerPerkCSV()

#endregion

# Source: https://github.com/gatheringhallstudios/MHWorldData
# DB Model: https://lucid.app/lucidchart/9bb20e80-bc4d-4554-b7de-69b98f221707/edit?view_items=vfXvHWz-LJRf&invitationId=inv_6be87b84-7a83-4069-a5f2-9a2da022a2b1

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# Use https://dbd.tricky.lol/api for everything that you can
# Default images: https://packs.dbdicontoolbox.com/Dead-By-Daylight-Default-Icons.zip