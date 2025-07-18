from random import random
from math import log

# CALCULAR F (no hace falta porque no usamos TI)
# basta con ver que f es un caso particular de una gamma

# mu es el parámetro de la gamma --> la exponencial usa 1/mu
def Erlang_gamma(k, mu):
    U = 1
    for _ in range(k):
        U *= 1 - random()
    return -log(U) / (1/mu)

def Erlang_suma_exp(k, mu):
    suma = 0
    for _ in range(k):
        U = random()
        suma += -log(1 - U)
    return suma / (1/mu)        # equiv a suma * mu

"""
import sympy as sp

x, k, mu = sp.symbols('x k mu', real=True, positive=True)
f = x**(k - 1) * sp.exp(-x / mu)

# Derivar y buscar máximos
f_prime = sp.diff(f, x)
crit_points = sp.solve(f_prime, x)

print("Máximo potencial en x =", crit_points)
"""


