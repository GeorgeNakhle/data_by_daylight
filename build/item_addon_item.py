from imports import *

def item_addon_item():
    file = open("./source_data/item_addon_item.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["addonID", "itemID"])

    res = requests.get("https://dbd.tricky.lol/api/items?role=survivor")
    response = json.loads(res.text)

    itemID = []
    itemType = []
    # Key, Value because url doesn't return array
    for key, value in response.items():
        itemID.append(key)
        itemType.append(value["item_type"])

    res = requests.get("https://dbd.tricky.lol/api/addons?role=survivor")
    response = json.loads(res.text)

    index = 0
    # Key, Value because url doesn't return array
    for key, value in response.items():
        for id in itemID:
            if itemType[index] == value["item_type"]:
                writer.writerow([key, id])
            index += 1
        index = 0

    file.close()
    successMessage("item_addon_item.csv")