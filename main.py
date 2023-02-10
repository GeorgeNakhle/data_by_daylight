from bs4 import BeautifulSoup
import requests
import re
from io import StringIO
from html.parser import HTMLParser
import csv
import os
import shutil

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

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

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

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#endregion

def createSurvivorCSV():
    print("WIP")

def createKillerCSV():
    print("WIP")

def createSurvivorPerkCSV():
    file = open("./csv/survivorPerk.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["id", "icon", "name", "description", "survivorID"])

    page = requests.get("https://deadbydaylight.fandom.com/wiki/Perks")
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.select("table.wikitable.sortable")[0]

    # Table data
    icons = table.find_all("img", attrs={"data-image-name":re.compile("IconPerks")})
    names = table.find_all("img", attrs={"data-image-name":re.compile("IconPerks")})
    descriptions = table.find_all("div", attrs={"class":"rawPerkDesc"})
    survivorIds = table.find_all("img", attrs={"alt":re.compile("charSelect")})
    survivorIdIndex = 0

    # General survivor perks
    general_table = soup.select("table.wikitable")[0]
    general_names = general_table.find_all("img", attrs={"data-image-name":re.compile("IconPerks")})
    for i in range(0, len(general_names)):
        general_names[i] = general_names[i].attrs["alt"]

    for i in range(0, len(icons)):
        # survivorID set to 0 if general perk
        if (names[i].attrs["alt"] in general_names):
            survivorId = 0
        else:
            survivorId = survivorIds[survivorIdIndex].attrs["alt"].split()[0][1:]
            survivorIdIndex+=1

        print("--------------------------------\n--------------------------------\n")
        print(bcolors.WARNING  + "Id: {}\nIcon: {}\nName: {}\n\nDescription: {}Survivor: {}\n".format(str(i), icons[i].attrs["data-src"], names[i].attrs["alt"], strip_tags(descriptions[i].text), survivorId) + bcolors.ENDC)
        writer.writerow([str(i), icons[i].attrs["data-src"], names[i].attrs["alt"], strip_tags(descriptions[i].text), survivorId])

    successMessage("survivorPerks.csv")
    file.close()

def createKillerPerkCSV():
    print("WIP")

#endregion

#region MAIN



clearFolder("./csv/")
#createSurvivorCSV()
#createKillerCSV()
createSurvivorPerkCSV()
#createKillerPerkCSV()

#endregion

# Source: https://github.com/gatheringhallstudios/MHWorldData
# b(text) - Boldes the text: '''text'''
# i(text) - Italic style for text: ''text''