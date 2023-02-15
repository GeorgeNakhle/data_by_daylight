from imports import *

def power_addon():
    file = open("./source_data/power_addon.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "powerID", "name", "description", "rarity", "image"])

    res = requests.get("https://dbd.tricky.lol/api/addons?role=killer")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if len(value["parents"]) == 0:
            powerID = None
        else:
            powerID = value["parents"][0]

        writer.writerow([key, powerID, value["name"], value["description"], rarity[value["rarity"]].value, getImagePath(value["image"])])

    file.close()
    successMessage("power_addon.csv")