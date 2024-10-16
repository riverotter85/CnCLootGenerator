import random
from loot_table import LootTable

class GemsTable(LootTable):
    def __init__(self):
        super().__init__()
        self.table = [
            (1, 10, (["amber", "amethyst", "jadeite"], "5 gp")),
            (11, 20, (["precious opal", "banded eye", "malachite"], "10 gp")),
            (21, 40, (["moonstone", "pearl", "lapis lazuli", "tiger eye"], "25 gp")),
            (41, 60, (["bloodstone", "white agate", "violet-blue sapphire"], "50 gp")),
            (61, 75, (["whitish moonstone", "common opal"], "100 gp")),
            (76, 85, (["green nephrite", "peridot", "amethyst"], "250 gp")),
            (86, 90, (["violet garnet", "green garnet", "fire opal", "topaz"], "500 gp")),
            (91, 94, (["emerald", "black opal", "tourmaline"], "1000 gp")),
            (95, 98, (["star ruby", "jade", "yellow sapphire", "green sapphire", "black sapphire", "white sapphire"], "2500 gp")),
            (99, 100, (["diamond", "blood red ruby", "blue sapphire"], "5000 gp"))
    ]

    def roll(self):
        gems_tier_roll = self.roll_percentile()
        gems_tier = self.search_items(gems_tier_roll, self.table)
        gem = random.choice(gems_tier[0])

        return gem + " (value: " + gems_tier[1] + ")"