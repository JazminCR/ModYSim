from scipy.stats import kstest, norm
import numpy as np
from random import random
from math import log, sqrt

# son datos continuos --> kolmogorov
datos = [1.628, 1.352, 1.8, 1.42, 1.594, 2.132, 1.614, 1.924, 1.692]

# distribución normal con parámetros no especificados
# esimar la media y el desvío

def mean(data):
    return sum(data)/len(data)

def std(data):
    m = mean(data)
    return sqrt(sum((v - m)**2 for v in data)/(len(data)-1))

media_hat = mean(datos)
desvio_hat = std(datos)

def kolmogorov_smirnov_stat(datos):
    stat, p_valor = kstest(datos, 'norm', args=(media_hat, desvio_hat))
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
# la quiero para distintos parámetros
def crear_funcion_dist(mu, sigma):
    def funcion_dist(x):
        return norm.cdf(x, loc= mu, scale= sigma)
    return funcion_dist


D = estadisticoD_ks(datos, crear_funcion_dist(media_hat, desvio_hat))

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

#---------------------------------------------------------------------------------------------------------------------------------------------

def rechazo(nivel, pvalor):
    if pvalor < nivel:
        print(f"La hipótesis nula se rechaza")
    else:
        print(f"La hipótesis nula no se rechaza")

rechazo(0.0004, p_valor_km_sim(Nsim, n, D))

#---------------------------------------------------------------------------------------------------------------------------------------------

# Nos dan una muestra de uniformes

datos_U = [0.23, 0.12, 0.45, 0.67, 0.01, 0.51, 0.38, 0.92, 0.84]

# Pide calcular el estadístico a partir de esos datos

def kolmogorov_smirnov_stat(datos):
    stat, p_valor = kstest(datos, 'norm', args=(media_hat, desvio_hat))
    print("Estadístico KS:", stat)
    print("p-valor:", p_valor)
    return p_valor

kolmogorov_smirnov_stat(datos_U)  # usarlo para chequear los resultados

# Calcular el estadístico
D_U = estadisticoD_ks(datos_U, crear_funcion_dist(media_hat, desvio_hat))

print("Valor del estadístico D a partir de muestra de uniformes:", D_U)

if D_U > D:
    print("El estadístico de la simulación es mayor que el observado.")
else:
    print("El estadístico de la simulación es menor que el observado.")

'''
Un valor D más grande indica mayor discrepancia entre los datos y la distribución teórica (en este caso, la normal).
'''