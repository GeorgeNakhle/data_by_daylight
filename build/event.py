from imports import *

def event():
    file = open("./source_data/event.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "name", "type", "multiplier", "start", "end"])

    res = requests.get("https://dbd.tricky.lol/api/events")
    response = json.loads(res.text)

    for i in response:
        writer.writerow([i["id"], i["name"], eventType[i["type"]].value, i["multiplier"], i["start"], i["end"]])

    file.close()
    successMessage("event.csv")