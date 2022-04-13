from math import sqrt


def score(x, y, circles):
    """Calculates score for location of dart on dartboard"""
    r = sqrt(x**2 + y**2)
    scoring = dict(zip(circles, list(reversed(circles))))
    return calc_score(r, scoring)


def calc_score(r, scoring):
    # Potential change of the api to get upper bound from data or to ask for additional variable with
    if r in range(10):
        scr = list(scoring.keys())
        if scr[0] != 0:
            scr.insert(0, 0)
        if scr[-1] != 10:
            scr.append(10)
        for i in range(len(scr) - 1):
            if int(r) in range(scr[i], scr[i + 1]):
                return scoring[scr[i + 1]]
    return 0
