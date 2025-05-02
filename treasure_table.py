from loot_table import LootTable
from gems_table import GemsTable
from extraordinary_items_table import ExtraordinaryItemsTable
from magic_items_table import MagicItemsTable

class TreasureTable(LootTable):
    def __init__(self):
        super().__init__()
        self.table = [
            ("1", (50, "2d4", 10, 10, "1d4", -10, 10, "1d2", 5, "1", 100)),
            ("2", (55, "4d4", 10, 20, "1d4+1", -8, 20, "1d2+1", 10, "1", 200)),
            ("3", (60, "6d4", 10, 30, "1d4+2", -6, 30, "1d2+2", 15, "1", 300)),
            ("4", (65, "8d4", 10, 40, "1d4+3", -4, 40, "1d2+3", 20, "1", 500)),
            ("5", (70, "2d6", 50, 50, "1d6+2", -2, 50, "1d4+2", 30, "1d2", 800)),
            ("6", (75, "4d6", 50, 60, "1d6+3", 0, 60, "1d4+3", 40, "1d2", 1300)),
            ("7", (80, "6d6", 50, 70, "1d6+4", 0, 70, "1d4+4", 50, "1d2", 2100)),
            ("8", (85, "8d6", 50, 80, "1d6+5", 0, 80, "1d4+5", 60, "1d2", 3400)),
            ("9", (90, "2d8", 100, 90, "1d8+4", 0, 90, "1d6+4", 70, "1d3", 5500)),
            ("10", (91, "4d8", 100, 91, "1d8+5", 0, 91, "1d6+5", 80, "1d3", 0)),
            ("11", (92, "6d8", 100, 92, "1d8+6", 0, 92, "1d6+6", 90, "1d3", 0)),
            ("12", (93, "8d8", 100, 93, "1d8+7", 0, 93, "1d6+7", 92, "1d3", 0)),
            ("13", (94, "2d10", 200, 94, "1d10+6", 0, 94, "1d8+6", 94, "1d4", 0)),
            ("14", (95, "4d10", 200, 95, "1d10+7", 0, 95, "1d8+7", 96, "1d4", 0)),
            ("15", (96, "6d10", 200, 96, "1d10+8", 0, 96, "1d8+8", 98, "1d4", 0)),
            ("16", (97, "8d10", 200, 97, "1d10+9", 0, 97, "1d8+9", 99, "1d4", 0)),
            ("17", (98, "2d12", 400, 98, "1d12+8", 0, 98, "1d8+8", 100, "1d6", 0)),
            ("18", (99, "4d12", 400, 99, "1d12+9", 0, 99, "1d8+9", 100, "1d6", 0))
        ]

        self.treasure_tables = {}
        self.treasure_tables["gems"] = GemsTable()
        self.treasure_tables["extraordinary items"] = ExtraordinaryItemsTable()
        self.treasure_tables["magic items"] = MagicItemsTable()

    def search_treasure_table(self, treasure_type):
        for type, item in self.table:
            if treasure_type == type:
                return item
        return None

    def roll_gem(self, gem_modifier=0):
        return self.treasure_tables["gems"].roll(gem_modifier)
    
    def roll_extraordinary_item(self):
        return self.treasure_tables["extraordinary items"].roll()
    
    def roll_magic_item(self, max_experience=0):
        return self.treasure_tables["magic items"].roll(max_experience)

    def roll_treasure(self, treasure_type, monster_state):
        table_entry = self.search_treasure_table(treasure_type)

        if table_entry is None:
            return "not found"

        treasure_found = ""
        num_rolls = 1
        item_modifier = 1

        if int(monster_state) > 2:
            num_rolls = 2

        # Roll for gold
        roll = self.roll_percentile(num_rolls)
        if roll <= table_entry[0]:
            gp_amount = int(self.roll_dice(table_entry[1]))

            if int(monster_state) > 1: # Monster is in lair
                gp_amount *= table_entry[2]

            if int(monster_state) > 2: # Monster is also hoarding treasure
                gp_amount *= 100
                item_modifier = 2

            treasure_found += "\nGold Pieces: " + str(gp_amount) + " gp"

        # Roll for gems
        roll = self.roll_percentile(num_rolls)
        if roll <= table_entry[3]:
            gems = []
            num_gems = int(self.roll_dice(table_entry[4])) * item_modifier
            for i in range(num_gems):
                gem = self.treasure_tables["gems"].roll(table_entry[5])
                gems.append(gem)

            treasure_found += "\nGems: " + ", ".join(gems)
        
        # Roll for extraordinary items
        roll = self.roll_percentile(num_rolls)
        if roll <= table_entry[6]:
            extraordinary_items = []
            num_extraordinary_items = int(self.roll_dice(table_entry[7])) * item_modifier
            for i in range(num_extraordinary_items):
                extraordinary_item = self.treasure_tables["extraordinary items"].roll()
                extraordinary_items.append(extraordinary_item)

            treasure_found += "\nExtraordinary Items: " + ", ".join(extraordinary_items)

        # Roll for magic items
        roll = self.roll_percentile(num_rolls)
        if roll <= table_entry[8]:
            magic_items = []
            num_magic_items = int(self.roll_dice(table_entry[9])) * item_modifier
            for i in range(num_magic_items):
                magic_item = self.treasure_tables["magic items"].roll(table_entry[10])
                magic_items.append(magic_item)
            
            treasure_found += "\nMagic Items: " + ", ".join(magic_items)
        
        # If nothing was rolled, we show that no treasure was found
        if treasure_found == "":
            treasure_found = "No Treasure"

        return treasure_found