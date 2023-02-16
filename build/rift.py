from imports import *

def rift():
    file = open("./source_data/rift.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "tier", "start", "end"])

    # Second API fetch because end timestamp is not in 'rift' endpoint
    res = requests.get("https://dbd.tricky.lol/api/archives")
    response = json.loads(res.text)

    end = []
    # Key, Value because url doesn't return array
    for key, value in response.items():
        if "TOME" in value["name"]:
            end.append(value["end"])

    res = requests.get("https://dbd.tricky.lol/api/rift")
    response = json.loads(res.text)

    index = 0
    # Key, Value because url doesn't return array
    for key, value in response.items():
        writer.writerow([key, value["tiers"], value["start"], end[index]])
        index += 1

    file.close()
    successMessage("rift.csv")