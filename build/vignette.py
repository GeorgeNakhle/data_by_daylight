from imports import *

def vignette():
    file = open("./source_data/vignette.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["id", "tomeID", "title", "subtitle"])

    res = requests.get("https://dbd.tricky.lol/api/journals")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        tomeID = key
        for vignette in value["vignettes"]:
            writer.writerow([vignette, tomeID, value["vignettes"][vignette]["title"], value["vignettes"][vignette]["subtitle"]])

    file.close()
    successMessage("vignette.csv")