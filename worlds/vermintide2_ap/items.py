from typing import Dict, List
from BaseClasses import Item, ItemClassification
from .ItemData import ItemData, ItemGroups

BASE_ID = 3_000_000

# ============================================================
# Item Table
# ============================================================

ITEM_TABLE: Dict[str, ItemData] = {

    # ----------------------------------------------------------
    # Difficulty Unlocks
    # progression: gates entire difficulty tiers in location rules
    # ----------------------------------------------------------
    "Unlock Veteran Difficulty":   ItemData(ItemGroups.DifficultyUnlock, BASE_ID + 0,  ItemClassification.progression),
    "Unlock Champion Difficulty":  ItemData(ItemGroups.DifficultyUnlock, BASE_ID + 1,  ItemClassification.progression),
    "Unlock Legend Difficulty":    ItemData(ItemGroups.DifficultyUnlock, BASE_ID + 2,  ItemClassification.progression),
    "Unlock Cataclysm Difficulty": ItemData(ItemGroups.DifficultyUnlock, BASE_ID + 3,  ItemClassification.progression),

    # ----------------------------------------------------------
    # Careers — Viktor Saltzpyre
    # Default career (Witch Hunter Captain) is always unlocked, not in pool.
    # progression: hero-completion locations require having a career for that hero
    # ----------------------------------------------------------
    "Bounty Hunter":               ItemData(ItemGroups.Career, BASE_ID + 10, ItemClassification.progression),
    "Zealot":                      ItemData(ItemGroups.Career, BASE_ID + 11, ItemClassification.progression),
    "Warrior Priest of Sigmar":    ItemData(ItemGroups.Career | ItemGroups.DLC, BASE_ID + 12, ItemClassification.progression),

    # ----------------------------------------------------------
    # Careers — Bardin Goreksson
    # Default career (Ranger Veteran) is always unlocked, not in pool.
    # ----------------------------------------------------------
    "Ironbreaker":                 ItemData(ItemGroups.Career, BASE_ID + 20, ItemClassification.progression),
    "Slayer":                      ItemData(ItemGroups.Career, BASE_ID + 21, ItemClassification.progression),
    "Outcast Engineer":            ItemData(ItemGroups.Career | ItemGroups.DLC, BASE_ID + 22, ItemClassification.progression),

    # ----------------------------------------------------------
    # Careers — Kerillian
    # Default career (Waystalker) is always unlocked, not in pool.
    # ----------------------------------------------------------
    "Handmaiden":                  ItemData(ItemGroups.Career, BASE_ID + 30, ItemClassification.progression),
    "Shade":                       ItemData(ItemGroups.Career, BASE_ID + 31, ItemClassification.progression),
    "Sister of the Thorn":         ItemData(ItemGroups.Career | ItemGroups.DLC, BASE_ID + 32, ItemClassification.progression),

    # ----------------------------------------------------------
    # Careers — Sienna Fuegonasus
    # Default career (Battle Wizard) is always unlocked, not in pool.
    # ----------------------------------------------------------
    "Pyromancer":                  ItemData(ItemGroups.Career, BASE_ID + 40, ItemClassification.progression),
    "Unchained":                   ItemData(ItemGroups.Career, BASE_ID + 41, ItemClassification.progression),
    "Necromancer":                 ItemData(ItemGroups.Career | ItemGroups.DLC, BASE_ID + 42, ItemClassification.progression),

    # ----------------------------------------------------------
    # Careers — Markus Kruber
    # Default career (Mercenary) is always unlocked, not in pool.
    # ----------------------------------------------------------
    "Huntsman":                    ItemData(ItemGroups.Career, BASE_ID + 50, ItemClassification.progression),
    "Foot Knight":                 ItemData(ItemGroups.Career, BASE_ID + 51, ItemClassification.progression),
    "Grail Knight":                ItemData(ItemGroups.Career | ItemGroups.DLC, BASE_ID + 52, ItemClassification.progression),

    # ----------------------------------------------------------
    # Traps
    # ----------------------------------------------------------
    "Trap: Spawn Monster":         ItemData(ItemGroups.Trap, BASE_ID + 100, ItemClassification.trap, count=3),
    "Trap: Spawn Horde":           ItemData(ItemGroups.Trap, BASE_ID + 101, ItemClassification.trap, count=5),
    "Trap: Spawn Patrol":          ItemData(ItemGroups.Trap, BASE_ID + 102, ItemClassification.trap, count=3),
    "Trap: Drop Firebomb":         ItemData(ItemGroups.Trap, BASE_ID + 103, ItemClassification.trap, count=4),
    "Trap: Empty Career Ability":  ItemData(ItemGroups.Trap, BASE_ID + 104, ItemClassification.trap, count=4),

    # ----------------------------------------------------------
    # Filler
    # count=0: amount is calculated dynamically in create_items()
    # to pad the pool to match location count
    # ----------------------------------------------------------
    "Ravaged Art":                 ItemData(ItemGroups.Filler, BASE_ID + 200, ItemClassification.filler, count=0),

    # ----------------------------------------------------------
    # Helmgart Campaign Missions
    # progression: used in logic to gate lord missions behind standard missions
    # ----------------------------------------------------------
    "Righteous Stand":             ItemData(ItemGroups.Mission, BASE_ID + 300, ItemClassification.progression),
    "Convocation of Decay":        ItemData(ItemGroups.Mission, BASE_ID + 301, ItemClassification.progression),
    "Hunger in the Dark":          ItemData(ItemGroups.Mission, BASE_ID + 302, ItemClassification.progression),
    "Against the Grain":           ItemData(ItemGroups.Mission, BASE_ID + 303, ItemClassification.progression),
    "Screaming Bell":              ItemData(ItemGroups.Mission, BASE_ID + 304, ItemClassification.progression),
    "Athel Yenlui":                ItemData(ItemGroups.Mission, BASE_ID + 305, ItemClassification.progression),
    "Festering Ground":            ItemData(ItemGroups.Mission, BASE_ID + 306, ItemClassification.progression),
    # Lord missions
    "Halescourge":                 ItemData(ItemGroups.Mission, BASE_ID + 310, ItemClassification.progression),
    "Into the Nest":               ItemData(ItemGroups.Mission, BASE_ID + 311, ItemClassification.progression),
    "Fort Brachsenbrucke":         ItemData(ItemGroups.Mission, BASE_ID + 312, ItemClassification.progression),
    "The Skittergate":             ItemData(ItemGroups.Mission, BASE_ID + 313, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — Shadows Over Bogenhafen (free DLC)
    # ----------------------------------------------------------
    "The Pit":                     ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Bogenhafen,       BASE_ID + 400, ItemClassification.progression),
    "The Blightreaper":            ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Bogenhafen,       BASE_ID + 401, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — Back to Ubersreik
    # ----------------------------------------------------------
    "The Horn of Magnus":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 410, ItemClassification.progression),
    "Garden of Morr":              ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 411, ItemClassification.progression),
    "Engines of War":              ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 412, ItemClassification.progression),
    "Fortunes of War":             ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 413, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — Winds of Magic
    # ----------------------------------------------------------
    "Dark Omens":                  ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,    BASE_ID + 420, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — The Curse of Drachenfels
    # ----------------------------------------------------------
    "Old Haunts":                  ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Drachenfels,      BASE_ID + 430, ItemClassification.progression),
    "Blood in the Darkness":       ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Drachenfels,      BASE_ID + 431, ItemClassification.progression),
    "The Enchanter's Lair":        ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Drachenfels,      BASE_ID + 432, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — A Treacherous Adventure
    # ----------------------------------------------------------
    "Trail of Treachery":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Treachery,        BASE_ID + 440, ItemClassification.progression),
    "Tower of Treachery":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Treachery,        BASE_ID + 441, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — Karak Azgaraz
    # ----------------------------------------------------------
    "Mission of Mercy":            ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     BASE_ID + 450, ItemClassification.progression),
    "A Grudge Served Cold":        ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     BASE_ID + 451, ItemClassification.progression),
    "Khazukan Kazakit-Ha!":        ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     BASE_ID + 452, ItemClassification.progression),
    "A Parting of the Waves":      ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     BASE_ID + 453, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — Verminous Dreams
    # ----------------------------------------------------------
    "The Forsaken Temple":         ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_VerminousDreams,  BASE_ID + 460, ItemClassification.progression),
    "Devious Delvings":            ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_VerminousDreams,  BASE_ID + 461, ItemClassification.progression),
    "The Well of Dreams":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_VerminousDreams,  BASE_ID + 462, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — Reikland Tales
    # ----------------------------------------------------------
    "Return to the Reik":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ReiklandTales,    BASE_ID + 470, ItemClassification.progression),

    # ----------------------------------------------------------
    # DLC Missions — Chaos Wastes
    # ----------------------------------------------------------
    "Expedition of Fortitude":     ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      BASE_ID + 480, ItemClassification.progression),
    "Expedition of Courage":       ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      BASE_ID + 481, ItemClassification.progression),
    "Expedition of Determination": ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      BASE_ID + 482, ItemClassification.progression),
    "Expedition to the Citadel":   ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      BASE_ID + 483, ItemClassification.progression),

    # ----------------------------------------------------------
    # Weapons — Viktor Saltzpyre (melee)
    # useful: good to have but not referenced in logic rules
    # ----------------------------------------------------------
    "Rapier":                       ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   BASE_ID + 1000, ItemClassification.useful),
    "Falchion":                     ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   BASE_ID + 1001, ItemClassification.useful),
    "Axe (Viktor Saltzpyre)":       ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   BASE_ID + 1002, ItemClassification.useful),
    "Greatsword (Viktor Saltzpyre)":ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   BASE_ID + 1003, ItemClassification.useful),
    "Flail":                        ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   BASE_ID + 1004, ItemClassification.useful),
    "Axe and Falchion":             ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 1005, ItemClassification.useful),
    "Billhook":                     ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,     BASE_ID + 1006, ItemClassification.useful),
    # Warrior Priest exclusive melee
    "Flail and Shield":             ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.DLC,                             BASE_ID + 1007, ItemClassification.useful),
    "Reckoner Great Hammer":        ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.ZealotWeapon | ItemGroups.DLC,   BASE_ID + 1008, ItemClassification.useful),
    "Paired Skull-Splitters":       ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.ZealotWeapon | ItemGroups.DLC,   BASE_ID + 1009, ItemClassification.useful),
    "Skull-Splitter and Tome":      ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.DLC,                             BASE_ID + 1010, ItemClassification.useful),
    "Skull-Splitter and Shield":    ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.DLC,                             BASE_ID + 1011, ItemClassification.useful),
    "Skull-Splitter Hammer":        ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.ZealotWeapon | ItemGroups.DLC,   BASE_ID + 1012, ItemClassification.useful),

    # Weapons — Viktor Saltzpyre (ranged)
    "Brace of Pistols":             ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   BASE_ID + 1020, ItemClassification.useful),
    "Volley Crossbow (Viktor)":     ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   BASE_ID + 1021, ItemClassification.useful),
    "Repeater Pistol":              ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   BASE_ID + 1022, ItemClassification.useful),
    "Crossbow (Viktor Saltzpyre)":  ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   BASE_ID + 1023, ItemClassification.useful),
    "Griffonfoot Pistols":          ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon | ItemGroups.DLC,                                  BASE_ID + 1024, ItemClassification.useful),

    # ----------------------------------------------------------
    # Weapons — Bardin Goreksson (melee)
    # ----------------------------------------------------------
    "Great Hammer (Bardin)":        ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   BASE_ID + 1100, ItemClassification.useful),
    "Great Axe":                    ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   BASE_ID + 1101, ItemClassification.useful),
    "Axe (Bardin Goreksson)":       ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   BASE_ID + 1102, ItemClassification.useful),
    "Hammer":                       ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   BASE_ID + 1103, ItemClassification.useful),
    "War Pick":                     ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   BASE_ID + 1104, ItemClassification.useful),
    "Dual Hammers":                 ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 1105, ItemClassification.useful),
    "Cog Hammer":                   ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon | ItemGroups.DLC,                                  BASE_ID + 1106, ItemClassification.useful),
    # Shield weapons
    "Axe and Shield":               ItemData(ItemGroups.Weapon | ItemGroups.BardinShields,                                                   BASE_ID + 1107, ItemClassification.useful),
    "Hammer and Shield":            ItemData(ItemGroups.Weapon | ItemGroups.BardinShields,                                                   BASE_ID + 1108, ItemClassification.useful),
    # Slayer exclusive
    "Dual Axes":                    ItemData(ItemGroups.Weapon | ItemGroups.SlayerWeapon,                                                    BASE_ID + 1109, ItemClassification.useful),
    "Throwing Axes":                ItemData(ItemGroups.Weapon | ItemGroups.SlayerWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,     BASE_ID + 1110, ItemClassification.useful),

    # Weapons — Bardin Goreksson (ranged)
    "Crossbow (Bardin Goreksson)":  ItemData(ItemGroups.Weapon | ItemGroups.BardinCrossbow,                                                  BASE_ID + 1120, ItemClassification.useful),
    "Handgun (Bardin Goreksson)":   ItemData(ItemGroups.Weapon | ItemGroups.BardinRWeapon,                                                   BASE_ID + 1121, ItemClassification.useful),
    "Grudge-Raker":                 ItemData(ItemGroups.Weapon | ItemGroups.BardinRWeapon,                                                   BASE_ID + 1122, ItemClassification.useful),
    "Masterwork Pistol":            ItemData(ItemGroups.Weapon | ItemGroups.BardinRWeapon | ItemGroups.DLC,                                  BASE_ID + 1123, ItemClassification.useful),
    "Drakefire Pistols":            ItemData(ItemGroups.Weapon | ItemGroups.BardinTechWeapon,                                                BASE_ID + 1124, ItemClassification.useful),
    "Drakegun":                     ItemData(ItemGroups.Weapon | ItemGroups.BardinTechWeapon,                                                BASE_ID + 1125, ItemClassification.useful),
    "Trollhammer Torpedo":          ItemData(ItemGroups.Weapon | ItemGroups.BardinTechWeapon | ItemGroups.DLC,                               BASE_ID + 1126, ItemClassification.useful),

    # ----------------------------------------------------------
    # Weapons — Kerillian (melee)
    # ----------------------------------------------------------
    "Sword (Kerillian)":            ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                BASE_ID + 1200, ItemClassification.useful),
    "Dual Daggers":                 ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                BASE_ID + 1201, ItemClassification.useful),
    "Dual Swords":                  ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                BASE_ID + 1202, ItemClassification.useful),
    "Sword and Dagger":             ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                BASE_ID + 1203, ItemClassification.useful),
    "Glaive":                       ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                BASE_ID + 1204, ItemClassification.useful),
    "Greatsword (Kerillian)":       ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                BASE_ID + 1205, ItemClassification.useful),
    "Elven Spear":                  ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                BASE_ID + 1206, ItemClassification.useful),
    "Elven Axe":                    ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik, BASE_ID + 1207, ItemClassification.useful),
    "Spear and Shield (Kerillian)": ItemData(ItemGroups.Weapon | ItemGroups.HandmaidenWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic, BASE_ID + 1208, ItemClassification.useful),

    # Weapons — Kerillian (ranged)
    "Swiftbow":                     ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon,                                                BASE_ID + 1220, ItemClassification.useful),
    "Longbow (Kerillian)":          ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon,                                                BASE_ID + 1221, ItemClassification.useful),
    "Hagbane Shortbow":             ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon,                                                BASE_ID + 1222, ItemClassification.useful),
    "Volley Crossbow (Kerillian)":  ItemData(ItemGroups.Weapon | ItemGroups.ShadeWeapon,                                                     BASE_ID + 1223, ItemClassification.useful),
    "Moonfire Bow":                 ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon | ItemGroups.DLC,                               BASE_ID + 1224, ItemClassification.useful),
    "Briar Javelin":                ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon | ItemGroups.DLC,                               BASE_ID + 1225, ItemClassification.useful),
    "Deepwood Staff":               ItemData(ItemGroups.Weapon | ItemGroups.SOTTWeapon | ItemGroups.DLC,                                     BASE_ID + 1226, ItemClassification.useful),

    # ----------------------------------------------------------
    # Weapons — Sienna Fuegonasus (melee)
    # ----------------------------------------------------------
    "Sword (Sienna Fuegonasus)":    ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   BASE_ID + 1300, ItemClassification.useful),
    "Mace (Sienna Fuegonasus)":     ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   BASE_ID + 1301, ItemClassification.useful),
    "Fire Sword":                   ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   BASE_ID + 1302, ItemClassification.useful),
    "Dagger":                       ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   BASE_ID + 1303, ItemClassification.useful),
    "Crowbill":                     ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 1304, ItemClassification.useful),
    "Flaming Flail":                ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,     BASE_ID + 1305, ItemClassification.useful),
    "Ensorcelled Reaper":           ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon | ItemGroups.DLC,                                  BASE_ID + 1306, ItemClassification.useful),

    # Weapons — Sienna Fuegonasus (ranged/staves)
    "Fireball Staff":               ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   BASE_ID + 1320, ItemClassification.useful),
    "Flamestorm Staff":             ItemData(ItemGroups.Weapon | ItemGroups.SiennaFlameWeapon,                                               BASE_ID + 1321, ItemClassification.useful),
    "Bolt Staff":                   ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   BASE_ID + 1322, ItemClassification.useful),
    "Beam Staff":                   ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   BASE_ID + 1323, ItemClassification.useful),
    "Conflagration Staff":          ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   BASE_ID + 1324, ItemClassification.useful),
    "Coruscation Staff":            ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon | ItemGroups.DLC,                                  BASE_ID + 1325, ItemClassification.useful),
    "Soulstealer Staff":            ItemData(ItemGroups.Weapon | ItemGroups.NecromancerWeapon | ItemGroups.DLC,                              BASE_ID + 1326, ItemClassification.useful),

    # ----------------------------------------------------------
    # Weapons — Markus Kruber (melee)
    # ----------------------------------------------------------
    "Greatsword (Markus Kruber)":   ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   BASE_ID + 1400, ItemClassification.useful),
    "Halberd":                      ItemData(ItemGroups.Weapon | ItemGroups.NoGrailWeapon,                                                   BASE_ID + 1401, ItemClassification.useful),
    "Sword (Markus Kruber)":        ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   BASE_ID + 1402, ItemClassification.useful),
    "Executioner Sword":            ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   BASE_ID + 1403, ItemClassification.useful),
    "Great Hammer (Markus Kruber)": ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   BASE_ID + 1404, ItemClassification.useful),
    "Sword and Shield":             ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   BASE_ID + 1405, ItemClassification.useful),
    "Mace (Markus Kruber)":         ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   BASE_ID + 1406, ItemClassification.useful),
    "Mace and Shield":              ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   BASE_ID + 1407, ItemClassification.useful),
    "Mace and Sword":               ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  BASE_ID + 1408, ItemClassification.useful),
    "Tuskgor Spear":                ItemData(ItemGroups.Weapon | ItemGroups.KruberSpear | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,       BASE_ID + 1409, ItemClassification.useful),
    "Bretonnian Longsword":         ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon | ItemGroups.DLC,                                  BASE_ID + 1410, ItemClassification.useful),
    "Bretonnian Sword and Shield":  ItemData(ItemGroups.Weapon | ItemGroups.GrailKnightWeapon | ItemGroups.DLC,                              BASE_ID + 1411, ItemClassification.useful),
    "Spear and Shield (Kruber)":    ItemData(ItemGroups.Weapon | ItemGroups.NoGrailWeapon | ItemGroups.DLC,                                  BASE_ID + 1412, ItemClassification.useful),

    # Weapons — Markus Kruber (ranged)
    "Blunderbuss":                  ItemData(ItemGroups.Weapon | ItemGroups.KruberRWeapon,                                                   BASE_ID + 1420, ItemClassification.useful),
    "Handgun (Markus Kruber)":      ItemData(ItemGroups.Weapon | ItemGroups.KruberRWeapon,                                                   BASE_ID + 1421, ItemClassification.useful),
    "Longbow (Markus Kruber)":      ItemData(ItemGroups.Weapon | ItemGroups.HuntsmanWeapon,                                                  BASE_ID + 1422, ItemClassification.useful),
    "Repeater Handgun":             ItemData(ItemGroups.Weapon | ItemGroups.KruberRWeapon,                                                   BASE_ID + 1423, ItemClassification.useful),
}


# ============================================================
# Flat lookup dict required by the World class
# ============================================================

item_name_to_id: Dict[str, int] = {
    name: data.code for name, data in ITEM_TABLE.items()
}


# ============================================================
# Helper functions
# ============================================================

def get_items_by_group(group: ItemGroups) -> List[str]:
    """Return all item names that belong to a given ItemGroups flag."""
    return [name for name, data in ITEM_TABLE.items() if group in data.category]


def get_career_items(include_dlc: bool = True) -> List[str]:
    """Return all career unlock item names, optionally excluding DLC careers."""
    items = get_items_by_group(ItemGroups.Career)
    if not include_dlc:
        items = [name for name in items if ItemGroups.DLC not in ITEM_TABLE[name].category]
    return items


def get_weapon_items(include_dlc: bool = True) -> List[str]:
    """Return all weapon item names, optionally excluding DLC weapons."""
    items = get_items_by_group(ItemGroups.Weapon)
    if not include_dlc:
        items = [name for name in items if ItemGroups.DLC not in ITEM_TABLE[name].category]
    return items


def get_mission_items(include_dlc: bool = True) -> List[str]:
    """Return all mission item names, optionally excluding DLC missions."""
    items = get_items_by_group(ItemGroups.Mission)
    if not include_dlc:
        items = [name for name in items if ItemGroups.DLC not in ITEM_TABLE[name].category]
    return items


def get_dlc_mission_items(dlc_group: ItemGroups) -> List[str]:
    """Return mission items for a specific DLC group flag e.g. ItemGroups.DLC_Drachenfels."""
    return [name for name, data in ITEM_TABLE.items()
            if ItemGroups.Mission in data.category and dlc_group in data.category]


def get_trap_items() -> List[str]:
    """Return all trap item names."""
    return get_items_by_group(ItemGroups.Trap)


def get_filler_item_name() -> str:
    """Return the name of the filler item used to pad the pool."""
    return "Ravaged Art"