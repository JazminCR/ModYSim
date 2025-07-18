from random import random
from random import randint
from time import time

def udiscreta(n):
  U = random()
  return int(n * U) + 1

def AyR(c):
    probs_x = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    prob_y = 1 / 10
    # y = randint(1, 10)
    y = udiscreta(10)
    u = random()
    if u < probs_x[y-1] / (c * prob_y):
        return y 
    else:
        return AyR(c)
    
print("Simulación con c = 1.4:", AyR(1.4))
start_AyR_min = time()
for i in range(10000):
    AyR(1.4)
final_time_AyR_min = time() - start_AyR_min
print(final_time_AyR_min)

print("Simulación con c = 3:", AyR(3))
start_AyR = time()
for i in range(10000):
    AyR(3)
final_time_AyR = time() - start_AyR
print(final_time_AyR)
    
def TI(p, x):
    U = random()
    i = 0
    F = p[0]
    while U >= F:
        i += 1
        F += p[i]
    return x[i]

prob = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
val_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Simulación t. inversa:", TI(prob, val_x))
start_TI = time()
for i in range(10000):
    TI(prob, val_x)
final_time_TI = time() - start_TI
print(final_time_TI)

prob_sort = [0.14, 0.12, 0.11, 0.11, 0.10, 0.09, 0.09, 0.09, 0.08, 0.07]
val_x_sort = [2, 5, 1, 9, 6, 3, 7, 10, 4, 8]
print("Simulación t. inversa mejorada:", TI(prob_sort, val_x_sort))
start_TI_mej = time()
for i in range(10000):
    TI(prob_sort, val_x_sort)
final_time_TI_mej = time() - start_TI_mej
print(final_time_TI_mej)

"""
def ordenar_probabilidades(p, x):
    # Empareja las probabilidades con sus valores
    pares = list(zip(p, x))
    # Ordena los pares por probabilidad (mayor a menor)
    pares_ordenados = sorted(pares, key=lambda par: par[0], reverse=True)
    # Separa las listas nuevamente
    p_ordenado, x_ordenado = zip(*pares_ordenados)
    return list(p_ordenado), list(x_ordenado)

# Ejemplo de uso:
prob = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
val_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

p_ordenado, x_ordenado = ordenar_probabilidades(prob, val_x)

print("Probabilidades ordenadas:", p_ordenado)
print("Valores x ordenados:", x_ordenado)
"""

def urna(l):
    A = []
    prob = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    for i in range(len(prob)):
        for j in range(int(prob[i]*l)):
            A.append(i+1)
    k = int(random() * l)
    return A[k]

print("Simulación urna:", urna(100))
start_urna = time()
for i in range(10000):
    urna(100)
final_time_urna = time() - start_urna
print(final_time_urna)

def urna_mej():
    prob = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    dec = [int(p * 10) for p in prob]  
    cen = [int(p * 100) - d * 10 for p, d in zip(prob, dec)]  

    D = []
    C = []
    for i in range(len(prob)):
        for _ in range(dec[i]):
            D.append(i+1)
        for _ in range(cen[i]):
            C.append(i+1)

    peso_dec = sum(dec) / 100

    u = random()
    if u < peso_dec:
        i = int(random() * len(D))
        return D[i]
    else:
        i = int(random() * len(C))
        return C[i]
    
print("Simulación urna mejorada:", urna_mej())
start_urna_mej = time()
for i in range(10000):
    urna_mej()
final_time_urna_mej = time() - start_urna_mej
print(final_time_urna_mej)


"""
# --- Función para medir tiempo de ejecución ---
def medir_tiempo(func, n_sim, *args):
    start = time.time()
    for _ in range(n_sim):
        func(*args)
    end = time.time()
    return end - start

# --- Cantidad de simulaciones ---
n = 10000

# --- Comparar tiempos ---
tiempo_TI = medir_tiempo(TI, n, prob, val_x)
tiempo_AyR = medir_tiempo(AyR, n, 1.4)
tiempo_urna = medir_tiempo(urna, n, 100)
tiempo_urna_mej = medir_tiempo(urna_mej, n)

# --- Mostrar resultados ---
print(f"Tiempo Transformada Inversa: {tiempo_TI:.4f} segundos")
print(f"Tiempo Aceptación-Rechazo (c=1.4): {tiempo_AyR:.4f} segundos")
print(f"Tiempo Urna (l=100): {tiempo_urna:.4f} segundos")
print(f"Tiempo Urna Mejorada: {tiempo_urna_mej:.4f} segundos")
"""