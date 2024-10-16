import random
from loot_table import LootTable

class ExtraordinaryItemsTable(LootTable):
    # Asterisk denotes that the type is the Castle Keeper's choice, and that the value varies (show this info to user)
    expert_weapons = [
        (1, 5, ("arrow*", "1 gp")),
        (6, 10, ("battle axe", "100 gp")),
        (11, 15, ("bolt*", "12 sp")),
        (16, 20, ("bow*", "Varies")),
        (21, 25, ("crossbow*", "Varies")),
        (26, 30, ("dagger", "20 gp")),
        (31, 35, ("dart", "5 gp")),
        (36, 40, ("flail*", "Varies")),
        (41, 45, ("halberd", "100 gp")),
        (46, 50, ("hammer*", "Varies")),
        (51, 55, ("hand axe", "40 gp")),
        (56, 60, ("javelin", "10 gp")),
        (61, 65, ("lance*", "Varies")),
        (66, 70, ("mace*", "Varies")),
        (71, 75, ("morningstar", "80 gp")),
        (76, 80, ("scimitar", "150 gp")),
        (81, 85, ("spear*", "Varies")),
        (86, 90, ("sword*", "Varies")),
        (91, 95, ("trident", "100 gp")),
        (96, 100, ("two-Handed axe", "300 gp"))
    ]

    jewelry = [
        (1, 5, ("ankle chain", "")),
        (6, 10, ("arm band", "")),
        (11, 15, ("belt", "")),
        (16, 20, ("bracelet", "")),
        (21, 25, ("broach", "")),
        (26, 30, ("buckle", "")),
        (31, 35, ("button (usually 2-4, each worth 1 gp)", "")),
        (36, 40, ("collar", "")),
        (41, 45, ("choker", "")),
        (46, 50, ("earrings", "")),
        (51, 55, ("locket", "")),
        (56, 60, ("medallion", "")),
        (61, 65, ("necklace", "")),
        (66, 70, ("pendent", "")),
        (71, 75, ("ring", "")),
        (76, 80, ("stud", "")),
        (81, 85, ("tiara", "")),
        (86, 90, ("toe ring", "")),
        (91, 95, ("torque", "")),
        (96, 100, ("waist chain", ""))
    ]


    worn_and_ceremonial_items = [
        (1, 5, ("coronet", "")),
        (6, 10, ("crown", "")),
        (11, 15, ("orb", "")),
        (16, 20, ("scepter", "")),
        (21, 25, ("signet ring", "")),
        (26, 30, ("holy symbol", "")),
        (31, 35, ("holy water", "")),
        (36, 40, ("idol", "")),
        (41, 45, ("relic", "")),
        (46, 50, ("rune stones", "")),
        (51, 55, ("fur coat", "2d10")),
        (56, 60, ("hair shirt", "1d10")),
        (61, 65, ("leather jerkin", "2d10")),
        (66, 70, ("oilskin cloth", "2d10")),
        (71, 75, ("silk garment", "5d10")),
        (76, 80, ("gown", "1d10")),
        (81, 85, ("hood", "1d4")),
        (86, 90, ("mantle", "1d4")),
        (91, 95, ("surcoat", "3d10")),
        (96, 100, ("tabard", "2d10"))
    ]


    hand_crafted_items = [
        (1, 5, ("wooden bird cage", "20 gp")),
        (6, 10, ("ivory pipe", "50 gp")),
        (11, 15, ("paper, ink, and quill (in scroll case or box)", "15 gp")),
        (16, 20, ("silver snuff box", "100 gp")),
        (21, 25, ("mechanical toy", "2d10")),
        (26, 30, ("china place settings (1-12, each worth 2 gp)", "2d6x10")),
        (31, 35, ("crystal vase", "10d10")),
        (36, 40, ("pewter goblet", "2 gp")),
        (41, 45, ("silver-plated trencher", "4 gp")),
        (46, 50, ("wooden gourd", "1 gp")),
        (51, 55, ("golden harp", "")),
        (56, 60, ("hunter's horn", "")),
        (61, 65, ("lute of vaughn", "120 gp")),
        (66, 70, ("elven mandolin", "100 gp")),
        (71, 75, ("dragonclaw panpipes", "500 gp")),
        (76, 80, ("animal pelt", "10d10x10")),
        (81, 85, ("decorative egg", "100 gp")),
        (86, 90, ("statue", "")),
        (91, 95, ("carved wood", "")),
        (96, 100, ("miniature figurine", ""))
    ]


    antiquities = [
        (1, 5, ("book(s)", "10d10")),
        (6, 10, ("chart(s)", "5d10")),
        (11, 15, ("map", "5d10")),
        (16, 20, ("scroll", "10d10")),
        (21, 25, ("stone tablet", "10d10x10")),
        (26, 30, ("banner", "250 gp")),
        (31, 35, ("painting", "10d10x10")),
        (36, 40, ("rug", "10d10")),
        (41, 45, ("tapestry", "10d10x100")),
        (46, 50, ("trophy", "10d10")),
        (51, 55, ("brazier", "")),
        (56, 60, ("candelabra", "")),
        (61, 65, ("coffer", "")),
        (66, 70, ("mirror", "")),
        (71, 75, ("urn", "")),
        (76, 80, ("death mask", "")),
        (81, 85, ("hour glass", "")),
        (86, 90, ("music box", "")),
        (91, 95, ("wine", "2d10x10")),
        (96, 100, ("troll knuckles", ""))
    ]

    values = [
        (1, 2, ("clay", "10 gp")),
        (3, 8, ("wood", "50 gp")),
        (9, 11, ("wood with silver inlay", "100 gp")),
        (12, 13, ("wood with gold inlay", "250 gp")),
        (14, 14, ("wood with gemstones", "500 gp")),
        (15, 19, ("stone", "100 gp")),
        (20, 23, ("stone with gemstones", "500 gp")),
        (24, 24, ("bone with jewels", "1000 gp")),
        (25, 34, ("silver", "250 gp")),
        (35, 39, ("silver with gold", "500 gp")),
        (40, 44, ("silver with platinum", "750 gp")),
        (45, 50, ("silver with gemstones", "1250 gp")),
        (51, 53, ("ivory", "500 gp")),
        (54, 56, ("ivory with silver", "750 gp")),
        (57, 58, ("ivory with gold", "1000 gp")),
        (59, 60, ("ivory with gemstones", "3000 gp")),
        (61, 63, ("jade", "750 gp")),
        (64, 67, ("jade with ivory", "1000 gp")),
        (68, 70, ("jade silver or gold", "1250 gp")),
        (71, 72, ("jade with platinum", "2000 gp")),
        (73, 74, ("jade with gemstones", "5000 gp")),
        (75, 86, ("gold", "1000 gp")),
        (87, 89, ("gold with platinum", "3500 gp")),
        (90, 93, ("gold with gemstones", "7500 gp")),
        (94, 96, ("platinum", "10000 gp")),
        (97, 98, ("platinum with gemstones", "15000 gp")),
        (99, 99, ("platinum with mithril", "20000 gp")),
        (100, 100, ("mithril", "50000 gp"))
    ]

    def __init__(self):
        super().__init__()
        self.table = [
            (1, 20, "expert weapons"),
            (21, 40, "jewelry"),
            (41, 60, "worn & ceremonial items"),
            (61, 80, "hand crafted items"),
            (81, 100, "antiquities")
        ]

        self.extraordinary_item_tables = {}
        self.extraordinary_item_tables["expert weapons"] = ExtraordinaryItemsTable.expert_weapons
        self.extraordinary_item_tables["jewelry"] = ExtraordinaryItemsTable.jewelry
        self.extraordinary_item_tables["worn & ceremonial items"] = ExtraordinaryItemsTable.worn_and_ceremonial_items
        self.extraordinary_item_tables["hand crafted items"] = ExtraordinaryItemsTable.hand_crafted_items
        self.extraordinary_item_tables["antiquities"] = ExtraordinaryItemsTable.antiquities
        self.extraordinary_item_tables["values"] = ExtraordinaryItemsTable.values

    def roll(self):
        roll = self.roll_percentile()
        extraordinary_item_tier = self.search_items(roll, self.table)

        roll = self.roll_percentile()
        extraordinary_item = self.search_items(roll, self.extraordinary_item_tables[extraordinary_item_tier])

        item = extraordinary_item[0]
        gp_value = extraordinary_item[1]
        if gp_value == "":
            roll = self.roll_percentile()
            value_item = self.search_items(roll, self.extraordinary_item_tables["values"])
            gp_value = value_item[1] + " (" + value_item[0] + ")"
        elif "d" in gp_value:
            gp_value = self.roll_dice(gp_value) + " gp"
            

        return item + " (value: " + gp_value + ")"