from random import seed, uniform
from math import sqrt
from scipy import stats

seed(20)

def bernoulli_circulo(radio):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    return sqrt(x**2+y**2) <= radio

def estimador_p(radio, d):
    n = 0
    p = 0
    while n <= 100 or sqrt(p * (1 - p) / n) > d:
        n += 1
        X = bernoulli_circulo(radio)
        p = p + (X - p) / n
    return p

print(f"Proporción de puntos que caen dentro del círculo: {estimador_p(1, 0.01)}")

'''
La proporción de puntos dentro del círculo está en (0,1)
pero para estimar pi hay que multiplicar esa proporción por 4
por lo cual no se puede usar estimador_p con varianza p(1-p)
hay que usar la fórmula de la varianza scuad
'''
L = 0.1   # ancho
cf = 0.95   # confianza
alfa = 1 - cf
# calcular z_(alpha/2) que cumple P(Z > z_(alpha/2)) = alpha/2
z_alfa_2 = stats.norm.ppf(1 - alfa/2)

def media_muestral_ic(radio, z_alfa_2, L):
    d = L / (2 * z_alfa_2)
    media = bernoulli_circulo(radio)
    n = 1
    scuad = 0
    while n <= 100 or sqrt(scuad / n) > d:
        n += 1
        X = 4 * bernoulli_circulo(radio)
        media_ant = media
        media = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media, media - z_alfa_2 * sqrt(scuad/n), media + z_alfa_2 * sqrt(scuad/n)

sim, media, a, b = media_muestral_ic(1, z_alfa_2, L)
print("Cantidad de simulaciones necesarias:", sim)
print("Valor estimado de pi:", media)
print(f"Intervalo: {a:.5f}, {b:.5f}")