from dataclasses import dataclass
from typing import Optional

@dataclass
class MissionData:
    locations: list[str]
    dlc_group: Optional[str] = None
    is_lord: bool = False

mission_data: dict[str, MissionData] = {
    # Base campaign
    "Righteous Stand":      MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "Convocation of Decay": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "Hunger in The Dark":   MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "Athel Yenlui":         MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "The Screaming Bell":   MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "Fort Brachsenbrucke":  MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "Against The Grain":    MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "Empire in Flames":     MissionData(locations=["Complete The Level",   "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),
    "Festering Ground":     MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"]),

    # Lord missions
    "Halescourge":   MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2", "Slay Burblespue Halescourge"],   is_lord=True),
    "Into The Nest": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2", "Slay Skarrik Spinemanglr"],      is_lord=True),
    "The War Camp":  MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2", "Slay Bodvarr Ribspreader"],      is_lord=True),
    "The Skittergate":MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2", "Slay Rasknitt and Deathrattler", "Slay Gatekeeper Naglfahr"], is_lord=True),

    # Shadows Over Bogenhafen
    "The Pit":         MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Shadows Over Bogenhafen"),
    "The Blightreaper":MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Shadows Over Bogenhafen"),

    # Back to Ubersreik
    "The Horn of Magnus": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Back to Ubersreik"),
    "Garden of Morr":     MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Back to Ubersreik"),
    "Engines of War":     MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Back to Ubersreik"),
    "Fortunes of War":    MissionData(locations=["Complete Wave 1", "Complete Wave 2", "Complete Wave 3", "Complete Wave 4", "Complete Wave 5", "Complete Wave 6", "Complete Wave 7", "Complete Wave 8"], dlc_group="Back to Ubersreik"),

    # Winds of Magic
    "Dark Omens": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Winds of Magic"),

    # The Curse of Drachenfels
    "Old Haunts":          MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"],                                              dlc_group="The Curse of Drachenfels"),
    "Blood in the Darkness":MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"],                                             dlc_group="The Curse of Drachenfels"),
    "The Enchanters Lair": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2", "Slay Nurgloth the Eternal"],                 dlc_group="The Curse of Drachenfels"),

    # A Treacherous Adventure
    "Trail of Treachery": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"],                              dlc_group="A Treacherous Adventure"),
    "Tower of Treachery": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2", "Slay Sofia Fuegonasus"],     dlc_group="A Treacherous Adventure"),

    # Karak Azgaraz
    "Mission of Mercy":       MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Karak Azgaraz"),
    "A Grudge Served Cold":   MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Karak Azgaraz"),
    "Khazukan Kazakit-Ha!":   MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Karak Azgaraz"),
    "A Parting of the Waves": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Karak Azgaraz"),

    # Verminous Dreams
    "The Forsaken Temple": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Verminous Dreams"),
    "Devious Delvings":    MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Verminous Dreams"),
    "The Well of Dreams":  MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Verminous Dreams"),

    # Reikland Tales
    "Return to the Reik": MissionData(locations=["Complete The Mission", "Tome 1", "Tome 2", "Tome 3", "Grimoire 1", "Grimoire 2"], dlc_group="Reikland Tales"),

    # Chaos Wastes
    "Expedition of Fortitude":     MissionData(locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear", "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear", "Stage 7 Arena of Fortitude Complete"],     dlc_group="Chaos Wastes"),
    "Expedition of Courage":       MissionData(locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear", "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear", "Stage 7 Arena of Courage Complete"],       dlc_group="Chaos Wastes"),
    "Expedition of Determination": MissionData(locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear", "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear", "Stage 7 Arena of Determination Complete"], dlc_group="Chaos Wastes"),
    "Expedition to the Citadel":   MissionData(locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear", "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear", "Stage 7 Clear", "Complete The Citadel of Eternity"], dlc_group="Chaos Wastes"),
}