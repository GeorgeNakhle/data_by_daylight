from imports import *

def createKillerCSV():
    file = open("./source_data/killer.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "dlcID", "powerID", "name", "difficulty", "gender", "bio", "lore", "speedMS", "speedPercentage", "terrorRadius", "image"])

    res = requests.get("https://dbd.tricky.lol/api/characters?role=killer")
    response = json.loads(res.text)

    for key, value in response.items():
        writer.writerow([key, value["dlc"], value["item"], value["name"], difficulty[value["difficulty"]].value, gender[value["gender"]].value, value["bio"], value["story"], getSpeedMS(value["tunables"]["maxwalkspeed"]), getSpeedPercentage(value["tunables"]["maxwalkspeed"]), getTerrorRadius(value["tunables"]["terrorradius"]), getImagePath(value["image"])])

    file.close()
    successMessage("killer.csv")