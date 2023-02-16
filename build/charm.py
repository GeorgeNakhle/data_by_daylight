from imports import *

def charm():
    file = open("./source_data/charm.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "name", "description", "collection", "role", "rarity", "image"])

    # API fetch on all cosmetics because of gift code charms
    res = requests.get("https://dbd.tricky.lol/api/cosmetics")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if value["type"] != "charm" and value["category"] != "charm":
            continue

        if value["role"] == None:
            roleType = role["shared"].value
        else:
            roleType = role[value["role"]].value

        writer.writerow([key, value["name"], value["description"], value["collection"], roleType, rarity[value["rarity"]].value, getImagePath(value["image"])])

    file.close()
    successMessage("charm.csv")