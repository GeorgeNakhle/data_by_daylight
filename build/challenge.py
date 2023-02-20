from imports import *

def challenge():
    file = open("./source_data/challenge.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["tomeID", "name", "level", "role", "objective", "reward"])

    res = requests.get("https://dbd.tricky.lol/api/archives")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    previousChallenge = []
    for key, value in response.items():
        tomeID = key
        for level in value["levels"]:
            for challenge in value["levels"][level]["nodes"]:
                # Doesn't include prologue, epilogue, and reward nodes
                # Doesn't include duplicate challenges (i.e. Bountiful Harvest (x3) from Tome 5, Level 1)
                if (challenge["name"] == "Prologue" or challenge["name"] == "Epilogue" or challenge["name"] == "reward") or (tomeID in previousChallenge and challenge["name"] in previousChallenge and level in previousChallenge):
                    continue
                else:
                    name = challenge["name"]
                    previousChallenge.clear()
                    previousChallenge.append(tomeID)
                    previousChallenge.append(name)
                    previousChallenge.append(level)

                writer.writerow([tomeID, name, level, role[challenge["role"]].value, challenge["objective"], challenge["rewards"]])

    file.close()
    successMessage("challenge.csv")