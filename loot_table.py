import random

class LootTable:
    def __init__(self):
        self.table = []

    @staticmethod
    def roll_percentile():
        return random.randint(1, 100)

    @staticmethod
    def search_items(i, items):
        for start, end, item in items:
            if start <= i <= end:
                return item
        return None