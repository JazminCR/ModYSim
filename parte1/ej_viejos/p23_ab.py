from random import random
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)

from math import exp

def g(u):
    return ( u / (u - exp(u)))

#def g(u):
#    denominador = u - exp(u)
#    if abs(denominador) < 1e-6:  # umbral de seguridad para evitar divisiones muy grandes
#        return 0  # o podrías usar `continue` en el loop, o ignorar el punto
#    return u / denominador


def MonteCarlo(g, a, b, Nsim):
    integral = 0
    for _ in range (Nsim):
        integral += g(a + (b-a) * random())
    return integral * (b-a) / Nsim


for N in [1000, 5000, 10000]:
    estimado = MonteCarlo(g, -3, 3, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")