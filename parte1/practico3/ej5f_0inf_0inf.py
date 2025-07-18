from random import random
from math import exp

def I(x, y):
    if y < x:
        return 1
    else:
        return 0

def g(x, y):
    return exp(-(x+y))*I(x, y)

def MonteCarlo_cambio_variable(g, Nsim):
    suma = 0
    for _ in range(Nsim):
        u = random()
        v = random()
        suma += g(1/u - 1, 1/v -1) / ((u**2) * (v**2))
    return suma / Nsim

for N in [1000, 5000, 10000]:
    estimado = MonteCarlo_cambio_variable(g, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")
