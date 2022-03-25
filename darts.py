from math import sqrt


def score(x, y):
    r = sqrt(x**2 + y**2)

    if r <= 1:
        return 10
    if 1 < r <= 5:
        return 5
    if 5 < r <= 10:
        return 1
    return 0
