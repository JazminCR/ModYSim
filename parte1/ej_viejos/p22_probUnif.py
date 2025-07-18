from random import uniform

def simular_juego(n=100000):
    ganadas_por_A = 0

    for _ in range(n):
        u = uniform(0, 1)
        v = uniform(0, 1)
        if u > 0.6 or v > 0.6:
            ganadas_por_A += 1
        else:
            pass
    
    return ganadas_por_A / n

print(simular_juego())

#import numpy as np
#
#def estimar_probabilidad_A(n=10000):
#    U = np.random.uniform(0, 1, n)
#    V = np.random.uniform(0, 1, n)
#    M = np.maximum(U, V)
#    gana_A = M > 0.6
#    return np.mean(gana_A)
#
#prob_estimada = estimar_probabilidad_A()
#print(f"Probabilidad estimada de que A gane: {prob_estimada:.4f}")
