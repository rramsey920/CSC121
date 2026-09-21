import random

moisture = random.randint(22, 25)


def sample():
    global moisture
    moisture = moisture - random.randint(1, 5)
    return moisture