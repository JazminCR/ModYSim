from random import random, uniform
from math import sqrt
from time import time

def suma_unif():
    U = random()
    V = random()
    return U + V

def genX_TI():
    U = random()
    if U < 0.5:
        return sqrt(2*U)
    else:
        return 2 - sqrt(2 - 2*U)
    
def genX_AyR():
    while True:
        Y = uniform(0, 2) # generar uniforme continua
        U = random()
        if Y < 1:
            if U < Y:
                return Y
        elif Y >= 1:
            if U < 2 - Y:
                return Y

def promedio(fun, nsim):
    suma = 0
    for _ in range(nsim):
        suma += fun()
    return suma / nsim

nsim = 10000

print("Simulación con suma de uniformes:")
start_sum = time()
esp_sum = promedio(suma_unif, nsim)
final_time_sum_miliseg = (time() - start_sum) * 1000
print("Tiempo en ms:" , final_time_sum_miliseg)
print("Promedio:" , esp_sum)

print("Simulación con TI:")
start_TI = time()
esp_TI = promedio(genX_TI, nsim)
final_time_TI_miliseg = (time() - start_TI) * 1000
print("Tiempo en ms:" , final_time_TI_miliseg)
print("Promedio:" , esp_TI)

print("Simulación con AyR:")
start_AyR = time()
esp_AyR = promedio(genX_AyR, nsim)
final_time_AyR_miliseg = (time() - start_AyR) * 1000
print("Tiempo en ms:" , final_time_AyR_miliseg)
print("Promedio:" , esp_AyR)

def prob_mayor_x0(fun, nsim, x0):
    cuenta = 0
    for _ in range(nsim):
        x = fun()
        if x > x0:
            cuenta += 1
    return cuenta / nsim

x0 = 1.5
print("P(X > 1.5) con suma de unif:" , prob_mayor_x0(suma_unif, nsim, x0))
print("P(X > 1.5) con TI:" , prob_mayor_x0(genX_TI, nsim, x0))
print("P(X > 1.5) con AyR:" , prob_mayor_x0(genX_AyR, nsim, x0))
