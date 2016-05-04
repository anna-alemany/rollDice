import random

class dice(object):
    def __init__(self, sides = 6):
        self.sides = sides
        return

    def roll(self, times = 1):
        k = []
        for i in range(times):
            k.append(random.randint(1, self.sides))
        return k


