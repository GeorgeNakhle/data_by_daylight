from imports import *

def survivor():
    file = open("./source_data/survivor.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "dlcID", "name", "gender", "bio", "lore", "image"])

    res = requests.get("https://dbd.tricky.lol/api/dlc")
    response = json.loads(res.text)

    currentDLCs = []
    # Key, Value because url doesn't return array
    for key, value in response.items():
        currentDLCs.append(key)


    res = requests.get("https://dbd.tricky.lol/api/characters?role=survivor")
    response = json.loads(res.text)

    index = 0
    for i in response:
        # Sometimes survivor is added to API before their image is
        if not os.path.isfile(getImagePath(i["image"])):
            image = ""
        else:
            image = getImagePath(i["image"])

        # Sometimes survivor is added to API before their DLC is
        if i["dlc"] not in currentDLCs:
            dlcID = None
        else:
            dlcID = i["dlc"].title()

        writer.writerow([index, dlcID, i["name"], gender[i["gender"]].value, i["bio"], i["story"], image])
        index += 1

    file.close()
    successMessage("survivor.csv")
