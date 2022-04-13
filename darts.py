from math import sqrt


def score(x, y, circles=[1, 5, 10]):
    """Calculates score for location of dart on dartboard"""
    r = sqrt(x**2 + y**2)
    # Zip maps each element in a list to the respective elemnt in the other list
    scoring = dict(zip(circles, list(reversed(circles))))
    return calc_score(r, scoring)


def calc_score(r, scoring):
    if r < 0 or r > 10:
        return 0

    # get the list of keys from our dict
    scr = list(scoring.keys())
    # insert 0 at index 0 in order to also cover the initial test case
    # TODO: Check if 0 is in position 0 only then insert 0
    scr.insert(0, 0)
    # loop through an enumerated list of our extend dict keys to be able to
    # access both the current and the next item in list scr[i] and scr[i+1]
    for i, item in enumerate(scr):
        if i < len(scr) - 1:
            if int(r) in range(scr[i], scr[i + 1]):
                return scoring[scr[i + 1]]
