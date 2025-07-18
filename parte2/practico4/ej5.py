from random import random
from time import time
from math import comb

def binomial_TI(n, p):
    c = p / (1-p)
    prob = (1-p)**n
    F = prob
    i = 0
    U = random()
    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i += 1
    return i

def binomial_TI_mej(n, p):
    if p > 1/2:
        i = binomial_TI(n, 1 - p)
        return n - i
    else:
        return binomial_TI(n, p)
    
def bin_ensayos(n, p):
    exitos = 0
    for i in range(n):
        U = random()
        if U <= p:
            exitos += 1
    return exitos

n = 10
p = 0.3

start_bin_TI = time()
for i in range(10000):
    binomial_TI(n, p)
final_time_bin_TI = time() - start_bin_TI
print("TI:" , final_time_bin_TI)

start_bin_TI_mej = time()
for i in range(10000):
    binomial_TI_mej(n, p)
final_time_bin_TI_mej = time() - start_bin_TI_mej
print("TI mejorada:" , final_time_bin_TI_mej)

start_bin_TI_ensayos = time()
for i in range(10000):
    bin_ensayos(n, p)
final_time_bin_ensayos = time() - start_bin_TI_ensayos
print("Ensayos:" , final_time_bin_ensayos)

# parte b
cont_TI = [0 for _ in range(n+1)] #lista de 0´s con indice desde 0 hasta 10
cont_TI_mej = [0 for _ in range(n+1)]
cont_ens = [0 for _ in range(n+1)]

# --- Simular e ir guardando ocurrencias
nsim = 10000
for i in range(nsim):
    res = binomial_TI(n, p)
    cont_TI[res] += 1

for i in range(nsim):
    res = binomial_TI_mej(n, p)
    cont_TI_mej[res] += 1

for i in range(nsim):
    res = bin_ensayos(n, p)
    cont_ens[res] += 1

# --- Estimar valor con mayor ocurrencia ---
valor_moda_TI = cont_TI.index(max(cont_TI))
valor_moda_TI_mej = cont_TI_mej.index(max(cont_TI_mej))
valor_moda_ens = cont_ens.index(max(cont_ens))

# --- Estimar proporción de valores 0 y 10 ---
prop0_TI = cont_TI[0] / nsim
prop10_TI = cont_TI[10] / nsim

prop0_TI_mej = cont_TI_mej[0] / nsim
prop10_TI_mej = cont_TI_mej[10] / nsim

prop0_ens = cont_ens[0] / nsim
prop10_ens = cont_ens[10] / nsim

print(f"Valor con mayor ocurrencia TI (moda estimada): {valor_moda_TI}")
print(f"Proporción de veces que salió 0 TI: {prop0_TI:.10f}")
print(f"Proporción de veces que salió 10 TI: {prop10_TI:.10f}")

print(f"Valor con mayor ocurrencia TI mej (moda estimada): {valor_moda_TI_mej}")
print(f"Proporción de veces que salió 0 TI mej: {prop0_TI_mej:.10f}")
print(f"Proporción de veces que salió 10 TI mej: {prop10_TI_mej:.10f}")

print(f"Valor con mayor ocurrencia ensayos (moda estimada): {valor_moda_ens}")
print(f"Proporción de veces que salió 0 ensayos: {prop0_ens:.10f}")
print(f"Proporción de veces que salió 10 ensayos: {prop10_ens:.10f}")

# parte c
def prob_binomial(n, p, x):
    c = comb(n, x)  # math.factorial(n) / (math.factorial(x) * math.factorial(n-x))
    return c * (p ** x) * ((1 - p) ** (n - x))

probs_teoricas = [prob_binomial(n, p, x) for x in range(n + 1)]
# print("Prob teoricas:", probs_teoricas) si se quiere una lista con todas las probs

print("\nProbabilidades teóricas:")
for x in range(n + 1):
    print(f"P(X={x}) = {probs_teoricas[x]:.4f}")

print(f"\nProbabilidad teórica de X=0: {probs_teoricas[0]:.4f}")
print(f"Probabilidad teórica de X=10: {probs_teoricas[10]:.4f}")

