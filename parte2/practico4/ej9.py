from random import random
from math import log

def geom_TI(p):
    U = random()
    return int(log(1-U) / log(1-p)) + 1

def geom_TI_recursiva(p):
    U = random()
    i = 1
    pi = p
    F = pi
    while U >= F:
        pi = (1 - p) * pi   # formula recursiva
        F += pi
        i += 1
    return i

def geom_ens(p):
    i = 1
    while True:
        U = random()
        if U < p:
            return i
        i += 1

# ej: p = 0.3
# U = 0.5 , U = 0.6 , U = 0.2 --> i = 3

def promedio_geom(fun, p, nsim=10000):
    suma = 0
    for _ in range(nsim):
        suma += fun(p)
    return suma / nsim

res = promedio_geom(geom_ens, 0.2, 10000)
print(res)