from bs4 import BeautifulSoup
import requests
import re
from io import StringIO
from html.parser import HTMLParser
import csv
import os

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
    page = requests.get("https://deadbydaylight.fandom.com/wiki/Perks#List_of_All_Available_Perks")
    soup = BeautifulSoup(page.text, "html.parser")

    survivor_perk_table = soup.select("table.wikitable.sortable")[0]
    survivor_perk_perkId = 0
    survivor_perk_icons = survivor_perk_table.find_all("img", attrs={"data-image-name":re.compile("IconPerks")})
    survivor_perk_names = survivor_perk_table.find_all("img", attrs={"data-image-name":re.compile("IconPerks")})
    survivor_perk_descriptions = survivor_perk_table.find_all("div", attrs={"class":"rawPerkDesc"})
    survivor_perk_surivorIds = survivor_perk_table.find_all("img", attrs={"alt":re.compile("charSelect")})

    if os.path.exists("./csv/survivorPerk.csv"):
        os.remove("./csv/survivorPerk.csv")

    file = open("./csv/survivorPerk.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["id", "icon", "name", "description", "survivorID"])

    for perk_icon, perk_name, perk_description, perk_survivorId in zip(survivor_perk_icons, survivor_perk_names, survivor_perk_descriptions, survivor_perk_surivorIds):
        print("--------------------------------\n--------------------------------\n")
        
        if (perk_name.attrs["alt"] in ["Dark Sense", "Déjà Vu", "Guardian", "Hope", "Inner Healing"]):
            # DONT ITERATE ON survivor_perk_surivorIds
            # FORCE Id = 0
            print(bcolors.FAIL + "GENERAL PERK" + bcolors.ENDC)
        
        print(bcolors.WARNING  + "ID: {}\nIcon: {}\n\nName: {}\n\nDescription: {}Survivor: {}\n".format(str(survivor_perk_perkId), perk_icon.attrs["data-src"], perk_name.attrs["alt"], strip_tags(perk_description.text), perk_survivorId.attrs["alt"].split()[0][1:]) + bcolors.ENDC)
        writer.writerow([str(survivor_perk_perkId), perk_icon.attrs["data-src"], perk_name.attrs["alt"], strip_tags(perk_description.text), perk_survivorId.attrs["alt"].split()[0][1:]])
        survivor_perk_perkId+=1

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