from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MissionData:
    tomes: int = 3
    grimoires: int = 2
    lord_slays: list[str] = field(default_factory=list)
    custom_locations: list[str] = field(default_factory=list)
    chests: int = 2
    ammo_crates: int = 1
    ravaged_art: int = 1
    dlc_group: Optional[str] = None
    is_lord: bool = False


mission_data: dict[str, MissionData] = {
    # Base campaign
    "Righteous Stand":      MissionData(),
    "Convocation of Decay": MissionData(),
    "Hunger in The Dark":   MissionData(),
    "Athel Yenlui":         MissionData(),
    "The Screaming Bell":   MissionData(),
    "Fort Brachsenbrucke":  MissionData(),
    "Against The Grain":    MissionData(),
    "Empire in Flames":     MissionData(),
    "Festering Ground":     MissionData(),

    # Lord missions
    "Halescourge":    MissionData(lord_slays=["Burblespue Halescourge"],                       is_lord=True),
    "Into The Nest":  MissionData(lord_slays=["Skarrik Spinemanglr"],                          is_lord=True),
    "The War Camp":   MissionData(lord_slays=["Bodvarr Ribspreader"],                          is_lord=True),
    "The Skittergate":MissionData(lord_slays=["Rasknitt and Deathrattler", "Gatekeeper Naglfahr"], is_lord=True),

    # Shadows Over Bogenhafen
    "The Pit":         MissionData(dlc_group="Shadows Over Bogenhafen"),
    "The Blightreaper":MissionData(dlc_group="Shadows Over Bogenhafen"),

    # Back to Ubersreik
    "The Horn of Magnus": MissionData(dlc_group="Back to Ubersreik"),
    "Garden of Morr":     MissionData(dlc_group="Back to Ubersreik"),
    "Engines of War":     MissionData(dlc_group="Back to Ubersreik"),
    "Fortunes of War":    MissionData(
        tomes=0, grimoires=0, chests=0, ammo_crates=0, ravaged_art=0,
        custom_locations=["Complete Wave 1", "Complete Wave 2", "Complete Wave 3",
                          "Complete Wave 4", "Complete Wave 5", "Complete Wave 6",
                          "Complete Wave 7", "Complete Wave 8"],
        dlc_group="Back to Ubersreik"
    ),

    # Winds of Magic
    "Dark Omens": MissionData(dlc_group="Winds of Magic"),

    # The Curse of Drachenfels
    "Old Haunts":           MissionData(dlc_group="The Curse of Drachenfels"),
    "Blood in the Darkness":MissionData(dlc_group="The Curse of Drachenfels"),
    "The Enchanters Lair":  MissionData(lord_slays=["Nurgloth the Eternal"], dlc_group="The Curse of Drachenfels"),

    # A Treacherous Adventure
    "Trail of Treachery": MissionData(dlc_group="A Treacherous Adventure"),
    "Tower of Treachery": MissionData(lord_slays=["Sofia Fuegonasus"], dlc_group="A Treacherous Adventure"),

    # Karak Azgaraz
    "Mission of Mercy":       MissionData(dlc_group="Karak Azgaraz"),
    "A Grudge Served Cold":   MissionData(dlc_group="Karak Azgaraz"),
    "Khazukan Kazakit-Ha!":   MissionData(dlc_group="Karak Azgaraz"),
    "A Parting of the Waves": MissionData(dlc_group="Karak Azgaraz"),

    # Verminous Dreams
    "The Forsaken Temple": MissionData(dlc_group="Verminous Dreams"),
    "Devious Delvings":    MissionData(dlc_group="Verminous Dreams"),
    "The Well of Dreams":  MissionData(dlc_group="Verminous Dreams"),

    # Reikland Tales
    "Return to the Reik": MissionData(dlc_group="Reikland Tales"),

    # Chaos Wastes
    "Expedition of Fortitude":     MissionData(tomes=0, grimoires=0, chests=0, ammo_crates=0, ravaged_art=0, dlc_group="Chaos Wastes",
        custom_locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear",
                          "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear",
                          "Stage 7 Arena of Fortitude Complete"]),
    "Expedition of Courage":       MissionData(tomes=0, grimoires=0, chests=0, ammo_crates=0, ravaged_art=0, dlc_group="Chaos Wastes",
        custom_locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear",
                          "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear",
                          "Stage 7 Arena of Courage Complete"]),
    "Expedition of Determination": MissionData(tomes=0, grimoires=0, chests=0, ammo_crates=0, ravaged_art=0, dlc_group="Chaos Wastes",
        custom_locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear",
                          "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear",
                          "Stage 7 Arena of Determination Complete"]),
    "Expedition to the Citadel":   MissionData(tomes=0, grimoires=0, chests=0, ammo_crates=0, ravaged_art=0, dlc_group="Chaos Wastes",
        custom_locations=["Stage 1 Clear", "Stage 2 Clear", "Stage 3 Clear",
                          "Stage 4 Clear", "Stage 5 Clear", "Stage 6 Clear",
                          "Stage 7 Clear", "Complete The Citadel of Eternity"]),
}