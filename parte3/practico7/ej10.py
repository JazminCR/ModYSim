from scipy.stats import kstest, norm
import numpy as np
from random import random
from math import log, sqrt

# son datos continuos --> kolmogorov
datos = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]

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

# Si se necesita hacer una segunda simulación porque el pvalor es cercano al área de rechazo:

def p_valor_km_2sim_parnoesp(Nsim, n, D):
    pvalor = 0
    for i in range(Nsim):
        x_gen = list(norm.rvs(loc=media_hat, scale=desvio_hat, size=n))
        x_gen.sort()
        media_sim = mean(x_gen)
        desvio_sim = std(x_gen)
        d_sim = estadisticoD_ks(x_gen, crear_funcion_dist(media_sim, desvio_sim))
        if d_sim >= D:
            pvalor += 1
    pvalor = pvalor / Nsim
    return pvalor

print("El p-valor en la segunda simulación es:", p_valor_km_2sim_parnoesp(Nsim, n, D))

