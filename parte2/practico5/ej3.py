from random import random
from math import log
from simular import simulate

# X es una lista de funciones generadoras (como generarX_TI_Weibull, etc.)
# P es una lista de probabilidades que en total deben sumar 1

def met_comp(X, P):
    # Construimos la distribución acumulada F
    F = []
    acumulado = 0
    for p in P:
        acumulado += p
        F.append(round(acumulado, 2))

    # Generamos un U ~ U(0,1)
    U = random()

    # Buscamos el índice i tal que U < F[i]
    i = 0
    while U >= F[i]:
        i += 1

    # Llamamos a la función correspondiente
    return X[i]()

def gen_exp(l):
    U = random()
    return -log(1 - U) / l

def esperanza(nsim=10000):
    suma = 0
    P = [0.5, 0.3, 0.2]
    for _ in range(nsim):
        # Usamos lambdas para que X sea una lista de funciones generadoras
        # para que se genere un valor distinto en cada simulación
        X = [lambda: gen_exp(1/3), lambda: gen_exp(1/5), lambda: gen_exp(1/7)]
        suma += met_comp(X, P)
    return suma / nsim

print(f"E[X] estimado con 10000 simulaciones = {esperanza()}")