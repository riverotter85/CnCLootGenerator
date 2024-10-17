from loot_table import LootTable

class MagicItemsTable(LootTable):
    potions = [
        (1, 3, ("potion of aid", "400 gp", "200")),
        (4, 6, ("oil of bless", "300 gp", "100")),
        (7, 9, ("potion of blur", "400 gp", "200")),
        (10, 12, ("potion of clairaudience/clairvoyance", "500 gp", "300")),
        (13, 15, ("potion of cure light wounds", "300 gp", "100")),
        (16, 18, ("potion of cure serious wounds", "500 gp", "300")),
        (19, 21, ("potion of cure critical wounds", "700 gp", "500")),
        (22, 24, ("potion of delay poison", "400 gp", "200")),
        (25, 27, ("potion of endure elements", "300 gp", "100")),
        (28, 30, ("potion of fly", "500 gp", "300")),
        (31, 33, ("potion of gaseous form", "500 gp", "300")),
        (34, 36, [("potion of giant strength (hill)", "700 gp", "500"),
                  ("potion of giant strength (stone)", "700 gp", "500"),
                  ("potion of giant strength (frost)", "700 gp", "500"),
                  ("potion of giant strength (fire)", "700 gp", "500"),
                  ("potion of giant strength (cloud)", "700 gp", "500"),
                  ("potion of giant strength (storm)", "700 gp", "500")]),
        (37, 39, ("potion of haste", "500 gp", "300")),
        (40, 42, ("potion of heal", "800 gp", "600")),
        (43, 45, [("potion of invisibility", "400 gp", "200"),
                  ("oil of invisibility", "400 gp", "200")]),
        (46, 48, [("potion of levitation", "400 gp", "200"),
                  ("oil of levitation", "400 gp", "200")]), # Expand
        (49, 51, ("potion of longevity", "12000 gp", "1500")),
        (52, 54, ("potion of neutralize poison", "600 gp", "400")),
        (55, 57, ("potion of nondetection", "500 gp", "300")),
        (58, 60, ("potion of pass without trace", "300 gp", "100")),
        (61, 63, [("potion of protection from alignment (good)", "300 gp", "100"),
                  ("potion of protection from alignment (evil)", "300 gp", "100"),
                  ("potion of protection from alignment (law)", "300 gp", "100"),
                  ("potion of protection from alignment (chaos)", "300 gp", "100")]), # Expand
        (64, 66, ("potion of protection from arrows", "500 gp", "300")),
        (67, 69, ("potion of remove blindness/deafness", "500 gp", "300")),
        (70, 72, ("potion of remove curse", "500 gp", "300")),
        (73, 75, ("potion of remove disease", "500 gp", "300")),
        (76, 78, ("potion of remove paralysis", "400 gp", "200")),
        (79, 81, ("potion of restoration", "700 gp", "400")),
        (82, 84, ("potion of sanctuary", "300 gp", "100")),
        (85, 87, ("potion of shield of faith +2", "300 gp", "100")),
        (88, 90, ("potion of spider climb", "300 gp", "100")),
        (91, 93, ("potion of tongues", "500 gp", "300")),
        (94, 96, ("potion of water breathing", "500 gp", "300")),
        (97, 99, ("potion of water walk", "900 gp", "700")),
        (100, 100, ("potion of trap the soul", "1,100 gp", "900"))
    ]

    scrolls = [
        (1, 8, ("scroll of 1 spell level", "300 gp", "100")),
        (9, 16, ("scroll of 2 spell levels", "400 gp", "200")),
        (17,24, ("scroll of 3 spell levels", "500 gp", "300")),
        (25, 32, ("scroll of 4 spell levels", "600 gp", "400")),
        (33, 40, ("scroll of 5 spell levels", "700 gp", "500")),
        (41, 45, ("scroll of 6 spell levels", "800 gp", "600")),
        (46, 50, ("scroll of 7 spell levels", "900 gp", "700")),
        (51, 55, ("scroll of 8 spell levels", "1000 gp", "800")),
        (56, 60, ("scroll of 9 spell levels", "1100 gp", "900")),
        (61, 65, ("scroll of 10 spell levels", "1200 gp", "1000")),
        (66, 68, ("scroll of 11 spell levels", "1300 gp", "1100")),
        (69, 71, ("scroll of 12 spell levels", "1400 gp", "1200")),
        (72, 74, ("scroll of 13 spell levels", "1500 gp", "1300")),
        (75, 77, ("scroll of 14 spell levels", "1600 gp", "1400")),
        (78, 80, ("scroll of 15 spell levels", "1700 gp", "1500")),
        (81, 82, ("scroll of teleport without error", "900 gp", "700")),
        (83, 84, ("scroll of symbol", "1000 gp", "800")),
        (85, 86, ("scroll of trap the soul", "1100 gp", "900")),
        (87, 88, ("scroll of time stop", "1100 gp", "900")),
        (89, 90, ("scroll of true resurrection", "1100 gp", "900")),
        (91, 92, ("scroll of mass heal", "1000 gp", "800")),
        (93, 94, ("scroll of gate", "1100 gp", "900")),
        (95, 96, ("scroll of create greater undead", "1000 gp", "800")),
        (97, 98, ("scroll of shape change", "1100 gp", "900")),
        (99, 100, ("scroll of clone", "1100 gp", "900"))
    ]

    weapons = [
        (1, 40, "swords"),
        (41, 50, "special swords"),
        (51, 90, "miscellaneous weapons"),
        (91, 100, "special miscellaneous weapons")
    ]

    swords = [
        (1, 10, "bastard sword"),
        (11, 30, ["broad sword", "falchion"]),
        (31, 50, ["short sword", "scimitar", "rapier"]),
        (51, 90, "long sword"),
        (91, 100, "two handed sword")
    ]

    weapon_armor_bonus = [
        (1, 45, ("+1", "1000 gp", "250")),
        (46, 75, ("+2", "4000 gp", "750")),
        (76, 90, ("+3", "9000 gp", "1200")),
        (91, 98, ("+4", "16000 gp", "1750")),
        (99, 100, ("+5", "25000 gp", "2500"))
    ]

    special_swords = [
        (1, 8, [("+3 bane sword of undead", "13500 gp", "4500"), # Making duplicate entries because I don't want a proper table for this
                ("+3 bane sword of spell-casters", "13500 gp", "4500"),
                ("+3 bane sword of orcs", "13500 gp", "4500"),
                ("+3 bane sword of orcs", "13500 gp", "4500"),
                ("+3 bane sword of goblins", "13500 gp", "4500"),
                ("+3 bane sword of goblins", "13500 gp", "4500"),
                ("+3 bane sword of giants", "13500 gp", "4500"),
                ("+3 bane sword of giants", "13500 gp", "4500"),
                ("+3 bane sword of lycanthropes", "13500 gp", "4500"),
                ("+3 bane sword of lycanthropes", "13500 gp", "4500"),
                ("+3 bane sword of demons/devils", "13500 gp", "4500"),
                ("+3 bane sword of dragons", "13500 gp", "4500")]),
        (9, 16, ("+2 sword of dancing", "12500 gp", "4100")),
        (17, 24, ("+4 sword of defending", "24500 gp", "8100")),
        (25, 32, [("+2/+4 black dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 blue dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 green dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 red dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 white dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 brass dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 bronze dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 copper dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 gold dragon slayer", "29000 gp", "7250"),
                  ("+2/+4 silver dragon slayer", "29000 gp", "7250")]),
        (33, 36, ("+3 featheredged sword", "31750 gp", "15000")),
        (37, 44, ("+2 flaming sword", "7750 gp", "2000")),
        (45, 52, ("+3 frost brand", "13725 gp", "3000")),
        (53, 56, ("+2 (+5) holy avenger", "55000 gp", "27000")),
        (57, 60, ("+2 sword of life stealing", "17000 gp", "5600")),
        (61, 68, ("+2 luck blade", "21500 gp", "7100")),
        (69, 72, ("+2 nine lives stealer", "8500 gp", "2800")),
        (73, 80, ("+2 sword of puncturing", "12000 gp", "3000")),
        (81, 88, ("+3 sylvan sword", "10000 gp", "3000")),
        (89, 92, ("+4 vorpal sword", "38750 gp", "19000")),
        (93, 100, ("+3 sword of wounding", "16000 gp", "5300"))
    ]

    miscellaneous_weapons = [
        (1, 2, "arrows (10)"),
        (3, 8, "battle axe"),
        (9, 12, "hand/throwing axe"),
        (13, 16, "two-handed axe"),
        (17, 20, "bardiche"),
        (21, 24, "bolts (10)"),
        (25, 28, "bow"),
        (29, 32, "club"),
        (33, 36, "crossbow"),
        (37, 40, "crowbill (lucerne)"),
        (41, 44, "dagger"),
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
        (1, 8, ("+3 bane weapon", "13500 gp", "4500")),
        (9, 11, ("club of dagda", "10000 gp", "4000")),
        (12, 15, ("+1 dagger of venom", "4750 gp", "1070")),
        (16, 24, ("+2 (+3) dwarven thrower", "18000 gp", "6000")),
        (25, 28, ("+3 featheredged axe", "31750 gp", "15000")),
        (29, 36, ("javelin of lightning", "4500 gp", "450")),
        (37, 40, ("+3 mace of disruption", "25500 gp", "8500")),
        (41, 48, ("+3 mace of smiting", "17500 gp", "5800")),
        (49, 56, ("+2 mace of terror", "8500 gp", "2100")),
        (57, 60, ("+2 nine lives stealer", "8500 gp", "2800")),
        (61, 64, ("+2 oath bow", "25000 gp", "5000")),
        (65, 68, ("+1 slaying arrow/bolt", "9500 gp", "2300")),
        (69, 76, ("+1 sleep arrow/bolt", "1250 gp", "350")),
        (77, 84, ("+3 sylvan weapon", "10000 gp", "3000")),
        (85, 92, ("+1 trident of fish command", "5000 gp", "1200")),
        (93, 100, ("+3 weapon of wounding", "16000 gp", "5300"))
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
        (1, 40, ("animated shield", "1000 gp", "250")),
        (41, 70, ("+1 shield of bashing", "1000 gp", "250")),
        (71, 85, ("blinding shield", "1000 gp", "250")),
        (86, 95, ("+2 lion's shield", "4000 gp", "750")),
        (96, 100, ("+2 shield of the cid", "4000 gp", "750"))
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
        (1, 9, ("+3 armor of kavacha", "9000 gp", "1200")),
        (10, 18, [("armor of cold resistance (+2)", "4000 gp", "750"),
                  ("armor of fire resistance (+2)", "4000 gp", "750")]),
        (19, 36, ("+4 dwarven plate", "16000 gp", "1750")),
        (37, 54, ("+5 elven chain", "25000 gp", "2500")),
        (55, 64, ("+3 armor of etherealness", "9000 gp", "1200")),
        (65, 82, ("+1 plate armor of the deep", "1000 gp", "250")),
        (83, 100, [("armor of spell resistance (+1)", "10000 gp", "1000"),
                   ("armor of spell resistance (+2)", "20000 gp", "2000"),
                   ("armor of spell resistance (+5)", "50000 gp", "5000"),
                   ("armor of spell resistance (+8)", "80000 gp", "8000")])
    ]

    miscellaneous_magic = [
        (1, 20, "miscellaneous a"),
        (21, 40, "miscellaneous b"),
        (41, 60, "miscellaneous c"),
        (61, 80, "miscellaneous d"),
        (81, 100, "miscellaneous e")
    ]

    miscellaneous_a = [
        (1, 4, [("amulet of health (+2)", "4000 gp", "1000"),
                ("amulet of health (+4)", "16000 gp", "2000"),
                ("amulet of health (+6)", "36000 gp", "3000")]),
        (5, 8, [("amulet of mighty fists (+1)", "1000 gp", "500"),
                ("amulet of mighty fists (+2)", "4000 gp", "1000"),
                ("amulet of mighty fists (+3)", "8000 gp", "1500"),
                ("amulet of mighty fists (+4)", "16000 gp", "2000"),
                ("amulet of mighty fists (+5)", "25000 gp", "2500")]),
        (9, 12, [("amulet of natural armor (+1)", "1000 gp", "500"),
                 ("amulet of natural armor (+2)", "4000 gp", "1000"),
                 ("amulet of natural armor (+3)", "8000 gp", "1500"),
                 ("amulet of natural armor (+4)", "16000 gp", "2000"),
                 ("amulet of natural armor (+5)", "25000 gp", "2500")]),
        (13, 16, ("amulet of the planes", "20250 gp", "6750")),
        (17, 20, ("bag of holding", "25500 gp", "8500")),
        (21, 24, [("bag of tricks (gray-colored)", "1000 gp", "300"),
                  ("bag of tricks (rust-colored)", "4000 gp", "1250"),
                  ("bag of tricks (tan-colored)", "16000 gp", "3000")]),
        (25, 28, [("belt of giant strength (hill)", "10000 gp", "1000"),
                  ("belt of giant strength (frost)", "20000 gp", "1000"),
                  ("belt of giant strength (fire)", "30000 gp", "1000"),
                  ("belt of giant strength (stone)", "40000 gp", "1000"),
                  ("belt of giant strength (cloud)", "50000 gp", "1000"),
                  ("belt of giant strength (storm)", "60000 gp", "1000")]),
        (29, 32, ("blessed book", "112000 gp", "11200")),
        (33, 36, ("folding boat", "17500 gp", "1750")),
        (37, 40, ("boots of elvenkind", "13500 gp", "3500")),
        (41, 44, ("boots of levitation", "11000 gp", "2500")),
        (45, 48, ("boots of speed", "12750 gp", "1275")),
        (49, 52, ("boots of striding and springing", "9000 gp", "900")),
        (53, 56, ("boots of teleportation", "20250 gp", "6750")),
        (57, 60, ("boots of the winterlands", "9500 gp", "950")),
        (61, 64, ("bowl of commanding water elementals", "25500 gp", "8500")),
        (65, 68, [("bracers of armor (+1)", "1000 gp", "500"),
                  ("bracers of armor (+2)", "4000 gp", "1000"),
                  ("bracers of armor (+3)", "8000 gp", "1500"),
                  ("bracers of armor (+4)", "16000 gp", "2000"),
                  ("bracers of armor (+5)", "25000 gp", "2500")]),
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
        (1, 4, ("chime of interruption", "13500 gp", "1350")),
        (5, 8, ("chime of opening", "10500 gp", "1050")),
        (9, 12, ("circlet of persuasion", "11250 gp", "1125")),
        (13, 16, ("cloak of arachnida", "17500 gp", "1750")),
        (17, 20, ("cloak of the bat", "13500 gp", "3000")),
        (21, 24, [("cloak of charisma (+2)", "4000 gp", "1000"),
                  ("cloak of charisma (+4)", "16000 gp", "2000"),
                  ("cloak of charisma (+6)", "36000 gp", "3000")]),
        (25, 28, ("cloak of displacement", "17000 gp", "1700")),
        (29, 32, ("cloak of elvenkind", "15500 gp", "3000")),
        (33, 36, ("cloak of etherealness", "11250 gp", "2500")),
        (37, 40, ("cloak of the manta ray", "9000 gp", "2500")),
        (41, 44, [("cloak of resistance (+1)", "1000 gp", "500"),
                  ("cloak of resistance (+2)", "4000 gp", "1000"),
                  ("cloak of resistance (+3)", "8000 gp", "1500"),
                  ("cloak of resistance (+4)", "16000 gp", "2000"),
                  ("cloak of resistance (+5)", "25000 gp", "2500")]),
        (45, 46, ("sampo coin", "10000 gp", "2750")),
        (47, 48, [("crystal ball", "42000 gp", "5000"),
                  ("crystal ball (with see invisibility)", "50000 gp", "5000"),
                  ("crystal ball (with detect thoughts)", "51000 gp", "5000"),
                  ("crystal ball (with telepathic bond)", "70000 gp", "5000"),
                  ("crystal ball (with true seeing)", "80000 gp", "5000")]),
        (49, 52, ("cube of force", "47250 gp", "4000")),
        (53, 56, ("cube of frost resistance", "12750 gp", "1270")),
        (57, 60, ("cubic gate", "24750 gp", "4500")),
        (61, 64, ("decanter of endless water", "13500 gp", "1350")),
        (65, 66, ("dragon's teeth", "7000 gp", "12000")),
        (67, 68, ("drums of panic", "4750 gp", "475")),
        (69, 72, ("dust of appearance", "8500 gp", "850")),
        (73, 76, ("dust of disappearance", "5500 gp", "550")),
        (77, 80, ("dust of illusion", "5500 gp", "550")),
        (81, 84, ("efficient quiver", "8500 gp", "850")),
        (85, 88, ("efreeti bottle", "47250 gp", "4700")),
        (89, 92, ("elemental gem", "20250 gp", "2000")),
        (93, 96, ("eversmoking bottle", "4250 gp", "425")),
        (97, 100, ("eyes of doom", "free round at the house of sludge", "7"))
    ]

    miscellaneous_c = [
        (1, 3, ("eyes of the eagle", "4250 gp", "425")),
        (4, 7, [("figurine of wondrous power (bronze griffon)", "10000 gp", "2000"),
                ("figurine of wondrous power (ebony fly)", "10000 gp", "2000"),
                ("figurine of wondrous power (golden lions)", "16500 gp", "3300"),
                ("figurine of wondrous power (ivory goats)", "21000 gp", "4000"),
                ("figurine of wondrous power (marble elephant)", "17000 gp", "3400"),
                ("figurine of wondrous power (obsidian steed)", "28500 gp", "5700"),
                ("figurine of wondrous power (onyx dog)", "15500 gp", "3100"),
                ("figurine of wondrous power (serpentine owl)", "9100 gp", "1820"),
                ("figurine of wondrous power (silver raven)", "3800 gp", "760")]),
        (8, 11, ("feather token", "4500 gp", "450")),
        (12, 13, ("fruit of the lotus tree", "10000 gp", "5000")),
        (14, 16, ("gauntlets of ogre power", "9500 gp", "950")),
        (17, 20, ("gem of brightness", "17750 gp", "2000")),
        (21, 24, ("gem of seeing", "15250 gp", "1500")),
        (25, 28, [("gloves of dexterity (+2)", "4000 gp", "1000"),
                  ("gloves of dexterity (+4)", "16000 gp", "2000"),
                  ("gloves of dexterity (+6)", "36000 gp", "3000")]),
        (29, 32, ("gloves of swimming and climbing", "9000 gp", "900")),
        (33, 36, ("handy haversack", "12250 gp", "1225")),
        (37, 40, ("harp of charming", "7750 gp", "2000")),
        (41, 44, ("hat of disguise", "5500 gp", "550")),
        (45, 48, ("helm of brilliance", "34750 gp", "3000")),
        (49, 52, ("helm of comprehend language & read magic", "4250 gp", "425")),
        (53, 56, ("helm of telepathy", "17250 gp", "3450")),
        (57, 60, ("helm of teleportation", "20250 gp", "2250")),
        (61, 64, ("helm of underwater action", "4500 gp", "1125")),
        (65, 68, ("horn of blasting", "17500 gp", "1750")),
        (69, 72, ("horn of fog", "4250 gp", "425")),
        (73, 76, ("horn of goodness/evil", "4250 gp", "1050")),
        (77, 80, ("horn of the merfolk", "12500 gp", "2500")),
        (81, 84, [("horn of valhalla (silver)", "32000 gp", "1250"),
                  ("horn of valhalla (brass)", "32000 gp", "2500"),
                  ("horn of valhalla (bronze)", "32000 gp", "5000"),
                  ("horn of valhalla (iron)", "32000 gp", "10000")]),
        (85, 88, ("horseshoes of speed", "7750 gp", "775")),
        (89, 92, ("horseshoes of the zephyr", "9750 gp", "975")),
        (93, 96, ("instant fortress", "22500 gp", "2250")),
        (97, 100, [("ioun stones (clear spindle)", "4000 gp", "500"),
                   ("ioun stones (dusty rose prism)", "5000 gp", "500"),
                   ("ioun stones (deep red sphere)", "8000 gp", "1000"),
                   ("ioun stones (incandescent blue sphere)", "8000 gp", "1000"),
                   ("ioun stones (pale blue rhomboid)", "8000 gp", "1000"),
                   ("ioun stones (pink rhomboid)", "8000 gp", "1000"),
                   ("ioun stones (pink & green sphere)", "8000 gp", "1000"),
                   ("ioun stones (scarlet & blue sphere)", "8000 gp", "1000"),
                   ("ioun stones (dark blue rhomboid)", "10000 gp", "1000"),
                   ("ioun stones (vibrant purple prism)", "36000 gp", "1500"),
                   ("ioun stones (iridescent spindle)", "18000 gp", "1000"),
                   ("ioun stones (pale lavender ellipsoid)", "20000 gp", "2000"),
                   ("ioun stones (pearly white spindle)", "20000 gp", "1000"),
                   ("ioun stones (pale green prism)", "30000 gp", "1500"),
                   ("ioun stones (orange prism)", "30000 gp", "300"),
                   ("ioun stones (lavendar & green prism)", "40000 gp", "5000")])
    ]

    miscellaneous_d = [
        (1, 4, ("iron bands of binding", "17500 gp", "1750")),
        (5, 7, ("iron flask", "0", "0")), # Flask itself has no intrinsic value
        (8, 9, ("lady of the lake's gift", "15000 gp", "7500")),
        (10, 11, ("lyre of building", "13500 gp", "2000")),
        (12, 13, ("mantle of barb-e-bayan", "6000 gp", "2500")),
        (14, 16, ("mantle of spell resistance", "200000 gp", "20000")),
        (17, 20, [("manual of bodily health (+1)", "10000 gp", "500"),
                  ("manual of bodily health (+2)", "22500 gp", "1000"),
                  ("manual of bodily health (+3)", "35000 gp", "1500"),
                  ("manual of bodily health (+4)", "47500 gp", "2000"),
                  ("manual of bodily health (+5)", "60000 gp", "2500")]),
        (21, 24, [("manual of gainful exercise (+1)", "10000 gp", "500"),
                  ("manual of gainful exercise (+2)", "22500 gp", "1000"),
                  ("manual of gainful exercise (+3)", "35000 gp", "1500"),
                  ("manual of gainful exercise (+4)", "47500 gp", "2000"),
                  ("manual of gainful exercise (+5)", "60000 gp", "2500")]),
        (25, 28, [("manual of quickness of action (+1)", "10000 gp", "500"),
                  ("manual of quickness of action (+2)", "22500 gp", "1000"),
                  ("manual of quickness of action (+3)", "35000 gp", "1500"),
                  ("manual of quickness of action (+4)", "47500 gp", "2000"),
                  ("manual of quickness of action (+5)", "60000 gp", "2500")]),
        (29, 32, ("mattock of the titans", "11500 gp", "1150")),
        (33, 36, ("maul of the titans", "13500 gp", "1350")),
        (37, 38, ("mead of stuttungr", "5000 gp", "2500/level")), # Have extra logic for parsing the xp here
        (39, 41, ("medallion of thoughts", "5500 gp", "1500")),
        (42, 44, ("mirror of life trapping", "39000 gp", "2300")),
        (45, 48, ("mirror of mental prowess", "37250 gp", "3720")),
        (49, 52, ("mirror of opposition", "25600 gp", "2560")),
        (53, 56, ("necklace of adaptation", "4500 gp", "450")),
        (57, 60, [("necklace of fireballs (type I)", "1650 gp", "165"),
                  ("necklace of fireballs (type II)", "2700 gp", "270"),
                  ("necklace of fireballs (type III)", "4350 gp", "435"),
                  ("necklace of fireballs (type IV)", "5400 gp", "540"),
                  ("necklace of fireballs (type V)", "5850 gp", "585"),
                  ("necklace of fireballs (type VI)", "8100 gp", "810"),
                  ("necklace of fireballs (type VII)", "8700 gp", "870")]),
        (61, 64, ("orb of storms", "49500 gp", "2500")),
        (65, 68, [("pearl of power (1st-level spell)", "1000 gp", "1000"),
                  ("pearl of power (2nd-level spell)", "4000 gp", "2000"),
                  ("pearl of power (3rd-level spell)", "9000 gp", "3000"),
                  ("pearl of power (4th-level spell)", "16000 gp", "4000"),
                  ("pearl of power (5th-level spell)", "25000 gp", "5000"),
                  ("pearl of power (6th-level spell)", "36000 gp", "6000"),
                  ("pearl of power (7th-level spell)", "49000 gp", "7000"),
                  ("pearl of power (8th-level spell)", "64000 gp", "8000"),
                  ("pearl of power (9th-level spell)", "81000 gp", "9000")]),
        (69, 72, ("pearl of the sirens", "13500 gp", "1350")),
        (73, 76, ("periapt of health", "9500 gp", "950")),
        (77, 80, ("periapt of proof against poison", "9500 gp", "950")),
        (81, 84, [("periapt of wisdom (+2)", "4000 gp", "1000"),
                  ("periapt of wisdom (+4)", "16000 gp", "2000"),
                  ("periapt of wisdom (+6)", "36000 gp", "3000")]),
        (85, 88, ("periapt of wound closure", "17000 gp", "1000")),
        (89, 92, ("phylactery of faithfulness", "5500 gp", "1250")),
        (93, 96, ("phylactery of undead turning", "16000 gp", "1600")),
        (97, 100, ("pipes of the sewers", "7500 gp", "750"))
    ]

    miscellaneous_e = [
        (1, 4, ("portable hole", "29250 gp", "2950")),
        (5, 8, ("restorative ointment", "5500 gp", "550")),
        (9, 12, ("ring gates", "30500 gp", "3050")),
        (13, 16, ("robe of the arch-magi", "7500 gp", "7500")),
        (17, 20, ("robe of blending", "23000 gp", "2300")),
        (21, 24, ("robe of eyes", "17500 gp", "1750")),
        (25, 28, ("robe of scintillating colors", "13500 gp", "1350")),
        (29, 32, ("robe of useful items", "14000 gp", "1400")),
        (33, 36, ("rope of climbing", "5750 gp", "575")),
        (37, 40, ("rope of entanglement", "7750 gp", "775")),
        (41, 44, ("scabbard of sharpness", "17500 gp", "1700")),
        (45, 48, ("scarab of protection", "34000 gp", "1200")),
        (49, 52, ("shrouds of disintegration", "1650 gp", "165")),
        (53, 56, ("slippers of spider climbing", "9000 gp", "900")),
        (57, 60, ("stone of alarm", "1400 gp", "140")),
        (61, 64, ("stone of controlling earth elementals", "56500 gp", "8500")),
        (65, 68, ("stone of good luck", "4250 gp", "425")),
        (69, 72, ("stone horse", "8500 gp", "850")),
        (73, 75, [("strand of prayer beads (lesser)", "9600 gp", "960"),
                  ("strand of prayer beads (standard)", "45800 gp", "4580"),
                  ("strand of prayer beads (greater)", "95800 gp", "9580")]),
        (76, 77, [("thunderstones (1 stone)", "2000 gp", "1000"),
                  ("thunderstones (2 stones)", "4000 gp", "2000"),
                  ("thunderstones (3 stones)", "6000 gp", "3000"),
                  ("thunderstones (4 stones)", "8000 gp", "4000")]),
        (78, 80, [("tome of clear thought (+1)", "1000 gp", "500"),
                  ("tome of clear thought (+2)", "4000 gp", "1000"),
                  ("tome of clear thought (+3)", "8000 gp", "1500"),
                  ("tome of clear thought (+4)", "16000 gp", "2000"),
                  ("tome of clear thought (+5)", "25000 gp", "2500")]),
        (81, 83, [("tome of leadership and influence (+1)", "1000 gp", "500"),
                  ("tome of leadership and influence (+2)", "4000 gp", "1000"),
                  ("tome of leadership and influence (+3)", "8000 gp", "1500"),
                  ("tome of leadership and influence (+4)", "16000 gp", "2000"),
                  ("tome of leadership and influence (+5)", "25000 gp", "2500")]),
        (84, 85, ("tome of raudskinna", "12000 gp", "8000")),
        (86, 88, [("tome of understanding (+1)", "1000 gp", "500"),
                  ("tome of understanding (+2)", "4000 gp", "1000"),
                  ("tome of understanding (+3)", "8000 gp", "1500"),
                  ("tome of understanding (+4)", "16000 gp", "2000"),
                  ("tome of understanding (+5)", "25000 gp", "2500")]),
        (89, 92, ("well of many worlds", "40450 gp", "2000")),
        (93, 96, ("wind fans", "5500 gp", "550")),
        (97, 100, ("wings of flying", "15750 gp", "1575"))
    ]

    rings = [
        (1, 4, ("ring of animal friendship", "1650 gp", "330")),
        (5, 8, ("ring of blinking", "9800 gp", "1960")),
        (9, 12, ("ring of chameleon power", "5800 gp", "1160")),
        (13, 16, ("ring of climbing", "2800 gp", "560")),
        (17, 20, ("ring of counter spells", "5050 gp", "1010")),
        (21, 21, [("ring of air elemental command", "45000 gp", "9000"),
                  ("ring of earth elemental command", "45000 gp", "9000"),
                  ("ring of fire elemental command", "45000 gp", "9000"),
                  ("ring of water elemental command", "45000 gp", "9000")]),
        (22, 25, ("ring of energy resistance", "25000 gp", "5000")),
        (26, 29, ("ring of evasion", "20000 gp", "5000")),
        (30, 33, ("ring of feather falling", "1550 gp", "310")),
        (34, 37, ("ring of force shield", "5050 gp", "1010")),
        (38, 41, ("ring of freedom of movement", "8300 gp", "1660")),
        (42, 44, ("ring of friend shield", "6050 gp", "1210")),
        (45, 45, ("ring of gyges", "5800 gp", "1200")),
        (46, 46, ("ring of invisibility", "5800 gp", "1160")),
        (47, 50, ("ring of jumping", "1550 gp", "310")),
        (51, 51, ("lancelot's ring", "8000 gp", "3000")),
        (52, 54, ("ring of mind shielding", "5800 gp", "1160")),
        (55, 58, [("ring of protection (+1)", "2300 gp", "460"),
                  ("ring of protection (+2)", "5300 gp", "1060"),
                  ("ring of protection (+3)", "11300 gp", "2260"),
                  ("ring of protection (+4)", "17300 gp", "3460"),
                  ("ring of protection (+5)", "26300 gp", "5260"),
                  ("ring of protection (+6)", "37300 gp", "7460")]),
        (59, 62, ("ring of ram", "5800 gp", "1160")),
        (63, 63, ("ring of regeneration", "24050 gp", "4810")),
        (64, 67, ("ring of shooting stars", "9300 gp", "1860")),
        (68, 71, [("ring of spell storing (minor)", "5050 gp", "1010"),
                  ("ring of spell storing (standard)", "12550 gp", "2510"),
                  ("ring of spell storing (major)", "38000 gp", "7600")]),
        (72, 75, ("ring of spell turning", "41800 gp", "8360")),
        (76, 79, ("ring of sustenance", "2800 gp", "560")),
        (80, 83, ("ring of swimming", "1300 gp", "260")),
        (84, 87, ("ring of telekinesis", "12550 gp", "2510")),
        (88, 88, ("ring of three wishes", "114750 gp", "5000")),
        (89, 92, ("ring of water walking", "5800 gp", "1160")),
        (93, 96, [("ring of wizardry (minor)", "20000 gp", "1000"),
                  ("ring of wizardry (major)", "40000 gp", "2000"),
                  ("ring of wizardry (greater)", "70000 gp", "3000"),
                  ("ring of wizardry (arch)", "100000 gp", "4000")]),
        (97, 100, ("ring of x-ray vision", "9300 gp", "930"))
    ]

    rods_staves_wands = [
        (1, 4, ("rod of absorption", "50000 gp", "8300")),
        (5, 5, ("rod of cancellation", "13500 gp", "2250")),
        (6, 6, ("rod of lordly might", "20500 gp", "3400")),
        (7, 10, ("rod of negation", "9500 gp", "1500")),
        (11, 14, ("rod of python", "8750 gp", "1400")),
        (15, 18, ("rod of rulership", "20000 gp", "3200")),
        (19, 22, ("rod of thunder & lightning", "29000 gp", "4800")),
        (23, 26, ("rod of withering", "25000 gp", "4000")),
        (27, 30, ("rod of wonder", "13500 gp", "2250")),
        (31, 34, ("staff of abjuration", "54000 gp", "9000")),
        (35, 38, ("staff of conjuration", "47000 gp", "7800")),
        (39, 42, ("staff of evocation", "47000 gp", "7880")),
        (43, 46, ("staff of fire", "23000 gp", "3800")),
        (47, 50, ("staff of frost", "32500 gp", "5400")),
        (51, 54, ("staff of healing", "31000 gp", "5100")),
        (55, 58, ("staff of power", "72000 gp", "12000")),
        (59, 59, ("staff of resurrection", "41000 gp", "6800")),
        (60, 63, ("staff of woodlands", "42000 gp", "7000")),
        (64, 67, ("wand of color spray", "12250 gp", "2000")),
        (68, 71, ("wand of darkness", "12250 gp", "2000")),
        (72, 75, ("wand of dispel magic", "16750 gp", "2800")),
        (76, 79, ("wand of illusion", "22000 gp", "3600")),
        (80, 80, ("wand of invisibility", "31000 gp", "5000")),
        (81, 84, ("wand of levitation", "26000 gp", "4300")),
        (85, 88, ("wand of magic missile", "12250 gp", "2000")),
        (89, 92, ("wand of polymorph", "23000 gp", "3800")),
        (93, 96, ("wand of restoration", "18000 gp", "3000")),
        (97, 100, ("wand of suggestion", "14500 gp", "2400"))
    ]

    cursed_items = [
        (1, 4, "amulet of inescapable location"),
        (5, 8, "armor of rage"),
        (9, 12, "bag of devouring"),
        (13, 16, "boots of dancing"),
        (17, 20, "bracers of defenselessness"),
        (21, 24, "flask of curses"),
        (25, 28, "gauntlets of fumbling"),
        (29, 32, "helm of opposite alignment"),
        (33, 36, "incense of obsession"),
        (37, 40, "mace of blood"),
        (41, 44, "medallion of thought projection"),
        (45, 48, "necklace of strangulation"),
        (49, 52, "net of snaring"),
        (53, 56, "periapt of foul rotting"),
        (57, 60, "potion of poison"),
        (61, 64, "robe of powerlessness"),
        (65, 68, "robe of vermin"),
        (69, 72, "ring of clumsiness"),
        (73, 76, "scarab of death"),
        (77, 80, "cursed backbiter spear"),
        (81, 84, "stone of weight"),
        (85, 88, "-2 cursed sword"),
        (89, 92, "berserking sword"),
        (93, 96, "vacuous grimoire"),
        (97, 100, "zane's ire")
    ]

    artifacts = [
        (1, 3, "aegis"),
        (4, 5, "andvaranaut"),
        (6, 8, "angurvadal"),
        (9, 10, "book of infinite spells"),
        (11, 13, "caduceus"),
        (14, 15, "carnwennan"),
        (16, 18, "chentu"),
        (19, 20, "cowl of the black fox"),
        (21, 23, "deck of many things"),
        (24, 25, "excalibur"),
        (26, 28, "fail-not bow of tristan"),
        (29, 31, "hammer of thunderbolts"),
        (32, 35, "hand of glory"),
        (36, 37, "jarrod's blade"),
        (38, 40, "kladenets"),
        (41, 42, "lantern of diogenes"),
        (43, 45, "mace of the dove"),
        (46, 47, "mantle of lorenzo"),
        (48, 50, "mjolnir"),
        (51, 53, "moaning diamond"),
        (54, 55, "orbs of dragonkind"),
        (56, 58, "philosopher's stone"),
        (59, 60, "ruji jingu bang"),
        (61, 63, "saint's mace"),
        (64, 65, "shadowstaff"),
        (66, 68, "sharanga"),
        (69, 70, "shield of maccabee"),
        (71, 73, "shield of the sun"),
        (74, 76, "sphere of annihilation"),
        (77, 78, "staff of the magi"),
        (79, 80, "sword of conaire mor"),
        (81, 83, "sword of tarnhelm"),
        (84, 86, "talisman of pure good"),
        (87, 89, "talisman of the sphere"),
        (90, 92, "talisman of pure evil"),
        (93, 94, "tarnhelm"),
        (95, 97, "tome of the unclean"),
        (98, 98, "tyrfing"),
        (99, 99, "uchide no kozuchi"),
        (100, 100, "varunastra")
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
        self.magic_item_tables["armor & shields"] = MagicItemsTable.armor_and_shields
        self.magic_item_tables["miscellaneous magic"] = MagicItemsTable.miscellaneous_magic
        self.magic_item_tables["rings"] = MagicItemsTable.rings
        self.magic_item_tables["rods, staves, wands"] = MagicItemsTable.rods_staves_wands
        self.magic_item_tables["cursed items"] = MagicItemsTable.cursed_items
        self.magic_item_tables["artifacts"] = MagicItemsTable.artifacts

        self.magic_item_tables["swords"] = MagicItemsTable.swords
        self.magic_item_tables["weapon/armor bonus"] = MagicItemsTable.weapon_armor_bonus
        self.magic_item_tables["special swords"] = MagicItemsTable.special_swords
        self.magic_item_tables["miscellaneous weapons"] = MagicItemsTable.miscellaneous_weapons
        self.magic_item_tables["special miscellaneous weapons"] = MagicItemsTable.special_miscellaneous_weapons
        self.magic_item_tables["shield"] = MagicItemsTable.shield
        self.magic_item_tables["random shield type"] = MagicItemsTable.random_shield_type
        self.magic_item_tables["armor"] = MagicItemsTable.armor
        self.magic_item_tables["random armor type"] = MagicItemsTable.random_armor_type
        self.magic_item_tables["miscellaneous a"] = MagicItemsTable.miscellaneous_a
        self.magic_item_tables["miscellaneous b"] = MagicItemsTable.miscellaneous_b
        self.magic_item_tables["miscellaneous c"] = MagicItemsTable.miscellaneous_c
        self.magic_item_tables["miscellaneous d"] = MagicItemsTable.miscellaneous_d
        self.magic_item_tables["miscellaneous e"] = MagicItemsTable.miscellaneous_e

    @staticmethod
    def format_table_results(item, value, experience):
        return item + " (" + value + ", " + experience + " xp)"

    def get_potion(self, index):
        result = self.search_items(index, self.magic_item_tables["potions"])
        return self.format_table_results(result[0], result[1], result[2])

    def get_scroll(self, index):
        result = self.search_items(index, self.magic_item_tables["scrolls"])
        return self.format_table_results(result[0], result[1], result[2])

    def get_weapons_category(self, category_index):
        return self.search_items(category_index, self.magic_item_tables["weapons"])

    def get_sword(self, sword_index, weapon_bonus_index):
        weapon = self.search_items(sword_index, self.magic_item_tables["swords"])
        weapon_bonus = self.search_items(weapon_bonus_index, self.magic_item_tables["weapon/armor bonus"])
        result = weapon_bonus[0] + " " + weapon

        return self.format_table_results(result, weapon_bonus[1], weapon_bonus[2])

    def get_special_sword(self, special_sword_index, sword_index):
        weapon = self.search_items(special_sword_index, self.magic_item_tables["special swords"])
        sword_type = self.search_items(sword_index, self.magic_item_tables["swords"])
        result = weapon[0] + " (" + sword_type + ")"

        return self.format_table_results(result, weapon[1], weapon[2])

    def get_miscellaneous_weapon(self, miscellaneous_weapon_index, weapon_bonus_index):
        weapon = self.search_items(miscellaneous_weapon_index, self.magic_item_tables["miscellaneous weapons"])
        weapon_bonus = self.search_items(weapon_bonus_index, self.magic_item_tables["weapon/armor bonus"])
        result = weapon_bonus[0] + " " + weapon

        return self.format_table_results(result, weapon_bonus[1], weapon_bonus[2])

    def get_special_miscellaneous_weapon(self, special_miscellaneous_weapon_index, weapon_bonus_index, miscellaneous_weapon_index):
        weapon = self.search_items(special_miscellaneous_weapon_index, self.magic_item_tables["special miscellaneous weapons"])
        result = weapon[0]

        if "+" not in weapon[0]: # Need to give it a weapon bonus
            weapon_bonus = self.search_items(weapon_bonus_index, self.magic_item_tables["weapon/armor bonus"])
            result = weapon_bonus[0] + " " + result 

        if "weapon" in weapon[0]: # Need to specify weapon type
            misc_weapon = self.search_items(miscellaneous_weapon_index, self.magic_item_tables["miscellaneous weapons"])
            result = result + " (" + misc_weapon + ")"                    

        return self.format_table_results(result, weapon[1], weapon[2])

    def get_armor_and_shields_category(self, armor_and_shields_index):
        return self.search_items(armor_and_shields_index, self.magic_item_tables["armor & shields"])

    def get_random_shield_type(self, random_shield_type_index):
        shield_type = self.search_items(random_shield_type_index, self.magic_item_tables["random shield type"])
        
        # If we roll random shield type once again, re-roll; additionally, a shield of bashing cannot be a pavis,
        # so re-roll if that occurs
        shield = "random shield type"
        while shield == "random shield type" or (shield == "pavis" and "bashing" in shield_type[0]):
            shield = self.search_items(self.roll_percentile(), self.magic_item_tables["shield"])

        result = shield_type[0] + " (" + shield + ")"

        return self.format_table_results(result, shield_type[1], shield_type[2])

    def get_shield(self, shield_index, armor_bonus_index):
        shield = self.search_items(shield_index, self.magic_item_tables["shield"])
        armor_bonus = self.search_items(armor_bonus_index, self.magic_item_tables["weapon/armor bonus"])
        result = armor_bonus[0] + " " + shield + " shield"

        return self.format_table_results(result, armor_bonus[1], armor_bonus[2])

    def get_random_armor_type(self, random_armor_type_index):
        armor_type = self.search_items(random_armor_type_index, self.magic_item_tables["random armor type"])
        result = armor_type[0]

        if "resistance" in armor_type[0]:
            armor = "random armor type"
            while armor == "random armor type":
                armor = self.search_items(self.roll_percentile(), self.magic_item_tables["armor"])
            
            result = armor + " " + result
        
        return self.format_table_results(result, armor_type[1], armor_type[2])

    def get_armor(self, armor_index, armor_bonus_index):
        armor = self.search_items(armor_index, self.magic_item_tables["armor"])
        armor_bonus = self.search_items(armor_bonus_index, self.magic_item_tables["weapon/armor bonus"])
        result = armor_bonus[0] + " " + armor + " armor"

        return self.format_table_results(result, armor_bonus[1], armor_bonus[2])

    def get_miscellaneous_magic(self, category_index, magic_index):
        category = self.search_items(category_index, self.magic_item_tables["miscellaneous magic"])
        result = self.search_items(magic_index, self.magic_item_tables[category])

        return self.format_table_results(result[0], result[1], result[2])

    def get_ring(self, ring_index):
        result = self.search_items(ring_index, self.magic_item_tables["rings"])

        return self.format_table_results(result[0], result[1], result[2])

    def get_rod_stave_wand(self, rod_stave_wand_index):
        result = self.search_items(rod_stave_wand_index, self.magic_item_tables["rods, staves, wands"])

        return self.format_table_results(result[0], result[1], result[2])

    def get_cursed_item(self, cursed_item_index):
        result = self.search_items(cursed_item_index, self.magic_item_tables["cursed items"])

        return self.format_table_results(result, "0 gp", "0")

    def get_artifact(self, artifact_index):
        result = self.search_items(artifact_index, self.magic_item_tables["artifacts"])

        return self.format_table_results(result, "priceless", "20000")

    def roll(self):
        # Initialize return variables to their default values
        magic_item = "not found"

        magic_item_tier = self.search_items(self.roll_percentile(), self.table)

        if magic_item_tier == "potions":
            magic_item = self.get_potion(self.roll_percentile())

        elif magic_item_tier == "scrolls":
            magic_item = self.get_scroll(self.roll_percentile())

        elif magic_item_tier == "weapons":
            result = self.get_weapons_category(self.roll_percentile())
            if result == "swords":
                magic_item = self.get_sword(self.roll_percentile(), self.roll_percentile())

            elif result == "special swords":
                magic_item = self.get_special_sword(self.roll_percentile(), self.roll_percentile())

            elif result == "miscellaneous weapons":
                magic_item = self.get_miscellaneous_weapon(self.roll_percentile(), self.roll_percentile())

            elif result == "special miscellaneous weapons":
                magic_item = self.get_special_miscellaneous_weapon(self.roll_percentile(), self.roll_percentile(), self.roll_percentile())

        elif magic_item_tier == "armor & shields":
            result = self.get_armor_and_shields_category(self.roll_percentile())
            if result == "shield":
                magic_item = self.search_items(self.roll_percentile(), self.magic_item_tables["shield"])

                if magic_item == "random shield type":
                    magic_item = self.get_random_shield_type(self.roll_percentile())
                else:
                    magic_item = self.get_shield(self.roll_percentile(), self.roll_percentile())

            elif result == "armor":
                magic_item = self.search_items(self.roll_percentile(), self.magic_item_tables["armor"])

                if magic_item == "random armor type":
                    self.get_random_armor_type(self.roll_percentile())
                else:
                    self.get_armor(self.roll_percentile(), self.roll_percentile())

        elif magic_item_tier == "miscellaneous magic":
            magic_item = self.get_miscellaneous_magic(self.roll_percentile(), self.roll_percentile())

        elif magic_item_tier == "rings":
            magic_item = self.get_ring(self.roll_percentile())

        elif magic_item_tier == "rods, staves, wands":
            magic_item = self.get_rod_stave_wand(self.roll_percentile())

        elif magic_item_tier == "cursed items":
            magic_item = self.get_cursed_item(self.roll_percentile())

        elif magic_item_tier == "artifacts":
            magic_item = self.get_artifact(self.roll_percentile())

        return magic_item