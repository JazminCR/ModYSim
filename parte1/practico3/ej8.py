from random import random
from math import exp

def max_N():
    for N in [100, 1000, 10000, 100000, 1000000]:
        contadores = []
        for _ in range(N):
            mult = 1
            contador = 0
            while mult >= exp(-3):
                mult *= random()
                contador += 1
            contadores.append(contador-1)
            # el ciclo se rompe justo cuando el producto baja del umbral exp(-3)

        estimacion_esp = sum(contadores) / N # calcula la esperanza
        print(f"para {N} experimentos mi aprox es {estimacion_esp}")

max_N()


# quiero una función que me devuelva solo el valor de N
def valores_N():
    mult = 1
    contador = 0
    while mult >= exp(-3):
        mult *= random()
        contador += 1
    return contador - 1

def prob_N_i(i, Nsim):
    return sum(valores_N() == i for _ in range(Nsim)) / Nsim

# Estimar P(N = 3)
for i in range(7):
    print(f"P(N = {i}) ≈ {prob_N_i(i, 1000000)}")
