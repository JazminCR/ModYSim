from random import random
from time import time
from math import comb

def TI(p, x):
    U = random()
    i = 0
    F = p[0]
    while U >= F:
        i += 1
        F += p[i]
    return x[i]

prob = [0.35, 0.2, 0.2, 0.15, 0.1] # de mayor a menor para optimizar
val_x = [3, 1, 4, 0, 2]
start_TI = time()
for i in range(10000):
    TI(prob, val_x)
final_time_TI = time() - start_TI
print("Tiempo (seg) TI:", final_time_TI)

# para generar la variable Y
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

# para calcular la prob de Y
def prob_binomial(n, p, x):
    c = comb(n, x)  # math.factorial(n) / (math.factorial(x) * math.factorial(n-x))
    return c * (p ** x) * ((1 - p) ** (n - x))

def AyR(c):
    probs_x = [0.15, 0.2, 0.1, 0.35, 0.2] # en el orden dado
    y = binomial_TI(4, 0.45)
    prob_y = prob_binomial(4, 0.45, y)
    u = random()
    if u < probs_x[y] / (c * prob_y):
        return y 
    else:
        return AyR(c)

# calcular el valor de c cuando Y es binomial
def c_ayr():
    probs_x = [0.15, 0.20, 0.10, 0.35, 0.20]
    results = []
    for i in range(5):
        results.append(probs_x[i]/prob_binomial(4, 0.45, i))
    print("El valor de c es:" , max(results))
    return max(results)

c = c_ayr()
start_AyR_min = time()
for i in range(10000):
    AyR(c)
final_time_AyR_min = time() - start_AyR_min
print("Tiempo (seg) AyR con Y bin:" , final_time_AyR_min)
    