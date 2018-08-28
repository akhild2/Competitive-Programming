import random

def rand7():
    return random.randrange(1, 8)


def rand5():
    while True:
        r = rand7()
        if r < 6:
            return r


def rand5natural():
    return random.randrange(1, 6)