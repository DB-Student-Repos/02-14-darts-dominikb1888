from math import sqrt
def score(a,b):
    c = sqrt(a**2 + b**2)

    result = 0
    print(result, "A")

    if c <= 1:
        result = 10
        print(result, "B")

    if c <= 5:
        result = 5
        print(result, "C")

    if c < 10:
        result = 1
        print(result, "D")


    print(result, "E")
    return result
