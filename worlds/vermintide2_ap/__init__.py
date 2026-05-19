from BaseClasses import Item
from .Regions import create_regions
from .StateLogic import StateLogic
from .Options import Vermintide2Options, Goal
from .Items import Items
from .Locations import Locations, LocationData
from worlds.AutoWorld import World
from . import Components

class Vermintide2World(World):
    """
    Warhammer: Vermintide 2 is a first-person co-op action game set in the
    apocalyptic End Times of the Warhammer Fantasy universe. Fight through
    the Helmgart campaign across 13 maps against Skaven, Beastmen and Chaos.
    """
    game = "Warhammer: Vermintide 2"
    options_dataclass = Vermintide2Options
    options: Vermintide2Options
    topology_present = False
    state_logic: StateLogic | None = None
    items: Items | None = None

    base_id = 3_350_000
    Items.setup(base_id)
    Locations.setup(base_id)

    item_name_to_id = Items.item_name_to_id
    location_name_to_id = Locations().get_locations_for_data_package()
    item_name_groups = Items.get_item_names_per_category()

    def generate_early(self) -> None:
        self.state_logic = StateLogic(self.player)
        self.items = Items(self.player, self.random, self.options)

    def create_regions(self) -> None:
        assert self.state_logic is not None and self.items is not None
        locations = Locations(self.options, self.state_logic, self.items).get_locations()
        create_regions(self.multiworld, self.player, self.state_logic, locations)

    def create_items(self) -> None:
        assert self.items is not None
        number_of_locations = len(self.multiworld.get_unfilled_locations(self.player))
        precollected = self.multiworld.precollected_items[self.player]
        self.multiworld.itempool += self.items.build_item_pool(self.random, precollected, number_of_locations)

    def set_rules(self) -> None:
        assert self.state_logic is not None
        if self.options.goal == Goal.option_skittergate:
            self.multiworld.completion_condition[self.player] = \
                self.state_logic.can_complete_skittergate
        elif self.options.goal == Goal.option_chaos_wastes:
            self.multiworld.completion_condition[self.player] = \
                self.state_logic.can_complete_citadel

    def get_filler_item_name(self) -> str:
        if self.items:
            return self.items.get_filler_item_name(self.random, None)
        return Items.get_filler_item_name_uninitialized(self.random)

    def create_item(self, name: str) -> Item:
        if self.items:
            return self.items.create_item(name, self.player)
        return Items.create_item_uninitialized(name, self.player)

    def fill_slot_data(self) -> dict[str, object]:
        return {
            "goal": self.options.goal.value,
            "campaign": list(self.options.campaign.value),
            "add_tomes": bool(self.options.add_tomes),
            "add_grimoires": bool(self.options.add_grimoires),
            "add_weapon": bool(self.options.add_weapon),
            "trap_chance": self.options.trap_chance.value,
            "death_link": bool(self.options.death_link),
        }