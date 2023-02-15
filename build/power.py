from imports import *

def power():
    file = open("./source_data/power.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "name", "description", "image"])

    res = requests.get("https://dbd.tricky.lol/api/items?type=power")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        writer.writerow([key, value["name"], value["description"], getImagePath(value["image"])])

    file.close()
    successMessage("power.csv")