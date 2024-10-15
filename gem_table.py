import random
from loot_table import LootTable

class GemTable(LootTable):
    def __init__(self):
        super().__init__()
        self.table = [
            (1, 10, (["amber", "amethyst", "jadeite"], 5)),
            (11, 20, (["precious opal", "banded eye", "malachite"], 10)),
            (21, 40, (["moonstone", "pearl", "lapis lazuli", "tiger eye"], 25)),
            (41, 60, (["bloodstone", "white agate", "violet-blue sapphire"], 50)),
            (61, 75, (["whitish moonstone", "common opal"], 100)),
            (76, 85, (["green nephrite", "peridot", "amethyst"], 250)),
            (86, 90, (["violet garnet", "green garnet", "fire opal", "topaz"], 500)),
            (91, 94, (["emerald", "black opal", "tourmaline"], 1000)),
            (95, 98, (["star ruby", "jade", "yellow sapphire", "green sapphire", "black sapphire", "white sapphire"], 2500)),
            (99, 100, (["diamond", "blood red ruby", "blue sapphire"], 5000))
    ]

    def roll(self):
        gems_tier_roll = GemTable.roll_percentile()
        gems_tier = GemTable.search_items(gems_tier_roll, self.table)
        gem = random.choice(gems_tier[0])

        return gem + " (gp value: " + str(gems_tier[1]) + ")"