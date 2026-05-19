from dataclasses import dataclass
from enum import IntFlag
from BaseClasses import Item, ItemClassification

class VermintideItem(Item):
    """An item in the Warhammer: Vermintide 2 randomizer."""
    game = "Warhammer: Vermintide 2"


# ============================================================
# Item Groups (bitmask categories for filtering)
# ============================================================

class ItemGroups(IntFlag):
    # Top-level categories
    Mission          = 1 << 1
    Career           = 1 << 2
    Weapon           = 1 << 3
    DifficultyUnlock = 1 << 4
    Trap             = 1 << 5
    Filler           = 1 << 6

    # DLC flag — OR this onto any DLC item for easy filtering
    DLC              = 1 << 7

    # Per-DLC mission categories
    DLC_Drachenfels      = 1 << 8
    DLC_ChaosWastes      = 1 << 9
    DLC_Bogenhafen       = 1 << 10
    DLC_BackToUbersreik  = 1 << 11
    DLC_WindsOfMagic     = 1 << 12
    DLC_KarakAzgaraz     = 1 << 13
    DLC_Treachery        = 1 << 14
    DLC_VerminousDreams  = 1 << 15
    DLC_ReiklandTales    = 1 << 16

    # Weapon subcategories — Viktor Saltzpyre
    ViktorMWeapon        = 1 << 17
    ViktorRWeapon        = 1 << 18
    ZealotWeapon         = 1 << 19
    WarriorPriestWeapon  = 1 << 20

    # Weapon subcategories — Bardin Goreksson
    BardinMWeapon        = 1 << 21
    BardinShields        = 1 << 22
    BardinRWeapon        = 1 << 23
    BardinCrossbow       = 1 << 24
    BardinTechWeapon     = 1 << 25
    SlayerWeapon         = 1 << 26

    # Weapon subcategories — Kerillian
    KerillianMWeapon     = 1 << 27
    KerillianRWeapon     = 1 << 28
    HandmaidenWeapon     = 1 << 29
    ShadeWeapon          = 1 << 30
    SOTTWeapon           = 1 << 31   # Sister of the Thorn

    # Weapon subcategories — Sienna Fuegonasus
    SiennaMWeapon        = 1 << 32
    SiennaRWeapon        = 1 << 33
    SiennaFlameWeapon    = 1 << 34
    NecromancerWeapon    = 1 << 35

    # Weapon subcategories — Markus Kruber
    KruberMWeapon        = 1 << 36
    KruberRWeapon        = 1 << 37
    NoGrailWeapon        = 1 << 38   # Halberd/spear, not Grail Knight exclusive
    GrailKnightWeapon    = 1 << 39
    HuntsmanWeapon       = 1 << 40
    KruberSpear          = 1 << 41

    PowerLevel           = 1 << 42

@dataclass
class ItemData:
    """
    Metadata for a single item in the pool.

    :param category: Bitmask of ItemGroups this item belongs to.
    :param code: Unique integer ID. Must be unique across all items in this game.
    :param classification: AP item classification (progression, useful, trap, filler).
    :param count: How many copies go in the pool. 0 = defined but not added by default
                  (used for filler items whose count is calculated dynamically).
    """
    category: ItemGroups
    code: int
    classification: ItemClassification = ItemClassification.filler
    count: int = 1