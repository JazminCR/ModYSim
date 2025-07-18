from random import random
from math import exp
from time import time

def poisson(l):
    U = random()
    i = 0
    p = exp(-l)
    F = p
    while U >= F:
        i += 1
        p *= l / i
        F += p
    return i

def poisson_mej(l):
    p = exp(-l)
    F = p
    for j in range(1, int(l) + 1):
        p *= l / j
        F += p
    U = random()
    if U >= F:
        j = int(l) + 1
        while U >= F:
            p *= l / j
            F += p
            j += 1
        return j - 1
    else:
        j = int(l)
        while U < F:
            F -= p
            p *= j / l
            j -= 1
        return j + 1
    
def prob_mayor(fun, l, x, nsim):
    exito = 0
    for i in range(nsim):
        res = fun(l)
        if res > x:
            exito += 1
    return exito / nsim

start_TI = time()
prob_mayor_2_TI = prob_mayor(poisson, 10, 2, 1000)
final_TI = time() - start_TI
print("P(Y > 2) con TI:" , prob_mayor_2_TI)
print("Tiempo (seg) TI:" , final_TI)

start_TI_mej = time()
prob_mayor_2_TI_mej = prob_mayor(poisson_mej, 10, 2, 1000)
final_TI_mej = time() - start_TI_mej
print("P(Y > 2) con TI mej:" , prob_mayor_2_TI_mej)
print("Tiempo (seg) TI mej:" , final_TI_mej)
