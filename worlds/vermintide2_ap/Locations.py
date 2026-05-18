from collections.abc import Callable
from typing import ClassVar, Optional

from BaseClasses import CollectionState
from .Items import Items
from .MissionData import mission_data
from .StateLogic import StateLogic
from .Options import Vermintide2Options, Goal


class LocationData:
    __slots__ = ("region", "name", "code", "rule")
    region: str
    name: str
    code: Optional[int]
    rule: Optional[Callable[[CollectionState], bool]]

    def __init__(self, region: str, name: str, code: Optional[int],
                 rule: Optional[Callable[[CollectionState], bool]] = None):
        self.region = region
        self.name = name
        self.code = code
        self.rule = rule


class VictoryLocation(LocationData):
    def __init__(self, region: str, rule: Callable[[CollectionState], bool]):
        super().__init__(
            region=region,
            name="Victory",
            code=None,
            rule=rule
        )


class GlobalLocation(LocationData):
    def __init__(self, name: str, location_id: int,
                 rule: Optional[Callable[[CollectionState], bool]] = None):
        super().__init__(
            region="Menu",
            name=name,
            code=location_id,
            rule=rule
        )

class GlobalHeroLocation(GlobalLocation):
    def __init__(self, hero_name: str, career: str, code: int,
                 state_logic: StateLogic):
        super().__init__(
            f"Complete a Mission as {career} {hero_name}",
            code,
            lambda state: state_logic.can_play_career(state, career)
        )


class GlobalSlayLocation(GlobalLocation):
    def __init__(self, enemy_name: str, code: int,
                 rule: Optional[Callable[[CollectionState], bool]] = None):
        super().__init__(f"Slay a {enemy_name}", code, rule)


class GlobalSlayTotalLocation(GlobalLocation):
    def __init__(self, count: int, enemy_type: str, code: int,
                 rule: Optional[Callable[[CollectionState], bool]] = None):
        super().__init__(f"Slay a total of {count} {enemy_type}", code, rule)


class MissionLocation(LocationData):
    def __init__(self, mission: str, difficulty: str, code: int,
                 state_logic: StateLogic):
        super().__init__(
            region=mission,
            name=f"Complete The Mission {mission} on {difficulty}",
            code=code,
            rule=lambda state: state_logic.has_difficulty_unlocked(state,
                                                                   difficulty)
        )


class TomeLocation(LocationData):
    def __init__(self, mission: str, tome_number: int, code: int):
        super().__init__(
            region=mission,
            name=f"Tome {tome_number} ({mission})",
            code=code,
            rule=None
        )


class GrimoireLocation(LocationData):
    def __init__(self, mission: str, grimoire_number: int, code: int):
        super().__init__(
            region=mission,
            name=f"Tome {grimoire_number} ({mission})",
            code=code,
            rule=None
        )


class LordLocation(LocationData):
    def __init__(self, mission: str, lord_name: str, code: int):
        super().__init__(
            region=mission,
            name=f"Slay {lord_name}",
            code=code,
            rule=None
        )


class Locations:
    base_id: ClassVar[int] = 0
    options: Vermintide2Options
    state_logic: StateLogic
    items: Items

    @classmethod
    def setup(cls, base_id: int) -> None:
        cls.base_id = base_id
        cls.global_location_start = base_id + 2000
        cls.mission_location_start = base_id + 3000
        cls.event_location_start = base_id + 4000

    def __init__(self, options: Vermintide2Options,
                 state_logic: StateLogic,
                 items: Items):
        self.options = options
        self.state_logic = state_logic
        self.items = items

    global_location_start: ClassVar[int]
    mission_location_start: ClassVar[int]
    event_locations_start: ClassVar[int]

    def get_global_locations(self) -> list[LocationData]:
        return [
            # Taal's Horn Keep — no rule
            GlobalLocation("Enter Catrinne's Secret Tower",
                           self.base_id + 2000),
            GlobalLocation("Complete the Jumping Puzzle", self.base_id + 2001),

            # Slay monsters
            GlobalSlayLocation("Rat Ogre", self.base_id + 2020,
                               self.state_logic.missions_or_item(5, "The Screaming Bell")),
            GlobalSlayLocation("Stormfiend", self.base_id + 2021,
                               self.state_logic.missions(5)),
            GlobalSlayLocation("Bile Troll", self.base_id + 2022,
                               self.state_logic.missions_or_item(5, "Hunger In The Dark")),
            GlobalSlayLocation("Chaos Spawn", self.base_id + 2023,
                               self.state_logic.missions(5)),
            GlobalSlayLocation("Minotaur", self.base_id + 2024,
                               self.state_logic.missions(6)),
            GlobalLocation("Slay 10 Monsters", self.base_id + 2025,
                           self.state_logic.missions(10)),

            # Slay elites
            GlobalLocation("Defeat a Scaven Patrol", self.base_id + 2030,
                           self.state_logic.missions(3)),
            GlobalLocation("Defeat a pack of Plague Monks", self.base_id + 2031,
                           self.state_logic.missions(3)),
            GlobalSlayLocation("Chaos Warrior", self.base_id + 2032,
                               self.state_logic.missions(3)),
            GlobalSlayLocation("Chaos Warrior with Shield", self.base_id + 2033,
                           self.state_logic.missions(3)),
            GlobalSlayLocation("Bestigor", self.base_id + 2034,
                               self.state_logic.missions(4)),
            GlobalSlayTotalLocation(25, "Elites", self.base_id + 2035,
                                    self.state_logic.missions(5)),
            GlobalSlayTotalLocation(50, "Elites", self.base_id + 2036,
                                    self.state_logic.missions(8)),
            GlobalSlayTotalLocation(100, "Elites", self.base_id + 2037,
                                    self.state_logic.missions(10)),

            # Slay specials
            GlobalSlayLocation("Poison Wind Globadier", self.base_id + 2040,
                               self.state_logic.missions(3)),
            GlobalSlayLocation("Ratling Gunner", self.base_id + 2041,
                               self.state_logic.missions(3)),
            GlobalSlayLocation("Gutter Runner", self.base_id + 2042,
                               self.state_logic.missions(3)),
            GlobalSlayLocation("Blightstormer", self.base_id + 2043,
                               self.state_logic.missions(3)),
            GlobalSlayLocation("Lifeleech", self.base_id + 2044,
                               self.state_logic.missions(3)),
            GlobalSlayLocation("Packmaster", self.base_id + 2045,
                               self.state_logic.missions(3)),
            GlobalSlayLocation("Warpfire Thrower", self.base_id + 2046,
                               self.state_logic.missions(3)),
            GlobalSlayTotalLocation(10, "Specials", self.base_id + 2047,
                                    self.state_logic.missions(3)),
            GlobalSlayTotalLocation(20, "Specials", self.base_id + 2048,
                                    self.state_logic.missions(6)),
            GlobalSlayTotalLocation(50, "Specials", self.base_id + 2049,
                                    self.state_logic.missions(9)),

            # Career checks — Viktor Saltzpyre (default: Witch Hunter Captain)
            GlobalHeroLocation("Viktor Saltzpyre", "Bounty Hunter", self.base_id + 2050, self.state_logic),
            GlobalHeroLocation("Viktor Saltzpyre", "Zealot",              self.base_id + 2051, self.state_logic),
            GlobalHeroLocation("Viktor Saltzpyre", "Warrior Priest of Sigmar", self.base_id + 2052, self.state_logic),

            # Career checks — Bardin Goreksson (default: Ranger Veteran)
            GlobalHeroLocation("Bardin Goreksson", "Ironbreaker",         self.base_id + 2060, self.state_logic),
            GlobalHeroLocation("Bardin Goreksson", "Slayer",              self.base_id + 2061, self.state_logic),
            GlobalHeroLocation("Bardin Goreksson", "Outcast Engineer",    self.base_id + 2062, self.state_logic),

            # Career checks — Kerillian (default: Waystalker)
            GlobalHeroLocation("Kerillian", "Handmaiden",                 self.base_id + 2070, self.state_logic),
            GlobalHeroLocation("Kerillian", "Shade",                      self.base_id + 2071, self.state_logic),
            GlobalHeroLocation("Kerillian", "Sister of the Thorn",        self.base_id + 2072, self.state_logic),

            # Career checks — Sienna Fuegonasus (default: Battle Wizard)
            GlobalHeroLocation("Sienna Fuegonasus", "Pyromancer",         self.base_id + 2080, self.state_logic),
            GlobalHeroLocation("Sienna Fuegonasus", "Unchained",          self.base_id + 2081, self.state_logic),
            GlobalHeroLocation("Sienna Fuegonasus", "Necromancer",        self.base_id + 2082, self.state_logic),

            # Career checks — Markus Kruber (default: Mercenary)
            GlobalHeroLocation("Markus Kruber", "Huntsman",               self.base_id + 2090, self.state_logic),
            GlobalHeroLocation("Markus Kruber", "Foot Knight",            self.base_id + 2091, self.state_logic),
            GlobalHeroLocation("Markus Kruber", "Grail Knight",           self.base_id + 2092, self.state_logic),
        ]

    def get_mission_locations(self, for_data_package: bool = False) -> list[
        LocationData]:
        location_table: list[LocationData] = []
        location_id = self.mission_location_start

        for mission, data in mission_data.items():
            if not for_data_package and data.dlc_group:
                dlc_key = data.dlc_group.replace(" ", "_")
                if dlc_key not in self.options.campaign.value:
                    location_id += len(data.locations)
                    continue

            for loc_name in data.locations:
                if not for_data_package:
                    if "Tome" in loc_name and not self.options.add_tomes:
                        location_id += 1
                        continue
                    if "Grimoire" in loc_name and not self.options.add_grimoires:
                        location_id += 1
                        continue

                location_table.append(
                    MissionLocation(mission, loc_name, location_id, self.state_logic))
                location_id += 1

        return location_table

    def get_event_locations(self) -> list[LocationData]:
        if self.options.goal == Goal.option_chaos_wastes:
            return [VictoryLocation(
                region="CitadelofEternity",
                rule=self.state_logic.can_complete_citadel
            )]
        #Default path
        return [VictoryLocation(
            region="The Skittergate",
            rule = self.state_logic.can_complete_skittergate
        )]

    def get_locations_for_data_package(self) -> dict[str, int]:
        """Must include all possible location names and their IDs"""
        location_table = self.get_global_locations()
        location_table.extend(self.get_mission_locations(for_data_package=True))

        return {location.name: location.code for location in location_table
                if location.code is not None}

    def get_locations(self) -> list[LocationData]:
        """Only return locations active for this game based on settings"""
        if not self.options or not self.state_logic:
            raise Exception(
                "Locations must be initialized with options and state_logic before calling get_locations()")

        location_table = self.get_global_locations()
        location_table.extend(self.get_mission_locations())
        location_table.extend(self.get_event_locations())

        return location_table
