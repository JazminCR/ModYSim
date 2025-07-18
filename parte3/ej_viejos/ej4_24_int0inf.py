from math import sqrt
import numpy as np
from random import random, seed
from scipy import stats

seed(42)

def f(x):
  return x / (1 + x**4)

# escalar para llevar (0, infty) -> (0, 1)
def g(x):
  return f(1/x - 1) / x**2


semiancho = 0.001
L = 2 * semiancho   # ancho
cf = 0.95           # confianza
alfa = 1 - cf

# calcular z_(alpha/2) que cumple P(Z > z_(alpha/2)) = alpha/2
z_alfa_2 = stats.norm.ppf(1 - alfa/2)

# scuad representa a s**2 --> estimador de var muestral
# s_media representa al estimador del desvío de la media
def media_muestral(z_alfa_2, L):
    # calcular el criterio de corte en base al semiancho y confianza
    d = L / (2 * z_alfa_2)
    mediaX = g(random())
    n = 1
    scuad = 0
    s_media = np.inf  # inicialización desvío de la media
    lista = []  # para guardar los valores de la media, desvío e IC
    while s_media >= d:
        n += 1
        X = g(random())
        media_ant = mediaX
        mediaX = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1/(n-1)) + n * (mediaX-media_ant)**2
        s_media = sqrt(scuad/n) # desvío de la media, eso usarlo para la condición del while
        # s = sqrt(scuad) creo que es lo que se debería devolver
        if n in [1000, 5000, 7000]: # guardar los valores de las simulaciones que se piden
           lista.append(mediaX)
           lista.append(s_media)
           lista.append((mediaX - z_alfa_2 * s_media, mediaX + z_alfa_2 * s_media))   # tupla con los extremos del intervalo
    # guardar los valores cuando se cumple la condición del while
    lista.append(mediaX)
    lista.append(s_media)
    lista.append((mediaX - z_alfa_2 * s_media, mediaX + z_alfa_2 * s_media))

    print(f'Valor del corte (d) = {d},\nSimulaciones requeridas (n) = {n}')
    print()
    print('  #sim','|','  int  ','|','  s   ','|','  intervalo')
    for i,j in zip([0,3,6,9],['  1000','  5000','  7000',n]):
        print(j,'|',f'{lista[i]:.4f}','|',f'{lista[i+1]:.4f}','|',f'({lista[i+2][0]:.4f},{lista[i+2][1]:.4f})')

    return mediaX   # estimación de la integral usando Monte Carlo

valor_integral = media_muestral(z_alfa_2, L)
print(f'Valor estimado de la integral = {valor_integral:.6f}')