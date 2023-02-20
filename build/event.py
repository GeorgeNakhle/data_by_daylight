from imports import *

def event():
    file = open("./source_data/event.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "name", "type", "multiplier", "start", "end"])

    res = requests.get("https://dbd.tricky.lol/api/events")
    response = json.loads(res.text)

    for i in response:
        if i["name"] == None:
            continue

        # Add timestamp to id because bloodpoint events aren't unique
        if eventType[i["type"]].value == "Bloodpoints":
            id = i["id"].replace("NAME", str(i["start"]))
        else:
            id = i["id"]

        writer.writerow([id, i["name"].title(), eventType[i["type"]].value, i["multiplier"], i["start"], i["end"]])

    file.close()
    successMessage("event.csv")