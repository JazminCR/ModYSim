from random import random, randint
from math import log

def eventos_poisson(lam, T):
    t = -log(1 - random()) / lam
    eventos = []
    while t <= T:
        eventos.append(t)
        t += -log(1 - random()) / lam
    return eventos, len(eventos)

def llegada_aficionados():
    tiempos = eventos_poisson(5, 1)[0]  # toma eventos del return
    aficionados = []
    for tiempo in tiempos:
        aficionados.append(randint(20, 40))
    return aficionados
    # si return tiempos podría ver en qué tiempos ocurrieron los eventos

def aficionados_en_una_hora():
    _, cantidad_buses = eventos_poisson(5, 1)  # toma la cantidad de eventos del return (otra forma)
    total_aficionados = 0
    for _ in range(cantidad_buses):
        capacidad = randint(20, 40)  # uniforme discreta (entero) en [20, 40] 
        total_aficionados += capacidad
    return total_aficionados

print("Aficionados en 1 hs:" , aficionados_en_una_hora())

print("Llegada aficionados:" , llegada_aficionados())
