from random import random
from math import log
import numpy as np
from scipy.stats import kstest

def exponencial(lamda: float):
    """
    Genera el valor de una exponencial con paramtro lamda
    """
    U = 1 - random()
    return -log(1-U) / lamda

# Generar 30 v.a exponenciales con media 1
# lambda = 1/media = 1/1 = 1

exp_30 = [exponencial(1) for _ in range(30)]

# calcular el estadístico (son datos continuos --> kolmogorov)
datos = exp_30
def kolmogorov_smirnov_stat(datos):
    stat, p_valor = kstest(datos, 'expon', args=(0, 1))
    print("Estadístico KS:", stat)
    print("p-valor:", p_valor)
    return p_valor

kolmogorov_smirnov_stat(datos)  # usarlo para chequear los resultados

# Calcular el estadístico
def estadisticoD_ks(muestra, f):
    muestra.sort()                      # ordenar los datos de menor a mayor
    D = 0
    n = len(muestra)
    for i in range(1, n+1):  # recorrer la muestra ordenada
        Fi = f(muestra[i-1])
        D = max(D, i/n - Fi, Fi - (i-1)/n)
    return D

# Definir la función F
def funcion_dist(x):
    return (1 - np.exp(-x/1))

D = estadisticoD_ks(datos, funcion_dist)

print("Valor del estadístico D:", D)

# el p-valor se calcula por simulación pq sino es más complicado

np.random.seed(32)

n = len(datos)  # tamaño de la muestra

def p_valor_km_sim(Nsim, n, D):
    pvalor = 0
    for _ in range(Nsim):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        d_sim = estadisticoD_ks(uniformes, (lambda x: x)) # aca es siempre uniforme
        if d_sim >= D:
            pvalor += 1
    return pvalor/Nsim

Nsim = 1000
print("El p-valor mediante simulación es:", p_valor_km_sim(Nsim, n, D))