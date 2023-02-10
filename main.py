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

def successMessage(msg):
    print(bcolors.OKGREEN + "{} created!".format(msg) + bcolors.ENDC)

def createSurvivorCSV():

    successMessage("survivor.csv")

def createKillerCSV():

    successMessage("killer.csv")

def createSurvivorPerkCSV():

    successMessage("survivorPerk.csv")

def createKillerPerkCSV():

    successMessage("killerPerk.csv")

#endregion

#region MAIN

clearFolder("./csv/")
createSurvivorCSV()
createKillerCSV()
createSurvivorPerkCSV()
createKillerPerkCSV()

#endregion

# Source: https://github.com/gatheringhallstudios/MHWorldData