from imports import *

def tome():
    file = open("./source_data/tome.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "title", "type", "release"])

    res = requests.get("https://dbd.tricky.lol/api/archives")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if "TOME" in value["name"]:
            type = "Tome"
        else:
            type = "Event"

        writer.writerow([key, value["name"].title(), type, value["start"]])

    file.close()
    successMessage("tome.csv")