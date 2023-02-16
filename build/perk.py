from imports import *

def perk():
    file = open("./source_data/perk.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "survivorID", "killerID", "name", "role", "description", "tunables", "teachable", "image"])

    res = requests.get("https://dbd.tricky.lol/api/perks")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if value["character"] == None:
            # General perk (any)
            survivorID = value["character"]
            killerID = value["character"]
        elif isSurvivor(value["character"]):
            # Survivor perk (not general)
            survivorID = value["character"]
            killerID = None
        else:
            # Killer perk (not general)
            survivorID = None
            killerID = value["character"]

        if value["teachable"] == 0:
            teachable = None
        else:
            teachable = value["teachable"]
        
        writer.writerow([key, survivorID, killerID, value["name"], role[value["role"]].value, value["description"], value["tunables"], teachable, getImagePath(value["image"])])

    file.close()
    successMessage("perk.csv")