from random import random
from math import log

def gen_Y_exp():
    U = random()
    return -log(1-U)

def gen_X_mezcla():
    Y = gen_Y_exp()
    U = random()
    return U**(1/Y)

"""
solo para probar(calcular media)
sims = [gen_X_mezcla() for _ in range(10000)]
print("Media estimada:", sum(sims) / len(sims))
"""
