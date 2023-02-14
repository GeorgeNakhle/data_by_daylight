from imports import *

def offering():
    file = open("./source_data/offering.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "name", "role", "rarity", "description", "tags", "retired", "image"])

    res = requests.get("https://dbd.tricky.lol/api/offerings")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if value["role"] == None:
            roleVal = value["role"]
        else:
            roleVal = role[value["role"]].value

        writer.writerow([key, value["name"], roleVal, rarity[value["rarity"]].value, value["description"], value["tags"], value["retired"], value["image"]])

    file.close()
    successMessage("offering.csv")