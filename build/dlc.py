from imports import *

def dlc():
    file = open("./source_data/dlc.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "name", "description", "steamID", "release"])

    res = requests.get("https://dbd.tricky.lol/api/dlc")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        writer.writerow([key.title(), value["name"], value["description"], value["steamid"], value["time"]])

    file.close()
    successMessage("dlc.csv")