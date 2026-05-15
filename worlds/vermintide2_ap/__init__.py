import settings
import typing
from .options import Vermintide2Options  # the options we defined earlier
from .items import Items  # data used below to add items to the World
from .locations import Locations  # same as above
from worlds.AutoWorld import World


class Vermintide2World(World):
    """
    Warhammer: Vermintide 2 is a first-person co-op action game set in the
    apocalyptic End Times of the Warhammer Fantasy universe. Fight through
    the Helmgart campaign across 13 maps against Skaven, Beastmen and Chaos.
    """
    game = "Warhammer: Vermintide 2"
    options_dataclass = Vermintide2Options  # options the player can set
    options: Vermintide2Options  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    base_id = 1234
    # instead of dynamic numbering, IDs could be part of data

    item_name_to_id = Items.item_names_and_ids
    location_name_to_id = Locations().get_locations_for_data_package()
    item_name_groups = Items.get_item_names_per_category(game_logic)

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "weapons": {"sword", "lance"},
    }

