from random import random
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)

def g(u):
    return ( u / ((u**2)-1) )

def MonteCarlo(g, a, b, Nsim):
    integral = 0
    for _ in range (Nsim):
        integral += g(a + (b-a) * random())
    return integral * (b-a) / Nsim


for N in [1000, 5000, 10000]:
    estimado = MonteCarlo(g, 2, 3, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")
