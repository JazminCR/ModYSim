from random import random

def ejercicio1():
    while True:
        Y = random()
        U = random()
        if U < 15*(Y**2 - 2*Y**3 + Y**4):
            return Y

def valor_esperado(nsims):
    sum_val_obt = 0
    for _ in range(nsims):
        sum_val_obt += ejercicio1()
    return sum_val_obt / nsims

print("--- Ejercicio 1 ---")
print("La estimación del valor esperado de X es:" , valor_esperado(10000))

def codigoX(p):
    U = random()
    i = 10
    pi = p
    F = pi
    while U >= F:
        pi = (1 - p) * pi   # formula recursiva
        F += pi
        i += 1
    return i

def valor_esperado(nsims):
    sum_val_obt = 0
    for _ in range(nsims):
        sum_val_obt += codigoX(0.5)
    return sum_val_obt / nsims

print("--- Ejercicio 2 ---")
print("La estimación de E[X] es:" , valor_esperado(10000))


