from random import random
from random import uniform
from math import sqrt

def monte_carlo(N):
    integral = 0
    for _ in range (N):
        u = random()
        g = sqrt(1+6*u + sqrt(1+6*u))
        integral += g
    return integral * (7-1) / N

print("Ejercicio 1")
for n in [1000, 10000, 100000]:
    estimado = monte_carlo(n)
    print(f"N = {n}, valor estimado ≈ {estimado:.6f}")


def juego():
    suma = 0
    contador = 0
    while (suma < 1):
        u = uniform(0, 1)
        contador += 1
        suma += u
    return contador

def pares(N):
    suma = 0
    for i in range(N):
        suma += (juego() % 2 != 0)
    return suma / N

print("Ejercicio 2")
for n in [100, 1000, 10000]:
    estimado = pares(n)
    print(f"N = {n}, probabilidad #sumandos sea impar ≈ {estimado:.6f}")
    