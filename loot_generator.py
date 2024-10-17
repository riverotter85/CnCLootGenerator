from gems_table import GemsTable
from extraordinary_items_table import ExtraordinaryItemsTable
from magic_items_table import MagicItemsTable

class LootGenerator:
    def __init__(self):
        self.tables = {}
        self.tables["Gems"] = GemsTable()
        self.tables["Extraordinary Items"] = ExtraordinaryItemsTable()
        self.tables["Magic Items"] = MagicItemsTable()

    # def add_table(self, table_name, items):
    #     self.tables[table_name] = LootTable(table_name, items)

    def generate_loot(self, table_name):
        if table_name in self.tables:
            item = self.tables[table_name].roll()
            return item
        else:
            return "Table not found."

# Define your loot tables
loot_generator = LootGenerator()

# Example Loot Tables
# loot_generator.add_table("Gems", GemTable())

# loot_generator.add_table("Uncommon Loot", [
#     (1, 30, "50 Gold Pieces"),
#     (31, 60, "Uncommon Weapon (Short Sword)"),
#     (61, 80, "Potion of Strength"),
#     (81, 90, "Spell Scroll (1st level)"),
#     (91, 100, "Uncommon Magical Item (roll on Magical Item Table)")
# ])

# loot_generator.add_table("Rare Loot", [
#     (1, 20, "100 Gold Pieces"),
#     (21, 50, "Rare Weapon (+1 Longsword)"),
#     (51, 70, "Rare Armor (+1 Chain Mail)"),
#     (71, 85, "Potion of Invisibility"),
#     (86, 100, "Rare Magical Item (roll on Magical Item Table)")
# ])

# loot_generator.add_table("Trinket Table", [
#     (1, 50, "Ornate Ring"),
#     (51, 100, "Enchanted Locket")
# ])

# loot_generator.add_table("Magical Item Table", [
#     (1, 40, "Wand of Magic Missile"),
#     (41, 70, "Cloak of Elvenkind"),
#     (71, 100, "Amulet of Health")
# ])

# Example of generating loot
def main():
    item_banner = ""

    while(True):
        print("==========================================")
        print("1) Gems")
        print("2) Extraordinary Items")
        print("3) Magic Items")
        print("4) Exit")
        print("==========================================")
        print(item_banner)
        option = input("Select one of the above options (1-4): ")
        
        if option == "1":
            loot = loot_generator.generate_loot("Gems")
            item_banner = "\nYou found: " + loot + "\n"
        elif option == "2":
            loot = loot_generator.generate_loot("Extraordinary Items")
            item_banner = "\nYou found: " + loot + "\n"
        elif option == "3":
            loot = loot_generator.generate_loot("Magic Items")
            item_banner = "\nYou found: " + loot + "\n"
        elif option == "4":
            print(f"Goodbye!")
            break
        else:
            item_banner = ""

if __name__ == "__main__":
    main()
