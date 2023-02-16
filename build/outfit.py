from imports import *

def outfit():
    file = open("./source_data/outfit.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "survivorID", "killerID", "name", "description", "role", "collection", "rarity", "purchasable", "discount", "image"])

    res = requests.get("https://dbd.tricky.lol/api/cosmetics?type=outfit")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if isSurvivor(value["character"]):
            # Survivor outfit (not general)
            survivorID = value["character"]
            killerID = None
            roleType = role["survivor"].value
        else:
            # Killer outfit (not general)
            survivorID = None
            killerID = value["character"]
            roleType = role["killer"].value

        writer.writerow([key, survivorID, killerID, value["name"], value["description"], roleType, value["collection"].title(), rarity[value["rarity"]].value, value["purchasable"], value["discounts"], getImagePath(value["image"])])

    file.close()
    successMessage("outfit.csv")