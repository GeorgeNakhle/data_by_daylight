from imports import *

def level():
    file = open("./source_data/level.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["riftID", "number", "type", "reward"])

    res = requests.get("https://dbd.tricky.lol/api/rift")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        riftID = key
        for freeLevel in value["free"]:
            writer.writerow([riftID, freeLevel, "Free", value["free"][freeLevel]])
        for premiumLevel in value["premium"]:
            writer.writerow([riftID, premiumLevel, "Premium", value["premium"][premiumLevel]])

    file.close()
    successMessage("level.csv")