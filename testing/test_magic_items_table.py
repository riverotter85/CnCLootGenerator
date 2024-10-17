import unittest
import sys
import os

# Setup path config for us to pull the proper script in the parent directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from magic_items_table import MagicItemsTable

class TestMagicItemsTable(unittest.TestCase):

    def test_format_table_results(self):
        item = "best loot ever"
        value = "1000 gp"
        experience = "200"
        benchmark = "best loot ever (1000 gp, 200 xp)"

        result = MagicItemsTable.format_table_results(item, value, experience)

        self.assertEqual(result, benchmark)

    def test_get_potion(self):
        roll = 15
        benchmark = "potion of cure light wounds (300 gp, 100 xp)"
        
        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_potion(roll)

        self.assertEqual(result, benchmark)

    def test_get_scroll(self):
        roll = 30
        benchmark = "scroll of 4 spell levels (600 gp, 400 xp)"
        
        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_scroll(roll)

        self.assertEqual(result, benchmark)

    def test_get_weapon(self):
        # stuff

    # def test_roll_shield(self):
    #     # stuff

    # def test_roll_armor(self):
    #     # stuff

    # def test_roll_miscellaneous_magic(self):
    #     # stuff

    # def test_roll_ring(self):
    #     # stuff

    # def test_roll_rods_staves_wands(self):
    #     # stuff

    # def test_roll_cursed_item(self):
    #     # stuff

    # def test_roll_artifact(self):
    #     # stuff

if __name__ == "__main__":
    unittest.main()