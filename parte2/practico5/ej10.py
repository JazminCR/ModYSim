from random import random, uniform
from math import sqrt, pi

def cauchy_razon_unif():
    b = 1 / sqrt(pi)
    c = 1 / sqrt(pi)
    while True:
        U = random() * c            # genera un nro entre 0 y c
        V = uniform(-1, 1) * b      # genera un nro entre -b y b
        if U**2 + V**2 < 1 / pi:    # condición de Cf
            return V/U
        
def cauchy_simp():
    while True:
        U = random()           # genera un nro entre 0 y 1
        V = uniform(-1, 1)     # genera un nro entre -1 y 1
        if U**2 + V**2 < 1:    # condición de Cf
            return V/U
    
def cauchy(lamda):
    while True:
        U = random()
        V = uniform(-1, 1)
        if U**2 + V**2 < 1:
            return lamda * V/U

def est_distribucion_cauchy(lam, nsim):
    exitos = 0
    for _ in range(nsim):
        n = cauchy(lam)
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


  

        
