import random

class LootTable:
    def __init__(self):
        self.table = []

    @staticmethod
    def roll_dice(str_value):
        addition_vals = str_value.split("+")
        multiple_vals = addition_vals[0].split("x")
        vals = multiple_vals[0].split("d")

        if len(vals) == 1:
            return vals[0]

        d_num = int(vals[0])
        d_range = int(vals[1])

        sum = 0
        for i in range(d_num):
            sum += random.randint(1, d_range)

        if len(multiple_vals) > 1:
            sum *= int(multiple_vals[1])
        
        if len(addition_vals) > 1:
            sum += int(addition_vals[1])

        return str(sum)

    @staticmethod
    def roll_percentile():
        return random.randint(1, 100)

    @staticmethod
    def search_items(i, items):
        for start, end, item in items:
            if start <= i <= end:
                if isinstance(item, list):
                    item = random.choice(item) # We've hit a sub-list, so pick one of the items at random
                return item
        return None