from random import random
from math import factorial

#@title algoritmo de tasa de riesgo
def x_tasa_discreta(p,**kwargs):
    k = 1
    sum = 1
    l = 1
    while True:
        u = random()
        if k == 1:
            pass
        else:
          sum -= p(x=k-1,**kwargs)
          # sum -= l*sum
        l = p(x=k,**kwargs)/sum
        if u < l:
            return k
        k += 1
     
# ejemplo de uso
def p(x, l=2):         # distribución de Poisson truncada
    return (l**x / factorial(x)) / sum(l**j / factorial(j) for j in range(10))

print(x_tasa_discreta(p, l=2))

# método de la tasa discreta para una variable geométrica
def geom_tasa_discreta(pr):
    k = 1
    while True:
        u = random.random()
        if u < pr:
            return k
        k += 1
