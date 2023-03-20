import random


def roll(num, size, mod):
    rolled = mod
    for i in range(num):
        rolled += random.randint(1, size)
    return rolled

