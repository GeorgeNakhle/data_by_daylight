from imports import *

def item_addon():
    file = open("./source_data/item_addon.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "name", "description", "type", "rarity", "image"])

    res = requests.get("https://dbd.tricky.lol/api/addons?role=survivor")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        writer.writerow([key, value["name"], value["description"], itemType[value["item_type"]].value, rarity[value["rarity"]].value, getImagePath(value["image"])])

    file.close()
    successMessage("item_addon.csv")