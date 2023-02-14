from imports import *

def createMetadataCSV():
    file = open("./source_data/metadata.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["endpoint", "version", "lastupdate"])

    res = requests.get("https://dbd.tricky.lol/api/versions")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        writer.writerow([key, value["version"], value["lastupdate"]])

    file.close()
    successMessage("metadata.csv")