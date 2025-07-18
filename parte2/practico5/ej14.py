from random import random
from math import log

def eventos_poisson_nohom(fun_lambda_t, lam, T):
    t = -log(1 - random())/ lam
    eventos = []
    while t <= T:
        U = random()
        if U <= fun_lambda_t(t) / lam:
            eventos.append(t)
        t += -log(1 - random()) / lam
    return eventos, len(eventos)

# el valor de lam debe ser >= max de lambda(t)
# T depende de hasta que t está definida la fun

def fun1(t):
    return 3 + 4 / (t+1)

T1 = 3
lam1 = 7
print("Ej 14 i:" , eventos_poisson_nohom(fun1, lam1, T1))

def fun2(t):
    return (t-2)**2 - 5*t + 17

T2 = 5
lam2 = 21
print("Ej 14 ii:" , eventos_poisson_nohom(fun2, lam2, T2))

def fun3(t):
    if 2 <= t <= 3:
        return t / 2 - 1
    elif 3 < t <= 6:
        return 1 - t / 6
    else:
        return 0

T3 = 6   # porque la función se define hasta ese tiempo, no importa antes
lam3 = 1
print("Ej 14 ii:" , eventos_poisson_nohom(fun3, lam3, T3))