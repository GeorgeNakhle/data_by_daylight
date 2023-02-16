from imports import *

def challenge():
    file = open("./source_data/challenge.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["tomeID", "name", "level", "role", "objective", "reward"])

    res = requests.get("https://dbd.tricky.lol/api/archives")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        tomeID = key
        for level in value["levels"]:
            for challenge in value["levels"][level]["nodes"]:
                # Note: Does not include prologue, epilogue, and reward nodes
                if challenge["name"] == "Prologue" or challenge["name"] == "Epilogue" or challenge["name"] == "reward":
                    continue
                else:
                    name = challenge["name"]

                writer.writerow([tomeID, name, level, role[challenge["role"]].value, challenge["objective"], challenge["rewards"]])

    file.close()
    successMessage("challenge.csv")