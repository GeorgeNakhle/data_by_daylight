from imports import *

def database():
    if os.path.isfile("dbd.db"):
        os.remove("dbd.db")
    conn = sqlite3.connect("dbd.db", detect_types=sqlite3.PARSE_DECLTYPES)
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    
    #region TOME TABLE
    c.execute("""CREATE TABLE tome (
                id text PRIMARY KEY,
                title text,
                type text,
                release timestamp
                )""")
    with open("./source_data/tome.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["title"] or None, i["type"] or None, i["release"] or None) for i in dr]
    c.executemany("INSERT INTO tome (id, title, type, release) VALUES (?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region CHALLENGE TABLE
    c.execute("""CREATE TABLE challenge (
                tomeID text,
                name text,
                level integer,
                role text,
                objective text,
                reward blob,
                PRIMARY KEY (tomeID, name, level),
                FOREIGN KEY (tomeID) REFERENCES tome (id)
                )""")
    with open("./source_data/challenge.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["tomeID"] or None, i["name"] or None, i["level"] or None, i["role"] or None, i["objective"] or None, i["reward"] or None) for i in dr]
    c.executemany("INSERT INTO challenge (tomeID, name, level, role, objective, reward) VALUES (?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region VIGNETTE TABLE
    c.execute("""CREATE TABLE vignette (
                id text PRIMARY KEY,
                tomeID text,
                title text,
                subtitle text,
                FOREIGN KEY (tomeID) REFERENCES tome (id)
                )""")
    with open("./source_data/vignette.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["tomeID"] or None, i["title"] or None, i["subtitle"] or None) for i in dr]
    c.executemany("INSERT INTO vignette (id, tomeID, title, subtitle) VALUES (?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region ENTRY TABLE
    c.execute("""CREATE TABLE entry (
                title text,
                vignetteID text,
                text text,
                PRIMARY KEY (title, vignetteID)
                FOREIGN KEY (vignetteID) REFERENCES vignette (id)
                )""")
    with open("./source_data/entry.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["title"] or None, i["vignetteID"] or None, i["text"] or None) for i in dr]
    c.executemany("INSERT INTO entry (title, vignetteID, text) VALUES (?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region RIFT TABLE
    c.execute("""CREATE TABLE rift (
                id text PRIMARY KEY,
                tier integer,
                start timestamp,
                end timestamp,
                FOREIGN KEY (id) REFERENCES tome (id)
                )""")
    with open("./source_data/rift.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["tier"] or None, i["start"] or None, i["end"] or None) for i in dr]
    c.executemany("INSERT INTO rift (id, tier, start, end) VALUES (?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region LEVEL TABLE
    c.execute("""CREATE TABLE level (
                riftID text,
                number integer,
                type text,
                reward blob,
                PRIMARY KEY (riftID, number, type),
                FOREIGN KEY (riftID) REFERENCES rift (id)
                )""")
    with open("./source_data/level.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["riftID"] or None, i["number"] or None, i["type"] or None, i["reward"] or None) for i in dr]
    c.executemany("INSERT INTO level (riftID, number, type, reward) VALUES (?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region EVENT TABLE
    c.execute("""CREATE TABLE event (
                id text PRIMARY KEY,
                name text,
                type text,
                multiplier real,
                start timestamp,
                end timestamp
                )""")
    with open("./source_data/event.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["name"] or None, i["type"] or None, i["multiplier"] or None, i["start"] or None, i["end"] or None) for i in dr]
    c.executemany("INSERT INTO event (id, name, type, multiplier, start, end) VALUES (?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region ITEM TABLE
    c.execute("""CREATE TABLE item (
                id text PRIMARY KEY,
                eventID text,
                name text,
                description text,
                type text,
                rarity text,
                image text,
                FOREIGN KEY (eventID) REFERENCES event (id)
                )""")
    with open("./source_data/item.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["eventID"] or None, i["name"] or None, i["description"] or None, i["type"] or None, i["rarity"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO item (id, eventID, name, description, type, rarity, image) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region ITEM_ADDON TABLE
    c.execute("""CREATE TABLE item_addon (
                id text PRIMARY KEY,
                name text,
                description text,
                type text,
                rarity text,
                image text
                )""")
    with open("./source_data/item_addon.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["name"] or None, i["description"] or None, i["type"] or None, i["rarity"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO item_addon (id, name, description, type, rarity, image) VALUES (?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region ITEM_ADDON_ITEM TABLE
    c.execute("""CREATE TABLE item_addon_item (
                addonID text,
                itemID text,
                PRIMARY KEY (addonID, itemID),
                FOREIGN KEY (addonID) REFERENCES item_addon (id),
                FOREIGN KEY (itemID) REFERENCES item (id)
                )""")
    with open("./source_data/item_addon_item.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["addonID"] or None, i["itemID"] or None) for i in dr]
    c.executemany("INSERT INTO item_addon_item (addonID, itemID) VALUES (?, ?);", to_db)
    conn.commit()
    #endregion

    #region CHARM TABLE
    c.execute("""CREATE TABLE charm (
                id text PRIMARY KEY,
                name text,
                description text,
                collection text,
                role text,
                rarity text,
                image text
                )""")
    with open("./source_data/charm.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["name"] or None, i["description"] or None, i["collection"] or None, i["role"] or None, i["rarity"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO charm (id, name, description, collection, role, rarity, image) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region DLC TABLE
    c.execute("""CREATE TABLE dlc (
                id text PRIMARY KEY,
                name text,
                description text,
                steamID integer,
                release timestamp
                )""")
    with open("./source_data/dlc.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["name"] or None, i["description"] or None, i["steamID"] or None, i["release"] or None) for i in dr]
    c.executemany("INSERT INTO dlc (id, name, description, steamID, release) VALUES (?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region SURVIVOR TABLE
    c.execute("""CREATE TABLE survivor (
                id integer PRIMARY KEY,
                dlcID text,
                name text,
                gender text,
                bio text,
                lore text,
                image text,
                FOREIGN KEY (dlcID) REFERENCES dlc (id)
                )""")
    with open("./source_data/survivor.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["dlcID"] or None, i["name"] or None, i["gender"] or None, i["bio"] or None, i["lore"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO survivor (id, dlcID, name, gender, bio, lore, image) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region POWER TABLE
    c.execute("""CREATE TABLE power (
                id text PRIMARY KEY,
                name text,
                description text,
                image text
                )""")
    with open("./source_data/power.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["name"] or None, i["description"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO power (id, name, description, image) VALUES (?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region POWER_ADDON TABLE
    c.execute("""CREATE TABLE power_addon (
                id text PRIMARY KEY,
                powerID text,
                name text,
                description text,
                rarity text,
                image text,
                FOREIGN KEY (powerID) REFERENCES power (id)
                )""")
    with open("./source_data/power_addon.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["powerID"] or None, i["name"] or None, i["description"] or None, i["rarity"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO power_addon (id, powerID, name, description, rarity, image) VALUES (?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region KILLER TABLE
    c.execute("""CREATE TABLE killer (
                id integer PRIMARY KEY,
                dlcID text,
                powerID text,
                name text,
                difficulty text,
                gender text,
                bio text,
                lore text,
                speedMS real,
                speedPercentage real,
                terrorRadius integer,
                image text,
                FOREIGN KEY (dlcID) REFERENCES dlc (id),
                FOREIGN KEY (powerID) REFERENCES power (id)
                )""")
    with open("./source_data/killer.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["dlcID"] or None, i["powerID"] or None, i["name"] or None, i["difficulty"] or None, i["gender"] or None, i["bio"] or None, i["lore"] or None, i["speedMS"] or None, i["speedPercentage"] or None, i["terrorRadius"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO killer (id, dlcID, powerID, name, difficulty, gender, bio, lore, speedMS, speedPercentage, terrorRadius, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region PERK TABLE
    c.execute("""CREATE TABLE perk (
                id text PRIMARY KEY,
                survivorID integer,
                killerID integer,
                name text,
                role text,
                description text,
                tunables blob,
                teachable integer,
                image text,
                FOREIGN KEY (survivorID) REFERENCES survivor (id),
                FOREIGN KEY (killerID) REFERENCES killer (id)
                )""")
    with open("./source_data/perk.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["survivorID"] or None, i["killerID"] or None, i["name"], i["role"] or None, i["description"] or None, i["tunables"] or None, i["teachable"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO perk (id, survivorID, killerID, name, role, description, tunables, teachable, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region OUTFIT TABLE
    c.execute("""CREATE TABLE outfit (
                id text PRIMARY KEY,
                survivorID integer,
                killerID integer,
                name text,
                description text,
                role text,
                collection text,
                rarity text,
                purchasable integer,
                discount blob,
                image text,
                FOREIGN KEY (survivorID) REFERENCES survivor (id),
                FOREIGN KEY (killerID) REFERENCES killer (id)
                )""")
    with open("./source_data/outfit.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["survivorID"] or None, i["killerID"] or None, i["name"] or None, i["description"] or None, i["role"] or None, i["collection"] or None, i["rarity"] or None, i["purchasable"] or None, i["discount"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO outfit (id, survivorID, killerID, name, description, role, collection, rarity, purchasable, discount, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region COSMETIC TABLE
    c.execute("""CREATE TABLE cosmetic (
                id text PRIMARY KEY,
                survivorID integer,
                killerID integer,
                outfitID text,
                name text,
                description text,
                role text,
                type text,
                collection text,
                rarity text,
                purchasable integer,
                image text,
                FOREIGN KEY (survivorID) REFERENCES survivor (id),
                FOREIGN KEY (killerID) REFERENCES killer (id),
                FOREIGN KEY (outfitID) REFERENCES outfit (id)
                )""")
    with open("./source_data/cosmetic.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["survivorID"] or None, i["killerID"] or None, i["outfitID"] or None, i["name"] or None, i["description"] or None, i["role"] or None, i["type"] or None, i["collection"] or None, i["rarity"] or None, i["purchasable"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO cosmetic (id, survivorID, killerID, outfitID, name, description, role, type, collection, rarity, purchasable, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region MAP TABLE
    c.execute("""CREATE TABLE map (
                id text PRIMARY KEY,
                dlcID text,
                name text,
                realm text,
                description text,
                image text,
                FOREIGN KEY (dlcID) REFERENCES dlc (id)
                )""")
    with open("./source_data/map.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["dlcID"] or None, i["name"] or None, i["realm"] or None, i["description"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO map (id, dlcID, name, realm, description, image) VALUES (?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region OFFERING TABLE
    c.execute("""CREATE TABLE offering (
                id text PRIMARY KEY,
                name text,
                role text,
                rarity text,
                description text,
                tags blob,
                retired integer,
                image text
                )""")
    with open("./source_data/offering.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["id"] or None, i["name"] or None, i["role"] or None, i["rarity"] or None, i["description"] or None, i["tags"] or None, i["retired"] or None, i["image"] or None) for i in dr]
    c.executemany("INSERT INTO offering (id, name, role, rarity, description, tags, retired, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    conn.commit()
    #endregion

    #region METADATA TABLE
    c.execute("""CREATE TABLE metadata (
                endpoint text PRIMARY KEY,
                version text,
                lastupdate timestamp
                )""")
    with open("./source_data/metadata.csv", "r", encoding="utf-8") as fin:
        dr = csv.DictReader(fin)
        to_db = [(i["endpoint"] or None, i["version"] or None, i["lastupdate"] or None) for i in dr]
    c.executemany("INSERT INTO metadata (endpoint, version, lastupdate) VALUES (?, ?, ?);", to_db)
    conn.commit()
    #endregion
    
    conn.close()
    successMessage("dbd.db")