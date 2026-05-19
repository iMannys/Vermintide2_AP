from collections.abc import Callable
from typing import Optional

from BaseClasses import Location, Region, MultiWorld, CollectionState
from .MissionData import mission_data
from .StateLogic import StateLogic
from .Locations import LocationData


class Vermintide2Location(Location):
    game: str = "Warhammer: Vermintide 2"

    def __init__(self, player: int, data: LocationData, region: Region):
        super().__init__(player, data.name, data.code, region)

        if data.code is None:
            self.event = True
            self.locked = True

        if data.rule:
            self.access_rule = data.rule


def create_regions(multiworld: MultiWorld, player: int, state_logic: StateLogic, locations: list[LocationData]) -> None:
    region_names = ["Menu"] + [mission for mission in mission_data]

    locations_per_region = get_locations_per_region(locations)
    regions = create_region_map(multiworld, player, locations_per_region, region_names)

    if __debug__:
        throw_if_any_location_not_assigned_to_region(regions, locations_per_region)

    multiworld.regions += regions.values()

    for mission in mission_data:
        connect(regions, "Menu", mission, state_logic.requires_mission(mission))


def create_region(multiworld: MultiWorld, player: int, locations_per_region: dict[str, list[LocationData]], name: str) -> Region:
    region = Region(name, player, multiworld)

    if name in locations_per_region:
        region.locations += [
            Vermintide2Location(player, location_data, region)
            for location_data in locations_per_region[name]
        ]

    return region

def create_region_map(multiworld: MultiWorld, player: int, locations_per_region: dict[str, list[LocationData]], region_names: list[str]) -> dict[str, Region]:
    return {
        name: create_region(multiworld, player, locations_per_region, name)
        for name in region_names
    }

def connect(regions: dict[str, Region], source: str, target: str, rule: Optional[Callable[[CollectionState], bool]] = None) -> None:
    regions[source].connect(regions[target], rule=rule)

def get_locations_per_region(locations: list[LocationData]) -> dict[str, list[LocationData]]:
    per_region: dict[str, list[LocationData]] = {}

    for location in locations:
        per_region.setdefault(location.region, []).append(location)

    return per_region

def throw_if_any_location_not_assigned_to_region(regions: dict[str, Region],
                                                  locations_per_region: dict[str, list[LocationData]]) -> None:
    existing_regions = set(regions)
    existing_location_regions = set(locations_per_region)

    if existing_location_regions - existing_regions:
        raise Exception(
            f"Vermintide2: the following regions are used in locations but don't exist: "
            f"{existing_location_regions - existing_regions}"
        )