from random import random
from time import time

def generarX_TI(n):
    U = random()
    return (U**(1/n))

def generarX_maxU(n):
    unif = []
    for _ in range(n):      # genera n valores (desde 0 a n-1)
        U = random()
        unif.append(U)
    return max(unif)

"""
forma equivalente pero más corta:
def generarX_maxU(n):
    return max([random() for _ in range(n)])
"""

def generarX_AyR(n):
    while True:
        Y = random()
        U = random()
        if U < (Y ** (n-1)):
            return Y
        
# hago algún cálculo para luego comparar los tiempos
def esperanza(fun, n, nsim):
    suma = 0
    for _ in range(nsim):
        suma += fun(n)
    return suma / nsim


n = 10
nsim = 10000

print("Simulación con TI:")
start_TI = time()
esp_TI = esperanza(generarX_TI, n, 10000)
final_time_TI = time() - start_TI
print("Tiempo:" , final_time_TI)
print("Esperanza:" , esp_TI)

print("Simulación con prod_max:")
start_prod = time()
esp_prod = esperanza(generarX_maxU, n, 10000)
final_time_prod = time() - start_prod
print("Tiempo:" , final_time_prod)
print("Esperanza:" , esp_prod)

print("Simulación con AyR:")
start_AyR = time()
esp_AyR = esperanza(generarX_AyR, n, 10000)
final_time_AyR = time() - start_AyR
print("Tiempo:" , final_time_AyR)
print("Esperanza:" , esp_AyR)