from collections.abc import Callable
from typing import ClassVar, Optional

from BaseClasses import CollectionState
from .Items import Items
from .MissionData import mission_data, MissionData
from .OkrisData import okris_challenges
from .StateLogic import StateLogic, difficulty_order
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
                 state_logic: Optional[StateLogic]):
        super().__init__(
            f"Complete a Mission as {career} {hero_name}",
            code,
            (lambda state: state_logic.can_play_career(state, career)) if state_logic else None
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
                 state_logic: Optional[StateLogic]):
        super().__init__(
            region=mission,
            name=f"Complete {mission} on {difficulty}",
            code=code,
            rule=(lambda state: state_logic.has_difficulty_unlocked(state, difficulty)) if state_logic else None
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
            name=f"Grimoire {grimoire_number} ({mission})",
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


class ChestLocation(LocationData):
    def __init__(self, mission: str, chest_number: int, code: int):
        super().__init__(
            region=mission,
            name=f"Loot Chest {chest_number} ({mission})",
            code=code,
            rule=None
        )


class AmmoCrateLocation(LocationData):
    def __init__(self, mission: str, crate_number: int, code: int):
        super().__init__(
            region=mission,
            name=f"Ammo Crate {crate_number} ({mission})",
            code=code,
            rule=None
        )


class RavagedArtLocation(LocationData):
    def __init__(self, mission: str, art_number: int, code: int):
        super().__init__(
            region=mission,
            name=f"Ravaged Art {art_number} ({mission})",
            code=code,
            rule=None
        )


class HeroLevelLocation(LocationData):
    def __init__(self, hero: str, level: int, code: int):
        super().__init__(
            region="Menu",
            name=f"Reach Level {level} as {hero}",
            code=code,
            rule=None
        )


class OkrisChallengeLocation(LocationData):
    def __init__(self, challenge: str, code: int):
        super().__init__(
            region="Menu",
            name=f"Okri's Challenge: {challenge}",
            code=code,
            rule=None
        )


def _location_slot_count(data: MissionData) -> int:
    if data.custom_locations:
        return len(data.custom_locations)
    return (len(difficulty_order) + data.tomes + data.grimoires
            + len(data.lord_slays) + data.chests + data.ammo_crates + data.ravaged_art)


class Locations:
    base_id: ClassVar[int] = 0
    options: Optional[Vermintide2Options]
    state_logic: Optional[StateLogic]
    items: Optional[Items]

    @classmethod
    def setup(cls, base_id: int) -> None:
        cls.base_id = base_id
        cls.global_location_start = base_id + 2000
        cls.mission_location_start = base_id + 3000
        cls.event_location_start = base_id + 4000
        cls.okris_location_start = base_id + 5000

    def __init__(self, options: Optional[Vermintide2Options] = None,
                 state_logic: Optional[StateLogic] = None,
                 items: Optional[Items] = None):
        self.options = options
        self.state_logic = state_logic
        self.items = items

    def _missions(self, count: int) -> Optional[Callable[[CollectionState], bool]]:
        return self.state_logic.missions(count) if self.state_logic else None

    def _missions_or_item(self, count: int, item: str) -> Optional[Callable[[CollectionState], bool]]:
        return self.state_logic.missions_or_item(count, item) if self.state_logic else None

    global_location_start: ClassVar[int]
    mission_location_start: ClassVar[int]
    event_locations_start: ClassVar[int]
    okris_location_start: ClassVar[int]

    def get_global_locations(self) -> list[LocationData]:
        return [
            # Taal's Horn Keep — no rule
            GlobalLocation("Enter Catrinne's Secret Tower",
                           self.base_id + 2000),
            GlobalLocation("Complete the Jumping Puzzle", self.base_id + 2001),

            # Slay monsters
            GlobalSlayLocation("Rat Ogre", self.base_id + 2020,
                               self._missions_or_item(5, "The Screaming Bell")),
            GlobalSlayLocation("Stormfiend", self.base_id + 2021,
                               self._missions(5)),
            GlobalSlayLocation("Bile Troll", self.base_id + 2022,
                               self._missions_or_item(5, "Hunger In The Dark")),
            GlobalSlayLocation("Chaos Spawn", self.base_id + 2023,
                               self._missions(5)),
            GlobalSlayLocation("Minotaur", self.base_id + 2024,
                               self._missions(6)),
            GlobalLocation("Slay 10 Monsters", self.base_id + 2025,
                           self._missions(10)),

            # Slay elites
            GlobalLocation("Defeat a Scaven Patrol", self.base_id + 2030,
                           self._missions(3)),
            GlobalLocation("Defeat a pack of Plague Monks", self.base_id + 2031,
                           self._missions(3)),
            GlobalSlayLocation("Chaos Warrior", self.base_id + 2032,
                               self._missions(3)),
            GlobalSlayLocation("Chaos Warrior with Shield", self.base_id + 2033,
                           self._missions(3)),
            GlobalSlayLocation("Bestigor", self.base_id + 2034,
                               self._missions(4)),
            GlobalSlayTotalLocation(25, "Elites", self.base_id + 2035,
                                    self._missions(5)),
            GlobalSlayTotalLocation(50, "Elites", self.base_id + 2036,
                                    self._missions(8)),
            GlobalSlayTotalLocation(100, "Elites", self.base_id + 2037,
                                    self._missions(10)),

            # Slay specials
            GlobalSlayLocation("Poison Wind Globadier", self.base_id + 2040,
                               self._missions(3)),
            GlobalSlayLocation("Ratling Gunner", self.base_id + 2041,
                               self._missions(3)),
            GlobalSlayLocation("Gutter Runner", self.base_id + 2042,
                               self._missions(3)),
            GlobalSlayLocation("Blightstormer", self.base_id + 2043,
                               self._missions(3)),
            GlobalSlayLocation("Lifeleech", self.base_id + 2044,
                               self._missions(3)),
            GlobalSlayLocation("Packmaster", self.base_id + 2045,
                               self._missions(3)),
            GlobalSlayLocation("Warpfire Thrower", self.base_id + 2046,
                               self._missions(3)),
            GlobalSlayTotalLocation(10, "Specials", self.base_id + 2047,
                                    self._missions(3)),
            GlobalSlayTotalLocation(20, "Specials", self.base_id + 2048,
                                    self._missions(6)),
            GlobalSlayTotalLocation(50, "Specials", self.base_id + 2049,
                                    self._missions(9)),

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

            # Hero level milestones — 5 heroes × 4 levels (2100–2119)
            *[
                HeroLevelLocation(hero, level, self.base_id + 2100 + hero_idx * 4 + level_idx)
                for hero_idx, hero in enumerate([
                    "Viktor Saltzpyre", "Bardin Goreksson", "Kerillian",
                    "Sienna Fuegonasus", "Markus Kruber"
                ])
                for level_idx, level in enumerate([5, 10, 20, 35])
            ],
        ]

    def get_mission_locations(self, for_data_package: bool = False) -> list[LocationData]:
        location_table: list[LocationData] = []
        location_id = self.mission_location_start

        for mission, data in mission_data.items():
            if not for_data_package and data.dlc_group:
                dlc_key = data.dlc_group.replace(" ", "_")
                if dlc_key not in self.options.campaign.value:
                    location_id += _location_slot_count(data)
                    continue

            if data.custom_locations:
                for loc_name in data.custom_locations:
                    location_table.append(LocationData(
                        region=mission,
                        name=f"{loc_name} ({mission})",
                        code=location_id
                    ))
                    location_id += 1
            else:
                for difficulty in difficulty_order:
                    location_table.append(MissionLocation(mission, difficulty, location_id, self.state_logic))
                    location_id += 1

                for i in range(1, data.tomes + 1):
                    if for_data_package or self.options.add_tomes:
                        location_table.append(TomeLocation(mission, i, location_id))
                    location_id += 1

                for i in range(1, data.grimoires + 1):
                    if for_data_package or self.options.add_grimoires:
                        location_table.append(GrimoireLocation(mission, i, location_id))
                    location_id += 1

                for lord_name in data.lord_slays:
                    location_table.append(LordLocation(mission, lord_name, location_id))
                    location_id += 1

                for i in range(1, data.chests + 1):
                    location_table.append(ChestLocation(mission, i, location_id))
                    location_id += 1

                for i in range(1, data.ammo_crates + 1):
                    location_table.append(AmmoCrateLocation(mission, i, location_id))
                    location_id += 1

                for i in range(1, data.ravaged_art + 1):
                    location_table.append(RavagedArtLocation(mission, i, location_id))
                    location_id += 1

        return location_table

    def get_okris_locations(self) -> list[LocationData]:
        return [
            OkrisChallengeLocation(challenge, self.okris_location_start + i)
            for i, challenge in enumerate(okris_challenges)
        ]

    def get_event_locations(self) -> list[LocationData]:
        if self.options.goal == Goal.option_chaos_wastes:
            return [VictoryLocation(
                region="Expedition to the Citadel",
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
        location_table.extend(self.get_okris_locations())

        return {location.name: location.code for location in location_table
                if location.code is not None}

    def get_locations(self) -> list[LocationData]:
        """Only return locations active for this game based on settings"""
        if not self.options or not self.state_logic:
            raise Exception(
                "Locations must be initialized with options and state_logic before calling get_locations()")

        location_table = self.get_global_locations()
        location_table.extend(self.get_mission_locations())
        location_table.extend(self.get_okris_locations())
        location_table.extend(self.get_event_locations())

        return location_table
