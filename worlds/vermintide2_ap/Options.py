from dataclasses import dataclass
from Options import (
    OptionSet, Toggle, PerGameCommonOptions, DeathLink, Range, Choice
)

_campaign_types = {
    "The_Curse_of_Drachenfels",
    "A_Treacherous_Adventure",
    "Karak_Azgaraz",
    "Verminous_Dreams",
    "Reikland_Tales",
    "Shadows_Over_Bogenhafen",
    "Back_to_Ubersreik",
    "Fortunes_of_War",
    "Winds_of_Magic",
    "Chaos_Wastes",
}


class CampaignOptions(OptionSet):
    """Precise list of DLC campaigns to include as locations."""
    display_name = "DLC Campaigns"
    valid_keys = _campaign_types
    default = frozenset()  # all off by default


class AddTomes(Toggle):
    """Adds 3 Tome locations per mission."""
    display_name = "Add Tomes"
    default = 1


class AddGrimoires(Toggle):
    """Adds 2 Grimoire locations per mission."""
    display_name = "Add Grimoires"
    default = 1


class DLCCareers(Toggle):
    """Adds the 5 DLC Careers and, if enabled, their weapons to the item pool."""
    display_name = "DLC Careers"
    default = 1


class AddWeapon(Toggle):
    """
    Adds individual weapons as items in the item pool.
    This adds a LOT of items — make sure you have enough locations.
    """
    display_name = "Add Weapons"
    default = 1


class BackToUbersreikWeapons(Toggle):
    """Adds weapons from the Back to Ubersreik DLC to the item pool. Does nothing if weapons are disabled."""
    display_name = "Back to Ubersreik Weapons"
    default = 1


class WindsOfMagicWeapons(Toggle):
    """Adds weapons from the Winds of Magic DLC to the item pool. Does nothing if weapons are disabled."""
    display_name = "Winds of Magic Weapons"
    default = 1


class ForgottenRelics(Toggle):
    """Adds weapons from the Forgotten Relics DLC to the item pool. Does nothing if weapons are disabled."""
    display_name = "Forgotten Relics Weapons"
    default = 1

_trap_types = {
    "Trap: Spawn Monster",
    "Trap: Spawn Horde",
    "Trap: Spawn Patrol",
    "Trap: Drop Firebomb",
    "Trap: Empty Career Ability",
}

class TrapChance(Range):
    """
    Chance of traps in the item pool.

    - **0:** No traps will be present
    - **100:** Every filler item will be a trap.
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 10


class TrapSelection(OptionSet):
    """
    Precise list of traps that may be in the item pool to find.
    """
    display_name = "Trap Selection"
    valid_keys = _trap_types

class Goal(Choice):
    """The victory condition for the game."""
    display_name = "Goal"
    option_skittergate = 0
    option_chaos_wastes = 1
    default = 0

@dataclass
class Vermintide2Options(PerGameCommonOptions):
    death_link: DeathLink

    # Location toggles
    add_tomes: AddTomes
    add_grimoires: AddGrimoires

    # Item pool toggles
    dlc_careers: DLCCareers
    add_weapon: AddWeapon
    back_to_ubersreik_weapons: BackToUbersreikWeapons
    winds_of_magic_weapons: WindsOfMagicWeapons
    forgotten_relics: ForgottenRelics

    # DLC campaign selection
    campaign: CampaignOptions

    trap_chance: TrapChance
    trap_selection: TrapSelection

    goal: Goal