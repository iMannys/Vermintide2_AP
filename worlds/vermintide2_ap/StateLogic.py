from collections.abc import Callable

from BaseClasses import CollectionState

# Default careers are excluded
hero_to_careers: dict[str, list[str]] = {
    "Viktor Saltzpyre": [
        "Witch Hunter Captain",
        "Bounty Hunter",
        "Zealot",
        "Warrior Priest of Sigmar",
    ],
    "Bardin Goreksson": [
        "Ranger Veteran",
        "Ironbreaker",
        "Slayer",
        "Outcast Engineer",
    ],
    "Kerillian": [
        "Waystalker",
        "Handmaiden",
        "Shade",
        "Sister of the Thorn",
    ],
    "Sienna Fuegonasus": [
        "Battle Wizard",
        "Pyromancer",
        "Unchained",
        "Necromancer",
    ],
    "Markus Kruber": [
        "Mercenary",
        "Huntsman",
        "Foot Knight",
        "Grail Knight",
    ],
}

difficulty_order = [
    "Recruit",
    "Veteran",
    "Champion",
    "Legend",
    "Cataclysm"
]


class StateLogic:
    def __init__(self, player: int):
        self.player = player

    def has_item(self, state: CollectionState, item: str) -> bool:
        return state.has(item, self.player)

    def has_missions(self, state: CollectionState, count: int) -> bool:
        # counts how many mission unlock items the player has received
        return state.count_group("Mission", self.player) >= count

    def has_difficulty(self, state: CollectionState, difficulty: str) -> bool:
        return state.has(f"Unlock {difficulty} Difficulty", self.player)

    def can_play_career(self, state: CollectionState, career: str) -> bool:
        return state.has(career, self.player)

    def has_lord_missions(self, state: CollectionState) -> bool:
        lords = ["Halescourge", "Into The Nest", "The War Camp"]
        return sum(state.has(lord, self.player) for lord in lords) == len(lords)

    def can_complete_skittergate(self, state: CollectionState) -> bool:
        return (self.has_item(state, "The Skittergate") and
                self.has_lord_missions(state))

    def can_complete_citadel(self, state: CollectionState) -> bool:
        return (self.has_item(state, "Expedition to the Citadel") and
                self.has_item(state, "Expedition of Fortitude") and
                self.has_item(state, "Expedition of Courage") and
                self.has_item(state, "Expedition of Determination"))

    def has_difficulty_unlocked(self, state: CollectionState,
                                difficulty: str) -> bool:
        idx = difficulty_order.index(difficulty)
        # Recruit is always available; each tier above requires its unlock item
        return all(
            state.has(f"Unlock {difficulty_order[i]} Difficulty", self.player)
            for i in range(1, idx + 1)
        )

    def missions(self, count: int) -> Callable[[CollectionState], bool]:
        def rule(state: CollectionState) -> bool:
            return self.has_missions(state, count)

        return rule

    def missions_or_item(self, count: int, item: str) -> Callable[
        [CollectionState], bool]:
        def rule(state: CollectionState) -> bool:
            return self.has_missions(state, count) or self.has_item(state, item)

        return rule

    def requires_mission(self, mission_name: str) -> Callable[
        [CollectionState], bool]:
        if mission_name == "The Skittergate":
            def rule(state: CollectionState) -> bool:
                return self.can_complete_skittergate(state)

            return rule

        if mission_name == "Expedition to the Citadel":
            def rule(state: CollectionState) -> bool:
                return self.can_complete_citadel(state)

            return rule

        def rule(state: CollectionState) -> bool:
            return self.has_item(state, mission_name)

        return rule