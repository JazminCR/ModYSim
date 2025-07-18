from random import random
import math
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)

def g(x): # original
    return 1 / ((x**2)*math.log(x+1))

def MonteCarlo(g, Nsim):
    suma = 0
    for _ in range(Nsim):
        u = random()
        suma += g(1/u) * (1/u**2)
        # suma += h(u) si se define h explicitamente
    return suma / Nsim

for N in [1000, 10000, 100000]:
    estimado = MonteCarlo(g, N)
    # estimado = MonteCarlo(h, N)  si se define h explicitamente
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")