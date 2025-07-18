from random import random
from math import exp

def g(x, y):
    return (1 - exp(-(x+y)))

def MonteCarlo_cambio_variable(g, Nsim):
    suma = 0
    for _ in range(Nsim):
        u = random()
        v = random()
        suma += g(u, v)
    return suma / Nsim

for N in [1000, 5000, 10000]:
    estimado = MonteCarlo_cambio_variable(g, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")