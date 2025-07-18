from scipy.stats import kstest, chi2
import numpy as np

# son datos continuos --> kolmogorov
datos = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]

def kolmogorov_smirnov_stat(datos):
    stat, p_valor = kstest(datos, 'uniform')
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

# Definir la función F
def funcion_dist(x):
    return x

D = estadisticoD_ks(datos, funcion_dist)

print("Valor del estadístico D:", D)

# el p-valor se calcula por simulación pq sino es más complicado

np.random.seed(42)

n = len(datos)  # tamaño de la muestra

def p_valor_km_sim(Nsim, n, D):
    pvalor = 0
    for _ in range(Nsim):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        d_sim = estadisticoD_ks(uniformes, (lambda x: x)) # aca es siempre uniforme, coincide que la F es también uniforme
        if d_sim >= D:
            pvalor += 1
    return pvalor/Nsim

Nsim = 1000
print("El p-valor mediante simulación es:", p_valor_km_sim(Nsim, n, D))

# se podría calcular también con chi cuadrado para datos continuos

bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
Ni, _ = np.histogram(datos, bins=bins)
pi = [0.2] * 5  # U(0,1) ⇒ cada bin debería tener la misma probabilidad

T = sum((Ni[i] - n * pi[i])**2 / (n * pi[i]) for i in range(5))
p_valor = chi2.sf(T, df=4)

print("Estadístico T con chi cuadrado:", T)
print("p-valor de chi cuadrado:", p_valor)
