from treasure_table import TreasureTable
from gems_table import GemsTable
from extraordinary_items_table import ExtraordinaryItemsTable
from magic_items_table import MagicItemsTable

treasure_table = TreasureTable()

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
        print("1) Treasure")
        print("2) Gems")
        print("3) Extraordinary Items")
        print("4) Magic Items")
        print("5) Exit")
        print("==========================================")
        print(item_banner)
        option = input("Select one of the above options (1-5): ")
        
        if option == "1":
            treasure_type = "0"
            while int(treasure_type) < 1 or int(treasure_type) > 18:
                treasure_type = input("Select treasure type (1-18): ")

            loot = treasure_table.roll_treasure(treasure_type)
            item_banner = "\nYou found: \n" + loot + "\n"
        elif option == "2":
            loot = treasure_table.roll_gem()
            item_banner = "\nYou found: " + loot + "\n"
        elif option == "3":
            loot = treasure_table.roll_extraordinary_item()
            item_banner = "\nYou found: " + loot + "\n"
        elif option == "4":
            loot = treasure_table.roll_magic_item()
            item_banner = "\nYou found: " + loot + "\n"
        elif option == "5":
            print(f"Goodbye!")
            break
        else:
            item_banner = ""

if __name__ == "__main__":
    main()
