import os
import pandas as pd

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

#endregion

#region MAIN

if os.path.exists("./csv/survivorPerk.csv") and os.path.exists("./csv/killerPerk.csv"):
    os.remove("./csv/survivorPerk.csv")

df = pd.read_html("https://deadbydaylight.fandom.com/wiki/Perks")

print(df[len(df) - 3]) # Survivor perk table
print(df[len(df) - 2]) # Killer perk table

df[len(df) - 3].to_csv("./csv/survivorPerk.csv")
df[len(df) - 2].to_csv("./csv/killerPerk.csv")

print(bcolors.OKGREEN + "survivorPerks.csv created!" + bcolors.OKCYAN)
print(bcolors.OKGREEN + "killerPerks.csv created!" + bcolors.OKCYAN)

#endregion

# Source: https://github.com/gatheringhallstudios/MHWorldData