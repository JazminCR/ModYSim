from scipy.stats import kstest, chi2
import numpy as np
from scipy.integrate import quad

# son datos continuos --> kolmogorov
datos = [0.59, 0.312, 0.665, 0.926, 0.577, 0.505, 0.615, 0.360, 0.899, 0.779, 0.293, 0.962]

# Función para chequear kstest !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def funcion_kstest(x):
    x = np.asarray(x)
    cdf = np.where(x < 0, 0, np.where(x > 1, 1, x**2))
    return cdf

def kolmogorov_smirnov_stat(datos):
    stat, p_valor = kstest(datos, funcion_kstest)
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
# primero definir la función de densidad (2x en [0,1])
def f(x):
    return 2*x if 0 <= x <= 1 else 0

# Función de distribución acumulada F(x) con integración numérica
def funcion_dist(x):
    if x < 0:
        return 0
    elif x > 1:
        return 1
    else:
        integral, _ = quad(f, 0, x)
        return integral


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
        d_sim = estadisticoD_ks(uniformes, (lambda x: x)) # aca es siempre uniforme
        if d_sim >= D:
            pvalor += 1
    return pvalor/Nsim

Nsim = 1000
print("El p-valor mediante simulación es:", p_valor_km_sim(Nsim, n, D))
