from random import random
# random() genera un nro aleatorio entre 0 y 1, o sea U ~ U(0, 1)

def g(u):
    return (1-u**2)**1.5

def MonteCarlo(g, Nsim):
    integral = 0
    for _ in range (Nsim):
        integral += g(random())
    return integral / Nsim


for N in [1000, 5000, 10000]:
    estimado = MonteCarlo(g, N)
    print(f"N = {N}, valor estimado ≈ {estimado:.10f}")

