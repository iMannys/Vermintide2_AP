from typing import Dict, List, ClassVar, Optional, Sequence
from BaseClasses import Item, ItemClassification
from .Options import Vermintide2Options
from .ItemData import ItemData, ItemGroups
from random import Random

class Items:
    item_data: ClassVar[dict[str, ItemData]] = {}

    @classmethod
    def setup(cls, base_id: int) -> None:
        cls.item_data = {

        # ----------------------------------------------------------
        # Difficulty Unlocks
        # progression: gates entire difficulty tiers in location rules
        # ----------------------------------------------------------
        "Unlock Veteran Difficulty":   ItemData(ItemGroups.DifficultyUnlock, base_id + 0,  ItemClassification.progression),
        "Unlock Champion Difficulty":  ItemData(ItemGroups.DifficultyUnlock, base_id + 1,  ItemClassification.progression),
        "Unlock Legend Difficulty":    ItemData(ItemGroups.DifficultyUnlock, base_id + 2,  ItemClassification.progression),
        "Unlock Cataclysm Difficulty": ItemData(ItemGroups.DifficultyUnlock, base_id + 3,  ItemClassification.progression),

        # ----------------------------------------------------------
        # Careers — Viktor Saltzpyre
        # Default career (Witch Hunter Captain) is always unlocked, not in pool.
        # progression: hero-completion locations require having a career for that hero
        # ----------------------------------------------------------
        "Bounty Hunter":               ItemData(ItemGroups.Career, base_id + 10, ItemClassification.progression),
        "Zealot":                      ItemData(ItemGroups.Career, base_id + 11, ItemClassification.progression),
        "Warrior Priest of Sigmar":    ItemData(ItemGroups.Career | ItemGroups.DLC, base_id + 12, ItemClassification.progression),

        # ----------------------------------------------------------
        # Careers — Bardin Goreksson
        # Default career (Ranger Veteran) is always unlocked, not in pool.
        # ----------------------------------------------------------
        "Ironbreaker":                 ItemData(ItemGroups.Career, base_id + 20, ItemClassification.progression),
        "Slayer":                      ItemData(ItemGroups.Career, base_id + 21, ItemClassification.progression),
        "Outcast Engineer":            ItemData(ItemGroups.Career | ItemGroups.DLC, base_id + 22, ItemClassification.progression),

        # ----------------------------------------------------------
        # Careers — Kerillian
        # Default career (Waystalker) is always unlocked, not in pool.
        # ----------------------------------------------------------
        "Handmaiden":                  ItemData(ItemGroups.Career, base_id + 30, ItemClassification.progression),
        "Shade":                       ItemData(ItemGroups.Career, base_id + 31, ItemClassification.progression),
        "Sister of the Thorn":         ItemData(ItemGroups.Career | ItemGroups.DLC, base_id + 32, ItemClassification.progression),

        # ----------------------------------------------------------
        # Careers — Sienna Fuegonasus
        # Default career (Battle Wizard) is always unlocked, not in pool.
        # ----------------------------------------------------------
        "Pyromancer":                  ItemData(ItemGroups.Career, base_id + 40, ItemClassification.progression),
        "Unchained":                   ItemData(ItemGroups.Career, base_id + 41, ItemClassification.progression),
        "Necromancer":                 ItemData(ItemGroups.Career | ItemGroups.DLC, base_id + 42, ItemClassification.progression),

        # ----------------------------------------------------------
        # Careers — Markus Kruber
        # Default career (Mercenary) is always unlocked, not in pool.
        # ----------------------------------------------------------
        "Huntsman":                    ItemData(ItemGroups.Career, base_id + 50, ItemClassification.progression),
        "Foot Knight":                 ItemData(ItemGroups.Career, base_id + 51, ItemClassification.progression),
        "Grail Knight":                ItemData(ItemGroups.Career | ItemGroups.DLC, base_id + 52, ItemClassification.progression),

        # ----------------------------------------------------------
        # Equipment Power Caps
        # progression: gates access to higher-tier gear and harder content
        # ----------------------------------------------------------
        "Equipment Power Cap 100":     ItemData(ItemGroups.PowerLevel, base_id + 500, ItemClassification.progression),
        "Equipment Power Cap 150":     ItemData(ItemGroups.PowerLevel, base_id + 501, ItemClassification.progression),
        "Equipment Power Cap 200":     ItemData(ItemGroups.PowerLevel, base_id + 502, ItemClassification.progression),
        "Equipment Power Cap 250":     ItemData(ItemGroups.PowerLevel, base_id + 503, ItemClassification.progression),
        "Equipment Power Cap 300":     ItemData(ItemGroups.PowerLevel, base_id + 504, ItemClassification.progression),

        # ----------------------------------------------------------
        # Traps
        # ----------------------------------------------------------
        "Trap: Spawn Monster":         ItemData(ItemGroups.Trap, base_id + 100, ItemClassification.trap, count=3),
        "Trap: Spawn Horde":           ItemData(ItemGroups.Trap, base_id + 101, ItemClassification.trap, count=5),
        "Trap: Spawn Patrol":          ItemData(ItemGroups.Trap, base_id + 102, ItemClassification.trap, count=3),
        "Trap: Drop Firebomb":         ItemData(ItemGroups.Trap, base_id + 103, ItemClassification.trap, count=4),
        "Trap: Empty Career Ability":  ItemData(ItemGroups.Trap, base_id + 104, ItemClassification.trap, count=4),

        # ----------------------------------------------------------
        # Filler
        # count=0: amount is calculated dynamically in create_items()
        # to pad the pool to match location count
        # ----------------------------------------------------------
        "Ravaged Art":                 ItemData(ItemGroups.Filler, base_id + 200, ItemClassification.filler, count=0),
        "Healing Draught":             ItemData(ItemGroups.Filler, base_id + 201, ItemClassification.filler, count=0),
        "Medical Supplies":            ItemData(ItemGroups.Filler, base_id + 202, ItemClassification.filler, count=0),
        "Potion of Concentration":     ItemData(ItemGroups.Filler, base_id + 203, ItemClassification.filler, count=0),
        "Potion of Speed":             ItemData(ItemGroups.Filler, base_id + 204, ItemClassification.filler, count=0),
        "Potion of Strength":          ItemData(ItemGroups.Filler, base_id + 205, ItemClassification.filler, count=0),
        "Bomb":                        ItemData(ItemGroups.Filler, base_id + 206, ItemClassification.filler, count=0),
        "Incendiary Bomb":             ItemData(ItemGroups.Filler, base_id + 207, ItemClassification.filler, count=0),
        "Engineer Bomb":               ItemData(ItemGroups.Filler & ItemGroups.DLC, base_id + 208, ItemClassification.filler, count=0),

        # ----------------------------------------------------------
        # Helmgart Campaign Missions
        # progression: used in logic to gate lord missions behind standard missions
        # ----------------------------------------------------------
        "Righteous Stand":             ItemData(ItemGroups.Mission, base_id + 300, ItemClassification.progression),
        "Convocation of Decay":        ItemData(ItemGroups.Mission, base_id + 301, ItemClassification.progression),
        "Hunger in The Dark":          ItemData(ItemGroups.Mission, base_id + 302, ItemClassification.progression),
        "Against The Grain":           ItemData(ItemGroups.Mission, base_id + 303, ItemClassification.progression),
        "The Screaming Bell":          ItemData(ItemGroups.Mission, base_id + 304, ItemClassification.progression),
        "Athel Yenlui":                ItemData(ItemGroups.Mission, base_id + 305, ItemClassification.progression),
        "Festering Ground":            ItemData(ItemGroups.Mission, base_id + 306, ItemClassification.progression),
        "Empire in Flames":            ItemData(ItemGroups.Mission, base_id + 307, ItemClassification.progression),
        # Lord missions
        "Halescourge":                 ItemData(ItemGroups.Mission, base_id + 310, ItemClassification.progression),
        "Into The Nest":               ItemData(ItemGroups.Mission, base_id + 311, ItemClassification.progression),
        "Fort Brachsenbrucke":         ItemData(ItemGroups.Mission, base_id + 312, ItemClassification.progression),
        "The Skittergate":             ItemData(ItemGroups.Mission, base_id + 313, ItemClassification.progression),
        "The War Camp":                ItemData(ItemGroups.Mission, base_id + 314, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — Shadows Over Bogenhafen (free DLC)
        # ----------------------------------------------------------
        "The Pit":                     ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Bogenhafen,       base_id + 400, ItemClassification.progression),
        "The Blightreaper":            ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Bogenhafen,       base_id + 401, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — Back to Ubersreik
        # ----------------------------------------------------------
        "The Horn of Magnus":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 410, ItemClassification.progression),
        "Garden of Morr":              ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 411, ItemClassification.progression),
        "Engines of War":              ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 412, ItemClassification.progression),
        "Fortunes of War":             ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 413, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — Winds of Magic
        # ----------------------------------------------------------
        "Dark Omens":                  ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,    base_id + 420, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — The Curse of Drachenfels
        # ----------------------------------------------------------
        "Old Haunts":                  ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Drachenfels,      base_id + 430, ItemClassification.progression),
        "Blood in the Darkness":       ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Drachenfels,      base_id + 431, ItemClassification.progression),
        "The Enchanters Lair":         ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Drachenfels,      base_id + 432, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — A Treacherous Adventure
        # ----------------------------------------------------------
        "Trail of Treachery":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Treachery,        base_id + 440, ItemClassification.progression),
        "Tower of Treachery":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_Treachery,        base_id + 441, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — Karak Azgaraz
        # ----------------------------------------------------------
        "Mission of Mercy":            ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     base_id + 450, ItemClassification.progression),
        "A Grudge Served Cold":        ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     base_id + 451, ItemClassification.progression),
        "Khazukan Kazakit-Ha!":        ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     base_id + 452, ItemClassification.progression),
        "A Parting of the Waves":      ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_KarakAzgaraz,     base_id + 453, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — Verminous Dreams
        # ----------------------------------------------------------
        "The Forsaken Temple":         ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_VerminousDreams,  base_id + 460, ItemClassification.progression),
        "Devious Delvings":            ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_VerminousDreams,  base_id + 461, ItemClassification.progression),
        "The Well of Dreams":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_VerminousDreams,  base_id + 462, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — Reikland Tales
        # ----------------------------------------------------------
        "Return to the Reik":          ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ReiklandTales,    base_id + 470, ItemClassification.progression),

        # ----------------------------------------------------------
        # DLC Missions — Chaos Wastes
        # ----------------------------------------------------------
        "Expedition of Fortitude":     ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      base_id + 480, ItemClassification.progression),
        "Expedition of Courage":       ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      base_id + 481, ItemClassification.progression),
        "Expedition of Determination": ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      base_id + 482, ItemClassification.progression),
        "Expedition to the Citadel":   ItemData(ItemGroups.Mission | ItemGroups.DLC | ItemGroups.DLC_ChaosWastes,      base_id + 483, ItemClassification.progression),

        # ----------------------------------------------------------
        # Weapons — Viktor Saltzpyre (melee)
        # useful: good to have but not referenced in logic rules
        # ----------------------------------------------------------
        "Rapier":                       ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   base_id + 1000, ItemClassification.useful),
        "Falchion":                     ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   base_id + 1001, ItemClassification.useful),
        "Axe (Viktor Saltzpyre)":       ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   base_id + 1002, ItemClassification.useful),
        "Greatsword (Viktor Saltzpyre)":ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   base_id + 1003, ItemClassification.useful),
        "Flail":                        ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon,                                                   base_id + 1004, ItemClassification.useful),
        "Axe and Falchion":             ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 1005, ItemClassification.useful),
        "Billhook":                     ItemData(ItemGroups.Weapon | ItemGroups.ViktorMWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,     base_id + 1006, ItemClassification.useful),
        # Warrior Priest exclusive melee
        "Flail and Shield":             ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.DLC,                             base_id + 1007, ItemClassification.useful),
        "Reckoner Great Hammer":        ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.ZealotWeapon | ItemGroups.DLC,   base_id + 1008, ItemClassification.useful),
        "Paired Skull-Splitters":       ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.ZealotWeapon | ItemGroups.DLC,   base_id + 1009, ItemClassification.useful),
        "Skull-Splitter and Tome":      ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.DLC,                             base_id + 1010, ItemClassification.useful),
        "Skull-Splitter and Shield":    ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.DLC,                             base_id + 1011, ItemClassification.useful),
        "Skull-Splitter Hammer":        ItemData(ItemGroups.Weapon | ItemGroups.WarriorPriestWeapon | ItemGroups.ZealotWeapon | ItemGroups.DLC,   base_id + 1012, ItemClassification.useful),

        # Weapons — Viktor Saltzpyre (ranged)
        "Brace of Pistols":             ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   base_id + 1020, ItemClassification.useful),
        "Volley Crossbow (Viktor)":     ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   base_id + 1021, ItemClassification.useful),
        "Repeater Pistol":              ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   base_id + 1022, ItemClassification.useful),
        "Crossbow (Viktor Saltzpyre)":  ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon,                                                   base_id + 1023, ItemClassification.useful),
        "Griffonfoot Pistols":          ItemData(ItemGroups.Weapon | ItemGroups.ViktorRWeapon | ItemGroups.DLC,                                  base_id + 1024, ItemClassification.useful),

        # ----------------------------------------------------------
        # Weapons — Bardin Goreksson (melee)
        # ----------------------------------------------------------
        "Great Hammer (Bardin)":        ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   base_id + 1100, ItemClassification.useful),
        "Great Axe":                    ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   base_id + 1101, ItemClassification.useful),
        "Axe (Bardin Goreksson)":       ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   base_id + 1102, ItemClassification.useful),
        "Hammer":                       ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   base_id + 1103, ItemClassification.useful),
        "War Pick":                     ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon,                                                   base_id + 1104, ItemClassification.useful),
        "Dual Hammers":                 ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 1105, ItemClassification.useful),
        "Cog Hammer":                   ItemData(ItemGroups.Weapon | ItemGroups.BardinMWeapon | ItemGroups.DLC,                                  base_id + 1106, ItemClassification.useful),
        # Shield weapons
        "Axe and Shield":               ItemData(ItemGroups.Weapon | ItemGroups.BardinShields,                                                   base_id + 1107, ItemClassification.useful),
        "Hammer and Shield":            ItemData(ItemGroups.Weapon | ItemGroups.BardinShields,                                                   base_id + 1108, ItemClassification.useful),
        # Slayer exclusive
        "Dual Axes":                    ItemData(ItemGroups.Weapon | ItemGroups.SlayerWeapon,                                                    base_id + 1109, ItemClassification.useful),
        "Throwing Axes":                ItemData(ItemGroups.Weapon | ItemGroups.SlayerWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,     base_id + 1110, ItemClassification.useful),

        # Weapons — Bardin Goreksson (ranged)
        "Crossbow (Bardin Goreksson)":  ItemData(ItemGroups.Weapon | ItemGroups.BardinCrossbow,                                                  base_id + 1120, ItemClassification.useful),
        "Handgun (Bardin Goreksson)":   ItemData(ItemGroups.Weapon | ItemGroups.BardinRWeapon,                                                   base_id + 1121, ItemClassification.useful),
        "Grudge-Raker":                 ItemData(ItemGroups.Weapon | ItemGroups.BardinRWeapon,                                                   base_id + 1122, ItemClassification.useful),
        "Masterwork Pistol":            ItemData(ItemGroups.Weapon | ItemGroups.BardinRWeapon | ItemGroups.DLC,                                  base_id + 1123, ItemClassification.useful),
        "Drakefire Pistols":            ItemData(ItemGroups.Weapon | ItemGroups.BardinTechWeapon,                                                base_id + 1124, ItemClassification.useful),
        "Drakegun":                     ItemData(ItemGroups.Weapon | ItemGroups.BardinTechWeapon,                                                base_id + 1125, ItemClassification.useful),
        "Trollhammer Torpedo":          ItemData(ItemGroups.Weapon | ItemGroups.BardinTechWeapon | ItemGroups.DLC,                               base_id + 1126, ItemClassification.useful),

        # ----------------------------------------------------------
        # Weapons — Kerillian (melee)
        # ----------------------------------------------------------
        "Sword (Kerillian)":            ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                base_id + 1200, ItemClassification.useful),
        "Dual Daggers":                 ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                base_id + 1201, ItemClassification.useful),
        "Dual Swords":                  ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                base_id + 1202, ItemClassification.useful),
        "Sword and Dagger":             ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                base_id + 1203, ItemClassification.useful),
        "Glaive":                       ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                base_id + 1204, ItemClassification.useful),
        "Greatsword (Kerillian)":       ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                base_id + 1205, ItemClassification.useful),
        "Elven Spear":                  ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon,                                                base_id + 1206, ItemClassification.useful),
        "Elven Axe":                    ItemData(ItemGroups.Weapon | ItemGroups.KerillianMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik, base_id + 1207, ItemClassification.useful),
        "Spear and Shield (Kerillian)": ItemData(ItemGroups.Weapon | ItemGroups.HandmaidenWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic, base_id + 1208, ItemClassification.useful),

        # Weapons — Kerillian (ranged)
        "Swiftbow":                     ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon,                                                base_id + 1220, ItemClassification.useful),
        "Longbow (Kerillian)":          ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon,                                                base_id + 1221, ItemClassification.useful),
        "Hagbane Shortbow":             ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon,                                                base_id + 1222, ItemClassification.useful),
        "Volley Crossbow (Kerillian)":  ItemData(ItemGroups.Weapon | ItemGroups.ShadeWeapon,                                                     base_id + 1223, ItemClassification.useful),
        "Moonfire Bow":                 ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon | ItemGroups.DLC,                               base_id + 1224, ItemClassification.useful),
        "Briar Javelin":                ItemData(ItemGroups.Weapon | ItemGroups.KerillianRWeapon | ItemGroups.DLC,                               base_id + 1225, ItemClassification.useful),
        "Deepwood Staff":               ItemData(ItemGroups.Weapon | ItemGroups.SOTTWeapon | ItemGroups.DLC,                                     base_id + 1226, ItemClassification.useful),

        # ----------------------------------------------------------
        # Weapons — Sienna Fuegonasus (melee)
        # ----------------------------------------------------------
        "Sword (Sienna Fuegonasus)":    ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   base_id + 1300, ItemClassification.useful),
        "Mace (Sienna Fuegonasus)":     ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   base_id + 1301, ItemClassification.useful),
        "Fire Sword":                   ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   base_id + 1302, ItemClassification.useful),
        "Dagger":                       ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon,                                                   base_id + 1303, ItemClassification.useful),
        "Crowbill":                     ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 1304, ItemClassification.useful),
        "Flaming Flail":                ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,     base_id + 1305, ItemClassification.useful),
        "Ensorcelled Reaper":           ItemData(ItemGroups.Weapon | ItemGroups.SiennaMWeapon | ItemGroups.DLC,                                  base_id + 1306, ItemClassification.useful),

        # Weapons — Sienna Fuegonasus (ranged/staves)
        "Fireball Staff":               ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   base_id + 1320, ItemClassification.useful),
        "Flamestorm Staff":             ItemData(ItemGroups.Weapon | ItemGroups.SiennaFlameWeapon,                                               base_id + 1321, ItemClassification.useful),
        "Bolt Staff":                   ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   base_id + 1322, ItemClassification.useful),
        "Beam Staff":                   ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   base_id + 1323, ItemClassification.useful),
        "Conflagration Staff":          ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon,                                                   base_id + 1324, ItemClassification.useful),
        "Coruscation Staff":            ItemData(ItemGroups.Weapon | ItemGroups.SiennaRWeapon | ItemGroups.DLC,                                  base_id + 1325, ItemClassification.useful),
        "Soulstealer Staff":            ItemData(ItemGroups.Weapon | ItemGroups.NecromancerWeapon | ItemGroups.DLC,                              base_id + 1326, ItemClassification.useful),

        # ----------------------------------------------------------
        # Weapons — Markus Kruber (melee)
        # ----------------------------------------------------------
        "Greatsword (Markus Kruber)":   ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   base_id + 1400, ItemClassification.useful),
        "Halberd":                      ItemData(ItemGroups.Weapon | ItemGroups.NoGrailWeapon,                                                   base_id + 1401, ItemClassification.useful),
        "Sword (Markus Kruber)":        ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   base_id + 1402, ItemClassification.useful),
        "Executioner Sword":            ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   base_id + 1403, ItemClassification.useful),
        "Great Hammer (Markus Kruber)": ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   base_id + 1404, ItemClassification.useful),
        "Sword and Shield":             ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   base_id + 1405, ItemClassification.useful),
        "Mace (Markus Kruber)":         ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   base_id + 1406, ItemClassification.useful),
        "Mace and Shield":              ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon,                                                   base_id + 1407, ItemClassification.useful),
        "Mace and Sword":               ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon | ItemGroups.DLC | ItemGroups.DLC_BackToUbersreik,  base_id + 1408, ItemClassification.useful),
        "Tuskgor Spear":                ItemData(ItemGroups.Weapon | ItemGroups.KruberSpear | ItemGroups.DLC | ItemGroups.DLC_WindsOfMagic,       base_id + 1409, ItemClassification.useful),
        "Bretonnian Longsword":         ItemData(ItemGroups.Weapon | ItemGroups.KruberMWeapon | ItemGroups.DLC,                                  base_id + 1410, ItemClassification.useful),
        "Bretonnian Sword and Shield":  ItemData(ItemGroups.Weapon | ItemGroups.GrailKnightWeapon | ItemGroups.DLC,                              base_id + 1411, ItemClassification.useful),
        "Spear and Shield (Kruber)":    ItemData(ItemGroups.Weapon | ItemGroups.NoGrailWeapon | ItemGroups.DLC,                                  base_id + 1412, ItemClassification.useful),

        # Weapons — Markus Kruber (ranged)
        "Blunderbuss":                  ItemData(ItemGroups.Weapon | ItemGroups.KruberRWeapon,                                                   base_id + 1420, ItemClassification.useful),
        "Handgun (Markus Kruber)":      ItemData(ItemGroups.Weapon | ItemGroups.KruberRWeapon,                                                   base_id + 1421, ItemClassification.useful),
        "Longbow (Markus Kruber)":      ItemData(ItemGroups.Weapon | ItemGroups.HuntsmanWeapon,                                                  base_id + 1422, ItemClassification.useful),
        "Repeater Handgun":             ItemData(ItemGroups.Weapon | ItemGroups.KruberRWeapon,                                                   base_id + 1423, ItemClassification.useful),
        }
        cls.item_name_to_id = {name: data.code for name, data in cls.item_data.items()}
        cls.filler_items = tuple(
            item for item, details in cls.item_data.items()
            if details.category & ItemGroups.Filler)

    item_name_to_id: ClassVar[dict[str, int]] = {}
    filler_items: ClassVar[tuple[str, ...]] = ()

    @classmethod
    def get_item_names_per_category(cls) -> dict[str, set[str]]:
        groups: dict[str, set[str]] = {}

        for name, data in cls.item_data.items():
            for group in ItemGroups:
                if data.category & group:
                    groups.setdefault(group.name, set()).add(name)

        return groups

    player: int
    random: Random

    trap_chance: int
    enabled_traps: tuple[str, ...]

    def __init__(self, player: Optional[int], random: Random,
                 options: Vermintide2Options):
        self.player = player
        self.random = random
        self.options = options

        self.trap_chance = self.options.trap_chance.value
        self.enabled_traps = tuple(
            sorted(self.options.trap_selection.value))

    @classmethod
    def create_item_uninitialized(cls, name: str, player: int) -> Item:
        data: ItemData = cls.item_data[name]
        return Item(name, data.classification, data.code, player)

    def create_item(self, name: str, player: int) -> Item:
        data: ItemData = self.item_data[name]
        item_type = data.classification

        return Item(name, item_type, data.code, player)

    @classmethod
    def get_filler_item_name_uninitialized(cls, random: Random) -> str:
        return random.choice(cls.filler_items)

    def get_filler_item_name(self, random: Random,
                             filler_items: Sequence[str] | None) -> str:
        if self.enabled_traps and random.random() < (self.trap_chance / 100):
            return random.choice(self.enabled_traps)

        if filler_items:
            return random.choice(filler_items)
        else:
            return Items.get_filler_item_name_uninitialized(random)

    def get_excluded_items(self, precollected_items: list[Item]) -> set[str]:
        excluded_items: set[str] = {
            item.name
            for item in precollected_items
            if item.name in self.item_data
        }

        enabled_dlc: frozenset[str] = self.options.campaign.value

        _dlc_flag_to_campaign: dict[ItemGroups, str] = {
            ItemGroups.DLC_Bogenhafen:      "Shadows_Over_Bogenhafen",
            ItemGroups.DLC_BackToUbersreik: "Back_to_Ubersreik",
            ItemGroups.DLC_WindsOfMagic:    "Winds_of_Magic",
            ItemGroups.DLC_Drachenfels:     "The_Curse_of_Drachenfels",
            ItemGroups.DLC_Treachery:       "A_Treacherous_Adventure",
            ItemGroups.DLC_KarakAzgaraz:    "Karak_Azgaraz",
            ItemGroups.DLC_VerminousDreams: "Verminous_Dreams",
            ItemGroups.DLC_ReiklandTales:   "Reikland_Tales",
            ItemGroups.DLC_ChaosWastes:     "Chaos_Wastes",
        }
        campaign_dlc_flags = (ItemGroups.DLC_Bogenhafen | ItemGroups.DLC_BackToUbersreik |
                              ItemGroups.DLC_WindsOfMagic | ItemGroups.DLC_Drachenfels |
                              ItemGroups.DLC_Treachery | ItemGroups.DLC_KarakAzgaraz |
                              ItemGroups.DLC_VerminousDreams | ItemGroups.DLC_ReiklandTales |
                              ItemGroups.DLC_ChaosWastes)

        for item, details in self.item_data.items():
            cat = details.category

            # Traps are used only as dynamic filler, not fixed pool items
            if cat & ItemGroups.Trap:
                excluded_items.add(item)
                continue

            if cat & ItemGroups.Weapon:
                if not self.options.add_weapon:
                    excluded_items.add(item)
                    continue
                if cat & ItemGroups.DLC_BackToUbersreik and not self.options.back_to_ubersreik_weapons:
                    excluded_items.add(item)
                    continue
                if cat & ItemGroups.DLC_WindsOfMagic and not self.options.winds_of_magic_weapons:
                    excluded_items.add(item)
                    continue
                # Forgotten Relics: DLC weapons not tied to a specific campaign
                if cat & ItemGroups.DLC and not (cat & campaign_dlc_flags) and not self.options.forgotten_relics:
                    excluded_items.add(item)
                    continue

            # DLC careers excluded when dlc_careers is off
            if cat & ItemGroups.Career and cat & ItemGroups.DLC and not self.options.dlc_careers:
                excluded_items.add(item)
                continue

            # DLC missions excluded when their campaign is not enabled
            if cat & ItemGroups.Mission and cat & ItemGroups.DLC:
                for dlc_flag, campaign_key in _dlc_flag_to_campaign.items():
                    if cat & dlc_flag and campaign_key not in enabled_dlc:
                        excluded_items.add(item)
                        break

        return excluded_items

    def build_item_pool(self, random: Random, precollected_items: list[Item],
                        number_of_locations: int) -> list[Item]:
        excluded_from_pool = self.get_excluded_items(precollected_items)

        # Expand each item by its count, skipping excluded/uncategorized items
        all_items = [
            self.create_item(name, self.player)
            for name, data in self.item_data.items()
            if data.category and name not in excluded_from_pool
            for _ in range(data.count)
        ]

        # Only keep filler items that belong to the Filler category
        pool = [
            item for item in all_items
            if item.classification != ItemClassification.filler
               or self.item_data[item.name].category & ItemGroups.Filler
        ]

        free_space = number_of_locations - len(pool)
        if free_space < 0:
            raise Exception(
                f"Location pool starved: {len(pool)} items for {number_of_locations} locations")

        # Fill remaining slots with filler/traps, excluding already-excluded filler items
        available_filler = [item for item in self.filler_items if
                            item not in excluded_from_pool]
        pool += [
            self.create_item(
                self.get_filler_item_name(random, available_filler),
                self.player)
            for _ in range(free_space)
        ]

        return pool
