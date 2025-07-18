import random
from scipy import stats
import numpy as np
from math import sqrt

def M():
  i = 1
  n_l = 0
  n_u = random.random()
  while n_l < n_u:
    i += 1
    n_l = n_u
    n_u = random.random()
  return i

random.seed(20)

def media_muestral():
    media = M()
    n = 1
    scuad = 0
    var_media = np.inf

    while var_media >= 0.01:
        n += 1
        X = M()
        media_ant = media
        media = media_ant + (X - media_ant) / n
        scuad =  scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
        var_media = scuad / n
    return n, media, var_media

n_sim, media, var_media = media_muestral() 

print(f'Simulaciones requeridas = {n_sim}\n'
      f'Valor estimado de e = {media:.5f}\n'
      f'Varianza muestral = {var_media:.4f}\n\n'
      f'Error absoluto = {np.e-media:.5f}\n'
      f'Error relativo = {(np.e-media)/np.e :.5f}\n'
)

######################################################################

L = 0.1   # ancho
cf = 0.95   # confianza
alfa = 1 - cf

# calcular z_(alpha/2) que cumple P(Z > z_(alpha/2)) = alpha/2
z_alfa_2 = stats.norm.ppf(1 - alfa/2)

random.seed(20)

def media_muestral_intervalo(z_alfa_2, L):
    d = L / (2 * z_alfa_2)
    media = M()
    n = 1
    scuad = 0
    while n <= 100 or sqrt(scuad / n) > d:
        n += 1
        X = M()
        media_ant = media
        media = media_ant + (X - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    print("Valor del corte (d):", d)
    print("Simulaciones requeridas (n):", n)
    return media, media - z_alfa_2 * sqrt(scuad/n), media + z_alfa_2 * sqrt(scuad/n)

media_ic , a, b = media_muestral_intervalo(z_alfa_2, L)
print("Estimación de e mediante IC de 95%:", media_ic)
print(f'Intervalo = ({a:.3f}, {b:.3f})\n\n')
print(f'Error absoluto = {np.abs(np.e-media_ic) :.5f}\n'
      f'Error relativo = {np.abs((np.e-media_ic)/np.e) :.5f}')
