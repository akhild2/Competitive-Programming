import random


def rand5():
    return random.randrange(1, 6)


def rand7():
    while True:
        r1 = 5 * (rand5() - 1)
        r2 = rand5()
        r = r1 + r2
        if r <= 21:
            return r % 7 + 1
