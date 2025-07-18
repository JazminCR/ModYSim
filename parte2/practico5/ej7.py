from random import random, uniform
from math import exp
from time import time

def generarX_TI():
    U = random()
    return (exp(U))


def generarX_AyR():
    while True:
        Y = (exp(1) - 1) * random() + 1     # generar uniforme continua
        # Y = uniform(1, exp(1)) otra forma pero no sé si se puede
        U = random()
        if U < (1 / Y):
            return Y
        
def promedio(fun, nsim):
    suma = 0
    for _ in range(nsim):
        suma += fun()
    return suma / nsim

nsim = 10000

print("Simulación con TI:")
start_TI = time()
esp_TI = promedio(generarX_TI, nsim)
final_time_TI_miliseg = (time() - start_TI) * 1000
print("Tiempo en ms:" , final_time_TI_miliseg)
print("Promedio:" , esp_TI)

print("Simulación con AyR:")
start_AyR = time()
esp_AyR = promedio(generarX_AyR, nsim)
final_time_AyR_miliseg = (time() - start_AyR) * 1000
print("Tiempo en ms:" , final_time_AyR_miliseg)
print("Promedio:" , esp_AyR)

def prob_menor_igual(nsim):
    prob = 0
    for _ in range(nsim):
        x = generarX_TI()
        if x <= 2:
            prob += 1
    return prob / nsim

print("P(X <= 2):" , prob_menor_igual(nsim))