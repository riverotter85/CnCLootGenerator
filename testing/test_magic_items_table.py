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

    def test_get_weapons_category(self):
        weapons_category_roll = 42
        benchmark = "special swords"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_weapons_category(weapons_category_roll)

        self.assertEqual(result, benchmark)

    def test_get_sword(self):
        sword_roll = 51
        weapon_bonus_roll = 40
        benchmark = "+1 long sword (1000 gp, 250 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_sword(sword_roll, weapon_bonus_roll)

        self.assertEqual(result, benchmark)

    def test_get_special_sword(self):
        special_sword_roll = 70
        sword_roll = 92
        benchmark = "+2 nine lives stealer (two handed sword) (8500 gp, 2800 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_special_sword(special_sword_roll, sword_roll)

        self.assertEqual(result, benchmark)

    def test_get_miscellaneous_weapon(self):
        miscellaneous_weapon_roll = 95
        weapon_bonus_roll = 98
        benchmark = "+4 trident (16000 gp, 1750 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_miscellaneous_weapon(miscellaneous_weapon_roll, weapon_bonus_roll)

        self.assertEqual(result, benchmark)
    
    def test_get_special_miscellaneous_weapon(self):
        special_miscellaneous_weapon_roll = 9
        weapon_bonus_roll = 99
        miscellaneous_weapon_roll = 39
        benchmark = "+5 club of dagda (10000 gp, 4000 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_special_miscellaneous_weapon(special_miscellaneous_weapon_roll, weapon_bonus_roll, miscellaneous_weapon_roll)

        self.assertEqual(result, benchmark)

    def test_get_armor_and_shields_category(self):
        armor_and_shields_category_roll = 21
        benchmark = "shield"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_armor_and_shields_category(armor_and_shields_category_roll)

        self.assertEqual(result, benchmark)

    def test_get_random_shield_type(self):
        random_shield_type_roll = 72
        benchmark = "blinding shield"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_random_shield_type(random_shield_type_roll)

        self.assertIn(benchmark, result)

    def test_get_shield(self):
        shield_roll = 41
        armor_bonus_roll = 98
        benchmark = "+4 medium shield (16000 gp, 1750 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_shield(shield_roll, armor_bonus_roll)

        self.assertEqual(result, benchmark)

    def test_get_random_armor_type(self):
        random_armor_type_roll = 8
        benchmark = "+3 armor of kavacha (9000 gp, 1200 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_random_armor_type(random_armor_type_roll)

        self.assertEqual(result, benchmark)
    
    def test_get_armor(self):
        armor_roll = 65
        armor_bonus_roll = 76
        benchmark = "+3 scale mail armor (9000 gp, 1200 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_armor(armor_roll, armor_bonus_roll)

        self.assertEqual(result, benchmark)
    
    def test_get_miscellanous_magic_a(self):
        category_roll = 10
        magic_roll = 82
        benchmark = "broom of flying (12750 gp, 4250 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_miscellaneous_magic(category_roll, magic_roll)

        self.assertEqual(result, benchmark)

    def test_get_miscellanous_magic_b(self):
        category_roll = 30
        magic_roll = 50
        benchmark = "cube of force (47250 gp, 4000 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_miscellaneous_magic(category_roll, magic_roll)

        self.assertEqual(result, benchmark)

    def test_get_miscellanous_magic_c(self):
        category_roll = 50
        magic_roll = 32
        benchmark = "gloves of swimming and climbing (9000 gp, 900 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_miscellaneous_magic(category_roll, magic_roll)

        self.assertEqual(result, benchmark)

    def test_get_miscellanous_magic_d(self):
        category_roll = 70
        magic_roll = 10
        benchmark = "lyre of building (13500 gp, 2000 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_miscellaneous_magic(category_roll, magic_roll)

        self.assertEqual(result, benchmark)

    def test_get_miscellanous_magic_e(self):
        category_roll = 90
        magic_roll = 45
        benchmark = "scarab of protection (34000 gp, 1200 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_miscellaneous_magic(category_roll, magic_roll)

        self.assertEqual(result, benchmark)

    def test_get_ring(self):
        ring_roll = 88
        benchmark = "ring of three wishes (114750 gp, 5000 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_ring(ring_roll)

        self.assertEqual(result, benchmark)

    def test_get_rod_stave_wand(self):
        rod_stave_wand_roll = 31
        benchmark = "staff of abjuration (54000 gp, 9000 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_rod_stave_wand(rod_stave_wand_roll)

        self.assertEqual(result, benchmark)
    
    def test_get_cursed_item(self):
        cursed_item_roll = 73
        benchmark = "scarab of death (0 gp, 0 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_cursed_item(cursed_item_roll)

        self.assertEqual(result, benchmark)

    def test_get_artifact(self):
        artifact_roll = 62
        benchmark = "saint's mace (priceless, 20000 xp)"

        magic_items_table = MagicItemsTable()
        result = magic_items_table.get_artifact(artifact_roll)

        self.assertEqual(result, benchmark)

if __name__ == "__main__":
    unittest.main()