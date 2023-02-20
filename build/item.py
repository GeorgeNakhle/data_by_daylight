from imports import *

def item():
    file = open("./source_data/item.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "eventID", "name", "description", "type", "rarity", "image"])

    res = requests.get("https://dbd.tricky.lol/api/items?role=survivor")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if value["rarity"] == "none":
            rarityType = None
        else:
            rarityType = rarity[value["rarity"]].value

        if value["item_type"] == None:
            type = itemType["limited"].value
        else:
            type = itemType[value["item_type"]].value

        writer.writerow([key, value["event"], value["name"], value["description"], type, rarityType, getImagePath(value["image"])])

    file.close()
    successMessage("item.csv")