import math
import random
from scipy.stats import kstest
import numpy as np

random.seed(123456789)

# Generación de nros aleatorios con distribución t-student
def rt(df):
    x = random.gauss(0.0 , 1.0)
    y = 2.0 * random.gammavariate(0.5*df, 2.0)
    return x / (math.sqrt(y/df))

# H0) Las muestras provienen de una distribución Normal(0,1)

# son datos continuos --> kolmogorov
def kolmogorov_smirnov_stat(datos):
    stat, p_valor = kstest(datos, 'norm')
    print("Estadístico KS:", stat)
    print("p-valor:", p_valor)
    return p_valor

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
    return math.erf(x/math.sqrt(2))/2 + 0.5

# el p-valor se calcula por simulación pq sino es más complicado

def p_valor_km_sim(Nsim, n, D):
    pvalor = 0
    for _ in range(Nsim):
        uniformes = np.random.uniform(0, 1, n)
        uniformes.sort()
        d_sim = estadisticoD_ks(uniformes, (lambda x: x)) # aca es siempre uniforme
        if d_sim >= D:
            pvalor += 1
    return pvalor/Nsim

# Parámetros
Nsim = 10000
n_list = [10, 20, 100, 1000]

print(" n | Estadístico D | p-valor simulado ")
print("--------------------------------------")

for n in n_list:
    datos = [rt(11) for _ in range(n)]  # generar muestra t-student con df=11
    D = estadisticoD_ks(datos, funcion_dist)
    p_val = p_valor_km_sim(Nsim, n, D)
    print(f"{n:3d} | {D:.5f}        | {p_val:.5f}")