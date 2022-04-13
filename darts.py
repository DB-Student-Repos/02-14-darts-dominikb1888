from math import sqrt

# scores = [1,3,5,7]
def score(x, y, circles=[1, 5, 10]):
    """Calculates score for location of dart on dartboard"""
    r = sqrt(x**2 + y**2)
    # r = 5
    return calc_score(r)

def calc_score(r, circles):
    # TODO: dynamically generate a dict from a list and its reversed 
    scoring = {
       1: 10,
       5: 5,
       10: 1,
    }

    if r < 0 or r > 10
        return 0

    # get the list of keys from our dict
    scr = list(scoring.keys())
    # insert 0 at index 0 in order to also cover the initial test case
    scr.insert(0, 0)
    # loop through an enumerated list of our extend dict keys to be able to
    # access both the current and the next item in list scr[i] and scr[i+1]
    for i, item in enumerate(scr):
        if i < len(scr) - 1:
            if int(r) in range(scr[i], scr[i + 1]):
                print(scoring[scr[i + 1]])    
                return scoring[scr[i + 1]] 


    # if 0 <= r <= 1:
    #     return 10
    # if 1 < r <= 5:
    #     return 5
    # if 5 < r <= 10:
    #     return 1


# scoring = {
#      1: 10,
#      5: 5,
#      10: 1,
#  }

# scoring = {
#     1:7,
#     3:3,
#     7:1,
# }

#  scoring.keys() 
#  [1,5,10]
#  [1,3,7]

# Dynamically generate these test cases:
# 0-1
# 1-5
# 5-10
