from numpy import mean
from scipy.stats import chi2, binom
from random import random
import math

muestra = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
n = len(muestra)

# distribución binomial(n_b=8, p)

# no se conoce p por lo que hay que estimarlo
# la estimación de p está dada por (media de la muestra = X_barra) / n_b
n_b = 8
p_hat = mean(muestra) / n_b

# Calcular pi
def prob_binomial(x, n, p):
    c = math.factorial(n) / (math.factorial(x) * math.factorial(n-x))
    pp = p ** x
    np = (1 - p) ** (n - x)
    return (c * pp * np)

pi = [prob_binomial(i, n_b, p_hat) for i in range(n_b + 1)]

'''
Otra forma de calcular pi 
pi = [binom.pmf(i, n_b, p_hat) for i in range(n_b + 1)]
'''

# Calcular Ni
def frecuencias_discretas(muestra):
    N = [0 for i in range(max(muestra)+1)]
    for i in muestra:
        N[i] += 1
    return N

Ni = frecuencias_discretas(muestra)

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
pvalor = chi2.sf(T, df=(len(Ni)-1-1))   # acá se resta la cantidad de parámetros no especificados !!!
print(f"El p-valor con aproximación chi-cuadrada es: {pvalor:.7f}")

# Calcular el p-valor mediante simulación

# En cada simulación:
# generar n datos a partir de la distribución F con el parámetro estimado p_hat
# volver a estimar el parámetro (o los) no especificado --> par_sim
# volver a calcular las frecuencias Ni --> Ni_sim
# ahora par_sim define una nueva F --> F_sim
# calcular las probabilidades pi_sim
# calcular el estadístico con las prob pi_sim

# Definir la distribución para poder generar variables
def binomial(n_b, p):
    """
    Genera el valor de una binomial con probabilidad p y n ensayos
    """
    c = p / (1 - p)
    prob = (1 - p) ** n_b
    F = prob
    i = 0
    U = random()
    while U >= F:
        prob *= c * (n_b - i) / (i + 1)
        F += prob
        i += 1
    return i

def p_valor_sim(Nsim, n, T):
    pvalor = 0
    for i in range(Nsim):
        x_gen = [binomial(n_b, p_hat) for _ in range(n)]    # muestra de tamaño n
        p_sim = mean(x_gen) / n_b
        pi_sim = [prob_binomial(i, n_b, p_sim) for i in range(n_b + 1)]
        Ni_sim = frecuencias_discretas(x_gen)
        t = estadisticoT_cc(pi_sim, Ni_sim)
        if t >= T:
            pvalor += 1
    pvalor = pvalor/ Nsim
    return pvalor

Nsim = 1000
pvalor_sim = p_valor_sim(Nsim, n, T)
print("p-valor con simulación:", pvalor_sim)