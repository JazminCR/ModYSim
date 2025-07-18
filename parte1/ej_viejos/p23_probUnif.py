import numpy as np
from random import uniform

def simular_juego(n=100000):
    ganadas_por_A = 0

    for _ in range(n):
        for _ in range(2):  # solo 2 intentos
            u = uniform(0, 1)
            v = uniform(0, 1)
            if u > 0.5 and v < 0.5:
                ganadas_por_A += 1
                break
            elif u < 0.5 and v > 0.5:
                break  # gana B → no sumamos
            # si es empate, se repite (solo una vez más)
    
    return ganadas_por_A / n

estimacion = simular_juego()
print(f"Probabilidad estimada de que A gane en 1ra o 2da jugada: {estimacion:.4f}")

#def simular_juego(n=100000):
#    ganadas_por_A = 0
#
#    for _ in range(n):
#        u = uniform(0, 1)
#        v = uniform(0, 1)
#        if u > 0.5 and v < 0.5:
#            ganadas_por_A += 1
#            pass
#        elif u < 0.5 and v > 0.5:
#            pass  # gana B → no sumamos
#        else:
#            u2 = uniform(0, 1)
#            v2 = uniform(0, 1)
#            if u2 > 0.5 and v2 < 0.5:
#                ganadas_por_A += 1
#                pass
#            elif u2 < 0.5 and v2 > 0.5:
#                pass
#            else:
#                pass
#    
#    return ganadas_por_A / n


# nro de jugadas hasta que alguien gana (no lo pide el ej)
#def tiempo_promedio(n=100000):
#    total_jugadas = 0
#
#    for _ in range(n):
#        jugadas = 0
#        while True:
#            u, v = np.random.uniform(), np.random.uniform()
#            jugadas += 1
#            if (u > 0.5 and v < 0.5) or (u < 0.5 and v > 0.5):
#                break  # alguien ganó
#        total_jugadas += jugadas
#
#    return total_jugadas / n
#
#promedio_jugadas = tiempo_promedio()
#print(f"Promedio de jugadas hasta que alguien gana: {promedio_jugadas:.4f}")
