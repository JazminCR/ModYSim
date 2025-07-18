from random import seed, uniform
from math import sqrt
from scipy import stats

seed(20)

def bernoulli_corazon():
    x = uniform(-1.5, 1.5)
    y = uniform(-1.5, 1.5)
    return (x**2 + y**2 - 1) ** 3 <= x**2 * abs(y)**3

def estimador_p_corazon(d):
    n = 0
    p = 0
    while n <= 100 or sqrt(p * (1 - p) / n) > d:
        n += 1
        X = bernoulli_corazon()
        p += (X - p) / n
    return p

print(f"Proporción dentro del corazón: {estimador_p_corazon(0.01)}")   # ver si dan algun valor para la desviacion estandar

L = 0.1     # ancho deseado
cf = 0.95   # nivel de confianza
alpha = 1 - cf
z_alfa_2 = stats.norm.ppf(1 - alpha / 2)

def area_corazon_ic(z_alfa_2, L):
    d = L / (2 * z_alfa_2)
    p = bernoulli_corazon()
    n = 1
    scuad = 0
    while n <= 100 or sqrt(scuad / n) > d:
        n += 1
        X = 9 * bernoulli_corazon()  # 9 es el área del cuadrado
        p_ant = p
        p = p_ant + (X - p_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (p - p_ant) ** 2
    return n, p, p - z_alfa_2 * sqrt(scuad / n), p + z_alfa_2 * sqrt(scuad / n)

sim, area, a, b = area_corazon_ic(z_alfa_2, L)
print("Cantidad de simulaciones necesarias:", sim)
print("Área estimada del corazón:", area)
print(f"Intervalo de confianza: ({a:.5f}, {b:.5f})")
