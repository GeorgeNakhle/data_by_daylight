from imports import *

def map():
    file = open("./source_data/map.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "dlcID", "name", "realm", "description", "image"])

    res = requests.get("https://dbd.tricky.lol/api/maps")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        if value["image"] == None:
            continue

        writer.writerow([key, value["dlc"], value["name"], value["realm"], value["description"], getImagePath(value["image"])])

    file.close()
    successMessage("map.csv")