from random import random
from math import exp
import time

# punto a
def aprox(N, Nsim):
    suma_h = 0
    # Nsim = 100
    # N = 10000
    for _ in range(Nsim):
        U = int(random() * N) + 1
        suma_h += exp(U / N)
    prom = suma_h / Nsim
    suma = N * prom

    print(f"La aproximación de la sumatoría es: {suma}")
    return suma

# punto c
def sum_real(N):
    suma = 0
    for k in range(1, N + 1):
        suma += exp(k / N)
    return suma

# Aproximación N=10000
t0 = time.perf_counter()
aprox_10000 = aprox(10000, 100)
t1 = time.perf_counter()

# Aproximación N=100
t2 = time.perf_counter()
aprox_100 = aprox(100, 100)
t3 = time.perf_counter()

# Suma exacta N=100
t4 = time.perf_counter()
exacto = sum_real(100)
t5 = time.perf_counter()

# Suma exacta N=10000
t6 = time.perf_counter()
exacto = sum_real(10000)
t7 = time.perf_counter()

print(f"Aproximación para N=10000: {aprox_10000} (Tiempo: {(t1 - t0)*1000:.4f} ms)")
print(f"Aproximación para N=100: {aprox_100} (Tiempo: {(t3 - t2)*1000:.4f} ms)")
print(f"Valor exacto para N=100: {exacto} (Tiempo: {(t5 - t4)*1000:.4f} ms)")
print(f"Valor exacto para N=10000: {exacto} (Tiempo: {(t7 - t6)*1000:.4f} ms)")

# para calcularlo en segundos
t0 = time.time()
aprox_10000 = aprox(10000, 100)
t1 = time.time()

print(f"Aproximación para N=10000: {aprox_10000} (Tiempo: {t1 - t0:.4f} s)")