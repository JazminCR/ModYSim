import numpy as np
from scipy.stats import chi2, binom
from random import random

pi = [0.31, 0.22, 0.12, 0.1, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]    # enunciado
Ni = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2] # enunciado

n = sum(Ni)

# Calcular el estadístico
def estadisticoT_cc(pi, Ni):
    n = sum(Ni)
    T = 0
    for i in range(len(Ni)):
        npi = n*pi[i]
        T += ((Ni[i] - npi)**2) / npi
    return T

T = estadisticoT_cc(pi, Ni)
print(f"El estadístico T es: {T}")

# Calcular el p-valor con la distribución chi cuadrado
pvalor = chi2.sf(T, df=(len(Ni)-1))
print(f"El p-valor con aproximación chi-cuadrada es: {pvalor}")

# Calcular el p-valor mediante simulación

# Primero defino una función para calcular las nuevas frecuencias Ni
# n tamaño de la muestra, pi vector de probabilidades
def simular_Ni(pi, n):
    Ni_s = []
    p = 1
    for i in range(len(pi)):
        x = binom.rvs(n=n, p=pi[i]/p)
        Ni_s.append(x)
        n -= x
        p -= pi[i]
    return Ni_s

def p_valor_sim(Nsim, n, T):
    pvalor = 0
    for i in range(Nsim):
        Ni_sim = list(np.random.multinomial(n, pi))
        # uso la multinomial porque al tener probabilidades muy cercanas a 0 mi función falla
        t = estadisticoT_cc(pi, Ni_sim)
        if t >= T:
            pvalor += 1
    pvalor = pvalor/ Nsim
    return pvalor

Nsim = 1000
pvalor_sim = p_valor_sim(Nsim, n, T)
print("p-valor con simulación:", pvalor_sim)