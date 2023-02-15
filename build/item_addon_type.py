from imports import *

def item_addon_type():
    file = open("./source_data/item_addon_type.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["addonID", "typeID"])

    res = requests.get("https://dbd.tricky.lol/api/addons?role=survivor")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        writer.writerow([key, itemType[value["item_type"]].value])

    file.close()
    successMessage("item_addon_type.csv")