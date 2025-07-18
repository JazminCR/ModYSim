from math import factorial
from random import random
from random import randint

def dist_prob(l, i, k):
    n = l**i / factorial(i)
    d = 0
    for j in range(k+1):
        d += l**j / factorial(j)
    return n/d

def TI(l, k):
    U = random()
    i = 0           # pq i inicia en 0
    p = dist_prob(l, i, k)
    F = p
    while U >= F:
        i += 1
        p = dist_prob(l, i, k)
        F += p
    return i

def AyR(l, k, c):
    y = randint(0, k)   # y v.a uniforme en (0, k) pq cumple el soporte
    prob_y = 1 / (k + 1)  # por ser uniforme
    u = random()
    prob_x = dist_prob(l, y, k)
    if u < prob_x / (c * prob_y):
        return y
    else:
        return AyR(l, k, c)

def c_AyR(l, k):
    prob_y = 1 / (k + 1)
    results = []
    for i in range(k + 1):
        results.append(dist_prob(l, i, k) / prob_y)
    return max(results)

# estimar P(X > 2) con k = 10, l = 0.7, rep 1000
k = 10
l = 0.7
nsim = 1000

# estimar TI
def prob_mayor2_TI(l, k, nsim):
    cont = 0
    for _ in range(nsim):
        res = TI(l, k)
        if res > 2:
            cont += 1
    return cont / nsim

est_TI = prob_mayor2_TI(l, k, nsim)
print("P(X>2) con TI" , est_TI)

# estimar AyR
def prob_mayor2_AyR(l, k, nsim, c):
    cont = 0
    for _ in range(nsim):
        res = AyR(l, k, c)
        if res > 2:
            cont += 1
    return cont / nsim

c = c_AyR(l, k)
est_AyR = prob_mayor2_AyR(l, k, nsim, c)
print("P(X>2) con AyR" , est_AyR)

"""
para reutilizar la función:
def prob_mayor2(f, nsim, **kwargs):
    cont = 0
    for _ in range(nsim):
        res = f(**kwargs)
        if res > 2:
            cont += 1
    return cont / nsim

# Para TI
est_TI = prob_mayor2(TI, nsim, l=l, k=k)
print("P(X>2) con TI:", est_TI)

# Para AyR
c = c_AyR(l, k)
est_AyR = prob_mayor2(AyR, nsim, l=l, k=k, c=c)
print("P(X>2) con AyR:", est_AyR)

"""

# calcular el valor exacto de la probabilidad 
def exact_prob(l, k):
    prob = 0
    for i in range(3, k+1):
        prob += dist_prob(l, i, k)
    return prob

print("exacta:" , exact_prob(l, k))

"""
comentado porque lo hizo el chat
# punto c
def AyR_truncada(a, b, p, c):
    while True:
        y = randint(a, b)
        u = random()
        q_y = 1 / (b - a + 1)
        if u < p(y) / (c * q_y):
            return y

def c_AyR_truncada(a, b, p):
    q = 1 / (b - a + 1)
    return max([p(i) / q for i in range(a, b + 1)])
"""