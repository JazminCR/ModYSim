from random import seed, uniform
from math import sqrt
from scipy import stats

seed(20)

def bernoulli_elipse():
    x = uniform(-2, 2)
    y = uniform(-1, 1)
    return (x / 2) ** 2 + y ** 2 <= 1

def estimador_p_elipse(d):
    n = 0
    p = 0
    while n <= 100 or sqrt(p * (1 - p) / n) > d:
        n += 1
        X = bernoulli_elipse()
        p += (X - p) / n
    return p

print(f"Proporción dentro de la elipse: {estimador_p_elipse(0.01)}")

L = 0.1     # ancho deseado
cf = 0.95   # nivel de confianza
alpha = 1 - cf
z_alfa_2 = stats.norm.ppf(1 - alpha / 2)

def area_elipse_ic(z_alfa_2, L):
    d = L / (2 * z_alfa_2)
    p = bernoulli_elipse()
    n = 1
    scuad = 0
    while n <= 100 or sqrt(scuad / n) > d:
        n += 1
        X = 8 * bernoulli_elipse()  # 8 es el área del rectángulo
        p_ant = p
        p = p_ant + (X - p_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (p - p_ant) ** 2
    return n, p, p - z_alfa_2 * sqrt(scuad / n), p + z_alfa_2 * sqrt(scuad / n)

sim, area, a, b = area_elipse_ic(z_alfa_2, L)
print("Cantidad de simulaciones necesarias:", sim)
print("Área estimada de la elipse:", area)
print(f"Intervalo de confianza: ({a:.5f}, {b:.5f})")
