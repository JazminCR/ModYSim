import numpy as np

def simular_juego(n):
    ganadas = 0
    for _ in range(n):
        U = np.random.uniform()
        if U < 0.5:
            X = np.random.uniform() + np.random.uniform()
        else:
            X = np.random.uniform() + np.random.uniform() + np.random.uniform()
        if X >= 1:
            ganadas += 1
    return ganadas / n

# Simulaciones para diferentes valores de n
for n in [100, 1000, 10000]:
    prob = simular_juego(n)
    print(f"n = {n}, probabilidad estimada = {prob:.4f}")


#Otra forma: 
#import random 

#def juego_azar():
#    u = random.random()
#    if u < 1/2:
#        w1 = random.random()
#        w2 = random.random()
#        x = w1 + w2
#    else:
#        w1 = random.random()
#        w2 = random.random()
#        w3 = random.random()
#        x = w1 + w2 + w3
#    return x
#nsim = 1000000
#prob = 0
#for i in range(0, nsim):
#    x = juego_azar()
#    if x >= 1:
#        prob += 1
#prob /= nsim
#print(prob)