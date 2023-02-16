from imports import *

def entry():
    file = open("./source_data/entry.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title", "vignetteID", "text"])

    res = requests.get("https://dbd.tricky.lol/api/journals")
    response = json.loads(res.text)

    # Key, Value because url doesn't return array
    for key, value in response.items():
        for vignette in value["vignettes"]:
            for entry in value["vignettes"][vignette]["entries"]:
                writer.writerow([entry["title"], vignette, entry["text"]])

    file.close()
    successMessage("entry.csv")