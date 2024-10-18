from loot_table import LootTable
from gems_table import GemsTable
from extraordinary_items_table import ExtraordinaryItemsTable
from magic_items_table import MagicItemsTable

class TreasureTable(LootTable):
    def __init__(self):
        super().__init__()
        self.table = [
            ("1", (50, "2d4", 10, "1d4", -10, 10, "1d2", 5, "1", 100)),
            ("2", (55, "4d4", 20, "1d4+1", -8, 20, "1d2+1", 10, "1", 200)),
            ("3", (60, "6d4", 30, "1d4+2", -6, 30, "1d2+2", 15, "1", 300)),
            ("4", (65, "8d4", 40, "1d4+3", -4, 40, "1d2+3", 20, "1", 500)),
            ("5", (70, "2d6", 50, "1d6+2", -2, 50, "1d4+2", 30, "1d2", 800)),
            ("6", (75, "4d6", 60, "1d6+3", 0, 60, "1d4+3", 40, "1d2", 1300)),
            ("7", (80, "6d6", 70, "1d6+4", 0, 70, "1d4+4", 50, "1d2", 2100)),
            ("8", (85, "8d6", 80, "1d6+5", 0, 80, "1d4+5", 60, "1d2", 3400)),
            ("9", (90, "2d8", 90, "1d8+4", 0, 90, "1d6+4", 70, "1d3", 5500)),
            ("10", (91, "4d8", 91, "1d8+5", 0, 91, "1d6+5", 80, "1d3", 0)),
            ("11", (92, "6d8", 92, "1d8+6", 0, 92, "1d6+6", 90, "1d3", 0)),
            ("12", (93, "8d8", 93, "1d8+7", 0, 93, "1d6+7", 92, "1d3", 0)),
            ("13", (94, "2d10", 94, "1d10+6", 0, 94, "1d8+6", 94, "1d4", 0)),
            ("14", (95, "4d10", 95, "1d10+7", 0, 95, "1d8+7", 96, "1d4", 0)),
            ("15", (96, "6d10", 96, "1d10+8", 0, 96, "1d8+8", 98, "1d4", 0)),
            ("16", (97, "8d10", 97, "1d10+9", 0, 97, "1d8+9", 99, "1d4", 0)),
            ("17", (98, "2d12", 98, "1d12+8", 0, 98, "1d8+8", 100, "1d6", 0)),
            ("18", (99, "4d12", 99, "1d12+9", 0, 99, "1d8+9", 100, "1d6", 0))
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

    def roll_treasure(self, treasure_type):
        table_entry = self.search_treasure_table(treasure_type)

        if table_entry is None:
            return "not found"

        treasure_found = ""

        # Roll for gold
        roll = self.roll_percentile()
        if roll <= table_entry[0]:
            gp_amount = self.roll_dice(table_entry[1])
            treasure_found += "\nGold Pieces: " + gp_amount + " gp"

        # Roll for gems
        roll = self.roll_percentile()
        if roll <= table_entry[2]:
            gems = []
            num_gems = int(self.roll_dice(table_entry[3]))
            for i in range(num_gems):
                gem = self.treasure_tables["gems"].roll(table_entry[4])
                gems.append(gem)

            treasure_found += "\nGems: " + ", ".join(gems)
        
        # Roll for extraordinary items
        roll = self.roll_percentile()
        if roll <= table_entry[5]:
            extraordinary_items = []
            num_extraordinary_items = int(self.roll_dice(table_entry[6]))
            for i in range(num_extraordinary_items):
                extraordinary_item = self.treasure_tables["extraordinary items"].roll()
                extraordinary_items.append(extraordinary_item)

            treasure_found += "\nExtraordinary Items: " + ", ".join(extraordinary_items)

        # Roll for magic items
        roll = self.roll_percentile()
        if roll <= table_entry[7]:
            magic_items = []
            num_magic_items = int(self.roll_dice(table_entry[8]))
            for i in range(num_magic_items):
                magic_item = self.treasure_tables["magic items"].roll(table_entry[9])
                magic_items.append(magic_item)
            
            treasure_found += "\nMagic Items: " + ", ".join(magic_items)
        
        # If nothing was rolled, we show that no treasure was found
        if treasure_found == "":
            treasure_found = "No Treasure"

        return treasure_found