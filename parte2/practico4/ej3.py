from random import random
from math import sqrt

def udiscreta(n):
  U = random()
  return int(n * U) + 1

def suma_dos_dados():
  """
  Simulates rolling two fair 6-sided dice and returns their sum.
  """
  return udiscreta(6) + udiscreta(6)

# simular el número de lanzamientos necesarios para cumplir el proceso
def Nlanzamientos():
  """
  Counts how many trials are needed until all sums from 2 to 12 appear at least once.
  """
  s = set()
  i = 0
  while len(s)<11:
    i += 1
    t = suma_dos_dados()
    s.add(t)
  return i

""" Otra forma:
def lanzamientos_dados():
    posibles_result = set((2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    suma = set()
    n = 0
    while suma != posibles_result:
        u = random.randint(1, 6)
        v = random.randint(1, 6)
        suma.add(u+v)
        n += 1
    return n
"""

# bi: estime el valor medio y la desviación estándar del número de lanzamientos
def esperanza(nsims):
    sum_val_obt = 0
    for i in range(nsims):
        sum_val_obt += Nlanzamientos()
    return sum_val_obt / nsims

def desviacion(nsims):
    media = esperanza(nsims)
    result = 0
    for i in range(nsims):
        result += (Nlanzamientos() - media)**2 
    return sqrt(result/nsims)

# bii
# cuenta cuántas veces dentro del total de simulaciones se da el resultado buscado
def prob_menor_igual(n, nsims):
    p = 0
    for i in range(nsims):
        result = Nlanzamientos()
        if result <= n:
            p += 1
    return p/nsims

# simulaciones repitiendo el algoritmo: 100, 1000, 10000 y 100000 veces.
nsims = [100, 1000, 10000, 100000]
for i in range(len(nsims)):
    # bi
    e = esperanza(nsims[i])
    d = desviacion(nsims[i])
    # bii
    mayor_igual_15 = 1 - prob_menor_igual(14, nsims[i])
    menor_igual_9 = prob_menor_igual(9, nsims[i])

    print(f"N° simulaciones: {nsims[i]}")
    print(f"Esperanza: {e}")
    print(f"Desviación estándar: {d}")
    print(f"Probabilidad de que N sea por lo menos 15: {mayor_igual_15}")
    print(f"Probabilidad de que N sea a lo sumo 9: {menor_igual_9}\n")