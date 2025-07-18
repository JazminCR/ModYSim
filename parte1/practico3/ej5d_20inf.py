from random import random
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)
from math import exp

def g(x): # original
    return exp(-x**2)

def MonteCarlo(g, Nsim):
    suma = 0
    for _ in range(Nsim):
        u = random()
        suma += g(1/u - 1) / u**2
    return (suma / Nsim) * 2   #pq es funcion par y la calculo desde 0 a inf

for N in [1000, 5000, 10000]:
    estimado = MonteCarlo(g, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")

