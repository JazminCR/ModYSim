from random import random
from math import tan, pi, cos, exp

def g(x):  # Función a integrar, por ejemplo exp(-x^2)
    return exp(-x**2)

def h(u):  # Cambio de variable con diferencial
    # x = tan(pi * (u - 0.5)) transforma u in [0,1] a x in (-inf, inf)
    x = tan(pi * (u - 0.5))
    # Derivada del cambio de variable: dx/du = pi * sec^2(pi*(u - 0.5))
    return g(x) * pi / (cos(pi * (u - 0.5)))**2

def MonteCarlo(h, Nsim):
    suma = 0
    for _ in range(Nsim):
        u = random()
        suma += h(u)
    return suma / Nsim

# Prueba para diferentes valores de N
for N in [1000, 5000, 10000]:
    estimado = MonteCarlo(h, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")

