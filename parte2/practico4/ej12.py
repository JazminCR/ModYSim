from random import random
from math import log

def QueDevuelve(p1,p2):
    X = int(log(1 - random()) / log(1 - p1)) + 1    # geom(p1)
    Y = int(log(1 - random()) / log(1 - p2)) + 1    # geom(p2)
    return min(X,Y)

print(QueDevuelve(0.05, 0.2))

# algoritmo que genera lo mismo pero usa un solo random()
def geomMin(p1, p2):
    prod = (1 - p1) * (1 - p2)
    p = 1 - prod
    u = random.random()
    return int(log(1 - u) / log(1 - p)) + 1