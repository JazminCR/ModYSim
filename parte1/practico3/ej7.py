from random import random
from math import exp

def estimar_N():
# calcula el valor de N
    suma = 0
    n = 0
    while suma <= 1:
        suma += random.uniform(0, 1)
        n += 1
    return n

def simulacion(n_simulaciones):
# realiza n_simulaciones para calcular el valor de N
    resultados = []
    for _ in range(n_simulaciones):
        resultados.append(estimar_N())
    return sum(resultados) / len(resultados)

n_values = [100, 1000, 10000, 100000, 1000000]
for n in n_values:
    estimado = simulacion(n)
    print(f"Para n = {n}, E[N] estimado ≈ {estimado:.5f}")

# otra forma (profe):

#for N in [100, 1000, 10000, 100000, 1000000]:
#    contadores = []
#    for _ in range(N):
#        suma = 0
#        contador = 0
#        while suma <= 1:
#            suma += random()
#            contador += 1
#        contadores.append(contador)
#
#    estimacion_esp = sum(contadores) / N
#    print(f"para {N} experimentos mi aprox es {estimacion_esp}")

from math import exp
print(f"e = {exp(1)}")
