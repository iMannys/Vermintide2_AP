import settings
import typing
from .options import Vermintide2Options
from .items import Items
from .locations import Locations
from worlds.AutoWorld import World


class Vermintide2World(World):
    """
    Warhammer: Vermintide 2 is a first-person co-op action game set in the
    apocalyptic End Times of the Warhammer Fantasy universe. Fight through
    the Helmgart campaign across 13 maps against Skaven, Beastmen and Chaos.
    """
    game = "Warhammer: Vermintide 2"
    options_dataclass = Vermintide2Options
    options: Vermintide2Options
    topology_present = True  # show path to required location checks in spoiler

    base_id = 3_350_000
    Items.setup(base_id)
    Locations.setup(base_id)

    item_name_to_id = Items.item_name_to_id
    location_name_to_id = Locations().get_locations_for_data_package()
    item_name_groups = Items.get_item_names_per_category()

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)



