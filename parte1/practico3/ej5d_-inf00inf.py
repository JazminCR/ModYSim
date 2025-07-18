from random import random
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)
from math import exp

def g(x): # original
    return exp(-x**2)

# Cambio para (0, ∞)
def h1(u):
    x = 1/u - 1
    return g(x) / u**2

# Cambio para (-∞, 0)
def h2(u):
    x = -1/u + 1
    return g(x) / u**2

def MonteCarlo(h, Nsim):
    return sum(h(random()) for _ in range(Nsim)) / Nsim

for N in [1000, 5000, 10000]:
    I1 = MonteCarlo(h1, N)  # de 0 a ∞
    I2 = MonteCarlo(h2, N)  # de -∞ a 0
    estimado = I1 + I2
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")
