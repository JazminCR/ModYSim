from random import random, randint
from math import abs, log

def udiscreta(n):
  U = random()
  return int(n * U)

def AyR(prob_x):
    y = randint(0, 3)
    # y = udiscreta(3)
    prob_y = 1 / 4
    u = random()
    if u < prob_x[y-1] / (1.4 * prob_y):
        return y 
    else:
        return AyR(prob_x)
    
# c calculado: c = 1.4
probs_x = [0.13, 0.22, 0.35, 0.3]

print(AyR(probs_x))

# poisson no homogeneo

def poisson_adelg_mej(fun_lambda, T):
    int = [0,1,2,6,8,9]
    lambdas = [10, 15, 20, 18, 14]
    eventos = []
    j = 0
    t = -log(1 - random()) / lambdas[j]
    while t <= T:
        if t <= int[j]:
            if random() <= fun_lambda / lambdas[j]:
                eventos.append(t)
            t += -log(1 - random()) / lambdas[j]
        else:
            t = int[j] + (t - int[j])*lambdas[j] / lambdas[j+1]
            j += 1
        return eventos, len(eventos)

# area

def area(N):
    dentro = 0
    for _ in range(N):
        x = random.uniform(-1.5, 1.5)
        y = random.uniform(-1.5, 1.5)
        if (x**2 + (y - abs(x)**(3/2))**2) <= 1:
            dentro += 1
    area_rectangulo = (1.5 - (-1.5)) * (1.5 - (-1.5))
    #base=1.5−(−1.5)=3
    #altura=1.5−(−1.5)=3
    return dentro / N * area_rectangulo

# Ejecutar con N = 100000
estimacion = area(100000)
print(f"Área estimada: {estimacion:.6f}")