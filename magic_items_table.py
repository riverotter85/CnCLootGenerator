from loot_table import LootTable

class MagicItemsTable(LootTable):
    potions = [
        (1, 3, ("aid", "400 gp", "200")),
        (4, 6, ("bless (oil)", "300 gp", "100")),
        (7, 9, ("blur", "400 gp", "200")),
        (10, 12, ("clairaudience/clairvoyance", "500 gp", "300")),
        (13, 15, ("cure light wounds", "300 gp", "100")),
        (16, 18, ("cure serious wounds", "500 gp", "300")),
        (19, 21, ("cure critical wounds", "700 gp", "500")),
        (22, 24, ("delay poison", "400 gp", "200")),
        (25, 27, ("endure elements", "300 gp", "100")),
        (28, 30, ("fly", "500 gp", "300")),
        (31, 33, ("gaseous form", "500 gp", "300")),
        (34, 36, ("giant strength (see explanatory text)", "700 gp", "500")),
        (37, 39, ("haste", "500 gp", "300")),
        (40, 42, ("heal", "800 gp", "600")),
        (43, 45, ("invisibility (potion or oil)", "400 gp", "200")),
        (46, 48, ("levitation (potion or oil)", "400 gp", "200")),
        (49, 51, ("longevity (see explanatory text)", "12000 gp", "1500")),
        (52, 54, ("neutralize poison", "600 gp", "400")),
        (55, 57, ("nondetection", "500 gp", "300")),
        (58, 60, ("pass without trace", "300 gp", "100")),
        (61, 63, ("protection from alignment (see explanatory text)", "300 gp", "100")),
        (64, 66, ("protection from arrows", "500 gp", "300")),
        (67, 69, ("remove blindness/deafness", "500 gp", "300")),
        (70, 72, ("remove curse", "500 gp", "300")),
        (73, 75, ("remove disease", "500 gp", "300")),
        (76, 78, ("remove paralysis", "400 gp", "200")),
        (79, 81, ("restoration", "700 gp", "400")),
        (82, 84, ("sanctuary", "300 gp", "100")),
        (85, 87, ("shield of faith +2", "300 gp", "100")),
        (88, 90, ("spider climb", "300 gp", "100")),
        (91, 93, ("tongues", "500 gp", "300")),
        (94, 96, ("water breathing", "500 gp", "300")),
        (97, 99, ("water walk", "900 gp", "700")),
        (100, 100, ("trap the soul", "1,100 gp", "900"))
    ]

    scrolls = [
        (1, 8, ("1 spell level", "300 gp", "100")),
        (9, 16, ("2 spell levels", "400 gp", "200")),
        (17,24, ("3 spell levels", "500 gp", "300")),
        (25, 32, ("4 spell levels", "600 gp", "400")),
        (33, 40, ("5 spell levels", "700 gp", "500")),
        (41, 45, ("6 spell levels", "800 gp", "600")),
        (46, 50, ("7 spell levels", "900 gp", "700")),
        (51, 55, ("8 spell levels", "1000 gp", "800")),
        (56, 60, ("9 spell levels", "1100 gp", "900")),
        (61, 65, ("10 spell levels", "1200 gp", "1000")),
        (66, 68, ("11 spell levels", "1300 gp", "1100")),
        (69, 71, ("12 spell levels", "1400 gp", "1200")),
        (72, 74, ("13 spell levels", "1500 gp", "1300")),
        (75, 77, ("14 spell levels", "1600 gp", "1400")),
        (78, 80, ("15 spell levels", "1700 gp", "1500")),
        (81, 82, ("teleport without error", "900 gp", "700")),
        (83, 84, ("symbol", "1000 gp", "800")),
        (85, 86, ("trap the soul", "1100 gp", "900")),
        (87, 88, ("time stop", "1100 gp", "900")),
        (89, 90, ("true resurrection", "1100 gp", "900")),
        (91, 92, ("mass heal", "1000 gp", "800")),
        (93, 94, ("gate", "1100 gp", "900")),
        (95, 96, ("create greater undead", "1000 gp", "800")),
        (97, 98, ("shape change", "1100 gp", "900")),
        (99, 100, ("clone", "1100 gp", "900"))
    ]

    weapons = [
        (1, 40, "swords"),
        (41, 50, "special swords"),
        (51, 90, "miscellaneous weapons"),
        (91, 100, "special miscellaneous weapons")
    ]

    swords = [
        (1, 10, ["bastard sword"]),
        (11, 30, ["broad sword", "falchion"]),
        (31, 50, ["short sword", "scimitar", "rapier"]),
        (51, 90, ["long sword"]),
        (91, 100, ["two handed sword"])
    ]

    weapon_armor_bonus = [
        (1, 45, ("+1", "1000 gp", "250")),
        (46, 75, ("+2", "4000 gp", "750")),
        (76, 90, ("+3", "9000 gp", "1200")),
        (91, 98, ("+4", "16000 gp", "1750")),
        (99, 100, ("+5", "25000 gp", "2500"))
    ]

    special_swords = [
        (1, 8, ("bane sword", "13500 gp", "4500")),
        (9, 16, ("sword of dancing", "12500 gp", "4100")),
        (17, 24, ("sword of defending", "24500 gp", "8100")),
        (25, 32, ("dragon slayer", "29000 gp", "7250")),
        (33, 36, ("featheredged sword", "31750 gp", "15000")),
        (37, 44, ("flaming sword", "7750 gp", "2000")),
        (45, 52, ("frost bane", "13725 gp", "3000")),
        (53, 56, ("holy avenger", "55000 gp", "27000")),
        (57, 60, ("sword of life stealing", "17000 gp", "5600")),
        (61, 68, ("luck blade", "21500 gp", "7100")),
        (69, 72, ("nine lives stealer", "8500 gp", "2800")),
        (73, 80, ("sword of puncturing", "12000 gp", "3000")),
        (81, 88, ("sylvan sword", "10000 gp", "3000")),
        (89, 92, ("vorpal sword", "38750 gp", "19000")),
        (93, 100, ("sword of wounding", "16000 gp", "5300"))
    ]

    miscellaneous_weapons = [
        (1, 2, "10 arrows"),
        (3, 8, "battle axe"),
        (9, 12, "hand/throwing axe"),
        (13, 16, "two-handed axe"),
        (17, 20, "bardiche"),
        (21, 24, "10 bolts"),
        (25, 28, "bow"),
        (29, 32, "club"),
        (33, 36, "crossbow"),
        (37, 40, "crowbill (lucerne)"),
        (41, 44, "daggger"),
        (45, 48, "dart"),
        (49, 52, "flail"),
        (53, 56, "halberd"),
        (57, 60, "hammer"),
        (61, 64, "javelin"),
        (65, 68, "lance"),
        (69, 72, "mace"),
        (73, 76, "morningstar"),
        (77, 80, "pole arm"),
        (81, 84, "sling"),
        (85, 88, "spear"),
        (89, 92, "staff"),
        (93, 96, "trident"),
        (97, 100, "whip")
    ]

    special_miscellaneous_weapons = [
        (1, 8, ("bane weapon", "13500 gp", "4500")),
        (9, 11, ("club of dagda", "10000 gp", "4000")),
        (12, 15, ("dagger of venom", "4750 gp", "1070")),
        (16, 24, ("dwarven thrower", "18000 gp", "6000")),
        (25, 28, ("featheredged axe", "31750 gp", "15000")),
        (29, 36, ("javelin of lightning", "4500 gp", "450")),
        (37, 40, ("mace of disruption", "25500 gp", "8500")),
        (41, 48, ("mace of smiting", "17500 gp", "5800")),
        (49, 56, ("mace of terror", "8500 gp", "2100")),
        (57, 60, ("nine lives stealer", "8500 gp", "2800")),
        (61, 64, ("oath bow", "25000 gp", "5000")),
        (65, 68, ("slaying arrow/bolt", "9500 gp", "2300")),
        (69, 76, ("sleep arrow/bolt", "1250 gp", "350")),
        (77, 84, ("sylvan weapon", "10000 gp", "3000")),
        (85, 92, ("trident of fish command", "5000 gp", "1200")),
        (93, 100, ("weapon of wounding", "16000 gp", "5300"))
    ]

    armor_and_shields = [
        (1, 75, "shield"),
        (76, 100, "armor")
    ]

    shield = [
        (1, 40, "buckler"),
        (41, 70, "medium"),
        (71, 90, "large"),
        (91, 99, "pavis"),
        (100, 100, "random shield type")
    ]

    random_shield_type = [
        (1, 40, "animated shield"),
        (41, 70, "bashing shield"),
        (71, 85, "blinding shield"),
        (86, 95, "lion's shield"),
        (96, 100, "shield of the cid")
    ]

    armor = [
        (1, 13, "padded"),
        (14, 29, "leather"),
        (30, 36, "studded"),
        (37, 46, "ring"),
        (47, 51, "mail shirt"),
        (52, 61, "hide"),
        (62, 71, "scale mail"),
        (72, 76, "chainmail"),
        (77, 85, "breastplate"),
        (86, 90, "splint mail"),
        (91, 95, "banded mail"),
        (96, 98, "plate mail"),
        (99, 99, "full plate"),
        (100, 100, "random armor type")
    ]

    random_armor_type = [
        (1, 9, "armor of kavacha"),
        (10, 18, "cold/fire resistance"),
        (19, 36, "dwarven plate"),
        (37, 54, "elven chain"),
        (55, 64, "plate of etherealness"),
        (65, 82, "plate armor of the deep"),
        (83, 100, "spell resistance")
    ]

    miscellaneous_magic = [
        (1, 20, "miscellaneous a"),
        (21, 40, "miscellaneous b"),
        (41, 60, "miscellaneous c"),
        (61, 80, "miscellaneous d"),
        (81, 100, "miscellaneous e")
    ]

    # NOTE: Come back to this and flesh out the missing value/xp fields (extra rules involved)
    miscellaneous_a = [
        (1, 4, ("amulet of health", "", "")),
        (5, 8, ("amulet of mighty fists", "", "")),
        (9, 12, ("amulet of natural armor", "", "")),
        (13, 16, ("amulet of the planes", "20250 gp", "6750")),
        (17, 20, ("bag of holding", "25500 gp", "8500")),
        (21, 24, ("bag of tricks", "", "")),
        (25, 28, ("belt of giant strength", "", "1000")),
        (29, 32, ("blessed book", "112000 gp", "0")),
        (33, 36, ("folding boat", "17500 gp", "1750")),
        (37, 40, ("boots of elvenkind", "13500 gp", "3500")),
        (41, 44, ("boots of levitation", "11000 gp", "2500")),
        (45, 48, ("boots of speed", "12750 gp", "1275")),
        (49, 52, ("boots of striding and springing", "9000 gp", "900")),
        (53, 56, ("boots of teleportation", "20250 gp", "6750")),
        (57, 60, ("boots of the winterlands", "9500 gp", "950")),
        (61, 64, ("bowl of commanding water elementals", "25500 gp", "8500")),
        (65, 68, ("bracers of armor", "", "")),
        (69, 72, ("bracers of deflection", "13500 gp", "4500")),
        (73, 76, ("brazier of commanding fire elementals", "25000 gp", "8500")),
        (77, 80, ("brooch of shielding", "11500 gp", "1150")),
        (81, 84, ("broom of flying", "12750 gp", "4250")),
        (85, 88, ("candle of invocation", "22000 gp", "7300")),
        (89, 92, ("cape of the mountebank", "16000 gp", "1600")),
        (93, 96, ("carpet of flying", "17250 gp", "5750")),
        (97, 100, ("censer of controlling air elementals", "25000 gp", "8500"))
    ]

    miscellaneous_b = [
        (0, 0, ("", "")),
    ]

    miscellaneous_c = [
        (0, 0, ("", "")),
    ]

    miscellaneous_d = [
        (0, 0, ("", "")),
    ]

    miscellaneous_e = [
        (0, 0, ("", "")),
    ]

    rings = [
        (0, 0, ("", "")),
    ]

    rods_staves_wands = [
        (0, 0, ("", "")),
    ]

    cursed_items = [
        (0, 0, ("", "")),
    ]

    artifacts = [
        (0, 0, ("", "")),
    ]

    def __init__(self):
        super().__init__()
        self.table = [
            (1, 15, "potions"),
            (16, 30, "scrolls"),
            (31, 45, "weapons"),
            (46, 60, "armor & shields"),
            (61, 80, "miscellaneous magic"),
            (81, 90, "rings"),
            (91, 97, "rods, staves, wands"),
            (98, 99, "cursed items"),
            (100, 100, "artifacts")
        ]

        self.magic_item_tables = {}
        self.magic_item_tables["potions"] = MagicItemsTable.potions
        self.magic_item_tables["scrolls"] = MagicItemsTable.scrolls
        self.magic_item_tables["weapons"] = MagicItemsTable.weapons
        self.magic_item_tables["swords"] = MagicItemsTable.swords
        self.magic_item_tables["weapon/armor bonus"] = MagicItemsTable.weapon_bonus
        self.magic_item_tables["special swords"] = MagicItemsTable.special_swords
        self.magic_item_tables["miscellaneous weapons"] = MagicItemsTable.miscellaneous_weapons
        self.magic_item_tables["special miscellaneous weapons"] = MagicItemsTable.special_miscellaneous_weapons
        self.magic_item_tables["armor & shields"] = MagicItemsTable.armor_and_shields
        self.magic_item_tables["shield"] = MagicItemsTable.shield
        self.magic_item_tables["random shield type"] = MagicItemsTable.random_shield_type
        self.magic_item_tables["armor"] = MagicItemsTable.armor
        self.magic_item_tables["random armor type"] = MagicItemsTable.random_armor_type
        self.magic_item_tables["miscellaneous magic"] = MagicItemsTable.miscellaneous_magic
        self.magic_item_tables["miscellaneous a"] = MagicItemsTable.miscellaneous_a
        self.magic_item_tables["miscellaneous b"] = MagicItemsTable.miscellaneous_b
        self.magic_item_tables["miscellaneous c"] = MagicItemsTable.miscellaneous_c
        self.magic_item_tables["miscellaneous d"] = MagicItemsTable.miscellaneous_d
        self.magic_item_tables["miscellaneous e"] = MagicItemsTable.miscellaneous_e
        self.magic_item_tables["rings"] = MagicItemsTable.rings
        self.magic_item_tables["rods, staves, wands"] = MagicItemsTable.rods_staves_wands
        self.magic_item_tables["cursed items"] = MagicItemsTable.cursed_items
        self.magic_item_tables["artifacts"] = MagicItemsTable.artifacts

    def roll(self):
        roll = self.roll_percentile()
        magic_item_tier = self.search_items(roll, self.table)

        roll = self.roll_percentile()
        magic_item = self.search_items(roll, self.magic_item_tables[magic_item_tier])

        # NOTE: Keep a close eye on this section; note that there is a lot of extra logic to have the above tables talking to each other
        item = magic_item[0]
        gp_value = magic_item[1]
        if "d" in gp_value:
            gp_value = self.roll_dice(gp_value) + " gp"
            

        return item + " (value: " + gp_value + ")"