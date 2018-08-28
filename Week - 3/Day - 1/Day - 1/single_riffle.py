def is_single_riffle(half1, half2, shuffled_deck):
    h1 = 0
    h2 = 0
    for card in shuffled_deck:
        if h1 < len(half1) and card == half1[h1]:
            h1 += 1
        elif h2 < len(half2) and card == half2[h2]:
            h2 += 1
        else:
            return False
    return True