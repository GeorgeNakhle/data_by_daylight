from imports import *

def createSurvivorCSV():
    file = open("./source_data/survivor.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "dlcID", "name", "gender", "bio", "lore", "image"])

    res = requests.get("https://dbd.tricky.lol/api/characters?role=survivor")
    response = json.loads(res.text)

    index = 0
    for i in response:
        writer.writerow([index, i["dlc"], i["name"], gender[i["gender"]].value, i["bio"], i["story"], getImagePath(i["image"])])
        index += 1

    file.close()
    successMessage("survivor.csv")
