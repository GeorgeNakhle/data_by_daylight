from imports import *

def killer():
    file = open("./source_data/killer.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "dlcID", "powerID", "name", "difficulty", "gender", "bio", "lore", "speedMS", "speedPercentage", "terrorRadius", "image"])

    res = requests.get("https://dbd.tricky.lol/api/dlc")
    response = json.loads(res.text)

    currentDLCs = []
    # Key, Value because url doesn't return array
    for key, value in response.items():
        currentDLCs.append(key)

    res = requests.get("https://dbd.tricky.lol/api/items?type=power")
    response = json.loads(res.text)

    currentPowers = []
    # Key, Value because url doesn't return array
    for key, value in response.items():
        currentPowers.append(key)

    res = requests.get("https://dbd.tricky.lol/api/characters?role=killer")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        # Sometimes killer is added to API before their image is
        if not os.path.isfile(getImagePath(value["image"])):
            image = ""
        else:
            image = getImagePath(value["image"])

        # Sometimes killer is added to API before their DLC is
        if value["dlc"] not in currentDLCs and value["item"] not in currentPowers:
            dlcID = None
            powerID = None
        else:
            if value["dlc"] != None:
                dlcID = value["dlc"].title()
            else:
                dlcID = None
            powerID = value["item"]

        writer.writerow([key, dlcID, powerID, value["name"], difficulty[value["difficulty"]].value, gender[value["gender"]].value, value["bio"], value["story"], getSpeedMS(value["tunables"]["maxwalkspeed"]), getSpeedPercentage(value["tunables"]["maxwalkspeed"]), getTerrorRadius(value["tunables"]["terrorradius"]), image])

    file.close()
    successMessage("killer.csv")