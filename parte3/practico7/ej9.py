from scipy.stats import kstest, chi2
import numpy as np
from random import random
from math import log

# son datos continuos --> kolmogorov
datos = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12.0, 16.2, 6.8, 14.7]

# distribución exponencial con parámetro no especificado
# esimar lambda como 1/(media de la muestra) = 1 / x_barra

lambda_hat = 1 / np.mean(datos)

def kolmogorov_smirnov_stat(datos):
    stat, p_valor = kstest(datos, 'expon', args=(0, (1/lambda_hat)))
    print("Estadístico KS:", stat)
    print("p-valor:", p_valor)
    return p_valor

kolmogorov_smirnov_stat(datos)  # usarlo para chequear los resultados

# Calcular el estadístico
def estadisticoD_ks(muestra, f):
    muestra.sort()  # ordenar los datos de menor a mayor
    D = 0
    n = len(muestra)
    for i in range(1, n+1):  # recorrer la muestra ordenada
        Fi = f(muestra[i-1])
        D = max(D, i/n - Fi, Fi - (i-1)/n)
    return D

# Definir la función F usando el parámetro estimado
# la quiero para distintos l
def crear_funcion_dist(l):
    def funcion_dist(x):
        return 1 - np.exp(-x / (1/l))
    return funcion_dist


D = estadisticoD_ks(datos, crear_funcion_dist(lambda_hat))

print("Valor del estadístico D:", D)

# el p-valor se calcula por simulación pq sino es más complicado

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

# Si se necesita hacer una segunda simulación porque el pvalor es cercano al área de rechazo:

# Defino la función de la distribución
def exponencial(lamda: float):
    """
    Genera el valor de una exponencial con paramtro lamda
    """
    U = 1 - random()
    return -log(1-U) / lamda

def p_valor_km_2sim_parnoesp(Nsim, n, D):
    pvalor = 0
    for i in range(Nsim):
        x_gen = [exponencial(lambda_hat) for _ in range(n)]
        x_gen.sort()
        lambda_sim = 1 / np.mean(x_gen)
        d_sim = estadisticoD_ks(x_gen, crear_funcion_dist(lambda_sim))
        if d_sim >= D:
            pvalor += 1
    pvalor = pvalor / Nsim
    return pvalor

print("El p-valor en la segunda simulación es:", p_valor_km_2sim_parnoesp(Nsim, n, D))

