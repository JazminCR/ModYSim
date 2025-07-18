from random import random
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)
from math import exp

def g(x, y): # original
    return exp((x+y)**2)

def MonteCarlo(g, Nsim):
    suma = 0
    for _ in range(Nsim):
        u = random()
        v = random()
        suma += g(u, v)
    area = 1 * 1    # en este caso no afecta
    # [a,b] x [c,d] --> area = (b - a) * (d - c)

    return area * suma / Nsim

for N in [1000, 5000, 10000]:
    estimado = MonteCarlo(g, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")
