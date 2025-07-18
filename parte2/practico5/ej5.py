import numpy as np
import matplotlib.pyplot as plt
from random import random
from math import log

def gen_exp(l):
    U = random()
    return -log(1-U) / l

# Número de variables
n = 10
# Parámetros λ para las distribuciones exponenciales
lambdas = [1, 2, 3]  # 3 distribuciones exponenciales con diferentes λ

# Listas para almacenar los resultados
maximos = []
minimos = []

# Generar 10 valores, cada uno el máximo y el mínimo entre las 3 distribuciones exponenciales
for _ in range(n):
    exp1 = gen_exp(lambdas[0])  # Exponencial con λ=1
    exp2 = gen_exp(lambdas[1])  # Exponencial con λ=2
    exp3 = gen_exp(lambdas[2])  # Exponencial con λ=3
    
    maximo = max(exp1, exp2, exp3)  # Máximo entre los 3 valores
    minimo = min(exp1, exp2, exp3)  # Mínimo entre los 3 valores
    
    maximos.append(maximo)
    minimos.append(minimo)

# Mostrar los resultados
print("Muestra de 10 valores máximos (M):", maximos)
print("Muestra de 10 valores mínimos (m):", minimos)