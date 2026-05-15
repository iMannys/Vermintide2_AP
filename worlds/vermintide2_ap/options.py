from dataclasses import dataclass
from Options import (
    OptionSet, Toggle, PerGameCommonOptions, DeathLink
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
    default = frozenset()  # all off by default, matching the apworld


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