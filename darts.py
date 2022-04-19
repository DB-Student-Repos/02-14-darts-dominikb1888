from math import sqrt
from collections import OrderedDict


def score(x, y, circles):
    """Calculates score for location of dart on dartboard"""
    r = sqrt(x**2 + y**2)
    return {
        (r == 0): 10,
        (0 < r <= 10): calc_score(r, circles),
        (r > 10): 0,
    }.get(True)


def calc_score(r, circles):
    # Potential change of the api to get upper bound from data or to ask for additional variable with
    scoring = create_score_dict(circles)
    scrlist = list(scoring.keys())
    for i in range(len(scrlist) - 1):
        if scrlist[i] < r <= scrlist[i + 1]:
            return scoring[scrlist[i]]


def create_score_dict(circles):
    circles = sorted(circles)
    if circles[0] != 0:
        circles.insert(0, 0)
    if circles[-1] != 10:
        circles.append(10)
    return OrderedDict(zip(circles, list(reversed(circles))))
