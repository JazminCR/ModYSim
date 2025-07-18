import numpy as np
from scipy.stats import chi2, binom

n = 564    # sum(Ni)

pi = [1/4, 1/2, 1/4]    # enunciado
Ni = [141, 291, 132]    # enunciado

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
        Ni_sim = simular_Ni(pi, n)
        t = estadisticoT_cc(pi, Ni_sim)
        if t >= T:
            pvalor += 1
    pvalor = pvalor/ Nsim
    return pvalor

Nsim = 1000
pvalor_sim = p_valor_sim(Nsim, n, T)
print("p-valor con simulación:", pvalor_sim)
