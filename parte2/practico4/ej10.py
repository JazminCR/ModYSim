from random import random

def dist_prob(j):
    t = 0.5 ** (j + 1)
    n = 0.5 * (2 ** (j - 1))
    d = 3 ** j
    return t + n/d

# para generar X uso la TI
def TI():
    U = random()
    j = 1           # pq j inicia en 1
    p = dist_prob(j)
    F = p
    while U >= F:
        j += 1
        p = dist_prob(j)
        F += p
    return j

# calcular la esperanza
def esperanza(nsim):
    res = 0
    suma = 0
    for _ in range(nsim):
        res = TI()
        suma += res
    return suma / nsim

print("E(X) con 1000 rep:" , esperanza(1000))

"""
esta parte es en papel

# no se deberia usar nsim si es un calculo exactp      
def esp_exacta(nsim):
    j = 1
    sum = 0
    for _ in range(nsim):
        sum += j * dist_prob(j)
        j += 1
    return sum

# tampoco debería haber error si es exacto
def esp_exacta_tol():
    sum = 0
    j = 1
    while True:
        prob = dist_prob(j)
        sum += j * prob
        # Si la probabilidad es muy pequeña (por ejemplo, menor a 1e-6), podemos detenernos
        if prob < 1e-6:  # Esta tolerancia se puede ajustar si es necesario
            break
        j += 1
    return sum

# Cálculo de la esperanza exacta
print("E(X) exacta con 1000 rep:" , esp_exacta(30))

print("E(X) exacta:", esp_exacta_tol())
"""