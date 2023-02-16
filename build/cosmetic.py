from imports import *

def cosmetic():
    file = open("./source_data/cosmetic.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "survivorID", "killerID", "outfitID", "name", "description", "role", "type", "collection", "rarity", "purchasable", "image"])

    res = requests.get("https://dbd.tricky.lol/api/cosmetics?type=item")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        # Gift code charms are in this endpoint, so skip them
        if value["category"] == "charm":
            continue

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

        if value["collection"] == None:
            collection = value["collection"]
        else:
            collection = value["collection"].title()

        writer.writerow([key, survivorID, killerID, value["outfit"], value["name"], value["description"], roleType, cosmeticType[value["category"]].value, collection, rarity[value["rarity"]].value, value["purchasable"], getImagePath(value["image"])])

    file.close()
    successMessage("cosmetic.csv")