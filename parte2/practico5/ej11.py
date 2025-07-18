from random import random
from math import tan, pi

def generar_cauchy_TI(l):     # a > 0
    U = random()
    return l * tan(pi * (U - 0.5))

def est_distribucion_cauchy(lam, nsim):
    exitos = 0
    for _ in range(nsim):
        n = generar_cauchy_TI(lam)
        if -lam <= n <= lam:
            exitos += 1
    return exitos / nsim

nsim = 10000

# Parámetros λ
lambdas = [1, 2.5, 0.3]

# Probabilidad teórica
probabilidad_teorica = 0.5

# Realizar simulaciones y mostrar resultados
for lam in lambdas:
    proporcion_simulada = est_distribucion_cauchy(lam, nsim)
    print(f"λ = {lam}: Proporción simulada = {proporcion_simulada:.4f}, Proporción teórica = {probabilidad_teorica:.4f}")

# e) comparo con ej10